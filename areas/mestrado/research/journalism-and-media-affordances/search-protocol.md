# Protocolo de busca

> **Validado pelo usuário em 2026-10-15**, inclusive a S5. Nenhuma busca foi executada ainda.

## Pergunta de pesquisa
Quais artigos publicados na *Journalism and Media* dialogam com o FAMO (affordances,
mecanismos e outcomes de polarização, curadoria, governança e jornalismo em plataformas) e
em que pontos do manuscrito podem ser citados?

## Strings de busca

Base: OpenAlex, filtro `primary_location.source.id:S4210232010` (*Journalism and Media*,
ISSN 2673-5172), busca em título e resumo (`--precise`), idiomas en|pt (G7).
Contagens de 2026-10-15, só metadados.

| # | String | Base | Itens |
|---|---|---|---|
| S1 | `affordance OR affordances` | OpenAlex, J&M | 24 |
| S2 | `polarization OR polarisation OR "echo chamber" OR "echo chambers" OR "filter bubble"` | OpenAlex, J&M | 29 |
| S3 | `(algorithm OR algorithmic OR algorithms OR recommendation OR "content moderation" OR "platform governance") AND ("social media" OR platform OR platforms)` | OpenAlex, J&M | 48 |
| S4 | `(incivility OR toxicity OR "hate speech" OR "news avoidance" OR "selective exposure") AND ("social media" OR platform OR platforms)` | OpenAlex, J&M | 7 |
| S5 | `(platformization OR platformisation OR "platform dependence") AND (algorithm OR algorithmic OR metrics OR visibility)` | OpenAlex, J&M | 53 |
| S6 | `(misinformation OR disinformation) AND ("social media" OR platform OR platforms) AND (algorithm OR algorithmic OR affordance OR affordances OR polarization OR "echo chamber")` | OpenAlex, J&M | 6 |

União sem repetidos: 108. Núcleo (S1 ∪ S2): 52.

**Passadas (G5, até 30 candidatos por execução)**, em ordem de prioridade:

| Passada | Strings | Observação |
|---|---|---|
| P1 | S1 | núcleo: affordances |
| P2 | S2 | núcleo: polarização |
| P3 | S3, S4, S6 | mecanismos e governança, possivelmente em duas passadas |
| P4 | S5 | jornalismo em plataformas, em duas passadas |

Itens já vistos numa passada anterior são retirados da seguinte antes da pontuação.

## Critérios de inclusão
1. Publicado na *Journalism and Media*.
2. Artigo de pesquisa ou revisão.
3. Trata de pelo menos um elemento do FAMO: affordances ou features de plataformas, um dos
   mecanismos ou outcomes de polarização, moderadores ou intervenções. Ou trata da relação
   entre jornalismo e o design das plataformas (curadoria, métricas, governança), ligada à
   Seção 10.2 do manuscrito.
4. Em inglês ou português (G7).

## Critérios de exclusão
1. Editoriais, erratas, resenhas e chamadas de edição especial.
2. Estudos de prática jornalística sem dimensão de plataforma ou de design.
3. Plataforma só como fonte de dados para um tema sem relação com o FAMO (por exemplo, um
   corpus do Twitter sobre um assunto qualquer).

## Recorte temporal
2020 (primeiro volume da revista) até a data da busca.

## Log de decisões

| Data | Decisão | Justificativa |
|---|---|---|
| 2026-10-15 | Tema dedicado, revisão semi-sistemática | Decisão do usuário. Busca numa revista só, reprodutível e auditável. |
| 2026-10-15 | Recorte: affordances + temas do FAMO | Decisão do usuário. Pontos de conexão vão além da Seção 7 (ex.: 10.2). |
| 2026-10-15 | S3–S6 exigem co-ocorrência com plataforma ou com o núcleo do FAMO | As versões amplas retornavam 77 (S3), 82 (S4) e 177 (S5) itens, a maioria sem relação com design de plataformas. |
| 2026-10-15 | S5 (jornalismo em plataformas) entra, com a restrição a algoritmo, métricas ou visibilidade | Aprovado pelo usuário. Liga-se à Seção 10.2 e ao mecanismo G1. |
| 2026-10-15 | Protocolo validado | Aprovação explícita do usuário. Próximo passo: `screening-protocol.md` e passada P1. |
| 2026-10-15 | P1 (S1): 24 candidatos, 3 aprovados | Nenhum acima de 6: "affordance" aparece quase sempre em sentido descritivo, e o termo casou com "afford"/"affordability" (2 falsos positivos). Registro em `deliverables/candidates-P1.md`. |
| 2026-10-15 | Download automatizado bloqueado pela MDPI (HTTP 403) | Todo aprovado vai para `pending.md`. O usuário baixa os PDFs (open access) pelo navegador e os deposita em `materials/`, que segue para `/process-materials`. |
| 2026-10-15 | P2 (S2): 29 resultados, 1 já visto, 28 candidatos, 5 aprovados | Registro em `deliverables/candidates-P2.md`. |
| 2026-10-15 | P3 dividida em P3a (S4 + S6) e P3b (S3) | S3 + S4 + S6 somam 61 resultados, acima do limite de 30 por passada (G5). P3a: 13 resultados, 1 repetido entre as strings, 3 já vistos, 9 candidatos. |
| 2026-10-15 | Busca pausada pelo usuário; avaliação do primeiro lote (P1 + P2, 8 artigos) | Decisão do usuário. P3a registrada em `deliverables/candidates-P3a.md` sem aprovação; P3b e P4 não executadas. Triagem no `screening-protocol.md` e avaliação em `manuscripts/smip-famo-framework/reviews/T04-journalism-and-media.md`. |
