#!/usr/bin/env python3
"""
Grant proposal preliminary results figure (post-2026-07-10 fix, verified).

Numbers transcribed from the sanctioned sources in
predictive_active_modular_time (regenerate with `uv run python -m
experiments.aggregate_ocl` and `pytest tests/test_hdc_recall.py`):

  Panel A: memory-substrate capacity — exact associative recall vs number of
           stored pairs K (D=512). Source: tests/test_hdc_recall.py:83
           (0.94 / 0.59 / 0.39 at K=32/64/96) — mechanism verification.
  Panel B: online class-incremental accuracy (CL-matrix ACC) on CORe50-NI,
           single-pass, frozen DINOv2 features, 3 seeds.
           Source: results/online_cl/summary_table.md.
           naive 0.625 · PAM multi@16 0.652 · PAM proto 0.627 · ER 0.877 ·
           PAM SLDA 0.925 · tPC encoder 0.022 (representation collapse).

Saved to grant_proposal/figures/prelim_results.pdf
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

# ── Verified numbers (see header for provenance) ──────────────────────────────
CAP_K       = [32, 64, 96]
CAP_RECALL  = [0.94, 0.59, 0.39]           # tests/test_hdc_recall.py, D=512

CL_METHODS  = ["naive", "PAM\nmulti", "PAM\nproto", "ER\n(grad.)", "PAM\nSLDA", "tPC\nencoder"]
CL_ACC      = [0.625, 0.652, 0.627, 0.877, 0.925, 0.022]
CL_COLOR    = ["#B0B0B0", "#81A9D4", "#81A9D4", "#999999", "#2D6A4F", "#C44E52"]

PAM_GREEN = "#2D6A4F"

def style_ax(ax):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.set_ylim(0, 1.05)
    ax.set_yticks([0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
    ax.yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1, decimals=0))
    ax.tick_params(labelsize=8)
    ax.grid(axis="y", alpha=0.22, lw=0.6)

fig, (ax_a, ax_b) = plt.subplots(1, 2, figsize=(7.2, 2.9))
fig.subplots_adjust(wspace=0.28)

# ─── Panel A: substrate capacity ─────────────────────────────────────────────
ax_a.plot(CAP_K, CAP_RECALL, "-o", lw=2.5, ms=7, color=PAM_GREEN,
          label="Kanerva/HDC substrate")
for k, r in zip(CAP_K, CAP_RECALL):
    ax_a.annotate(f"{r:.2f}", (k, r), textcoords="offset points",
                  xytext=(0, 9), ha="center", fontsize=8, color=PAM_GREEN)
style_ax(ax_a)
ax_a.set_xticks(CAP_K)
ax_a.set_xlabel("Stored pairs  $K$", fontsize=9)
ax_a.set_ylabel("Exact associative recall", fontsize=9)
ax_a.set_title("(A)  Memory substrate  ($D{=}512$)", fontsize=9, fontweight="bold")
ax_a.legend(fontsize=7, loc="upper right", frameon=False)

# ─── Panel B: online CL-ACC on CORe50-NI ─────────────────────────────────────
xs = range(len(CL_METHODS))
ax_b.bar(xs, CL_ACC, color=CL_COLOR, width=0.68, edgecolor="white")
for x, v in zip(xs, CL_ACC):
    ax_b.text(x, v + 0.02, f"{v:.2f}", ha="center", fontsize=7.5, color="black")
ax_b.axhline(CL_ACC[3], color="#999999", ls="--", lw=0.8, alpha=0.7)  # ER reference
style_ax(ax_b)
ax_b.set_xticks(list(xs))
ax_b.set_xticklabels(CL_METHODS, fontsize=7.2)
ax_b.set_ylabel("Class-incremental accuracy", fontsize=9)
ax_b.set_title("(B)  CORe50-NI online CL  (frozen features)", fontsize=9, fontweight="bold")

out = __import__("pathlib").Path(__file__).parent / "prelim_results.pdf"
fig.savefig(out, bbox_inches="tight", dpi=200)
plt.close(fig)
print(f"Saved → {out}")
