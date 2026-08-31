# Protocolo de busca — LLMs para geração de WBS/EAP

- **Localização**: innovox/radix/llm-wbs-generation
- **Tipo**: revisão semi-sistemática
- **Data**: 2026-08-29 (revisado)
- **Escopo**: estrito — **apenas** WBS/EAP × LLM

## Pergunta de pesquisa

Como Large Language Models vêm sendo aplicados à geração, decomposição e
estruturação hierárquica de Work Breakdown Structures (WBS/EAP), e quais são o
estado da arte, as abordagens, os métodos de avaliação e as lacunas em aberto?

## Delimitação em relação ao tema irmão

Este tema é **estrito**: exige a presença de WBS/EAP como objeto. Planejamento de
projeto, metodologias ágeis e gestão com LLM em geral pertencem a
`llm-project-management`.

O teste é duplo:
1. O trabalho trata de **WBS/EAP** (ou estrutura hierárquica de decomposição de
   escopo explicitamente equiparada a WBS)?
2. O **LLM produz ou apoia a produção** dessa estrutura (direção LLM → estrutura)?

Falhar em qualquer um exclui — o segundo tema recolhe o que for pertinente a ele.

## Bases consultadas

| Base | Papel |
|---|---|
| OpenAlex | Busca principal |
| Crossref | Metadados e BibTeX por DOI |
| Unpaywall / arXiv | Localização de PDF open access |

## Strings de busca

Todas exigem **WBS/EAP explícito**. Nenhuma string genérica de gestão de projetos.

| # | String | Alvo |
|---|---|---|
| W1 | `"work breakdown structure" AND (LLM OR "large language model" OR "generative AI" OR GPT)` | Núcleo: WBS × LLM |
| W2 | `("work breakdown structure" OR WBS) AND (generation OR generate OR automated OR automatic OR "automatic generation")` | Geração automática de WBS, com ou sem LLM nomeado |
| W3 | `("estrutura analítica de projeto" OR EAP) AND ("modelo de linguagem" OR LLM OR "inteligência artificial generativa")` | Literatura em português (G7 aceita pt) |
| W4 | `"work breakdown structure" AND (evaluation OR completeness OR consistency OR coverage OR quality) AND (automated OR generated OR AI)` | Avaliação de WBS gerado automaticamente |
| W5 | `("work breakdown structure" OR WBS) AND ("natural language" OR "text-to" OR "requirements") AND (decomposition OR generation)` | Geração de WBS a partir de linguagem natural/requisitos |

**Nota sobre W2 e W4**: não exigem LLM nomeado. Geração automática de WBS por
métodos anteriores (ontologias, case-based reasoning, template matching) é
fundamentação legítima do estado da arte — o campo pré-LLM define a linha de base
contra a qual os LLMs devem ser comparados. Marcar esses trabalhos como
*pré-LLM* no `candidates.md`.

## Critérios de inclusão

- **I1** — Trata de WBS/EAP como objeto central ou substantivo.
- **I2** — **E** envolve geração, decomposição ou estruturação automática/assistida
  dessa estrutura — por LLM, IA generativa ou método automatizado anterior.
- **I3** — Ou propõe método de avaliação de WBS gerado automaticamente.
- **I4** — Inglês ou português (G7).
- **I5** — Sem recorte inferior rígido para trabalhos **pré-LLM** de geração
  automática de WBS (fundamentação); 2019+ para trabalhos com LLM.

## Critérios de exclusão

- **E1** — Não menciona WBS/EAP nem estrutura hierárquica de escopo equiparável.
- **E2** — Menciona WBS apenas de passagem, sem que seja objeto do trabalho.
- **E3** — O WBS é **entrada** para o LLM (montado por humanos para treinar,
  alimentar ou condicionar o modelo), e não **saída** produzida por ele.
- **E4** — Idioma fora de inglês/português (G7).
- **E5** — Duplicata no corpus do tema.
- **E6** — Planejamento/gestão de projetos com LLM **sem** WBS/EAP como objeto —
  pertence a `llm-project-management`.

## Recorte temporal

- Trabalhos com LLM: 2019 em diante.
- Trabalhos pré-LLM de geração automática de WBS: **sem recorte inferior**, por
  servirem de fundamentação e linha de base.

## Tratamento de fontes não revisadas por pares

Preprints aceitos, marcados explicitamente. Prioridade a revisados por pares.

Dada a escassez esperada nesta interseção, teses, dissertações e relatórios
técnicos também são aceitos, com marcação de tipo de fonte.

## Limite por passada

30 candidatos (G5).

## Log de decisões

| Data | Decisão | Justificativa |
|---|---|---|
| 2026-08-29 | Recorte a partir de 2019 (trabalhos com LLM) | Alinhado à emergência dos LLMs |
| 2026-08-29 | Incluir termos em português (W3) | EAP é o termo corrente em pt; G7 aceita |
| 2026-08-29 | Aceitar preprints com marcação | Campo recente; excluí-los perderia o estado da arte |
| 2026-08-29 | E3 definido pela DIREÇÃO da relação | Zhen et al. 2024 usa WBS como entrada que treina o LLM; o tema investiga o inverso |
| 2026-08-29 | **Strings genéricas removidas** | S4 (project management) trouxe 19 dos 30 candidatos e afogou S1 (WBS×LLM), que não colocou nenhum no top-30. Realocadas para `llm-project-management` |
| 2026-08-29 | **W2 e W4 sem exigir LLM nomeado** | Geração automática de WBS pré-LLM é linha de base do estado da arte |
| 2026-08-29 | Corpus anterior realocado | Os 30 candidatos e o AutoScrum eram de gestão/ágil, não de WBS |
