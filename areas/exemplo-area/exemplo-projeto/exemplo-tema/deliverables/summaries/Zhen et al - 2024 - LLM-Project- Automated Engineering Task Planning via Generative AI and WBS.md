# LLM-Project: Automated Engineering Task Planning via Generative AI and WBS Integration

- **Citation key**: zhen2024llm
- **Objective**: Propose and implement a task planning system that integrates validated robotic instructions, deep learning models, and demonstration cases into a larger structure organised as a Work Breakdown Structure (WBS), the decomposition scheme commonly used in engineering project management.
- **Method**: Small-scale solutions are sequenced by temporal and resource dependencies; simulations and evaluation functions select the optimal structure as a Standard Operating Procedure (SOP). The SOPs then train a generative AI to mimic human experts in producing high-level structures, which are progressively transformed into low-level operations for execution.
- **Key findings**:
  - A generative model trained on SOP-structured data can produce high-level task structures for real-world needs and perform minor parameter generalisations.
  - The approach addresses temporal dependencies, spatial relationships, and resource allocation within the generated structures.
  - Execution results are recorded for automatic or manual analysis, and the feedback loop continuously improves the model's output.
  - The authors position the work as groundwork for combining generative AI with WBS data in robotic task planning; implementation is public at github.com/NOMIzy/LLM-Project.
- **Relevance to theme**: Directly on target. This is the clearest instance found of an LLM producing WBS-structured output — though the WBS here organises *robotic task planning* rather than a conventional project plan, so the transfer to general project management is an open question.
- **Keywords**: work breakdown structure, generative AI, robotic task planning, standard operating procedure, task decomposition
