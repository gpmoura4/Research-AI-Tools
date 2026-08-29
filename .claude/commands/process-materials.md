---
description: Processa PDFs depositados em materials/ — renomeia, resume e gera BibTeX
argument-hint: [area/projeto/tema]
allowed-tools: Bash(uv run:*), Read, Write, Glob
---

# /process-materials

Processa os PDFs que o usuário depositou em `materials/` de um tema: extrai metadados,
busca o BibTeX oficial no Crossref, renomeia os arquivos, escreve os resumos
estruturados e atualiza o `references.bib`.

Argumento recebido: `$1`

> **Este documento é o roteiro do AGENTE, não do usuário.** Os passos abaixo são
> executados numa única invocação do comando, sem parar entre eles. O passo 3
> (escrever os resumos) é leitura, não script: nenhum comando o faz. Portanto,
> ao invocar `/process-materials`, execute os passos 2, 3 e 4 em sequência e só
> devolva o controle ao usuário no passo 5 — ou antes, se precisar perguntar a
> localização (passo 1) ou relatar um bloqueio.

---

## Passo 1 — Resolver a localização

**Nunca assuma a área, o projeto ou o tema por conta própria** (CLAUDE.md, fluxo 1).

Liste o que existe:

```bash
uv run python -m scripts.process_materials list-locations
```

- Se `$1` veio completo (`area/projeto/tema`) e existe → use e siga para o Passo 2.
- Se `$1` está ausente ou incompleto → **pare e pergunte ao usuário**, apresentando as
  localizações listadas acima como opções, e ofereça criar uma nova. Não prossiga sem resposta.
- Se a localização informada não existe → confirme com o usuário antes de criá-la.

## Passo 2 — Extrair

```bash
uv run python -m scripts.process_materials extract <area>/<projeto>/<tema>
```

Isso lê cada PDF, resolve os metadados no Crossref e grava:

- `<tema>/.process-manifest.json` — o plano de processamento (nomes de arquivo,
  citation keys, metadados, notas).
- `<tema>/.extracted-text/*.txt` — o texto real de cada PDF.

Nada é movido ainda. **Leia o manifest** antes de continuar.

Relate ao usuário qualquer item com:
- `"metadata_source": "pdf-only"` → sem DOI e sem correspondência confiável; a entrada
  BibTeX sairá marcada como `% INCOMPLETE - verificar manualmente`.
- `"metadata_source": "crossref-title-search"` → correspondência por título, não por DOI.
  Mencione o `match_score` e peça conferência.
- `"text_extraction_failed": true` → provável PDF escaneado sem OCR.
- `"status": "duplicate"` → já está no `references.bib`; será ignorado (modo incremental).

## Passo 3 — Escrever os resumos

Para cada paper no manifest com `"status": "planned"`:

1. Leia o texto em `<tema>/.extracted-text/<nome>.txt` (caminho no campo `text_file`).
2. Leia o `context.md` do tema — ele alimenta o campo *Relevance to theme*.
3. Escreva `<tema>/deliverables/summaries/<mesmo-nome-do-pdf>.md`, sem a extensão `.pdf`.

**Guardrails obrigatórios:**

- **G3** — O resumo vem **exclusivamente do texto extraído**. Nunca use conhecimento
  próprio sobre o paper, nem que você o reconheça. Se `text_extraction_failed` for `true`
  ou o texto for insuficiente, o resumo deve declarar isso explicitamente numa primeira
  linha em itálico e cobrir só o que o texto permitir — nunca preencher as lacunas.
- **G6** — Escreva no idioma do campo `summary_language` do manifest (`en` por padrão;
  `pt` apenas quando o paper original for em português).
- Alvo de **150-250 palavras** no total.

Template exato (`summaries/<mesmo-nome-do-pdf>.md`):

```markdown
# <Título do paper>

- **Citation key**: <citation_key do manifest — o mesmo do references.bib>
- **Objective**: <1-2 frases>
- **Method**: <1-2 frases>
- **Key findings**:
  - <bullet>
  - <bullet>
- **Relevance to theme**: <1-2 frases conectando ao context.md>
- **Keywords**: <3-6, do paper; marque as inferidas com [inferred]>
```

## Passo 4 — Consolidar

```bash
uv run python -m scripts.process_materials commit <area>/<projeto>/<tema>
```

Move os PDFs renomeados para `deliverables/papers/` e insere as entradas no
`references.bib` (dedupe por DOI, depois por título normalizado). O comando **recusa**
qualquer paper sem resumo — se ele listar pendências, volte ao Passo 3.

Ao terminar, o manifest e o `.extracted-text/` são apagados.

## Passo 5 — Relatar

Informe ao usuário:

- Quantos PDFs foram processados, com os nomes finais.
- Quantas entradas entraram no `references.bib`.
- **Toda entrada `INCOMPLETE`** e toda correspondência por título — são os pontos que
  exigem conferência manual dele.
- Papers ignorados por duplicidade ou pelo limite de 30 por passada (G5).
