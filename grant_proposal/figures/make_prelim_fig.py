#!/usr/bin/env python3
"""
Grant proposal preliminary results figure.
Data sources (no hardcoded values):
  Panel A: results/noise_capacity_sweep.json — recall vs noise σ at K=100
  Panel B: results/triple_stress.json        — recall across 3 sequential class phases (σ=0.5)

Saved to grant_proposal/figures/prelim_results.pdf
"""

import json
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np

ROOT = Path(__file__).parent.parent.parent
sys.path.insert(0, str(ROOT))

# ── Load data ─────────────────────────────────────────────────────────────────

with open(ROOT / "results" / "noise_capacity_sweep.json") as f:
    raw_noise = json.load(f)

with open(ROOT / "results" / "triple_stress.json") as f:
    raw_stress = json.load(f)

# Panel A: convert string keys to typed keys
noise_data = {}
for model, kd in raw_noise.items():
    noise_data[model] = {}
    for k_str, sd in kd.items():
        k = int(k_str)
        noise_data[model][k] = {}
        for s_str, vals in sd.items():
            noise_data[model][k][float(s_str)] = vals

noise_vals = sorted({s for kd in noise_data.values() for sd in kd.values() for s in sd})
K_FIXED    = 100

# Panel B: triple_stress phase data
stress_results  = raw_stress["results"]
cumulative_n    = raw_stress["cumulative_n"]   # [160, 280, 400]
stress_config   = raw_stress["config"]
stress_sigma    = stress_config["noise"]        # e.g. 0.5

# ── Style ─────────────────────────────────────────────────────────────────────

COLORS = {
    "full":      "#2D6A4F",
    "tpc_flat":  "#3B82F6",
    "tpc_alone": "#8172B2",
    "cnn_flat":  "#C44E52",
    "lstm":      "#999999",
}
LABELS = {
    "full":      "PAM (tPC-KM-HDC)",
    "tpc_flat":  "tPC + flat KM",
    "tpc_alone": "tPC alone",
    "cnn_flat":  "CNN + flat KM",
    "lstm":      "LSTM",
}
LINES = {
    "full":      ("-",  "o", 2.5),
    "tpc_flat":  ("--", "s", 1.6),
    "tpc_alone": ("-.", "^", 1.6),
    "cnn_flat":  (":",  "v", 1.6),
    "lstm":      (":",  "D", 1.6),
}
MODEL_ORDER = ["full", "tpc_flat", "tpc_alone", "cnn_flat", "lstm"]
Y_TICKS = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]

def style_ax(ax):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.set_ylim(-0.15, 1.09)
    ax.set_yticks(Y_TICKS)
    ax.yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1, decimals=0))
    ax.tick_params(labelsize=8)
    ax.grid(axis="y", alpha=0.22, lw=0.6)

# ── Figure ────────────────────────────────────────────────────────────────────

fig, (ax_a, ax_b) = plt.subplots(1, 2, figsize=(7.2, 2.9), sharey=True)
fig.subplots_adjust(wspace=0.08)

# ─── Panel A: recall at σ=0.4, K=100 (bar chart) ─────────────────────────────
# The full noise sweep is uninformative in print (all methods saturate below
# σ=0.2 and collapse above σ=0.6); the discriminating point is σ=0.4.
# TODO: consider a third panel with the CORe50-NI online-accuracy curve once
# those results are exported to results/ — a stronger headline than MNIST.

SIGMA_STAR = 0.4
bar_keys = [k for k in MODEL_ORDER
            if k in noise_data and K_FIXED in noise_data[k]
            and SIGMA_STAR in noise_data[k][K_FIXED]]
bar_vals = [noise_data[k][K_FIXED][SIGMA_STAR].get("exact_recall", np.nan) for k in bar_keys]
bar_stds = [noise_data[k][K_FIXED][SIGMA_STAR].get("exact_recall_std", 0.0) for k in bar_keys]

xs = np.arange(len(bar_keys))
ax_a.bar(xs, bar_vals, yerr=bar_stds, width=0.62, capsize=3,
         color=[COLORS[k] for k in bar_keys],
         error_kw=dict(lw=0.8, ecolor="black", alpha=0.6))
for x, v in zip(xs, bar_vals):
    ax_a.annotate(f"{v:.0%}", (x, v), textcoords="offset points",
                  xytext=(0, 6), ha="center", fontsize=7)

style_ax(ax_a)
ax_a.set_ylim(0, 1.14)
ax_a.set_xticks(xs)
ax_a.set_xticklabels([LABELS[k] for k in bar_keys], rotation=20, ha="right", fontsize=7)
ax_a.set_ylabel("Exact recall", fontsize=9)
ax_a.set_title(f"(A)  Exact recall at σ = {SIGMA_STAR}  (K = {K_FIXED})",
               fontsize=9, fontweight="bold")

# ─── Panel B: recall across class phases (triple_stress) ─────────────────────

x_vals = cumulative_n   # [160, 280, 400] cumulative training items seen

for key in MODEL_ORDER:
    if key not in stress_results:
        continue
    phases = stress_results[key]   # list of dicts, one per phase
    vals = [p["exact_recall"] for p in phases]
    ls, mk, lw = LINES[key]
    ax_b.plot(x_vals, vals, ls, marker=mk, lw=lw, ms=5,
              color=COLORS[key], label=LABELS[key])

style_ax(ax_b)
ax_b.set_xlabel("Concepts seen (cumulative items)", fontsize=9)
ax_b.set_ylabel("")          # shared axis
ax_b.set_title(f"(B)  Continual multi-class learning  (σ = {stress_sigma})",
               fontsize=9, fontweight="bold")
ax_b.set_xticks(x_vals)
ax_b.legend(fontsize=7, loc="lower left", frameon=False)

# ── Save ─────────────────────────────────────────────────────────────────────

out = ROOT / "grant_proposal" / "figures" / "prelim_results.pdf"
fig.savefig(out, bbox_inches="tight", dpi=200)
plt.close(fig)
print(f"Saved → {out}")
