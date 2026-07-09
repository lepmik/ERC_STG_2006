# WoM-BaM World Models in Brains and Machines

From Normative Hippocampus Models to Robust Planning in Artificial Intelligence and back

Tristan Manfred Stöber

## A marvellous feat of our brain: Extracting structure from sequential observation

## Fundamental question: How to robustly represent a dynamic world?

## **C**lone-**S**tructured **C**ausal **G**raphs learn robust representations

preparatory work gradient-based CSCG

Nikzad, …, Stöber, in preparation

key innovation: modularity

#### Dreamer3 leads across tasks ... but fails in Memory Maze.

#### Objectives & Team

## 1) **Understand** - why do robust representations (not) emerge?

empirical

analytical

How are representations related to performance?

Representation learning as dynamical system Memory Maze testbench

A mathematical microscope for an a-priori understanding

Sieber et al., NeurIPS (2024)

## 2) **Build** - agents that act in dynamic environments

## Massive CA1 recordings in dynamic environment

Unpublished data by Tom McHugh (RIKEN)

miniscope ~ 200-500 cells each

**X X X** 25 animals recorded

**X X**

data transferred

#### arenas

linear track, left/right

open fields + objects

elevated plus maze

trace fear conditioning

tone associations

**11** different tasks/contexts in total

## 3) **Validate** model against hippocampal data

Do internal representations explain behavior?

#### Qualifications

#### documented expertise in key domains

**Stöber** et al., PLoS Comput. Biol. (2025) Neurosci. Biobehav. Rev. (2021) Lepperød, **Stöber**, et al., PLoS Comput. Biol. (2023) Pochinok, **Stöber**, et al., Nat. Commun. (2024) Alexander, …, **Stöber**, et al., J. Neuro. (2025) Lehr, …, **Stöber**, Hippocampus. (2023) Buccino, **Stöber**, et al., BIOCAS (2016)

**Stöber** et al., Commun. Biol. (2023)

Lehr, ..., **Stöber**,

Lehr & **Stöber**, PNAS (2021)

**Stöber** et al., Hippocampus (2020)

Vieth, **Stöber**, Triesch, Front. Neuroinform. (2021)

data analysis artificial neural networks

conceptual

#### leadership & independence

6 articles without PhD supervisor 3 articles as last author

supervision: 1 PhD, 4 MSc, 5 assistants, 12 interns

>600k Euro raised since PhD

independent fellowships (2)

#### peer-recognition:

- Johanna Quandt Young Academy, Frankfurt
- Young Academy of Norway

## Impact: From biological insight to artificial foresight

#### neuroscience

reinterpret hippocampal circuit

#### artificial intelligence

reliable and data-efficient algorithms

## WoM-BaM is at the center of the next NeuroAI frontier

Visual system and ConvNets

Dopamine and Reinforcement Learning

Hippocampus and World Models

Thank you!

# Backup slides

# Dreamer may have flawed representations

# Lack of orthogonalization in RNN and Transformer architectures

Fast and modular CSCG with a gradient-based reimplementation

# Obj. 2: From gradCSCG to a brain-inspired hybrid planning architecture

#### WP2.1: Improve scaling

- problem: clones are pre-initialised inefficient!
- solution: sparsity regularizer on emission matrix
- speed: mask inactive clones

CSCG O C

WP2.2: Combine gradCSCG with RNN

# Obj. 2: From gradCSCG to a brain-inspired hybrid planning architecture

WP2.3: Graph-augmented planning

Combining arenas and stimuli allows to address fundamental

# 11 tasks/contexts

- 1. Linear Track Exploration (Left)
- 2. Linear Track Exploration (Right)
- 3. Open Field Exploration
- 4. Elevated Plus Maze
- 5. Object Location Recognition
- 6. Novel Object Recognition
- 7. Trace Fear Conditioning (TFC) Learning
- 8. TFC Retrieval Test
- 9. Linear Track with Tone Association
- 10. TFC Learning Boost Session
- 11. Long-Term TFC Retrieval Test

# Team + infrastructure + collaborators

Compute

#### Collaborators

Tom McHugh

Dileep George

data CSGC

Alexander Ecker

deep learning

Andrew Lehr

neuronal geometry

| Objectives and work packages |                                                            | Activity<br>lead | Year : 2027 | 5    | Year 3<br>2029 | Year 4<br>2030 | Year 5<br>2031 |
|------------------------------|------------------------------------------------------------|------------------|-------------|------|----------------|----------------|----------------|
| Obj. 1                       | MiniGrid memory maze as testbench for internal represent   | ations           |             |      |                |                |                |
| WP1.1                        | Implementing the MiniGrid Memory maze                      | Ph.D. 1          | M1.1        |      |                |                |                |
| WP1.2                        | Comparing models in MiniGrid Memory maze                   | Ph.D. 1          |             | M1.2 |                |                |                |
| WP1.3                        | Theoretical analysis via Dynamical Systems Framework       | Ph.D. 1          |             |      |                | M1.3           |                |
| Obj. 2                       | Developing a brain-inspired hybrid planning architecture   |                  |             |      |                |                |                |
| WP2.1                        | Scalable and Dynamic CSCG through Learnable Components     | PI               |             | M2.1 |                |                |                |
| WP2.2                        | Hybrid Architectures for Flexible Temporal Integration     | PI               |             |      | M2.2           |                |                |
| WP2.3                        | Graph-Augmented Planning in Model-Based RL                 | PI               |             |      |                | N              | 12.3           |
| Obj. 3                       | Testing and explaining hippocampal activity in dynamic env | ironments        |             |      |                |                |                |
| WP3.1                        | Preprocessing and Activity Extraction from Miniscope Data  | Ph.D. 2          |             | M3.1 |                |                |                |
| WP3.2                        | Characterizing Hippocampal Representations                 | Ph.D. 2          |             |      | M3.2           |                |                |
| WP3.3                        | Normative models of hippocampal activity in complex env.   | Ph.D. 2          |             |      |                | M3.3           |                |
|                              | Project management and dissemination                       |                  |             |      |                |                |                |
|                              | Continous risk and quality management                      | PI & Team        |             |      |                |                |                |
|                              | Onboarding and technical setup                             | PI               |             |      |                |                |                |
|                              | Consolidation of findings                                  | PI               |             |      |                |                |                |
|                              | Offboarding and documentation                              | PI & Team        |             |      |                |                |                |
|                              | Dissemination                                              | PI & Team        |             |      |                |                |                |