# Automation of the Planning Phase of a Construction Project Using AI Agents

- **Citation key**: Korba_2026
- **Objective**: Automate resource generation and validation in the pre-construction phase, acting as a systemic safety barrier against the design anomalies and human errors that follow from the construction sector's digitalisation deficit.
- **Method**: A Multi-Agent System (MAS) architecture embedded in the n8n environment, powered by Gemini-class language models. A deterministic PostgreSQL database sits inside a Retrieval-Augmented Generation (RAG) architecture for real-time processing of Construction Law regulations. Chain-of-Thought reasoning plus structured prompt templates were used to eliminate model logic drift and ensure reproducibility.
- **Key findings**:
  - 96% acceleration of the pre-construction phase: formulating **WBS/CPM structures** dropped from a 480-minute baseline to roughly 20 minutes.
  - Human Error Probability (HEP) index reduced to a residual level below 1%.
  - Operational costs (OPEX) compressed substantially, with the design cycle confined to a single execution instead of iterative rework.
  - Compliance with the 7R Logistics Directive maintained throughout.
- **Relevance to theme**: Direct hit. LLM-driven agents *produce* WBS structures (correct direction under E3), and the paper reports a quantitative before/after baseline — 480 minutes to 20 — which is a rare form of evaluation in this literature. Note that the metric is process time and error probability, not the structural quality of the WBS itself; completeness and coverage of the generated structure are not assessed. Domain is construction under Polish Construction Law, so regulatory coupling limits direct transfer.
- **Keywords**: work breakdown structure, critical path method, multi-agent system, retrieval-augmented generation, construction planning, chain-of-thought, process automation
