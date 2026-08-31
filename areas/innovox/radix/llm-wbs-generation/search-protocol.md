# Protocolo de busca — LLMs para geração de WBS/EAP

- **Localização**: innovox/radix/llm-wbs-generation
- **Tipo**: revisão semi-sistemática
- **Data de elaboração**: 2026-08-29
- **Status**: aguardando validação do usuário

## Pergunta de pesquisa

Como Large Language Models vêm sendo aplicados à geração, decomposição e
estruturação hierárquica de Work Breakdown Structures (WBS/EAP), e quais são o
estado da arte, as principais abordagens, os métodos de avaliação empregados e as
lacunas de pesquisa em aberto?

## Bases consultadas

| Base | Papel |
|---|---|
| OpenAlex | Busca principal (índice agregador: cobre IEEE, ACM, Elsevier, Springer, arXiv) |
| Crossref | Metadados e BibTeX oficial por DOI |
| Unpaywall / arXiv | Localização de PDF open access |

## Strings de busca

Buscas em título + abstract (`title_and_abstract.search`), com operadores
booleanos e frases exatas.

| # | String | Alvo |
|---|---|---|
| S1 | `"work breakdown structure" AND (LLM OR "large language model" OR "generative AI")` | Núcleo: WBS + LLM |
| S2 | `("work breakdown structure" OR WBS OR "estrutura analítica de projeto") AND (generation OR automated OR automatic)` | Geração automática de WBS, incluindo termo em português |
| S3 | `"task decomposition" AND ("large language model" OR LLM) AND (hierarchical OR hierarchy)` | Decomposição hierárquica de tarefas por LLM |
| S4 | `("project planning" OR "project management") AND ("large language model" OR LLM OR "generative AI")` | GenAI em gestão de projetos |
| S5 | `("hierarchical structure" OR "hierarchical plan") AND ("large language model" OR LLM) AND (generation OR generate)` | Geração de estruturas hierárquicas |
| S6 | `("work breakdown structure" OR "project plan" OR "task decomposition" OR "hierarchical decomposition") AND (LLM OR "large language model" OR "generative AI") AND (evaluation OR completeness OR consistency OR coverage OR quality)` | Avaliação de estruturas de escopo/plano geradas por LLM |

## Critérios de inclusão

- **I1** — Trata de geração, decomposição ou estruturação hierárquica de escopo,
  tarefas ou planos, com uso de LLM/IA generativa.
- **I2** — Ou propõe/aplica método de avaliação de qualidade, completude,
  consistência ou cobertura de estruturas geradas por LLM.
- **I3** — Ou aplica LLM/GenAI a gestão de projetos com componente de planejamento
  ou decomposição.
- **I4** — Texto em inglês ou português (G7).
- **I5** — Publicado a partir de 2019 (recorte alinhado à emergência dos LLMs).

## Critérios de exclusão

- **E1** — LLM sem relação com decomposição, planejamento ou estruturação
  hierárquica.
- **E2** — Gestão de projetos sem componente de IA generativa.
- **E3** — Trabalhos em que o WBS/estrutura hierárquica é **entrada** para o LLM
  (estrutura montada por humanos que alimenta, treina ou condiciona o modelo), e
  não **saída** produzida por ele. O teste é a direção da relação, não o domínio
  de aplicação: o tema investiga o LLM *produzindo* a estrutura. Trabalhos assim
  podem entrar como correlatos de baixa prioridade, nunca como estado da arte.
- **E4** — Idioma fora de inglês/português (descarte automático por G7, sempre
  reportado).
- **E5** — Duplicata de item já presente no corpus do tema (dedupe por DOI e por
  título normalizado).

## Recorte temporal

2019 até o presente. Justificativa: os LLMs de uso geral tornam-se objeto de
pesquisa aplicada a partir desse período; trabalhos anteriores sobre WBS sem
componente de IA generativa ficam fora por E2.

## Tratamento de fontes não revisadas por pares

Preprints (arXiv, Zenodo, SSRN), datasets e materiais preliminares são **aceitos**,
mas devem ser marcados explicitamente como não revisados por pares no
`candidates.md` e no resumo correspondente. A priorização recai sobre fontes
revisadas por pares.

## Limite por passada

Máximo de 30 candidatos por execução (G5). Excedentes são reportados e podem ser
recuperados em passadas seguintes.

## Log de decisões

| Data | Decisão | Justificativa |
|---|---|---|
| 2026-08-29 | Recorte a partir de 2019 | Alinhado à emergência dos LLMs como objeto de pesquisa aplicada |
| 2026-08-29 | Incluir "estrutura analítica de projeto" nas strings | EAP é o termo corrente em português; G7 aceita pt |
| 2026-08-29 | Aceitar preprints com marcação explícita | Campo recente; excluir preprints perderia estado da arte |
| 2026-08-29 | E3 redefinido pela DIREÇÃO da relação | Zhen et al. 2024 usa WBS como *entrada* que treina o LLM; o tema investiga o LLM *produzindo* o WBS. O critério passa a ser a direção, não o domínio |
| 2026-08-29 | S6 reformulada | Versão inicial (avaliação de LLM em geral) traria ruído; agora ancorada em WBS/plano/decomposição como objeto avaliado |
