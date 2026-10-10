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
   são relatórios de revisão e, quando a tarefa pedir, ajustes aplicados na cópia de
   revisão em Google Docs (ver "Política de ajustes"). (O `.claude/settings.json` pede confirmação antes de
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
- **IDs de achado**: `T01-F01`, `T01-F02`… (subtarefa: `T01.1-F01`). Achados
  indiretos usam a mesma numeração, com prefixo `I`: `T01-I01`. O prefixo `A` é
  reservado aos ajustes (`T01-A1`; ver "Política de ajustes").
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
├── reference-coverage.md  # lista de referências do manuscrito × PDFs em references/
├── backlog.md      # propostas adiadas pelo usuário (B01, B02…), fora das tarefas em curso
├── paper/          # manuscrito (fonte e/ou PDF), versões datadas
├── references/     # PDFs das obras citadas
├── reviews/        # relatórios de tarefa
└── adjustments/    # ajustes por tarefa: T01-ajustes.md (fonte + log de aplicação)
```
`paper/` e `references/` não vão para o Git (manuscrito inédito; PDFs de terceiros).
Só `context.md`, `INDEX.md`, `reference-coverage.md`, `backlog.md`, `reviews/` e as fontes `.md` de
`adjustments/` são versionados.
Ao depositar ou obter PDFs em `references/`, atualizar `reference-coverage.md`.

## Política de ajustes
Vale para todas as tarefas. Ajustes no paper (texto, tabela ou figura) **nunca são
feitos no original dos autores nem no PDF em `paper/`**. São aplicados pelo agente,
via API do Google Docs, numa **cópia de revisão** em Google Docs criada pelo usuário
(o ID do documento fica em `context.md`), **um lote por vez**, após aprovação.

- **Registro**: `adjustments/<ID>-ajustes.md` é a fonte versionada de cada ajuste
  (âncora, texto original, novo texto, justificativa) e o log do que foi aplicado,
  quando e em qual revisão do documento. Aplicação:
  `uv run python -m scripts.gdocs_apply <doc-id> manuscripts/<slug>/adjustments/<ID>-ajustes.md --ids A6,A3`
  (sem `--apply` é simulação; com `--apply` grava).
- **Marcação no documento**:
  - o texto substituído **não é apagado**: fica **riscado** no lugar, com a formatação
    original;
  - o **novo texto** entra logo depois do trecho riscado, em **preto com marca-texto
    amarelo**;
  - ajuste de figura (imagem não editável) entra como nota em preto com marca-texto
    amarelo junto à legenda: `[AJUSTE T01-A11: …]`.
- **Controle**: antes de gravar, o script relê o documento, localiza cada ajuste pela
  âncora e confere que o texto original ainda está idêntico. Se divergir ou não for
  único, o ajuste é **pulado** e reportado. Ajuste já aplicado não é reaplicado.
- **Revisão de texto já inserido pelo agente**: enquanto o trecho novo ainda estiver com
  marca-texto amarelo (proposta não incorporada pelos autores), uma revisão o substitui
  diretamente, sem riscar, para não acumular versões. Registro no `.md` como `<ID>vN`
  (ex.: `T01-A6v2`, ação `revisar-insercao`), e a seção do ajuste original passa a trazer
  o texto vigente. O script recusa a troca se o trecho não estiver todo destacado, o que
  impede apagar texto dos autores.
- **Edições humanas sobre o texto inserido**: se o documento divergir do `.md` (alguém
  editou o trecho destacado), a edição humana é **preservada**. Antes de revisar,
  comparar documento × `.md`, incorporar a edição ao registro e só então trocar o texto.
- **Aprovação**: antes de aplicar, apresentar a lista de ajustes planejados (ID,
  localização, ação, objetivo em uma linha) e aguardar aprovação do usuário; aplicar
  por lotes, cada lote também aprovado.
- **Estrutura de cada ajuste**:
  - **ID** (`T01-A1`, `T01-A2`…) e o achado do relatório que o motiva (`T01-F03`).
  - **Localização exata no original**: seção, número do parágrafo dentro da seção e
    as **primeiras palavras do parágrafo** como âncora (o documento não tem números
    de linha estáveis). Tabelas: número, linha e coluna. Figuras: número e elemento.
  - **Ação**: substituir, inserir antes/depois, ou remover.
  - **Texto original exato**, quando for substituição ou remoção.
  - **Novo texto**, em inglês.
  - **Justificativa** curta, em português.
- **Regras para o novo texto**:
  - Apenas referências já presentes na lista do paper, citadas com a numeração da
    lista. Se a numeração no texto divergir da lista no trecho afetado, sinalizar.
  - **Não inventar fatos metodológicos.** O que só os autores sabem entra como
    placeholder explícito: `[AUTORES: confirmar se houve forward snowballing]`.
  - Manter o tom e o estilo do restante do paper.
  - Preferir ajustes cirúrgicos a reescritas amplas. Se um parágrafo inteiro precisar
    mudar, explicar por quê.
- **Estilo de redação do texto novo** (premissa do usuário, vale para todo texto escrito
  para o paper):
  - **Não usar travessão (—) nem ponto e vírgula (;)**, salvo quando forem de fato
    indispensáveis. Alternativas: frases separadas, vírgulas, dois-pontos, parênteses
    ou reestruturação da frase.
  - O traço curto (–) em intervalos numéricos (ex.: "2022–2023", "pp. 183–199") não é
    travessão e continua permitido.
  - Antes de propor ou aplicar qualquer texto, conferir essa regra no lote inteiro.

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
