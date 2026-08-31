---
description: Revisão de literatura — busca candidatos, aguarda aprovação, baixa e processa
argument-hint: [area/projeto/tema] [exploratória|semi-sistemática]
allowed-tools: Bash(uv run:*), Read, Write, Edit, Glob, AskUserQuestion
---

# /literature-review

Executa uma revisão de literatura para um tema: busca candidatos no OpenAlex,
apresenta a lista para aprovação **item a item**, baixa apenas os aprovados que
tiverem PDF open access, e registra o restante como pendência.

Argumentos recebidos: `$ARGUMENTS`

> **Este documento é o roteiro do AGENTE, não do usuário.** Execute os passos em
> sequência numa única invocação. Há duas paradas legítimas para falar com o
> usuário: o passo 1/2 (resolver localização e tipo, se não informados) e o
> passo 7 (aprovação dos candidatos, obrigatória — G4). Fora essas, conduza o
> fluxo até o fim sem devolver o controle no meio.

---

## Passo 1 — Resolver a localização

**Nunca assuma área, projeto ou tema** (CLAUDE.md, fluxo 1).

```bash
uv run python -m scripts.process_materials list-locations
```

- Localização completa (`area/projeto/tema`) nos argumentos e existente → siga.
- **Área ou projeto ausentes → PARE e pergunte** com `AskUserQuestion`, listando as
  áreas/projetos encontrados acima e oferecendo criar novos. Não prossiga sem resposta.
- Localização nova → confirme antes de criar.

## Passo 2 — Resolver o tipo de revisão

**Se o tipo não veio nos argumentos, PARE e pergunte** (CLAUDE.md, fluxo 2):

- **(a) exploratória/narrativa** — busca mais livre, sem protocolo formal.
- **(b) semi-sistemática** — exige `search-protocol.md` validado antes de buscar.

## Passo 3 — Ler o contexto do tema

Leia o `context.md`. Ele determina as strings de busca e, depois, os scores.

Se estiver vazio ou só com o placeholder, **pergunte ao usuário** a pergunta de
pesquisa e os conceitos-chave antes de buscar — uma busca sem contexto produz
candidatos irrelevantes. Ofereça preencher o `context.md` com as respostas.

## Passo 4 — (Semi-sistemática) Protocolo de busca

Só para o tipo (b). Escreva `<tema>/search-protocol.md`:

```markdown
# Protocolo de busca

## Pergunta de pesquisa
## Strings de busca
| # | String | Base |
|---|---|---|
## Critérios de inclusão
## Critérios de exclusão
## Recorte temporal
## Log de decisões
| Data | Decisão | Justificativa |
|---|---|---|
```

**Apresente o protocolo e aguarde a validação explícita do usuário antes de buscar.**

## Passo 4b — Protocolo de triagem (todos os tipos de revisão)

Escreva `<tema>/screening-protocol.md`, derivado do `context.md`. Ele serve para
triar os PDFs obtidos — em outro assistente de IA ou na leitura do próprio usuário
— decidindo se cada paper realmente pertence ao corpus.

A busca filtra por termos; ela não distingue um paper que **faz** o que o tema
investiga de um que apenas menciona os mesmos assuntos. Esta triagem faz esse corte
lendo o texto completo.

Estrutura obrigatória:

1. **O que esta triagem decide** — o critério discriminante do tema, em uma tabela
   curta. Quando o tema tiver uma direção de relação (X produz Y vs. Y alimenta X),
   ela é o critério central.
2. **Perguntas de investigação** — 4-8 perguntas objetivas derivadas do
   `context.md`, cada uma testando um aspecto do escopo declarado.
3. **Regras de veredito** — INCLUIR / TALVEZ / EXCLUIR, ancoradas nas perguntas e
   nos critérios de exclusão do `search-protocol.md` quando ele existir.
4. **Score de aderência 0-10** — faixas com significado explícito.
5. **Prompt pronto para colar** — bloco ```text autônomo, que o usuário envia junto
   com o PDF a qualquer IA. Deve exigir: responder só a partir do texto fornecido,
   citação literal sustentando cada afirmação, "não encontrado no texto" quando não
   houver evidência, e formato de saída fixo. Isso é o G3 aplicado à triagem.
6. **Registro das triagens** — tabela para o usuário acumular os vereditos.

## Passo 5 — Buscar

Derive 2-5 strings do `context.md` (termos em inglês tendem a render mais no OpenAlex;
inclua variações em português quando o tema for local).

```bash
uv run python -m scripts.literature_review search <area>/<proj>/<tema> \
  --query "primeira string" \
  --query "segunda string" \
  --type "exploratória/narrativa" \
  --from-year 2018
```

Isso deduplica contra o `references.bib` do tema, aplica o teto de 30 (G5) e grava
`candidates.md` com **todos os itens desmarcados** e `.search-manifest.json`.

**G7 — idioma.** A busca já filtra por inglês e português (`accepted_languages` no
config.yaml); papers em outros idiomas são descartados automaticamente. O comando
lista os descartes ao final — **repasse essa lista ao usuário**, para que ele saiba
o que a regra excluiu.

## Passo 6 — Pontuar os candidatos

Leia `.search-manifest.json` e, para cada candidato, atribua **score 0-10 com
justificativa de uma linha**, comparando o abstract real ao `context.md`.

**G2 — não invente candidatos.** Pontue apenas o que a API retornou. Nunca acrescente
um paper que você conhece mas que não veio na busca.

Edite `candidates.md` preenchendo o campo `**Score**` de cada item e **reordene os
itens por score decrescente**, renumerando-os. Depois apresente ao usuário um resumo
dos melhores itens e peça a aprovação.

## Passo 7 — Aprovação (G4)

O usuário aprova **item a item**, de duas formas:

- Editando `candidates.md` e marcando `[x]`.
- Respondendo no chat (ex.: "aprovo 1, 4 e 7") — nesse caso **você** marca os `[x]`
  correspondentes com Edit.

**Nunca marque itens por conta própria.** Sem marcação explícita do usuário, nada é
baixado. Não interprete "pode seguir" como aprovação de todos — confirme quais.

## Passo 8 — Baixar os aprovados

```bash
uv run python -m scripts.literature_review fetch <area>/<proj>/<tema>
```

O comando baixa **apenas os itens marcados**, tentando OpenAlex → arXiv → Unpaywall.
Recusa rodar se nenhum item estiver marcado.

- Baixado → segue para o pipeline da Fase 1 (gera `.process-manifest.json`).
- Bloqueado (paywall, HTML, erro) → linha em `pending.md` com host, link e motivo.
  **Nunca tente outro caminho para contornar o bloqueio.**

## Passo 9 — Resumos e consolidação

Para cada paper baixado, siga os passos 3 e 4 de `/process-materials`: leia o texto em
`.extracted-text/`, escreva o resumo no template (G3, G6) e depois:

```bash
uv run python -m scripts.process_materials commit <area>/<proj>/<tema>
```

## Passo 10 — Relatar

- Quantos candidatos encontrados, aprovados, baixados e pendentes.
- Nomes finais dos PDFs e entradas adicionadas ao `references.bib`.
- **Toda entrada `INCOMPLETE`** e todo item em `pending.md`, com o motivo.
- Duplicados ignorados e itens cortados pelo limite de 30 (G5).

Para conferir o estado a qualquer momento:

```bash
uv run python -m scripts.literature_review status <area>/<proj>/<tema>
```