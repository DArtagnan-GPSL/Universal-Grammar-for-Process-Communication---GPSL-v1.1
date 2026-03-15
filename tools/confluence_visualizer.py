"""
confluence_visualizer.py — Confluence Network Reasoning Visualiser
====================================================================

Animates a query moving through a K4 pod network.

Three panels:
  Left   — Network map (pods + shared nodes, colour = state)
  Centre — Active pod detail (internal K4 + agent outputs)
  Right  — Symbol trace (GPSL expression evolution)

Colour logic:
  grey   = inactive
  blue   = active analysis
  yellow = disagreement / unresolved
  green  = local consensus
  purple = refined result returning upward

Run:
  python3 confluence_visualizer.py

GPSL Project — March 2026
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.animation as animation
import numpy as np

# ── Colours ──────────────────────────────────────────────────────────────────
C_BG        = "#0d1220"
C_INACTIVE  = "#2a3a55"
C_ACTIVE    = "#3a8fd4"
C_DISAGREE  = "#f0a500"
C_AGREE     = "#50c878"
C_RETURN    = "#cc88ff"
C_EDGE      = "#334466"
C_EDGE_ACT  = "#5599cc"
C_LABEL     = "#ffffff"
C_SUBLABEL  = "#aaaacc"
C_TRACE_BG  = "#060e18"
C_POD_DETAIL= "#0a1a2a"

# ── Network layout ────────────────────────────────────────────────────────────
# Top level: O (prime), A (memory), B (reason), C (imagination), D (convergence)
# D zooms into sub-level: Da Db Dc Dd

TOP_PODS = {
    'O':  (5.0, 8.5),   # prime node
    'A':  (2.0, 6.0),
    'B':  (5.0, 6.0),
    'C':  (8.0, 6.0),
    'D':  (5.0, 3.5),   # zoom node
}

SHARED_NODES = {
    'sAB': (3.5, 7.0),
    'sBC': (6.5, 7.0),
    'sAD': (3.0, 4.8),
    'sBD': (5.0, 4.8),
    'sCD': (7.0, 4.8),
}

SUB_PODS = {
    'Da': (3.2, 1.5),
    'Db': (4.4, 1.5),
    'Dc': (5.6, 1.5),
    'Dd': (6.8, 1.5),
}

TOP_EDGES = [
    ('O','sAB'),('sAB','A'),('sAB','B'),
    ('O','sBC'),('sBC','B'),('sBC','C'),
    ('A','sAD'),('sAD','D'),
    ('B','sBD'),('sBD','D'),
    ('C','sCD'),('sCD','D'),
]

SUB_EDGES = [
    ('D','Da'),('D','Db'),('D','Dc'),('D','Dd'),
    ('Da','Db'),('Db','Dc'),('Dc','Dd'),('Dd','Da'),
    ('Da','Dc'),('Db','Dd'),
]

# ── Animation frames ──────────────────────────────────────────────────────────
# Each frame: (pod_states, active_pod, agent_step, trace_lines, description)
FRAMES = [
    # 0 — query enters
    {
        'pods':    {'O': C_ACTIVE},
        'shared':  {},
        'sub':     {},
        'pod_detail': 'O',
        'agent':   0,
        'trace':   ["Query enters prime node O"],
        'desc':    "Query enters — triage begins",
        'expr':    "",
    },
    # 1 — route to B (reason)
    {
        'pods':    {'O': C_ACTIVE, 'B': C_ACTIVE},
        'shared':  {'sBC': C_ACTIVE, 'sAB': C_ACTIVE},
        'sub':     {},
        'pod_detail': 'B',
        'agent':   0,
        'trace':   ["Query enters prime node O",
                    "Routed to Pod B (Reason)"],
        'desc':    "Routing — domain identified",
        'expr':    "",
    },
    # 2 — pod B debate begins
    {
        'pods':    {'O': C_ACTIVE, 'B': C_ACTIVE},
        'shared':  {'sAB': C_ACTIVE},
        'sub':     {},
        'pod_detail': 'B',
        'agent':   1,
        'trace':   ["Query enters prime node O",
                    "Routed to Pod B (Reason)",
                    "[D-01] → {I-03}"],
        'desc':    "Pod B — internal debate",
        'expr':    "[D-01] → {I-03}",
    },
    # 3 — agent 2 extends
    {
        'pods':    {'O': C_ACTIVE, 'B': C_ACTIVE},
        'shared':  {'sAB': C_ACTIVE},
        'sub':     {},
        'pod_detail': 'B',
        'agent':   2,
        'trace':   ["Query enters prime node O",
                    "Routed to Pod B (Reason)",
                    "[D-01] → {I-03}",
                    "[D-01] → {I-03} | {W-02}"],
        'desc':    "Pod B — expression extended",
        'expr':    "[D-01] → {I-03} | {W-02}",
    },
    # 4 — disagreement 2/2
    {
        'pods':    {'O': C_ACTIVE, 'B': C_DISAGREE},
        'shared':  {'sAB': C_DISAGREE, 'sBD': C_DISAGREE},
        'sub':     {},
        'pod_detail': 'B',
        'agent':   3,
        'trace':   ["Query enters prime node O",
                    "Routed to Pod B (Reason)",
                    "[D-01] → {I-03}",
                    "[D-01] → {I-03} | {W-02}",
                    "Disagreement 2/2 — zoom triggered"],
        'desc':    "Disagreement — zoom triggered",
        'expr':    "[D-01] → {I-03} | {W-02}",
    },
    # 5 — zoom into D
    {
        'pods':    {'O': C_ACTIVE, 'B': C_DISAGREE, 'D': C_ACTIVE},
        'shared':  {'sBD': C_DISAGREE},
        'sub':     {'Da': C_ACTIVE, 'Db': C_ACTIVE, 'Dc': C_ACTIVE, 'Dd': C_ACTIVE},
        'pod_detail': 'D',
        'agent':   0,
        'trace':   ["Query enters prime node O",
                    "Routed to Pod B (Reason)",
                    "[D-01] → {I-03}",
                    "[D-01] → {I-03} | {W-02}",
                    "Disagreement 2/2 — zoom triggered",
                    "Zoom → Pod D (Convergence / L2)"],
        'desc':    "Zoom — sub-pod activates",
        'expr':    "[D-01] → {I-03} | {W-02}",
    },
    # 6 — sub-pod debate
    {
        'pods':    {'O': C_ACTIVE, 'B': C_DISAGREE, 'D': C_ACTIVE},
        'shared':  {'sBD': C_DISAGREE},
        'sub':     {'Da': C_ACTIVE, 'Db': C_DISAGREE, 'Dc': C_ACTIVE, 'Dd': C_ACTIVE},
        'pod_detail': 'D',
        'agent':   2,
        'trace':   ["Query enters prime node O",
                    "Routed to Pod B (Reason)",
                    "[D-01] → {I-03}",
                    "[D-01] → {I-03} | {W-02}",
                    "Disagreement 2/2 — zoom triggered",
                    "Zoom → Pod D (Convergence / L2)",
                    "[D-01] → {I-03} | {W-02} :: [A-04]"],
        'desc':    "Sub-pod — threshold crossing found",
        'expr':    "[D-01] → {I-03} | {W-02} :: [A-04]",
    },
    # 7 — sub-pod consensus
    {
        'pods':    {'O': C_ACTIVE, 'B': C_DISAGREE, 'D': C_AGREE},
        'shared':  {'sBD': C_ACTIVE},
        'sub':     {'Da': C_AGREE, 'Db': C_AGREE, 'Dc': C_AGREE, 'Dd': C_AGREE},
        'pod_detail': 'D',
        'agent':   4,
        'trace':   ["Query enters prime node O",
                    "Routed to Pod B (Reason)",
                    "[D-01] → {I-03}",
                    "[D-01] → {I-03} | {W-02}",
                    "Disagreement 2/2 — zoom triggered",
                    "Zoom → Pod D (Convergence / L2)",
                    "[D-01] → {I-03} | {W-02} :: [A-04]",
                    "[D-01] → {I-03} | {W-02} :: [A-04] = {L-06}",
                    "Sub-pod consensus 4/4"],
        'desc':    "Sub-pod consensus — result ascends",
        'expr':    "[D-01] → {I-03} | {W-02} :: [A-04] = {L-06}",
    },
    # 8 — result returns upward
    {
        'pods':    {'O': C_RETURN, 'B': C_AGREE, 'D': C_RETURN},
        'shared':  {'sBD': C_RETURN, 'sAB': C_RETURN},
        'sub':     {'Da': C_RETURN, 'Db': C_RETURN, 'Dc': C_RETURN, 'Dd': C_RETURN},
        'pod_detail': 'O',
        'agent':   4,
        'trace':   ["Query enters prime node O",
                    "Routed to Pod B (Reason)",
                    "[D-01] → {I-03}",
                    "[D-01] → {I-03} | {W-02}",
                    "Disagreement 2/2 — zoom triggered",
                    "Zoom → Pod D (Convergence / L2)",
                    "[D-01] → {I-03} | {W-02} :: [A-04]",
                    "[D-01] → {I-03} | {W-02} :: [A-04] = {L-06}",
                    "Sub-pod consensus 4/4",
                    "Result ascends — confidence: high",
                    "Final: [D-01] → {I-03} | {W-02} :: [A-04] = {L-06}"],
        'desc':    "Return wave — result delivered",
        'expr':    "[D-01] → {I-03} | {W-02} :: [A-04] = {L-06}  ✓",
    },
]

AGENT_LABELS = ["A — Proposal", "B — Critique", "C — Reframe", "D — Synthesis", "✓ Consensus"]
AGENT_COLS   = [C_ACTIVE, C_DISAGREE, C_ACTIVE, C_AGREE, C_RETURN]


def draw_frame(fig, frame_data):
    fig.clf()
    fig.patch.set_facecolor(C_BG)

    # Three panels
    ax_net  = fig.add_axes([0.01, 0.08, 0.45, 0.88])   # network map
    ax_pod  = fig.add_axes([0.47, 0.35, 0.25, 0.58])   # pod detail
    ax_tr   = fig.add_axes([0.74, 0.08, 0.25, 0.88])   # trace

    for ax in [ax_net, ax_pod, ax_tr]:
        ax.set_facecolor(C_BG)
        ax.axis('off')

    pod_states    = frame_data['pods']
    shared_states = frame_data['shared']
    sub_states    = frame_data['sub']

    # ── Network map ───────────────────────────────────────────────────────────
    ax_net.set_xlim(0, 10)
    ax_net.set_ylim(0, 10)
    ax_net.text(5, 9.6, "Confluence Network", ha='center',
                fontsize=10, color=C_LABEL, fontweight='bold')
    ax_net.text(5, 9.2, frame_data['desc'], ha='center',
                fontsize=8, color=C_SUBLABEL, style='italic')

    # Draw top edges
    all_pos = {**TOP_PODS, **SHARED_NODES}
    for e in TOP_EDGES:
        x1,y1 = all_pos[e[0]]
        x2,y2 = all_pos[e[1]]
        col = C_EDGE_ACT if (pod_states.get(e[0]) or shared_states.get(e[1]) or
                              shared_states.get(e[0])) else C_EDGE
        ax_net.plot([x1,x2],[y1,y2], color=col, linewidth=1.2, zorder=1)

    # Draw sub edges
    all_sub = {**TOP_PODS, **SUB_PODS}
    for e in SUB_EDGES:
        if e[0] in all_sub and e[1] in all_sub:
            x1,y1 = all_sub[e[0]]
            x2,y2 = all_sub[e[1]]
            col = C_EDGE_ACT if sub_states else C_EDGE
            ax_net.plot([x1,x2],[y1,y2], color=col, linewidth=0.8,
                        linestyle='--', zorder=1, alpha=0.6)

    # Draw shared nodes
    for name, (x,y) in SHARED_NODES.items():
        col = shared_states.get(name, C_INACTIVE)
        ax_net.add_patch(plt.Circle((x,y), 0.18, color=col, zorder=3))
        ax_net.text(x, y, '◑', ha='center', va='center',
                    fontsize=7, color=C_LABEL, zorder=4)

    # Draw top pods
    for name, (x,y) in TOP_PODS.items():
        col = pod_states.get(name, C_INACTIVE)
        r = 0.55 if name == 'O' else 0.45
        rect = mpatches.FancyBboxPatch((x-r, y-0.35), r*2, 0.7,
               boxstyle="round,pad=0.06", facecolor=col,
               edgecolor="#aaccff" if col != C_INACTIVE else C_EDGE,
               linewidth=1.2, zorder=3)
        ax_net.add_patch(rect)
        ax_net.text(x, y+0.05, name, ha='center', va='center',
                    fontsize=10, color=C_LABEL, fontweight='bold', zorder=5)
        domain = {'O':'Prime','A':'Memory','B':'Reason','C':'Imagination','D':'Convergence'}
        ax_net.text(x, y-0.18, domain[name], ha='center', va='center',
                    fontsize=5.5, color=C_SUBLABEL, zorder=5)

    # Draw sub pods
    for name, (x,y) in SUB_PODS.items():
        col = sub_states.get(name, C_INACTIVE)
        rect = mpatches.FancyBboxPatch((x-0.35, y-0.25), 0.7, 0.5,
               boxstyle="round,pad=0.04", facecolor=col,
               edgecolor="#aaccff" if col != C_INACTIVE else C_EDGE,
               linewidth=0.9, zorder=3)
        ax_net.add_patch(rect)
        ax_net.text(x, y, name, ha='center', va='center',
                    fontsize=8, color=C_LABEL, fontweight='bold', zorder=5)

    # Zoom bracket
    if sub_states:
        ax_net.text(5.0, 2.6, "↑ zoom level 2", ha='center',
                    fontsize=7, color=C_DISAGREE, style='italic')

    # Legend
    legend_items = [
        (C_INACTIVE, "inactive"),
        (C_ACTIVE,   "active"),
        (C_DISAGREE, "disagreement"),
        (C_AGREE,    "consensus"),
        (C_RETURN,   "returning"),
    ]
    for i, (col, lbl) in enumerate(legend_items):
        ax_net.add_patch(plt.Circle((0.4, 0.8 - i*0.35), 0.1, color=col))
        ax_net.text(0.65, 0.8 - i*0.35, lbl, va='center',
                    fontsize=6.5, color=C_SUBLABEL)

    # ── Pod detail ────────────────────────────────────────────────────────────
    ax_pod.set_xlim(0, 5)
    ax_pod.set_ylim(0, 6)
    pname = frame_data['pod_detail']
    ax_pod.text(2.5, 5.7, f"Pod {pname} — internal K₄",
                ha='center', fontsize=8.5, color=C_LABEL, fontweight='bold')

    # Mini K4
    k4 = {'A':(2.5,4.5), 'B':(3.8,3.3), 'C':(2.5,2.1), 'D':(1.2,3.3)}
    for p,q in [('A','B'),('A','C'),('A','D'),('B','C'),('B','D'),('C','D')]:
        x1,y1 = k4[p]; x2,y2 = k4[q]
        ax_pod.plot([x1,x2],[y1,y2], color=C_EDGE_ACT, linewidth=0.9, alpha=0.6)

    astep = frame_data['agent']
    for i,(k,(x,y)) in enumerate(k4.items()):
        col = AGENT_COLS[min(i, astep)] if i <= astep else C_INACTIVE
        ax_pod.add_patch(plt.Circle((x,y), 0.35, color=col, zorder=4))
        ax_pod.text(x, y, k, ha='center', va='center',
                    fontsize=9, color=C_LABEL, fontweight='bold', zorder=5)

    # Agent status
    ax_pod.text(2.5, 1.4, "Agents:", ha='center', fontsize=7, color=C_SUBLABEL)
    for i, lbl in enumerate(AGENT_LABELS):
        col = AGENT_COLS[i] if i <= astep else C_INACTIVE
        ax_pod.text(2.5, 1.1 - i*0.22, lbl, ha='center',
                    fontsize=6.5, color=col)

    # Current expression
    expr = frame_data['expr']
    if expr:
        ax_pod.text(2.5, -0.15, expr, ha='center', fontsize=6.5,
                    color=C_AGREE if 'consensus' in frame_data['desc'].lower() else C_ACTIVE,
                    bbox=dict(boxstyle='round,pad=0.25', facecolor=C_POD_DETAIL,
                              edgecolor=C_EDGE_ACT, linewidth=0.8))

    # ── Symbol trace ──────────────────────────────────────────────────────────
    ax_tr.set_xlim(0, 10)
    ax_tr.set_ylim(0, 10)
    ax_tr.text(5, 9.6, "Symbol Trace", ha='center',
               fontsize=10, color=C_LABEL, fontweight='bold')
    ax_tr.text(5, 9.2, "GPSL expression evolution",
               ha='center', fontsize=7, color=C_SUBLABEL, style='italic')

    ax_tr.add_patch(mpatches.FancyBboxPatch((0.2, 0.2), 9.6, 8.6,
        boxstyle="round,pad=0.1", facecolor=C_TRACE_BG,
        edgecolor=C_EDGE, linewidth=0.8))

    lines = frame_data['trace']
    for i, line in enumerate(reversed(lines[-12:])):
        y = 8.5 - i * 0.68
        idx = len(lines) - i - 1
        col = C_RETURN if i == 0 else (C_AGREE if '✓' in line or 'consensus' in line.lower()
              else C_DISAGREE if 'disagree' in line.lower() or 'zoom' in line.lower()
              else C_SUBLABEL)
        prefix = f"{idx+1}. " if idx >= 0 else "   "
        ax_tr.text(0.5, y, prefix + line, va='center',
                   fontsize=6.8, color=col,
                   wrap=True)

    ax_tr.text(5, 0.5, f"Frame {FRAMES.index(frame_data)+1} / {len(FRAMES)}",
               ha='center', fontsize=6.5, color=C_INACTIVE)


def main():
    fig = plt.figure(figsize=(20, 10))
    fig.patch.set_facecolor(C_BG)

    # Save each frame as a PNG strip
    for i, frame in enumerate(FRAMES):
        draw_frame(fig, frame)
        plt.savefig(f'/home/claude/frame_{i:02d}.png',
                    dpi=120, bbox_inches='tight', facecolor=C_BG)
        print(f"frame {i+1}/{len(FRAMES)} saved")

    # Composite into a single animated GIF
    try:
        import subprocess
        frames_str = ' '.join([f'/home/claude/frame_{i:02d}.png' for i in range(len(FRAMES))])
        subprocess.run(
            f'convert -delay 120 -loop 0 {frames_str} /home/claude/confluence_animation.gif',
            shell=True, check=True
        )
        print("GIF saved")
    except Exception:
        print("GIF conversion not available — individual frames saved")

    # Save final frame as static PNG
    draw_frame(fig, FRAMES[-1])
    plt.savefig('/home/claude/confluence_visualizer_final.png',
                dpi=150, bbox_inches='tight', facecolor=C_BG)
    print("final frame saved")
    plt.close()


if __name__ == "__main__":
    main()
