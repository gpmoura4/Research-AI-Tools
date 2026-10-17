# Research Workspace — Contexto do Projeto

## Papel
Você é o agente de desenvolvimento e operação de um repositório que funciona como
ferramenta de pesquisa acadêmica. O repositório é operado via Claude Code: o agente
lê e escreve arquivos localmente, sem application standalone e sem frontend.

## Modos de trabalho
O repositório opera em dois modos, que coexistem sem se misturar. Identifique o
modo antes de agir; na dúvida, pergunte.

| Modo | Quando | Onde | Regras |
|---|---|---|---|
| **Revisão de literatura** | busca, triagem e síntese de papers sobre um tema | `areas/<area>/<projeto>/<tema>/` | este arquivo (seções marcadas "modo revisão de literatura") + `/literature-review`, `/process-materials` |
| **Revisão de manuscrito** | revisão crítica de um artigo do usuário antes da submissão; tarefas `T01`, `T02`… | `manuscripts/<slug-do-paper>/` | `manuscripts/CLAUDE.md` + `/manuscript-review` |

>> Ao receber uma tarefa de revisão de manuscrito (inclusive mencionada só pelo ID,
ex.: "T03"), LEIA `manuscripts/CLAUDE.md` e siga o roteiro de
`.claude/commands/manuscript-review.md` antes de qualquer outra ação. <<

Regras específicas de um modo não valem no outro. As seções "Regras comuns" e
"Stack e convenções técnicas" valem nos dois.

## Objetivo (modo revisão de literatura)
Dado um TEMA (contexto) e uma TAREFA (ex.: revisão de literatura), o agente executa
um pipeline que produz entregáveis organizados por tema: papers baixados e renomeados,
resumos estruturados, arquivo BibTeX consolidado, lista de pendências e diagramas
conceituais.

## Estrutura do repositório
Organização em três níveis: ÁREA da vida do usuário → PROJETO → TEMA.
Exemplos: areas/trabalho/projeto-a/tema-x/ ; areas/mestrado/dissertacao/debates-improdutivos/

research-workspace/
├── areas/
│   └── <slug-da-area>/                 # ex.: trabalho, mestrado
│       └── <slug-do-projeto>/          # ex.: projeto-a, dissertacao
│           └── <slug-do-tema>/
│               ├── context.md          # contexto do tema (escrito pelo usuário)
│               ├── search-protocol.md  # apenas p/ revisão semi-sistemática
│               ├── screening-protocol.md # perguntas de triagem + prompt p/ outra IA
│               ├── materials/          # PDFs/refs fornecidos manualmente pelo usuário
│               ├── screening/          # listas de títulos triadas pelo usuário (<lote>-elegiveis.txt)
│               └── deliverables/
│                   ├── batches/        # <lote>-baixados.md e <lote>-nao-baixados.md (lista + abstracts)
│                   ├── papers/         # PDFs renomeados: "Autores - Ano - Título.pdf"
│                   ├── summaries/      # 1 arquivo .md por paper
│                   ├── references.bib  # BibTeX consolidado do tema
│                   ├── pending.md      # papers não baixados (nome + link + motivo)
│                   ├── candidates.md   # lista de candidatos aguardando aprovação
│                   └── maps/
│                       ├── keywords-clusters.mmd
│                       ├── citation-graph.mmd
│                       └── thematic-taxonomy.mmd
├── manuscripts/                        # modo revisão de manuscrito (ver manuscripts/CLAUDE.md)
│   ├── CLAUDE.md                       # regras do modo
│   └── <slug-do-paper>/
│       ├── context.md                  # contexto do manuscrito + tema(s) de literatura vinculados
│       ├── INDEX.md                    # índice de tarefas e pendências abertas
│       ├── reference-coverage.md       # referências do manuscrito × PDFs disponíveis
│       ├── paper/                      # manuscrito, versões datadas (não versionado no Git)
│       ├── references/                 # PDFs das obras citadas: [n]_Autor_Ano.pdf (não versionado)
│       └── reviews/                    # relatórios T01-<slug>.md, T02-<slug>.md…
├── .claude/
│   ├── settings.json                   # pede confirmação antes de editar manuscripts/*/paper/
│   └── commands/                   # comandos: /literature-review, /process-materials, /manuscript-review, /map, /status
├── scripts/                        # scripts Python do pipeline
├── config.yaml                     # limites, APIs, convenções
└── CLAUDE.md                       # este arquivo

## Stack e convenções técnicas
- Python gerenciado exclusivamente com `uv` e `pyproject.toml`. Nunca usar pip direto.
- Diagramas em Mermaid (.mmd), versionáveis em Git.
- APIs de busca/metadados: OpenAlex (busca principal), Crossref (BibTeX por DOI),
  Semantic Scholar (grafo de citações), Unpaywall/arXiv (localização de PDF open access).
  Respeitar rate limits e usar polite pool (e-mail no header) quando aplicável.

## Regras comuns (valem nos dois modos)
- BibTeX: toda entrada BibTeX gravada no repositório, em qualquer modo, segue o G1
  (Crossref via DOI ou metadados verificáveis; nunca de memória).
- Busca de literatura nova, em qualquer modo, roda pelo fluxo do modo revisão de
  literatura, num tema de `areas/`, com aprovação humana por item (G4).
- Os guardrails G2–G7 abaixo são do modo revisão de literatura. A forma como se
  aplicam (ou não) ao modo de manuscrito está em `manuscripts/CLAUDE.md`.
- Commits (o repositório no GitHub já vazou uma chave e o manuscrito, no commit e9db5b6):
  adicionar arquivos sempre pelo nome — nunca `git add -A`, `git add .` ou `git add -f`;
  antes de commitar, conferir `git diff --cached --stat` e parar se aparecer algo de
  `credentials/`, `manuscripts/*/paper/`, `manuscripts/*/references/`, compactado
  (.zip etc.) ou PDF. Chaves ficam só em `credentials/` (fora do Git); o config.yaml
  guarda apenas o caminho. O hook `.githooks/pre-commit` (ativo via
  `git config core.hooksPath .githooks`) bloqueia esses casos; nunca usar `--no-verify`
  sem o ok do usuário.

## Fluxo de operação — modo revisão de literatura (visão geral)
1. Ao iniciar qualquer pesquisa/revisão, o agente resolve a LOCALIZAÇÃO do trabalho:
   área → projeto → tema (ex.: "trabalho, projeto A, tema X" ou
   "mestrado, dissertação, debates improdutivos").
   >> Se área ou projeto NÃO forem informados, o agente DEVE perguntar antes de
   iniciar, listando as áreas/projetos já existentes em `areas/` para o usuário
   escolher ou criar um novo. Nunca assumir a área por conta própria. <<
   Área/projeto/tema inexistentes são criados sob demanda (estrutura + context.md).
2. Usuário solicita revisão de literatura informando o tipo:
   (a) exploratória/narrativa ou (b) semi-sistemática.
   >> Se o tipo NÃO for informado, o agente DEVE perguntar antes de iniciar. <<
   Se semi-sistemática: gerar/validar `search-protocol.md` (strings de busca,
   critérios de inclusão/exclusão, log de decisões) antes de buscar.
2b. Em qualquer tipo de revisão, gerar `screening-protocol.md` a partir do
   context.md: perguntas de investigação objetivas, regras de veredito
   (INCLUIR/TALVEZ/EXCLUIR), score de aderência e um prompt pronto para colar em
   outro assistente de IA. Serve para triar os PDFs obtidos — a busca filtra por
   termos, mas não distingue quem FAZ o que o tema investiga de quem apenas
   menciona os mesmos assuntos.
3. Agente busca candidatos e grava `candidates.md` com: título, autores, ano, venue,
   abstract, score de relevância (0-10) justificado em 1 linha, DOI/link.
4. Usuário aprova itens da lista (aprovação por item, não em bloco).
5. Agente tenta baixar apenas os aprovados:
   - PDF open access acessível → baixa, renomeia, extrai metadados, gera resumo e BibTeX.
   - Bloqueado (paywall, captcha, erro) → registra em `pending.md` com nome do paper,
     link da plataforma onde está hospedado e status "pendente — cabe revisão manual".
     NUNCA tentar burlar paywall.
5b. Lista de títulos já triada pelo usuário (lote de triagem feito fora do
   repositório): a lista vale como aprovação item a item (G4). Gravar em
   `screening/<lote>-elegiveis.txt` e rodar
   `uv run python -m scripts.title_list fetch <area>/<proj>/<tema> --titles <arquivo> --batch <lote>`
   (repetir até zerar a fila: até 30 downloads por execução, pelo G5; `--retry` volta a
   tentar os itens não obtidos). Título sem correspondência verificável no
   OpenAlex/Crossref fica como "não localizado" (G2). Saída:
   `deliverables/batches/<lote>-baixados.md`, `<lote>-nao-baixados.md` + `pending.md`.
   Os PDFs de cada lote ficam em `deliverables/papers/<lote>/` (o lote-01 de
   `mestrado/research/polarizacao-redes-sociais`, anterior a essa regra, ficou na raiz
   de `papers/`). Paper já baixado em outro lote é referenciado, não duplicado.
6. Agente processa também PDFs que o usuário depositar em `materials/` (mesmo pipeline
   de renomeação, resumo e BibTeX).
7. Agente gera/atualiza os três diagramas em `maps/`.

## Guardrails do modo revisão de literatura (invioláveis)
- G1 — BibTeX: NUNCA gerar entradas BibTeX de memória do modelo. Toda entrada deve
  vir do Crossref (via DOI) ou de metadados extraídos verificáveis. Se não houver DOI
  nem metadados confiáveis, criar entrada mínima com campos vazios e marcar com
  comentário `% INCOMPLETE - verificar manualmente`.
- G2 — Sem alucinação de papers: nunca citar, resumir ou listar um paper que não
  tenha sido retornado por uma API ou fornecido pelo usuário. Todo item em
  candidates.md deve ter DOI ou URL real retornada pela busca.
- G3 — Resumos: gerados APENAS a partir do texto real do PDF (ou do abstract da API
  se o PDF não estiver disponível). Se o texto não puder ser extraído, o resumo diz
  explicitamente que se baseia apenas no abstract.
- G4 — Aprovação humana: nenhum download em lote sem aprovação explícita do usuário
  sobre a lista de candidatos.
- G5 — Limite por passada: máximo de 30 papers por execução (configurável em
  config.yaml, mas o padrão é 30).
- G6 — Idioma dos resumos: inglês por padrão; português apenas se o paper original
  for em português.
- G7 — Idioma dos papers: buscar e baixar APENAS textos em inglês ou português
  (configurável em `accepted_languages`, no config.yaml). Papers em outros idiomas
  são descartados dos candidatos e nunca baixados. O filtro atua em três camadas:
  na consulta ao OpenAlex, na revalidação do título+abstract (para registros sem
  metadado de idioma) e no texto do PDF já baixado. Os descartes devem ser
  SEMPRE reportados ao usuário — nunca silenciosamente.

## Convenção de renomeação de arquivos (modo revisão de literatura)
Formato: "<Autores> - <Ano> - <Título>.pdf"
- 1 autor: "Sobrenome"
- 2 autores: "Sobrenome1 e Sobrenome2"
- 3+ autores: "Sobrenome1 et al"
- Ano ausente: omitir o campo (ex.: "Silva - Título.pdf")
- Título: truncar em 80 caracteres (no último espaço antes do limite)
- Sanitização: remover/substituir caracteres inválidos em filesystem
  (/ \ : * ? " < > |), normalizar Unicode, colapsar espaços múltiplos.
- Colisão de nome: sufixar " (2)", " (3)" etc.

## Template de resumo — modo revisão de literatura (summaries/<mesmo-nome-do-pdf>.md)
Curto e estruturado — alvo de 150-250 palavras no total:
- **Citation key**: (a mesma do references.bib)
- **Objective**: 1-2 frases
- **Method**: 1-2 frases
- **Key findings**: 2-4 bullets
- **Relevance to theme**: 1-2 frases conectando ao context.md do tema
- **Keywords**: 3-6, extraídas do paper (ou inferidas, marcadas como [inferred])

## Deduplicação e re-execução (modo revisão de literatura)
- Dedupe por DOI (primário) e por título normalizado (fallback).
- Paper presente em dois temas (mesmo entre áreas/projetos diferentes): manter o
  PDF no tema onde foi processado primeiro e referenciar no outro (link relativo
  em summaries/), sem duplicar o arquivo. O references.bib de cada tema, porém,
  inclui a entrada completa (BibTeX pode repetir entre temas — cada tema deve ser
  autossuficiente para uso no Overleaf).
- Re-execução de revisão no mesmo tema: modo incremental por padrão (não sobrescrever
  entregáveis existentes; adicionar novos e atualizar references.bib e maps/).