# AutoScrum™: Automating Project Planning Using Language Model Programs

> **Preprint (arXiv:2306.03197v1) — não revisado por pares.**

- **Citation key**: schroder2023autoscrumtm
- **Objective**: Leverage the reasoning ability of large language models to design complex project plans given only a well-defined current state and desired state, bridging the gap between them automatically.
- **Method**: Two approaches are demonstrated. The scrum-based approach runs an automated pipeline of requirements gathering, user story mapping, feature identification and **task decomposition**, then generates questions and search terms to seek domain-specific information supporting task completion. The shortcut approach inspects the latest snapshot of current and desired states and emits the single next most reasonable task. Everything is automated through "Language Programs" — programs written in natural language that process input data through the model — implemented with the Guidance language on GPT-3.5-turbo (GPT-4 also usable).
- **Key findings**:
  - Project planning can be decomposed into a chain of natural-language programs, each handling one stage of the scrum pipeline.
  - The pipeline produces a hierarchy of artefacts — requirements, user stories, features, tasks — which is structurally analogous to a WBS, though the paper never uses that term.
  - The shortcut variant trades full planning for greedy next-task selection, useful when the plan need not be exhaustive.
  - Source code is public at github.com/autoscrum/autoscrum.
- **Relevance to theme**: Highest-scoring item of this search (10/10) and the closest match to the theme's core question: an LLM *producing* a hierarchical scope structure rather than consuming one. The vocabulary is Scrum (user stories, features, tasks) rather than WBS/EAP, and the paper offers no evaluation of the completeness, consistency or coverage of the generated structure — precisely the gap the RADIX review aims to identify.
- **Keywords**: large language models, autonomous agent, agile methodology, task decomposition, project planning, language programs
