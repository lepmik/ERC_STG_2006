# ERC Starting Grant 2026 — Reviewer Feedback
## FIND: Flexible Intelligence through Neurocomputational Design
### PI: Dr. Mikkel Elle Lepperød — Simula Research Laboratory

---

> [!NOTE]
> This review is structured following ERC evaluation criteria: (1) Ground-breaking nature and ambition of the research, (2) PI intellectual capacity and creativity, and (3) Methodology and feasibility. I adopt the stance of a **strict but constructive PE6 panel reviewer** familiar with machine learning, neuro-inspired AI, and memory-augmented architectures.

---

## Overall Assessment

**Verdict: Strong proposal with a compelling vision, but several structural and argumentative weaknesses that could be fatal at Step 1 if not addressed.**

The proposal tackles a genuinely important problem — bridging the gap between current AI's shallow temporal processing and the brain's lifelong memory and causal reasoning capabilities. The PAM architecture is an interesting integration of predictive coding, HDC, and external memory. However, the proposal suffers from **(1)** overclaiming relative to the evidence provided, **(2)** insufficient differentiation from a crowded field that has evolved rapidly, **(3)** a narrative that risks reading as a "system-building" exercise rather than a hypothesis-driven scientific programme, and **(4)** several feasibility concerns in the most ambitious work packages.

---

## 1. Ground-Breaking Nature and Ambition

### Strengths
- The **core vision** is compelling: unifying predictive coding, distributed memory, and active inference into a single architecture is genuinely novel and scientifically ambitious.
- The **positioning table** (Table 1) is effective and clearly shows a gap that PAM fills. The four-axis comparison (External Memory × Iterative Inference × Symbolic Binding × Active Inference) is a clean framing device.
- The **biological motivation** is well-grounded. The PI's neuroscience background is a genuine differentiator — this is not another "brain-inspired" proposal from someone who has never recorded a neuron.
- The **desert ant analogy** (200,000 steps vs. 2,000-step benchmarks) is a powerful rhetorical device that immediately conveys the scale of the ambition.

### Weaknesses

#### 1.1 The "Novelty by Combination" Problem
> [!WARNING]
> **Critical issue.** The novelty claim rests almost entirely on the *combination* of four existing ideas (tPC, HDC, Kanerva machines, active inference), each of which is well-established. Step 1 reviewers — who are generalists — may read this as incremental engineering rather than a conceptual breakthrough. The proposal must articulate more clearly **what new scientific understanding** emerges from this combination that is not predictable from the components.

**Suggestion:** Articulate a specific, testable **prediction** that PAM makes which no component system can make alone. For example: "The combination of HDC binding with iterative inference should produce a phase transition in recall capacity at a critical noise level — a prediction that does not follow from either HDC or predictive coding theory alone." This transforms the proposal from system-building into hypothesis-testing.

#### 1.2 Underspecified "Shallow Brain Hypothesis"
The proposal invokes the "shallow brain hypothesis" (Suzuki, 2023) as foundational but never unpacks what this means for PAM's architecture or what testable predictions it makes. A reviewer unfamiliar with this specific reference will be left wondering:
- What exactly is "shallow" about PAM? The architecture diagram shows multiple processing stages, routing, iterative inference — this does not look shallow.
- How does the shallow brain hypothesis constrain the design space? What architectural choices would violate it?

**Suggestion:** Either make the shallow brain hypothesis load-bearing (with explicit architectural constraints it imposes) or drop it and focus on the concrete mechanisms.

#### 1.3 Rapid Field Movement — Missing Key References
> [!IMPORTANT]
> The state-of-the-art review has notable gaps for a 2026 submission:

- **No mention of modern context-extension methods** for transformers (RoPE scaling, YaRN, ring attention, infini-attention). The claim "transformers forget beyond their context window" is increasingly outdated — models with 1M+ token contexts exist. The proposal needs to engage with *why* these approaches are insufficient rather than dismissing transformers wholesale.
- **No engagement with retrieval-augmented generation (RAG) + LLMs** as a competing paradigm for long-term memory. The single RAG citation (Lewis 2020) is 6 years old. Modern agentic RAG systems (e.g., MemGPT, Letta) explicitly tackle the long-term memory problem.
- **No mention of Mamba-2, xLSTM, RWKV, or other linear-attention/SSM variants** that have emerged as strong competitors for long-range tasks.
- **Missing discussion of Test-Time Training (TTT)** and similar approaches that learn at inference time — conceptually similar to PAM's iterative inference.
- **World model literature** is thin: no mention of GAIA-1, UniSim, or the video prediction line of work that addresses causal world modelling at scale.

The lack of engagement with these approaches will raise red flags with any ML-oriented reviewer.

#### 1.4 The "Locked Door" Motivating Example is Too Simple
The building exploration example (floor 3 door, floor 1 key) is used to motivate the entire programme, but it's a problem that hierarchical RL with hindsight experience replay (Andrychowicz et al., 2017 — which you cite!) already addresses. The proposal needs a motivating example that clearly distinguishes PAM's capabilities from existing solutions.

**Suggestion:** Use a more demanding example that requires *compositional causal reasoning* over long horizons — something that showcases all three pillars simultaneously. The Factorio production chain example from WP3 would actually be much more compelling as the opening motivator.

---

## 2. Principal Investigator — Intellectual Capacity and Creativity

### Strengths
- **Strong and coherent trajectory** from experimental neuroscience (Science Advances, PLoS Comp Bio with Kording) to neuro-inspired AI (NeurIPS, eLife). This is not a bolted-on interdisciplinary profile — the progression is organic and compelling.
- **Genuine lab-building achievement**: going from postdoc to leading a group of 3 PhDs + 1 postdoc with publications at top venues is impressive for an StG-stage career.
- **NORA Award** (2025) is a strong signal of national recognition.
- **Supervision track record** (2 PhDs completed, graduates at Stanford) is strong for this career stage.
- **International collaboration network** is excellent (Kording/Penn, Richards/Mila, Kumar/KTH, Leutgeb/UCSD).

### Weaknesses

#### 2.1 No First/Senior-Author ML Publication at a Top-Tier ML Venue
> [!WARNING]
> **This is a significant gap for a PE6 proposal.** The publication list is strong in neuroscience (Science Advances, PLoS Comp Bio, eLife) and includes one NeurIPS paper as senior author. However, the NeurIPS paper is on place cell representations — computational neuroscience, not machine learning architecture. For a proposal that claims to build the next generation of AI architectures, the absence of a publication demonstrating ML system-building expertise (e.g., at ICML, ICLR, or NeurIPS ML track) is notable.

The CV demonstrates that the PI can do rigorous neuroscience and supervise good students. The open question is whether the PI has the systems engineering expertise to build and benchmark complex ML architectures at scale.

**Suggestion:** If the PI has any ML engineering outputs (e.g., open-source codebases with adoption, benchmark results, technical reports), these should be highlighted. Alternatively, the postdoc hire should be framed as explicitly filling this gap — and the postdoc's expected profile should be described in more detail.

#### 2.2 50% PI Time Commitment
The proposal states PI at 50% on the ERC project. For an ambitious, integrative programme that requires tight coordination across three WPs, this may read as insufficient. What occupies the other 50%? The adjunct professorship (20%) is mentioned, and Simula baseline funding implies other group activities. Step 2 reviewers will probe this.

**Suggestion:** Clarify what the other 50% entails, and argue that activities are synergistic (e.g., teaching a NeuroAI course that feeds into recruitment, or other projects that share infrastructure).

---

## 3. Research Methodology and Feasibility (Step 2)

### Strengths
- The **four-tier benchmark hierarchy** is excellent — it shows methodological maturity and awareness that ambitious claims need incremental validation. The "decision gate" between Tiers 2 and 3 is particularly well-designed.
- **Success criteria** are quantitative and falsifiable (≥90% recall at σ=0.3, MSE within 10% of PatchTST, r>0.7 correlation, etc.). This is above average for ERC proposals.
- The **risk table** is honest and comprehensive. The structured ablation ladder for orchestration mechanisms is a particularly thoughtful contingency.
- **Collaborations** are well-justified with specific tangible contributions and co-authored history.

### Weaknesses

#### 3.1 Preliminary Results Are Too Preliminary
> [!CAUTION]
> **The central evidence — 98.1% recall on MNIST at σ=0.4 — is a toy-scale result being asked to carry a €2M, 5-year programme.** MNIST recall with 100 items is not a challenging benchmark by 2026 standards. The 3.75× forgetting reduction is more interesting but is shown on "three sequential class phases" — again, very small scale.

The gap between these results and the ambitions of WP3 (Minecraft, Factorio, 10,000+ step horizons) is enormous. A sceptical reviewer will question whether the team can actually bridge this gap.

**Suggestion:**
- If possible before submission, run PAM on at least one Tier 2 benchmark (ETT or Weather) and report results, even if imperfect. A "PAM achieves competitive MSE on Weather-720 despite not being tuned for forecasting" is worth more than a perfect MNIST number.
- At minimum, add a paragraph explicitly acknowledging the scale gap and explaining the concrete technical steps that bridge toy and real benchmarks.

#### 3.2 WP2 Is Overloaded and Underspecified
WP2 attempts to integrate: (a) action-augmented temporal predictive coding, (b) subspace-based compositional reasoning with HDC, (c) causal world model learning through active inference, and (d) comprehensive orchestration ablations. Any one of these is a full PhD project. All four in a single WP with one postdoc (and PI support) in Years 2-4 is extremely ambitious.

Specific concerns:
- **T2.2 (Compositional reasoning on ARC)** is essentially its own research agenda. ARC is unsolved by the ML community; claiming PAM will achieve >80% compositional retrieval accuracy on novel combinations is a bold claim with no supporting evidence.
- **T2.3 (Causal discovery through interventions)** — the description is hand-wavy. How exactly does the agent execute "targeted interventions" in Minecraft? What's the action space for interventions? How do you distinguish causal from correlational structure in a noisy RL environment?
- The connection between T2.1-T2.4 is unclear: are these sequential (T2.1 feeds T2.2 feeds T2.3) or parallel? The Gantt chart would help clarify, but the text doesn't make it obvious.

**Suggestion:** Consider narrowing WP2 to its most distinctive contribution. I would argue T2.2 (compositional reasoning via HDC) is the most novel and should be the centerpiece, with T2.1 and T2.3 serving as supporting tasks. T2.4 (ablations) is important but could be distributed across WPs.

#### 3.3 WP3 Has Very High Failure Risk with Insufficient Contingency
> [!WARNING]
> WP3 proposes to build an agent that plays Minecraft and Factorio with a three-level policy hierarchy, trained via a combination of PPO, HER, and HDC symbolic planning. This is an **extremely ambitious** systems engineering challenge. State-of-the-art Minecraft agents (STEVE-1, Voyager, GROOT) are built by large teams at major labs with enormous compute budgets.

Specific concerns:
- **PhD2 starts Year 2** and is expected to deliver T3.1-T3.3 in Years 3-5. A PhD student building a novel agent architecture for Minecraft and Factorio from scratch — including environment integration, curriculum design, and three-level hierarchical RL — is unrealistic in 3 years.
- The **success criterion** of "1.5× throughput vs. DreamerV3 on Factorio" is extremely ambitious. DreamerV3 is a well-optimised system from a world-class lab. Achieving 1.5× improvement with a novel, less-optimised architecture is not credible without substantial engineering investment.
- **Factorio as a benchmark** is very new (Kant et al., 2025). There may not be sufficient community infrastructure for reproducible comparison.
- The **contingency** (fallback to Memory Maze) is good but should be emphasised more prominently. If I were reviewing, I'd want to see Memory Maze positioned as a primary benchmark with Minecraft/Factorio as stretch goals.

**Suggestion:** Reframe WP3 with a clearer hierarchy of ambition:
1. **Must achieve:** Memory Maze at 10K steps with clear improvement over baselines
2. **Should achieve:** Simplified Minecraft tasks (navigation, basic crafting)
3. **Stretch goal:** Full Factorio production chains and complex Minecraft scenarios

#### 3.4 The "Orchestration" Design Space Is Too Open
The proposal lists **six** orchestration mechanisms (message passing, NCA, hypernetwork, predictive routing, competitive collaboration, energy-based). While framing these as an "ablation ladder" is clever, it also signals that the PI doesn't yet know which approach will work. For a €2M programme, this degree of design uncertainty is concerning.

**Suggestion:** Commit to NCA + message passing as the primary mechanisms (you have published results on both) and frame the others as theoretical alternatives to be explored if primary approaches fail. This reads as more focused.

#### 3.5 Compute Justification Needs Strengthening
The proposal requests additional funding for compute (~€0.5M based on the requirements doc) but the justification is buried in the host institution section ("~10⁵ GPU-hours based on ~800 GPU-hours per DreamerV3-scale training run × ~100 experiments"). This is a back-of-envelope estimate. Step 2 reviewers will want:
- Breakdown by WP
- Comparison with actual costs (what does 10⁵ hours on A100 cost?)
- Why Sigma2/eX3 allocation is insufficient

---

## 4. Structural and Writing Issues

### 4.1 Part I Does Not Stand Alone
> [!IMPORTANT]
> At Step 1, reviewers see **only** Part I + CV. Part I currently reads as an extended abstract that assumes the reader will see Part II. Critical details — the four-tier benchmark strategy, the specific success criteria, the team structure — only appear in Part II. If a Step 1 reviewer doesn't see these, they may judge the proposal as vague.

**Suggestion:** Part I needs to be self-contained. Move at least: (a) a summary of the benchmark strategy, (b) the team composition (PI + PD + 2 PhDs), and (c) 2-3 headline success criteria into Part I. This may require cutting some of the state-of-the-art discussion, which is currently too long relative to the objectives/strategy section.

### 4.2 The Abstract Buries the Lead
The abstract opens with "In the next decade, AI must make the leap..." — a generic statement that could appear in any AI proposal. The first sentence should immediately convey what is unique about FIND. Consider opening with the specific gap and PAM's solution.

**Suggestion:** "Current AI systems cannot reliably recall and reason over information separated by thousands of timesteps — a capability biological brains achieve routinely. FIND develops PAM, a novel architecture that [...]"

### 4.3 Main Hypothesis Is Not Falsifiable As Stated
"Modular specialization can emerge naturally from predictive principles and provide long-term memory support for active inference and adaptive learning, enabling causal world models without catastrophic forgetting."

This is a compound statement with at least four sub-claims. If modular specialisation emerges but doesn't support causal world models, has the hypothesis been falsified? The hypothesis needs to be decomposed or sharpened.

**Suggestion:** State one crisp, falsifiable central hypothesis and derive the WPs as tests of it. E.g.: "Predictive coding over distributed memory slots is both necessary and sufficient for long-horizon causal reasoning in open-ended environments."

### 4.4 Inconsistent Use of "PM" vs "PAM"
The text alternates between "PM" (e.g., T1.1: "PM must achieve ≥90% exact recall") and "PAM" (the defined acronym). This is confusing — is PM a sub-component? An earlier version of the system? This needs to be consistent throughout.

### 4.5 The "Theoretical Approach" Paragraph Is Overloaded
[01-part-I.tex](file:///Users/mikkel/Github/ERC_stg_2026/grant_proposal/01-part-I.tex#L89) contains a single paragraph that tries to describe the entire PAM architecture including Gumbel-softmax routing, ProgramEncoder, four specialist modules, iterative refinement, temporal predictive coding, and active inference. This is too dense. Break it into sub-points or a numbered list.

---

## 5. Minor Issues

| Issue | Location | Suggestion |
|---|---|---|
| `\setstretch{0.90}` in [main.tex](file:///Users/mikkel/Github/ERC_stg_2026/grant_proposal/main.tex#L172) reduces line spacing below single spacing — technically violates ERC formatting requirements | main.tex L172, 176, 189 | Verify this is acceptable; ERC guidelines say "single" spacing |
| The Gantt chart is included by `\input{figures/gantt}` but not visible in Part II text — milestones are not discussed | [03-part-II.tex](file:///Users/mikkel/Github/ERC_stg_2026/grant_proposal/03-part-II.tex#L101) | Add milestone text accompanying the Gantt |
| References from Part I and Part II are in separate `refsection` environments — check they don't duplicate numbering | [main.tex](file:///Users/mikkel/Github/ERC_stg_2026/grant_proposal/main.tex#L164-L193) | Verify compiled PDF |
| "Bio-inspired neural networks for AI application" project listed in CV (16 MNOK, 2020-2026) — reviewer may question overlap with FIND | [02-cv-trackrecord.tex](file:///Users/mikkel/Github/ERC_stg_2026/grant_proposal/02-cv-trackrecord.tex#L93) | Explicitly distinguish scope in Funding ID section |
| The FRIPRO rejection for FIND is disclosed — good practice, but the proposal should explain what changed | [03-part-II.tex](file:///Users/mikkel/Github/ERC_stg_2026/grant_proposal/03-part-II.tex#L163-L168) | Add 1 sentence on what's new in the ERC version |
| Career break (parental leave) mentioned but PhD year isn't clear — when was PhD awarded? | [02-cv-trackrecord.tex](file:///Users/mikkel/Github/ERC_stg_2026/grant_proposal/02-cv-trackrecord.tex#L22) | 2020 is listed — verify ERC StG eligibility window |
| "PM" used inconsistently with "PAM" in WP1 task descriptions | [03-part-II.tex](file:///Users/milkel/Github/ERC_stg_2026/grant_proposal/03-part-II.tex) | Unify terminology |
| The pop figure caption mentions "overly simple ANNs and overly complex biological neural networks" — this is dismissive of both fields | [pop-figure.tex](file:///Users/mikkel/Github/ERC_stg_2026/grant_proposal/figures/pop-figure.tex#L4) | Reword to be more precise about what aspects are simple/complex |

---

## 6. Summary of Recommended Actions

### Must-Fix (Likely Fatal if Unaddressed)

| # | Issue | Priority |
|---|---|---|
| 1 | **Make Part I self-contained**: include team, benchmark summary, and headline success criteria | 🔴 Critical |
| 2 | **Update state-of-the-art** to engage with 2024-2026 advances (long-context transformers, modern SSMs, agentic RAG, TTT) | 🔴 Critical |
| 3 | **Strengthen preliminary results** — run at least one non-toy benchmark before submission | 🔴 Critical |
| 4 | **Sharpen the central hypothesis** into a single falsifiable statement | 🔴 Critical |
| 5 | **Fix PM/PAM terminology inconsistency** | 🔴 Critical |

### Should-Fix (Significantly Strengthens Proposal)

| # | Issue | Priority |
|---|---|---|
| 6 | Narrow WP2 scope or add a second postdoc to justify ambition | 🟡 Important |
| 7 | Reframe WP3 with tiered ambition (must/should/stretch) | 🟡 Important |
| 8 | Articulate a specific prediction unique to the PAM combination | 🟡 Important |
| 9 | Address the PI's ML engineering credibility gap | 🟡 Important |
| 10 | Rewrite abstract with stronger opening | 🟡 Important |
| 11 | Check `\setstretch{0.90}` against ERC formatting rules | 🟡 Important |

### Nice-to-Fix (Polish)

| # | Issue | Priority |
|---|---|---|
| 12 | Commit to primary orchestration mechanisms, reduce design space | 🟢 Minor |
| 13 | Strengthen compute justification with per-WP breakdown | 🟢 Minor |
| 14 | Add milestones to accompany Gantt chart | 🟢 Minor |
| 15 | Clarify overlap with existing RCN projects | 🟢 Minor |
| 16 | Break up the dense "Theoretical approach" paragraph | 🟢 Minor |

---

> [!TIP]
> **Overall, this is a proposal with genuine scientific substance — the PI has a unique profile bridging neuroscience and AI, the PAM architecture is a novel combination, and the preliminary results (while toy-scale) demonstrate that the core mechanism works. The key risk is that it reads as a systems-engineering project ("we will build X") rather than a hypothesis-driven scientific programme ("we will test whether X"). Sharpening the narrative around testable predictions, updating the baselines to 2026 standards, and making Part I self-contained would significantly improve the chances of passing Step 1.**
