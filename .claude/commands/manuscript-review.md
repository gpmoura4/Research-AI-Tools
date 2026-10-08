---
description: Revisão de manuscrito — executa uma tarefa (T01, T02…) e grava o relatório
argument-hint: [slug-do-manuscrito] [ID e/ou descrição da tarefa]
allowed-tools: Bash(uv run:*), Bash(ls:*), Bash(mkdir:*), Read, Write, Edit, Glob, Grep, AskUserQuestion
---

# /manuscript-review

Executa uma tarefa de revisão crítica de um manuscrito do usuário e grava o
relatório em `manuscripts/<slug>/reviews/`, atualizando o `INDEX.md`.

Argumentos recebidos: `$ARGUMENTS`

> **Este documento é o roteiro do AGENTE, não do usuário.** Ele vale também quando
> o usuário envia a tarefa em texto livre, sem invocar o comando. Há três paradas
> legítimas: resolver o manuscrito (passo 1), confirmar a criação de um manuscrito
> novo (passo 2) e esclarecer uma tarefa ambígua (passo 4). Fora essas, conduza a
> tarefa até o fim.

---

## Passo 1 — Ler as regras e resolver o manuscrito

Leia `manuscripts/CLAUDE.md` (regras do modo). Depois liste os manuscritos:

```bash
ls manuscripts/
```

- Slug informado e existente → siga.
- Só um manuscrito existe e a tarefa claramente se refere a ele → siga, dizendo qual usou.
- Ambíguo ou ausente → **pare e pergunte** com `AskUserQuestion`.
- Slug inexistente → passo 2.

## Passo 2 — (Manuscrito novo) Criar a estrutura

**Confirme com o usuário antes de criar.** Depois:

```bash
mkdir -p manuscripts/<slug>/{paper,references,reviews}
```

Grave `context.md` e `INDEX.md` a partir dos templates abaixo. Peça ao usuário o
manuscrito (em `paper/`) e o contexto (Fase 2) antes da primeira tarefa.

## Passo 3 — Carregar o estado

Leia, nesta ordem:

1. `context.md` — journal-alvo, versão vigente, escopo, tema(s) de literatura vinculados.
2. `INDEX.md` — tarefas anteriores e pendências abertas.
3. Todos os relatórios em `reviews/` relevantes para a tarefa (na dúvida, todos).
   Anote os IDs de achados que a tarefa atual pode confirmar, corrigir ou retirar.
4. `reference-coverage.md` — quais obras citadas têm PDF. Se houver PDFs novos em
   `references/` que não constam dele, atualize-o antes de começar.
5. A versão vigente do manuscrito em `paper/`.

## Passo 4 — Definir a tarefa

- ID: o informado pelo usuário, ou o próximo livre no `INDEX.md` (`T01`, `T02`…;
  subtarefa `T01.1`…, dentro do relatório da tarefa-mãe).
- Escopo: o que a tarefa pede e o que fica de fora.
- **Ambígua → pare e pergunte** antes de começar (escopo, seções do paper,
  profundidade, se a subtarefa é nova ou continuação).

## Passo 5 — Executar a revisão

- Mapeie onde o tema da tarefa aparece no artigo e o que o fundamenta (referências,
  dados, figuras).
- Para cada referência relevante, leia o PDF em `references/`. Sem PDF → **[a verificar]**.
  Nunca presuma o conteúdo de uma obra.
- Cada apontamento: localização, Fato, Julgamento, severidade, ID.
- Registre problemas encontrados de passagem como achados indiretos.
- Sugestão que precise de literatura nova: sugira de memória com
  **[conferir dados bibliográficos]**, ou proponha uma busca no tema vinculado via
  `/literature-review` (com aprovação por item). Não rode a busca sem o usuário pedir.

## Passo 6 — Gravar o relatório

`reviews/<ID>-<slug-da-tarefa>.md`, com o template abaixo. Subtarefa: acrescente uma
seção `## <ID> — <título>` ao relatório da tarefa-mãe, com as mesmas seis subseções.

## Passo 7 — Atualizar o INDEX.md

- Linha da tarefa (ID, título, status, data, versão revisada, link).
- Pendências abertas: acrescente as novas e marque as resolvidas.
- Achados de relatórios anteriores corrigidos/retirados nesta tarefa: registre em
  "Correções entre revisões".

## Passo 8 — Relatar

No chat: contagem de achados por severidade, os críticos em uma linha cada,
pendências novas e link para o relatório. Não repita o relatório inteiro.

---

## Template — relatório (`reviews/<ID>-<slug>.md`)

```markdown
# <ID> — <Título da tarefa>

- **Manuscrito**: <slug>
- **Versão revisada**: `paper/<arquivo>`
- **Data**: <AAAA-MM-DD>
- **Relatórios anteriores consultados**: <IDs ou "nenhum">

## 1. Escopo
<O que a tarefa pede; o que fica de fora.>

## 2. Mapeamento
<Onde o tema aparece no artigo (seção/parágrafo/tabela/figura/página) e o que o
fundamenta (referências, dados, figuras).>

## 3. Avaliação

### <ID>-A01 — <título curto> · **<Crítico|Importante|Menor>**
- **Localização**: <seção, parágrafo, tabela, figura ou página>
- **Fato**: <o que o texto diz; citação literal no idioma original quando couber>
- **Julgamento**: <avaliação e justificativa>
- **Relação com revisões anteriores**: <"nova" | "confirma T01-A02" | "corrige T01-A03: …">

## 4. Achados indiretos

### <ID>-I01 — <título curto> · **<Crítico|Importante|Menor>**
- **Localização**:
- **Fato**:
- **Julgamento**:

## 5. Sugestões
<Por achado (referenciando o ID), sem reescrever o texto salvo pedido. Referências
sugeridas de memória levam [conferir dados bibliográficos].>

## 6. Pendências
| # | Item [a verificar] | Achado | O que falta |
|---|---|---|---|
```

## Template — `INDEX.md`

```markdown
# Índice de tarefas — <título curto do manuscrito>

| ID | Título | Status | Data | Versão revisada | Relatório |
|---|---|---|---|---|---|

Status: em andamento · concluída · aguardando usuário · substituída

## Pendências abertas
| Pendência | Origem (ID) | Status |
|---|---|---|

## Correções entre revisões
| Achado original | Corrigido em | Natureza da correção |
|---|---|---|
```

## Template — `context.md`

```markdown
# Contexto do manuscrito: <título>

- **Título provisório**:
- **Autores**:
- **Journal-alvo**:
- **Versão vigente**: `paper/<arquivo>`
- **Estilo de citação**: <numérico | autor-data>
- **Tema(s) de literatura vinculado(s)**: <areas/<area>/<projeto>/<tema> ou "nenhum">

## Objetivo e contribuição declarados

## Método

## Pontos de atenção indicados pelo usuário

## Notas
```
