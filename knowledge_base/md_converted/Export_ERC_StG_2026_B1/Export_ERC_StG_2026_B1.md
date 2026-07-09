## **ERC Starting Grant 2026 Part B1<sup>1</sup>**

## **Wo**rld **M**odels in **B**rains **a**nd **M**achines:

# From Normative Hippocampus Models to Robust Planning in Artificial Intelligence and Back

## WoM-BaM

## **Cover Page:**

- Tristan Manfred Stöber
- Georg-August-Universität Göttingen Stiftung Öffentlichen Rechts
- 60 months

A hallmark of intelligence is the ability to mentally simulate future scenarios and plan actions accordingly. This cognitive ability requires an internal model of the world. How the brain constructs, and uses such a world model is a fundamental, yet unresolved question. Normative models in neuroscience can explain the emergence of abstract representations from sequential observations, but their rigid formulation restricts them to static toy models. In artificial intelligence, world model based agents have matured significantly. However, despite impressive successes, leading state-of-the-art agents fail at long-horizon navigation and, as recent findings show, their internal dynamics do not match the structured representations observed in the brain, suggesting a fundamental architectural gap.

This project addresses world model learning in both brains and machines upfront with a cross-disciplinary approach that explains failure modes of state-of-the-art agents, overcomes their limitation with a novel brain-inspired architecture, and finally validates artificial world models against a unique dataset of brain activity recorded from mice navigating 11-different environments.

Key deliverables are a) a precise characterization of inductive biases required for well-structured internal representations, b) a new model class that pushes the frontiers for world model based reinforcement learning and that serves as powerful normative model for brain dynamics across contexts, and c) an in-depth analysis of hippocampal activity to reveal how the brain creates and reuses internal representations.

This project establishes a virtuous NeuroAI cycle: Insights from neuroscience will help to build more robust and interpretable AI, which in turn will serve as a powerful computational framework to deepen our understanding of how the brain builds its model of the world.

This project requires a cross-panel review due to its deeply integrated, cross-domain nature between Systems Neuroscience and Artificial Intelligence. On one hand, it engineers a novel, brain-inspired hybrid AI architecture to advance reinforcement learning, requiring evaluation by a Computer Science panel to assess its technical novelty and performance. On the other hand, it uses these AI agents as normative models to explain neural dynamics in a unique, large-scale dataset of mouse hippocampal activity, demanding review by a Neuroscience panel to validate the biological comparisons and the project's potential to advance our understanding of brain function. A single panel would lack the dual expertise to properly assess the project's core innovation: the bidirectional integration of insights from both domains.

1 Instructions for completing Part B1 can be found in the '*Information for Applicants to the Starting and Consolidator Grant 2026 Calls'*.

1

#### Part I of the Scientific Proposal (max. 5 pages, references do not count towards the page limit).

## Ground-breaking Nature & Impact

Evaluating future scenarios by mental time travel is a hallmark of intelligence and requires an internal representation of the world. To build such a world model, also called cognitive map, brains or artificial agents have to infer structural knowledge from sequential interactions with the environment. Understanding and reengineering world model learning is a fundamental problem in both neuroscience1-5 and artificial intelligence (AI)6-8. We postulate that the weakness of state-of-the-art (SOTA) reinforcement learning agents long-horizon tasks9,10 navigation stems from a fundamental flaw in their world model: In contrast to the brain these algorithms fail develop well-structured to representations.

World Models in Brains and Machines: From Normative Hippocampus Models to Robust Planning in Artificial Intelligence and Back

Obj. 2: Improve navigation by brain-inspired world model architecture

- Increase efficiency with on-demand recruitment of hidden states
- Hybrid architecture to combine temporal and structural knowledge
- Establish graph-augmented planning in model-based RL

Fig. 1: Project summary. The WoM-BaM project integrates insights on information processing in the hippocampus and navigation in artificial agents to understand how brains and machines can efficiently learn world models.

In this project my team and I will (Obj. 1) use both insights and tools from neuroscience to investigate the inductive biases leading to these shortcomings, (Obj. 2) develop a novel network architecture inspired by a leading normative hippocampus model to improve internal representations at scale, and (Obj. 3) validate our model against a novel biological data set from rodents that provide direct access to biological world models in dynamic environments.

By establishing a virtuous circle between neuroscience and artificial intelligence (Fig. 1), this project provides a powerful new framework for understanding how world models are formed and utilized, while also delivering a new generation of autonomous systems which are more capable, interpretable, and data-efficient

#### State-of-the-art & Open Ouestions

Well-structured internal representations allow biological and artificial agents to pick shortcuts on routes never taken and to provide guidance in situations where trial-and-error learning would be fatal. Thus, understanding the inductive biases that favor the emergence of such representations is an outstanding

scientific challenge. Significant progress has been made both on biological<sup>2,11,12,4,13</sup> and artificial neural systems<sup>14-18</sup>. Here, we integrate the so-called Cloned-Structured-Causal-Graph (CSCG) algorithm<sup>19,20</sup> with the Dreamer family of reinforcement learning agents<sup>10,21-23</sup>. This specific focus is deliberate: Dreamer provides a powerful, state-of-the-art agent architecture and recent findings<sup>24</sup> establish CSCG as the leading normative model for how the hippocampus forms structured, map-like representations. Our goal is to merge Dreamer's performance with CSCG's representational efficiency.

The Dreamer architecture vividly demonstrates the power of world models in reinforcement learning, outperforming specialized algorithms across diverse domains with a single configuration<sup>3</sup>. Its success stems from a three-part design<sup>25</sup>, combining: 1) an encoder that compresses sensory input into a latent state, 2) a recurrent world model, typically a Gated-Recurrent Unit (GRU), that predicts future latent states, and 3) an actor-critic planner that learns a policy by sampling trajectories from the world model.

Fig. 2: Dreamer performs well in small environments, left, but fails in larger environments, right. Adopted from Pasukonis et al. (2022)

Despite its success, Dreamer fails at navigating large environments in

the so-called memory maze navigation task (Fig. 2), which correlates with deterioration of its internal representations. Furthermore, a recently published state-space model shows only limited improvements<sup>10</sup>. This highlights a critical knowledge gap: We do not know what kind of representations are learned in SOTA agents, which inductive biases guide the emergence of such representations, and how they affect

navigation strategies. In the mammalian brain, the hippocampus plays a key role in representing the environment. Here, place cells encode spatial position in an allocentric fashion with a sparse coding scheme. A typical place cell is active whenever an animal enters a certain location, creating a spatial field of cellular activity. Many studies have shown that this coding scheme generalizes to other modalities such as time?, sound?s, contextual information?9-3?, or even the position of other animals?3.34. However, questions remain, such as how are representations reused across multiple contexts with different task demands?

Fig. 3: CSCG discovers latent structure from sequential interaction. Adopted from George et al. (2021).

The CSCG algorithm demonstrates that the emergence of place cells is naturally linked to world model learning 19,20. It compresses a series of observation and action pairs into a higher order representation of its environment (Fig. 3). While technically an overcomplete Hidden Markov Model (HMM) with fixed emission matrix. CSCG learns to disambiguate contexts from aliased observations. Obeying the Markovian property - i.e. any subsequent state depends only on the current state - CSCG is forced to represent a novel context with a new clone among its hidden nodes. The graph emerging from this cloning operation provides a condensed map of the environment and is suitable for planning, consolidation and abstraction. However, while elegantly creating well-structured representations in static and relatively small environments, it is unclear how to distill the underlying inductive bias from CSCG and use

## this insight to create algorithms with explicit representations of large and dynamic environments.

Further, recent experimental findings corroborate the fundamental difference in how modern artificial neural networks and biological brains represent latent information<sup>34</sup>. When learning a context-dependent task activity in the hippocampus decorrelates between trials in a specific, ordered manner. This pattern is uniquely replicated by the CSCG algorithm but absent in standard Recurrent Neural Networks (RNNs), Long Short-Term Memory networks (LSTMs), and Transformer architectures. Based on these findings, we hypothesize that the SOTA agents may suffer from dense and poorly-structured representations. This defect may lead models to adopt brittle, sequential path-following strategies - storing information as "to get from blue to green, turn right here, then go straight" - which may suffice in small environments but whose complexity explodes as the maze size and number of objects increase. In stark contrast, the brain and the CSCG algorithm utilize sparse, decorrelated codes, which facilitate flexible navigation. We acknowledge ongoing robotics work within simultaneous-localization-and-mapping with overlapping intuition, but different objectives<sup>35,06</sup>.

## Objectives

This project is built upon a deeply integrated, interdisciplinary NeuroAI loop: we use insights and tools from neuroscience to understand a key limitation of SOTA agents in planning, alleviate these problems by designing a novel network architecture and then compare internal representations of our own and existing agents against a novel, unpublished hippocampal dataset expected to provide inspiration for further development.

Obj. I seeks to understand why state-of-the-art artificial intelligence (AI) agents fail at navigating large, complex environments. To investigate this, we will first create a new, simplified, and scalable virtual test environment called the MiniGrid Memory maze to systematically probe the limits of SOTA AI models. Going beyond measuring task success, we will use analytical tools from computational neuroscience to conduct an in-depth comparison of the agents' internal representations, determining whether they are learning flexible, map-like representations or simply memorizing sequential paths. We will also test whether this is reflected in the agent's navigation behavior, such as its ability to take novel shortcuts<sup>37,38</sup>. In particular, we will characterize internal representations both on the level of individual units with decoding

Fig. 4: Demo of MiniGrid Memory Maze. Random generation of environments. Agent (red arrow) has to navigate to randomly chosen objects (coloured circles) until timeout. Agent only partly observes the environment (light grey) and follows the action sequence (yellow dots) to current target (purple).

models<sup>39</sup> and the whole population, characterizing the geometry of the activity manifold<sup>40</sup>. Finally, a theoretical analysis using a dynamical systems framework<sup>41</sup> will be employed to gain a principled

understanding of why certain AI architectures develop more effective internal representations, providing a clear roadmap for designing more robust and efficient AI agents. Here, the key idea is that RNNs such as quasi LSTMs, state space models - of which CSCG is a subtype, and the attention mechanism, central in transformers, can be reformulated in a common dynamical systems language, allowing direct comparison and a clear dissection of inductive biases.

Obi. 2 aims to develop brain-inspired hybrid AI architecture by enhancing CSCG to make it more scalable and flexible (Fig. 5). Here, we build upon our preliminary results demonstrating that CSCG can be implemented as a gradient-based deep-learning module42-44. First, we introduce clone recruitment to flexible performance. For this purpose, we replace the fixed emission matrix with a neural module with competitive dynamics among its units (softmax activations)42,45. Second, inspired by the dual-process theory from psychology46, we combine a neuralized CSCG module with a standard RNN to create a hybrid CSCG-RNN system capable of both flexible temporal processing (system 1) and structured reasoning (system 2). Finally, we will integrate this network module into Dreamer agents, using symbolic graph-based searches (like A\*) on its internal map for long-horizon planning. We expect these algorithms to be drastically more sample-efficient and reliable47.

Obi. 3 closes the NeuroAI loop by testing the biological plausibility of the newly developed Al agents against real brain activity. To do this, we will utilize a unique, unpublished dataset of hippocampal brain activity recorded from mice performing 11 different tasks across 34 days. This dataset has been provided by my collaborator Tom McHugh uniquely for this purpose. First, we will process raw data to extract reliable single-neuron activity and precisely align it with the animals' behavior. Next, we analyze population activity to create a detailed characterization hippocampus adapts its internal representation as tasks and contexts change 48,49. This dataset is special for its clever combination of different and emotional states. environments example we can test whether internal

Fig. 5: Summary of Obj. 2 - developing a brain-inspired hybrid AI architecture. Based on preliminary data showing that CSCG can be trained with backpropagation, we improve the scalability of CSCG, pioneer a CSCG-RNN hybrid and finally integrate this into the Dreamer architecture.

representations are expanded or reused across two adjacent linear tracks, whether temporal information from trace-fear-conditioning is differentially encoded and whether repeated conditioning influences encoding of other environments. Finally, we will train our novel AI models, alongside existing ones, on a simulated version of the 11-task experiment using a modified version of the MiniGrid memory maze and compare artificial internal representations to biological data, evaluating which model best explains the flexible activity observed in the mouse brain and identifying areas for further improvement.

#### Qualification & interdisciplinary approach

As the principal investigator, my documented expertise in analyzing both biological and artificial neural networks as well as characterizing behavior with machine learning tools, allows me to lead and integrate these distinct research streams. The commitment to bridging disciplines and to training the next generation of interdisciplinary scientists is further demonstrated by my role as co-organizer and lead instructor of a course

on AI in Medicine at the University Hospital Frankfurt since 2023. My core competency is amplified by a team of world-leading collaborators: Dileep George (Google), the inventor of the CSCG algorithm, provides

mentorship based on his foundational expertise in normative models of world-model learning, alongside a valuable perspective on industrial impact. Tom McHugh (RIKEN) is a critical data-providing partner, mentor and expert on hippocampal circuitry. Locally, the project is supported by Alexander Ecker (CIDAS), who provides mentorship on AI and ensures smooth integration into the Göttingen research ecosystem, and Andrew Lehr (UMG), whose specialization in manifold analysis is vital for the quantitative evaluation of both biological and artificial neural

**Fig. 6: Summary of Obj. 3 - validating normative models against hippocampal activity.** Internal representations are extracted from a unique dataset of Miniscope recordings across 11 tasks and 34 days and compared against normative models performing comparable tasks in the MiniGrid environment.

representations. The soundness of these collaborations is grounded in a history of tangible engagements, including five co-authored articles with Andrew Lehr, a recent in-person research stay in the lab of Tom McHugh, formal mentorship via the CIDAS fellowship 2025 by Alexander Ecker, and jointly organized workshops with Dileep George.

## **Major Outcomes**

Understanding world model learning in brains and machines **holds an outstanding potential for science, technology and society**. Specifically, the WoM-BaM project will contribute to this emerging fundamental research frontier by: a) **understanding failure modes of current technology** and creating a **framework for translating inductive biases for explicit world model learning**, b) developing a novel brain-inspired **hybrid RNN-CSCG architecture**, which is both **flexible** and has **explicit and interpretable knowledge representations**, and c) outlining the **dynamics of world model learning and the continual incorporation of new information into existing representations** as well as identifying limitations of existing normative models for directing further knowledge gains.

These findings will broadly benefit the following domains: In **Neuroscience**, our newly developed normative model will provide a **unique vantage point to reinterpret hippocampal circuitry**. For example, many unexplained functional properties, such as input-timing dependent plasticity 52,53 may be involved by providing a mechanism for dynamic clone creation. However, it is not clear when exactly clones are created. In the field of **Artificial intelligence**, determining **inductive biases that favor well-structured representations** has been a long-standing challenge. Our project will make a major contribution by demonstrating that this is possible beyond toy models while maintaining flexibility. **Technology**: Our developments are strategically relevant for next‑generation smart and autonomous agents in robotics and embedded systems, where power budgets are tight and reliability is paramount. To this aim, we maintain close contact with the neuromorphic community <sup>54</sup> and plan to eventually port the project's inductive biases for parsimonious representations onto energy‑efficient substrates, enabling low‑latency autonomy on edge devices. **Society**: We develop artificial agents that plan over long horizons, reason counterfactually, and expose their internal state in a way that can be inspected and validated before deployment. This capability is directly relevant to regulated, safety‑critical settings where decisions must be transparent and reliable, such as in healthcare, manufacturing, mobility and public administration.

## **Curriculum vitae and Track Record (max. 4 pages)**

## **PERSONAL DETAILS**

Stöber, Tristan Manfred

ORCID: 0000-0003-3853-0608

Website: https://tristanstoeber.github.io/

## **Education and key qualifications**

25/06/2021 PhD, Faculty of Mathematics and Natural Sciences, University of Oslo, Norway Supervisors: Prof.Marianne Fyhn, Prof. Arvind Kumar, Prof. Trygve Solstad, Prof. Jill Leutgeb

2016 MSc. Biology, University of Freiburg, Germany - 1.3/*very good on scale* from 1.0-6.0 2012 BSc. Biosciences, University of Münster, Germany - 1.3/*very good on scale* from 1.0-6.0

## **Current position(s)**

- 2025 present CIDAS Research Fellow, Department of Computer Science and Campus Institute Data Science, University of Göttingen, Germany | Independent research on world models in brains and machines
- 2023 present Research fellow (part-time), Department of Neurology, University Hospital Frankfurt, Germany | Lead organizer of *AI in Medicine* program, University Hospital Frankfurt, ~ 30 students/year

## **Previous positions**

- 2022 2025 Think@Ruhr Research Fellow, Institute for Neural Computation, Ruhr University Bochum, Germany | Independent research on hippocampal computation
- 2020 2022 Research Associate, Prof. Jochen Triesch, Frankfurt Institute for Advanced Studies, Germany
- 2020 2020 Head Engineer, Centre for Integrative Neuroplasticity, University of Oslo, Norway
- 2016 2017 Visiting Scientist, Prof. Jill Leutgeb, University of California San Diego, USA

## **Management & Leadership experience**

- 2017 Supervisor of (all/done): PhD Co-supervisor (1/0), Research Assistant (3/2), MSc (3/2), Interns (8/8)
- 2023 Board member, GRADE Graduate Research Academy of the Goethe University Frankfurt
- 2022 2024 Software architect & scientific advisor for brian2lava, a Brian2 interface for Intel's Lava-based neuromorphic computing.
- 2024 Course Science Communication, Main-Campus-Academy
- 2023 Course Time and Project Management for Postdocs, Main-Campus-Academy
- 2023 Course Leadership in Science and Research, Main-Campus-Academy
- 2018 Leader of Winning Team at Simula Hackathon 2018 | *Awarded ~2000 EUR*

## **RESEARCH ACHIEVEMENTS AND PEER RECOGNITION**

## **Publications as (joint) first author**

- 1. **Stöber, T. M.***, Lehr, A. B.*\*, Hafting, T., Kumar, A., Fyhn, M. (2020). Selective neuromodulation and mutual inhibition within the CA3–CA2 system can prioritize sequences for replay. Hippocampus, [doi.org/10.1002/hipo.23256](https://doi.org/10.1002/hipo.23256) | *Developed a novel framework for the functional role of hippocampal region CA2 as network module that can prioritize salient experiences for long term storage, my role: lead researcher, co-first and co-corresponding author*
- 2. **Stöber, T. M.**, Batulin, D., Triesch, J., Narayanan, R., Jedlicka, P. (2023). Degeneracy in epilepsy: multiple routes to hyperexcitable brain circuits and their repair. Communications Biology, [nature.com/articles/s42003-023-04823-0](https://www.nature.com/articles/s42003-023-04823-0) | *Outlined the importance of degenerate mechanisms across dif erent scales for epilepsy, my role: lead researcher*
- 3. **Stöber, T. M.**, Lehr, A. B., Fyhn, M., Kumar, A. (2025). Competition and Cooperation of Assembly Sequences in Recurrent Neural Networks. PLOS Computational Biology. [doi.org/10.1371/journal.pcbi.1013403](http://doi.org/10.1371/journal.pcbi.1013403) | Analysed *in-depth and demonstrated how activity sequences can cooperate and compete in both rate and spiking neural networks, corroborated that our CA2 framework can be implemented in biological plausible neural networks, main role: project leader, corresponding-author*

## **Publications as last author**

4. Lehr, A. B., Kumar, A., Tetzlaff, C., Hafting, T., Fyhn, M., **Stöber, T. M.** (2021). CA2 beyond social memory: Evidence for a fundamental role in hippocampal information processing. Neuroscience &

- Biobehavioral Reviews, [doi.org/10.1016/j.neubiorev.2021.03.020](https://doi.org/10.1016/j.neubiorev.2021.03.020) | *Synthesizing evidence pointing towards the general importance of hippocampal region CA2 in information processing, became a standard reference for the functional role of CA2, my role: project leader, co-corresponding author*
- 5. Lehr, A. B., Hitti, F. L., Deibel, S. H., **Stöber, T. M.** (2023). Silencing hippocampal CA2 reduces behavioral flexibility in spatial learning. Hippocampus, [doi.org/10.1002/hipo.23521](https://doi.org/10.1002/hipo.23521) | *First to demonstrate that hippocampal region CA2 is involved in behavioral flexibility. This confirms central prediction of CA2 framework, my role: project leader, corresponding author*
- *6.* Lehr, A. B., **Stöber, T. M.** (2021). Differential involvement of CA2 in internally vs. externally driven hippocampal sequences. Proceedings of the National Academy of Sciences, [doi.org/10.1073/pnas.2110671118](https://doi.org/10.1073/pnas.2110671118) | *Re-interpreting experimental evidence to suggest role for CA2 in sequence processing, my role: project leader, co-corresponding author*

## **Publications as contributing author**

- *7.* Vieth, M., **Stöber, T. M.**, Triesch, J. (2021). PymoNNto: A Flexible Modular Toolbox for Designing Brain-Inspired Neural Networks. Frontiers in Neuroinformatics, [doi.org/10.3389/fninf.2021.715131](https://doi.org/10.3389/fninf.2021.715131) | *A software framework for neural network simulation with maximal flexibility, my role: mentorship and dissemination*
- *8.* Lepperød, M. E., **Stöber, T. M.**, Hafting, T., Fyhn, M., Kording, K. P. (2023). Inferring causal connectivity from pairwise recordings and optogenetics. PLOS Computational Biology, [doi.org/10.1371/journal.pcbi.1011574](https://doi.org/10.1371/journal.pcbi.1011574) | *Empirical demonstration that instrumental variables can be used to infer causal connectivity from large scale recordings, my role: network simulation and data analysis*
- 9. Pochinok, I., **Stöber, T. M.**, Triesch, J., Chini, M., Hanganu-Opatz, I. L. (2024). A developmental increase of inhibition promotes the emergence of hippocampal ripples. Nature Communications, [nature.com/articles/s41467-024-44983-z](https://www.nature.com/articles/s41467-024-44983-z) | *Demonstrates the importance of developing inhibition for high frequency oscillations in the hippocampus, my role: architect and mentor for neural network simulation*
- 10. Alexander, G. M., Nikolova, V. D., **Stöber, T. M.**, Gruzdev, A., Moy, S. S., Dudek, S. M. (2025). Perineuronal nets on CA2 pyramidal cells and parvalbumin-expressing cells differentially regulate hippocampal dependent memory. Journal of Neuroscience. [doi.org/10.1523/JNEUROSCI.1626-24.2024](http://doi.org/10.1523/JNEUROSCI.1626-24.2024) | *Demonstrates the functional relevance of perineuronal nets in hippocampal region CA2, observed ef ect on behavioral flexibility support our CA2 framework, my role: machine learning analysis of behavior in Morris Water maze*

## **Positions of trust**

- 2025 Ph.D. examiner for Dr. Aliona Spitsyn at the University of Bordeaux
- 2024 Elected International Member of The Young Academy of Norway | *acceptance rate ~12%*
- 2024 Elected Fellow, Johanna Quandt Young Academy, Frankfurt | *Awarded 10k EUR*
- 2023 Ph.D. examiner for Dr. Maud Muller at Universite Paris Cite
- 2021 Invited reviewer for Scientific Reports, PLOS Computational Biology, and Hippocampus

## **Funded Proposals**

- 2025 2026 CIDAS-Fellowship 2025, University of Göttingen | *85k EUR*
- 2024 Ph.D. scholarship for Ivain Raslain, co-supervision, Sorbonne Université, Paris
- 2024 2025 Enfield: European Lighthouse to Manifest Trustworthy and Green AI Exchange | *14k EUR* 2024 International Liaison Fellowship 2024 to RIKEN Center for Brain Science, Tokyo, Japan, Goethe University's R3 Career Support | *2.7k EUR*
- 2023 2025 Think@Ruhr Research Fellowship | *~255k EUR*
- 2022 2023 Intel Neuromorphic Research Community Project Proposal, co-applicant | *218k USD*
- 2023 2023 Teaching project, Goethe University Frankfurt with Prof. Felix Rosenow | *50k EUR*
- 2016 Ph.D. Fellowship, Simula-UiO-UCSD Research and Ph.D. training programme

## **Awards and Scholarships:**

- 2023 2024 Scholarship, Main-Campus-Educator, Stiftung Polytechnische Gesellschaft, 9.6k EUR
- 2013 2014 Scholarship, Deutschlandstipendium, 7.2k EUR
- 2010 2011 Scholarship, German Academic Scholarship Foundation (2010-2011)
- 2008 Award, Best A-Level Score in 2008 and Outstanding Achievements in Natural Sciences
- 2008 Award, Outstanding Achievements in Physics, German Physical Society

## **Selected Invited Presentations:**

- 2024 Satellite workshop on Bernstein Conference
- 2024 Opening lecture & Co-organizer, NeuroAI: Advancing Artificial Intelligence through Brain-Inspired Innovation through brain inspired innovations, World AI Cannes Festival

| 2023 | Invited lecture, Donders, Nijmegen                    |
|------|-------------------------------------------------------|
| 2022 | Neuromorphic Algorithms, Volpriehausen                |
| 2022 | Invited lecture, INSERM, Paris                        |
| 2020 | Invited plenary presentation, FENS Virtual-Forum 2020 |

#### ADDITIONAL INFORMATION

## Career breaks, diverse career paths and major life events

Born on July 25th, 1988. Father of four children, born 2013, 2015, 2019, 2021. I took formal parental leave during the following periods: Oct. 2021 - Dec. 2021 (50%); Aug. 2020 (100%); May 2020 - Jul. 2020 (50%); Mar. 2020 - Apr. 2020 (20%); Apr. 2014 - Mar. 2016 (50%).

## Community Engagement

| 2021 -      | Speaker & co-founder of the GRADE Initiative - Learning in Spiking Neural Networks       |
|-------------|------------------------------------------------------------------------------------------|
| 2023 - 2024 | Instructor at the IDS Interdisciplinary School, supporting neuroscience students in Iran |
| 2023 - 2024 | Deputy member in the Tenure Track Evaluation Commission at Ruhr University Bochum        |
| 2023        | Co-organizer for the virtual symposium "A New View of Hippocampal Area CA2"              |
| 2023        | Lead-organizer for the "Half-Day Symposium: CA2 - big news from a tiny region" at the    |
|             | Ernst Strüngmann Institute (ESI) for Neuroscience in Frankfurt                           |
| 2018 - 2020 | Initiator & lead organizer of the Oslo Neuroscience Meetun                               |

## TRACK RECORD

## Highlights

- 10 published articles in peer-reviewed, internationally recognized scientific journals
- Scientific independence demonstrated by 3 last author publications and independent Think@Ruhr Fellowship, 2022-2025, and CIDAS Fellowship 2025-2026
- Raised and co-raised >600k EUR funding since Ph.D. defence, including fellowships, grants, scholarships and awards
- Recognized for scientific achievements by the Johanna Quandt Young Academy and the Norwegian Young Academy
- Community builder, 4 symposia organized since 2021, board member of graduate school

## Scientific independence

Already as a Ph.D. student I enjoyed a significant amount of scientific independence, as evidenced by a last author publication from that time<sup>55</sup>. During previous and ongoing postdoctoral fellowships I further substantiated my independence, as evidenced by two more last author publications. Further proof of my independence is the primary supervision of 8 interns, 3 research assistants, three master students and one co-supervision of a PhD student. Further, I am lead organizer and primary lecturer on the course AI in Medicine at the University Hospital in Frankfurt. This independence allowed me to refine my current research agenda, which revolves around world models in brains and machines and encompasses a deeply integrated, interdisciplinary research approach at the intersection of experimental and theoretical neuroscience as well as deep learning. The ERC starting grant would allow me to establish a research group that focuses on that timely and important topic.

#### Scientific achievements

My scientific contributions are characterized by a creative and innovative approach, challenging established paradigms and integrating diverse fields to forge new understanding. My achievements fall into two primary areas:

- 1. CA2 as sequence prioritization unit. I led a paradigm shift in the academic community's understanding of the hippocampal area CA2 away from a network that is mostly involved in social memory processing to a regulator of general hippocampal information processing<sup>375,155,65</sup>. Emerging from my Ph.D. work and corroborated by follow-up projects involving machine-learning based behavioral analysis<sup>37,57</sup> and neural network simulation<sup>38</sup>. I contributed to shifting the focus of the academic community on CA2 away from a network that is mostly involved in social memory processing to a regulator of general hippocampal information processing. This work was done mostly together with my previous intern and master student Andrew Lehr, who is now a major collaborator. We provided an alternative explanation for the functional role of CA2<sup>51</sup>, being the first to integrate the reciprocal anatomy, plasticity and physiology with neighboring region CA3.
- Dynamics of artificial neural networks. I contributed to understanding the dynamics of artificial neural networks on the level of simulation infrastructure<sup>50</sup>, the development of neural circuits<sup>60</sup>, and

sequence interactions<sup>58</sup>. Ongoing work addresses the role of self-organized criticality on synaptic plasticity (Stöber et al., in preparation). Also, I contributed to a project showing that spiking dynamics can be used to estimate the causal relation between neurons<sup>61</sup>. My work showcases an ability to innovate across different levels of analysis, from foundational simulation tools to the emergent properties of complex dynamics.

## Qualification for proposed project

This project is built upon a deeply integrated, interdisciplinary approach, with insights flowing from neuroscience to AI and back. As the principal investigator, my documented expertise in analyzing both biological \$^{1.5,600} and artificial  $^{8-60}$  neural networks as well as characterizing behavior with machine learning tools  $^{3.75}$ , allows me to lead and integrate these distinct research streams. The commitment to bridge as co-organizer and lead instructor of a course on AI in Medicine at the University Hospital Frankfurt since 2023. Here, I teach the fundamentals of deep neural networks, ranging from simple multilayer perceptrons to RNNs and transformer architectures

## **Bibliography**

- 1. O'Keefe, J. & Nadel, L. *The Hippocampus as a Cognitive Map*. vol. 3 (Clarendon Press Oxford, 1978).
- 2. Stachenfeld, K. L., Botvinick, M. M. & Gershman, S. J. The hippocampus as a predictive map. *Nat. Neurosci.* **20**, 1643–1653 (2017).
- 3. Whittington, J. C. R., McCaffary, D., Bakermans, J. J. W. & Behrens, T. E. J. How to build a cognitive map. *Nat. Neurosci.* **25**, 1257–1272 (2022).
- 4. Cone, I. & Clopath, C. Latent representations in hippocampal network model co-evolve with behavioral exploration of task structure. *Nat. Commun.* **15**, 687 (2024).
- 5. Chandra, S., Sharma, S., Chaudhuri, R. & Fiete, I. Episodic and associative memory from spatial scaffolds in the hippocampus. *Nature* 1–13 (2025) doi:10.1038/s41586-024-08392-y.
- 6. Lake, B. M., Ullman, T. D., Tenenbaum, J. B. & Gershman, S. J. Building machines that learn and think like people. *Behav. Brain Sci.* **40**, (2017).
- 7. Diester, I. *et al.* Internal world models in humans, animals, and AI. *Neuron* **112**, 2265–2268 (2024).
- 8. Friston, K. *et al.* World model learning and inference. *Neural Netw.* **144**, 573–590 (2021).
- 9. Pasukonis, J., Lillicrap, T. & Hafner, D. Evaluating long-term memory in 3d mazes. *ArXiv Prepr. ArXiv221013383* (2022).
- 10. Samsami, M. R., Zholus, A., Rajendran, J. & Chandar, S. Mastering memory tasks with world models. *ArXiv Prepr. ArXiv240304253* (2024).
- 11. Buzsáki, G. & Tingley, D. Space and time: The hippocampus as a sequence generator. *Trends Cogn. Sci.* **22**, 853–869 (2018).
- 12. Whittington, J. C. *et al.* The Tolman-Eichenbaum machine: Unifying space and relational memory through generalization in the hippocampal formation. *Cell* **183**, 1249–1263 (2020).
- 13. Chandra, S., Sharma, S., Chaudhuri, R. & Fiete, I. Episodic and associative memory from spatial scaffolds in the hippocampus. *Nature* **638**, 739–751 (2025).
- 14. Schölkopf, B. *et al.* Toward causal representation learning. *Proc. IEEE* **109**, 612–634 (2021).
- 15. Matsuo, Y. *et al.* Deep learning, reinforcement learning, and world models. *Neural Netw.* **152**, 267–275 (2022).

- 16. Kazerouni, I. A., Fitzgerald, L., Dooly, G. & Toal, D. A survey of state-of-the-art on visual SLAM. *Expert Syst. Appl.* **205**, 117734 (2022).
- 17. Assran, M. *et al.* V-jepa 2: Self-supervised video models enable understanding, prediction and planning. *ArXiv Prepr. ArXiv250609985* (2025).
- 18. Banino, A. *et al.* Vector-based navigation using grid-like representations in artificial agents. *Nature* **557**, 429–433 (2018).
- 19. George, D. *et al.* Clone-structured graph representations enable flexible learning and vicarious evaluation of cognitive maps. *Nat. Commun.* **12**, 1–17 (2021).
- 20. Raju, R. V. *et al.* Space is a latent sequence: A theory of the hippocampus. *Sci. Adv.* **10**, eadm8470 (2024).
- 21. Hafner, D., Lillicrap, T., Norouzi, M. & Ba, J. Mastering atari with discrete world models. *ArXiv Prepr. ArXiv201002193* (2020).
- 22. Chen, C., Wu, Y.-F., Yoon, J. & Ahn, S. Transdreamer: Reinforcement learning with transformer world models. *ArXiv Prepr. ArXiv220209481* (2022).
- 23. Hafner, D., Pasukonis, J., Ba, J. & Lillicrap, T. Mastering diverse control tasks through world models. *Nature* 1–7 (2025).
- 24. Sun, W. *et al.* Learning produces an orthogonalized state machine in the hippocampus. *Nature* (2025).
- 25. Hafner, D. *et al.* Learning latent dynamics for planning from pixels. in *International conference on machine learning* 2555–2565 (PMLR, 2019).
- 26. O'Keefe, J. & Dostrovsky, J. The hippocampus as a spatial map. Preliminary evidence from unit activity in the freely-moving rat. *Brain Res.* **34**, 171–175 (1971).
- 27. MacDonald, C. J., Carrow, S., Place, R. & Eichenbaum, H. Distinct hippocampal time cell sequences represent odor memories in immobilized rats. *J. Neurosci.* **33**, 14607–14616 (2013).
- 28. Aronov, D., Nevers, R. & Tank, D. W. Mapping of a non-spatial dimension by the hippocampal–entorhinal circuit. *Nature* **543**, 719–722 (2017).
- 29. Leutgeb, J. K. *et al.* Progressive transformation of hippocampal neuronal representations in "morphed" environments. *Neuron* **48**, 345–358 (2005).
- 30. Mehta, M. R., Quirk, M. C. & Wilson, M. A. Experience-dependent asymmetric shape of hippocampal receptive fields. *Neuron* **25**, 707–715 (2000).

- 31. Dudchenko, P. A. & Wood, E. R. Splitter cells: hippocampal place cells whose firing is modulated by where the animal is going or where it has been. in *Space, time and memory in the hippocampal formation* 253–272 (Springer, 2014).
- 32. Sun, C., Yang, W., Martin, J. & Tonegawa, S. Hippocampal neurons represent events as transferable units of experience. *Nat. Neurosci.* **23**, 651–663 (2020).
- 33. Danjo, T., Toyoizumi, T. & Fujisawa, S. Spatial representations of self and other in the hippocampus. *Science* **359**, 213–218 (2018).
- 34. Omer, D. B., Maimon, S. R., Las, L. & Ulanovsky, N. Social place-cells in the bat hippocampus. *Science* **359**, 218–224 (2018).
- 35. Milford, M. J., Wyeth, G. F. & Prasser, D. RatSLAM: a hippocampal model for simultaneous localization and mapping. in *IEEE International Conference on Robotics and Automation, 2004. Proceedings. ICRA'04. 2004* vol. 1 403–408 (IEEE, 2004).
- 36. Miao, L., Liu, W. & Deng, Z. A Frontier Review of Semantic SLAM Technologies Applied to the Open World. *Sensors* **25**, 4994 (2025).
- 37. Lehr, A. B., Hitti, F. L., Deibel, S. H. & Stöber, T. M. Silencing hippocampal CA2 reduces behavioral flexibility in spatial learning. *Hippocampus* **33**, 759–768 (2023).
- 38. Vijayabaskaran, S., Zeng, X., Ghazinouri, B., Wiskott, L. & Cheng, S. A taxonomy of spatial navigation in mammals: Insights from computational modeling. *Neurosci. Biobehav. Rev.* 106282 (2025).
- 39. Hardcastle, K., Maheswaranathan, N., Ganguli, S. & Giocomo, L. M. A Multiplexed, Heterogeneous, and Adaptive Code for Navigation in Medial Entorhinal Cortex. *Neuron* **94**, 375-387.e7 (2017).
- 40. Boyle, L. M., Posani, L., Irfan, S., Siegelbaum, S. A. & Fusi, S. Tuned geometries of hippocampal representations meet the computational demands of social memory. *Neuron* **112**, 1358-1371.e9 (2024).
- 41. Sieber, J., Alonso, C. A., Didier, A., Zeilinger, M. N. & Orvieto, A. Understanding the differences in foundation models: Attention, state space models, and recurrent neural networks. *Adv. Neural Inf. Process. Syst.* **37**, 134534–134566 (2024).
- 42. Tran, K., Bisk, Y., Vaswani, A., Marcu, D. & Knight, K. Unsupervised neural hidden Markov models. *ArXiv Prepr. ArXiv160909007* (2016).
- 43. Eisner, J. Inside-outside and forward-backward algorithms are just backprop (tutorial paper). in *Proceedings of the Workshop on Structured Prediction for NLP* 1–17 (2016).

- 44. He, J., Neubig, G. & Berg-Kirkpatrick, T. Unsupervised learning of syntactic structure with invertible neural projections. *ArXiv Prepr. ArXiv180809111* (2018).
- 45. Kappel, D., Nessler, B. & Maass, W. STDP installs in winner-take-all circuits an online approximation to hidden Markov model learning. *PLOS Comput. Biol.* **10**, (2014).
- 46. Kahneman, D. *Thinking, Fast and Slow*. (Macmillan, 2011).
- 47. Nawaz, U., Anees-ur-Rahaman, M. & Saeed, Z. A review of neuro-symbolic AI integrating reasoning and learning for advanced cognitive systems. *Intell. Syst. Appl.* **26**, 200541 (2025).
- 48. Mankin, E. A., Diehl, G. W., Sparks, F. T., Leutgeb, S. & Leutgeb, J. K. Hippocampal CA2 activity patterns change over time to a larger extent than between spatial contexts. *Neuron* 190–201 (2015).
- 49. Rubin, A., Geva, N., Sheintuch, L. & Ziv, Y. Hippocampal ensemble dynamics timestamp events in long-term memory. *Elife* **4**, e12247 (2015).
- 50. Gründemann, J. *et al.* Amygdala ensembles encode behavioral states. *Science* **364**, eaav8736 (2019).
- 51. Stöber, T. M., Lehr, A. B., Hafting, T., Kumar, A. & Fyhn, M. Mutual inhibition and selective neuromodulation within the CA3-CA2 system can prioritize sequences for replay. (2020).
- 52. Basu, J. *et al.* A cortico-hippocampal learning rule shapes inhibitory microcircuit activity to enhance hippocampal information flow. *Neuron* **79**, 1208–1221 (2013).
- 53. Leroy, F., Brann, D. H., Meira, T. & Siegelbaum, S. A. Input-timing-dependent plasticity in the hippocampal CA2 region and its potential role in social memory. *Neuron* **95**, 1089–1102 (2017).
- 54. Negri, F. *et al.* Brian2Lava: connecting Brian2 to neuromorphic hardware. in *Bernstein Conference 2023* (2023).
- 55. Lehr, A. B. *et al.* CA2 beyond social memory: Evidence for a fundamental role in hippocampal information processing. *Neurosci. Biobehav. Rev.* **126**, 398–412 (2021).
- 56. Lehr, A. B. & Stöber, T. M. Differential involvement of CA2 in internally vs. externally driven hippocampal sequences. *Proc. Natl. Acad. Sci.* **118**, e2110671118 (2021).
- 57. Alexander, G. M. *et al.* Perineuronal Nets on CA2 Pyramidal Cells and Parvalbumin-Expressing Cells Differentially Regulate Hippocampal-Dependent Memory. *J. Neurosci.* **45**, (2025).
- 58. Stöber, T. M. *et al.* Competition and cooperation of assembly sequences in recurrent neural networks. *PLOS Comput. Biol.* **21**, e1013403 (2025).

## *Stöber* Part B1 WoM-BaM

- 59. Vieth, M. A., Stöber, T. M. & Triesch, J. PymoNNto: a flexible modular toolbox for designing brain-inspired neural networks. *Front. Neuroinformatics* 50 (2021).
- 60. Pochinok, I., Stöber, T. M., Triesch, J., Chini, M. & Hanganu-Opatz, I. L. A developmental increase of inhibition promotes the emergence of hippocampal ripples. *Nat. Commun.* (2024).
- 61. Lepperød, M. E., Stöber, T., Hafting, T., Fyhn, M. & Kording, K. P. Inferring causal connectivity from pairwise recordings and optogenetics. *PLOS Comput. Biol.* **19**, e1011574 (2023).