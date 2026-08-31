# Protocolo de busca — LLMs em gestão e planejamento de projetos

- **Localização**: innovox/radix/llm-project-management
- **Tipo**: revisão semi-sistemática
- **Data**: 2026-08-29
- **Origem**: separado do tema `llm-wbs-generation`, que era amplo demais

## Pergunta de pesquisa

Como LLMs e IA generativa vêm sendo aplicados a gestão e planejamento de projetos
— geração de planos, decomposição de tarefas, apoio a metodologias ágeis e adoção
profissional — e o que isso revela sobre maturidade, limitações e métodos de
avaliação?

## Bases consultadas

| Base | Papel |
|---|---|
| OpenAlex | Busca principal |
| Crossref | Metadados e BibTeX por DOI |
| Unpaywall / arXiv | Localização de PDF open access |

## Strings de busca

Herdadas do protocolo original (S3, S4, S5), que se mostraram aderentes a **este**
tema, não ao de WBS.

| # | String | Alvo |
|---|---|---|
| P1 | `("project planning" OR "project management") AND ("large language model" OR LLM OR "generative AI")` | Núcleo: GenAI em gestão/planejamento |
| P2 | `"task decomposition" AND ("large language model" OR LLM) AND (hierarchical OR hierarchy)` | Decomposição hierárquica de tarefas |
| P3 | `("hierarchical structure" OR "hierarchical plan") AND ("large language model" OR LLM) AND (generation OR generate)` | Geração de planos hierárquicos |
| P4 | `(scrum OR agile OR sprint OR backlog) AND ("large language model" OR LLM OR "generative AI") AND (planning OR generation)` | Metodologias ágeis + GenAI |

## Critérios de inclusão

- **I1** — Aplica LLM/IA generativa a planejamento, decomposição de tarefas ou
  gestão de projetos.
- **I2** — Ou avalia artefatos de planejamento gerados por LLM.
- **I3** — Ou investiga adoção, apropriação e impacto de GenAI na prática de PM.
- **I4** — Inglês ou português (G7).
- **I5** — A partir de 2019.

## Critérios de exclusão

- **E1** — LLM sem relação com planejamento, decomposição ou gestão.
- **E2** — Gestão de projetos sem componente de IA generativa.
- **E3** — Decomposição puramente robótica ou de chamadas de API, sem transferência
  ao domínio de gestão.
- **E4** — Idioma fora de inglês/português (G7).
- **E5** — Duplicata no corpus do tema.
- **E6** — **Trabalho centrado em geração de WBS/EAP** — pertence ao tema
  `llm-wbs-generation`. Registrar a realocação no log.

## Recorte temporal

2019 até o presente.

## Tratamento de fontes não revisadas por pares

Preprints aceitos, marcados explicitamente. Prioridade a revisados por pares.

## Limite por passada

30 candidatos (G5).

## Log de decisões

| Data | Decisão | Justificativa |
|---|---|---|
| 2026-08-29 | Tema separado de `llm-wbs-generation` | A string de gestão trazia 19 dos 30 candidatos e afogava a string de WBS, que não colocava nenhum. Cada assunto passa a ter seu próprio limite de 30 |
| 2026-08-29 | Herdadas S3, S4, S5 do protocolo original | São aderentes a este tema; a busca já executada com elas é aproveitada |
| 2026-08-29 | Acrescentada P4 (ágil/scrum) | O corpus obtido revelou concentração em metodologias ágeis, sem string dedicada |
| 2026-08-29 | AutoScrum realocado para cá | Gera plano com decomposição hierárquica em vocabulário Scrum; nunca menciona WBS |
