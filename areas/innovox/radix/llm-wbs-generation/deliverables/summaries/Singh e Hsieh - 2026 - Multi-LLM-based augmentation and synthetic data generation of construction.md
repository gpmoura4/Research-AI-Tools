# Multi-LLM-based augmentation and synthetic data generation of construction schedules and task descriptions with SLM-as-a-judge assessment

- **Citation key**: Singh_2026
- **Objective**: Investigate whether LLMs can be systematically applied to enhance and generate construction schedule and task description data, and whether lightweight, locally deployed Small Language Models (SLMs) can evaluate those outputs against domain-specific rubrics in a scalable, privacy-preserving way. The stated motivation is the absence of high-quality, hierarchically structured **Work Breakdown Structure with Task Dependency (WBS-TD)** datasets, which restricts training and evaluation of AI models for automated construction workflows.
- **Method**: Three integrated components — (1) Role-Guided Modular Prompt Chaining (RGPC), transforming inconsistent WBS-TD inputs into logically ordered, semantically enriched outputs; (2) synthetic data generation through a multi-LLM pipeline with structured prompt strategies; (3) SLM-as-a-Judge, a rubric-based evaluation assessing structural, logical and domain-specific dimensions locally, without sensitive data leaving secure environments.
- **Key findings**:
  - Claude-3.5-Sonnet reached 77% quality in augmented schedule generation.
  - Gemini-2.0-Flash reached 92% in synthetic schedule generation.
  - DeepSeek-R1 gave the best balance of quality and diversity for synthetic task descriptions.
  - The framework produces reusable, machine-readable knowledge artefacts with strong domain alignment across tasks.
- **Relevance to theme**: Among the strongest matches found for this theme. It treats WBS-TD as the explicit object, uses LLMs to *produce* the structure (correct direction under E3), and — unusually — supplies a concrete evaluation method for the generated structure via rubric-based SLM judging. That evaluation dimension is exactly the gap the RADIX review seeks to characterise. Domain is construction rather than software, so transferability of the rubric to other project types is an open question.
- **Keywords**: work breakdown structure, task dependency, large language models, synthetic data generation, prompt chaining, SLM-as-a-judge, construction scheduling
