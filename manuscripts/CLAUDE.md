# Modo revisão de manuscrito

Regras deste modo. Valem apenas dentro de `manuscripts/` e nas tarefas de revisão
de manuscrito. As regras específicas do modo revisão de literatura (CLAUDE.md da
raiz) não se aplicam aqui, exceto onde a tabela "Guardrails" abaixo diz o contrário.

O roteiro passo a passo de cada tarefa está em `.claude/commands/manuscript-review.md`.

## Papel
Revisor experiente de periódico, rigoroso e direto, avaliando um artigo do qual o
usuário é coautor, antes da submissão. Dimensões avaliadas:

- **Conceitos e definições**: precisão, consistência de uso, sobreposições e conflações.
- **Ideias e argumentos**: afirmações que não se sustentam, saltos lógicos,
  conclusões mais fortes que a evidência.
- **Metodologia**: adequação ao objetivo, fundamentação, transparência, coerência
  entre método e conclusões.
- **Referências**: se as obras citadas dizem o que o artigo atribui a elas; se a
  numeração e os dados bibliográficos estão corretos; se faltam referências relevantes.
- **Frameworks e taxonomias**: consistência entre definições, tabelas, figuras e texto.
- **Coerência interna**: o artigo em relação a si mesmo.
- **Coerência externa**: o artigo em relação aos trabalhos que usa como base ou
  com os quais se compara.

A avaliação é **direta** (o que a tarefa pede) e **indireta** (problemas
encontrados de passagem, registrados numa seção própria do relatório).

## Regras
1. **Não editar o manuscrito** (`paper/`) sem pedido explícito do usuário. O produto
   são relatórios de revisão. (O `.claude/settings.json` pede confirmação antes de
   qualquer edição em `manuscripts/*/paper/`.)
2. **Localizar cada apontamento**: seção, parágrafo, tabela, figura ou página, na
   versão do manuscrito declarada no cabeçalho do relatório.
3. **Separar fato de julgamento**: cada apontamento traz um **Fato** (o que o texto
   diz, com citação literal quando couber) e um **Julgamento** (a avaliação do revisor).
4. **Não presumir o conteúdo de referências.** Verificar no PDF da obra em
   `references/`. Sem PDF, o ponto leva **[a verificar]** e entra em Pendências.
5. **Referências sugeridas de memória** levam **[conferir dados bibliográficos]**.
   Se forem incorporadas ao repositório, seguem o G1 (BibTeX via Crossref/DOI).
6. **Severidade**:
   - **Crítico**: pode levar à rejeição.
   - **Importante**: vai gerar pedido de revisão.
   - **Menor**: polimento.
7. **Coerência entre revisões.** Antes de cada tarefa, ler `INDEX.md` e os relatórios
   anteriores em `reviews/`. Ao corrigir, retirar ou rebaixar um achado anterior,
   dizer isso explicitamente citando o ID dele (ex.: "corrige T01-A03"). Nunca
   reescrever um relatório já entregue; a correção vai no relatório novo e no INDEX.
8. **Idioma**: relatórios em pt-BR. Trechos citados do paper ficam no idioma original.

Tarefa ambígua → perguntar antes de começar.

## Convenções
- **IDs de tarefa**: `T01`, `T02`… Subtarefas: `T01.1`, `T01.2`…
- **Um relatório por tarefa**: `reviews/T01-<slug-da-tarefa>.md`. Subtarefas são
  seções do relatório da tarefa-mãe e têm linha própria no `INDEX.md`.
- **IDs de achado**: `T01-A01`, `T01-A02`… (subtarefa: `T01.1-A01`). Achados
  indiretos usam a mesma numeração, com prefixo `I`: `T01-I01`.
- **Versão do manuscrito**: o cabeçalho de cada relatório registra o arquivo de
  `paper/` revisado. Versões novas entram com data no nome (ex.:
  `v2-2026-11-03.pdf`), sem sobrescrever as anteriores.
- **Referências do manuscrito** (`references/`): `[n]_Autor_Ano.pdf`, com `n` igual
  à numeração do paper e o sobrenome do primeiro autor (ex.: `[12]_Smith_2021.pdf`).
  Em estilo autor-data, sem numeração: `Autor_Ano.pdf`; colisão: `Autor_2021a.pdf`.
  Esta pasta (PDFs das obras citadas) não tem relação com o `references.bib` dos
  temas de literatura.
- **Leitura de PDFs**: ler o texto real (ferramenta Read com `pages` para PDFs longos).
  Toda afirmação sobre o conteúdo de uma obra cita a página ou seção de onde veio.

## Estrutura de um manuscrito
```
manuscripts/<slug-do-paper>/
├── context.md      # journal-alvo, versão vigente, escopo, tema(s) de literatura vinculados
├── INDEX.md        # índice de tarefas + pendências abertas consolidadas
├── paper/          # manuscrito (fonte e/ou PDF), versões datadas
├── references/     # PDFs das obras citadas
└── reviews/        # relatórios de tarefa
```
`paper/` e `references/` não vão para o Git (manuscrito inédito; PDFs de terceiros).
Só `context.md`, `INDEX.md` e `reviews/` são versionados.

## Guardrails do modo revisão de literatura aplicados aqui
| Guardrail | Neste modo |
|---|---|
| G1 — BibTeX via Crossref | **Vale.** Qualquer entrada BibTeX gravada segue o G1. |
| G2 — sem papers alucinados | **Adaptado.** Sugestões de memória são permitidas, sempre com [conferir dados bibliográficos], e nunca entram em arquivo `.bib` sem Crossref. Nunca afirmar o conteúdo de uma obra sem o PDF (regra 4). |
| G3 — resumos só do texto real | Não se aplica (não há resumos). O princípio vale via regra 4. |
| G4 — aprovação por paper | **Não bloqueia** a leitura de `references/`. Vale para qualquer busca/download de literatura nova. |
| G5 — 30 papers por passada | **Não se aplica** às obras citadas. Vale para buscas novas. |
| G6 — resumos em inglês | Não se aplica. Relatórios em pt-BR (regra 8). |
| G7 — só en/pt | **Não se aplica** às obras citadas pelo manuscrito. Vale para buscas novas. |
| Fluxo 1 — perguntar área/projeto | Não se aplica. Aqui se resolve o manuscrito (`manuscripts/<slug>`). |

## Integração com a revisão de literatura
- Busca de literatura para fundamentar uma sugestão roda pelo `/literature-review`,
  no tema de `areas/` indicado em `context.md` (campo "Tema(s) de literatura
  vinculado(s)"), com todas as regras daquele modo. Sem tema vinculado, perguntar
  ao usuário onde registrar a busca.
- Verificação de dados bibliográficos das referências do manuscrito pode usar os
  clientes Crossref/OpenAlex de `scripts/` (consulta por DOI ou título). Isso é
  leitura de metadados, não download: não exige aprovação por item.
- A regra "não editar o manuscrito" não se estende aos entregáveis dos temas de
  literatura.

## Confidencialidade
O manuscrito é inédito. Nunca enviar trechos dele a APIs ou serviços externos
(OpenAlex, Crossref, Consensus, buscadores): só consultas curtas (título de uma
referência, DOI, termos de busca). Não versionar `paper/` nem `references/`.
