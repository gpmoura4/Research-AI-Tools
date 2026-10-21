# Ajustes T06 — Figuras

- **Manuscrito**: smip-famo-framework · **Versão de referência**: cópia de revisão lida em 2026-10-20 (42 mecanismos, 7 blocos)
- **Relatório**: [`reviews/T06-figuras.md`](../reviews/T06-figuras.md) (diagnóstico e plano de lotes, §7)
- **Destino**: cópia de revisão em Google Docs (ID em `context.md`)
- **Imagens**: geradas por [`T06-figuras/gen_affordance_figs.py`](T06-figuras/gen_affordance_figs.py) a partir de [`T06-figuras/famo_data.json`](T06-figuras/famo_data.json) (Tabela 7). PNG a 600 dpi em `T06-figuras/out/` (fora do Git). Trocadas no documento por `scripts/gdocs_figures.py` (decisão D3 do usuário, 2026-10-20: OAuth do usuário, link público temporário apagado logo depois da inserção). A imagem antiga é removida do documento por pedido do usuário ("substituindo as imagens correspondentes") e fica guardada em `T06-figuras/out/originais/`.
- **Legendas**: `substituir-parcial` (o texto antigo fica riscado, o novo entra em amarelo). Sem travessão nem ponto e vírgula.
- **Ordem dos lotes**: o lote 2 (Figuras 4–9) vem antes do lote 1 (Figuras 2 e 3), que espera a decisão D1 (loop).

## T06-A1 — Figura 4 (AF1), legenda

| Campo | Valor |
|---|---|
| Achado | T06-F01, T06-F08 |
| Lote | 2 |
| Localização | 7.1, legenda da Figura 4 |
| Ação | substituir-parcial |
| Estado | aplicado em 2026-10-20 (legenda e imagem) |

```original
4. {{Algorithmic content curation (AF1)}}
```

```novo
4. {{Mechanisms fed by algorithmic content curation (AF1), grouped by block (Section 6). Solid lines mark direct links, dashed lines indirect links, and the bar-ended line a link through which the affordance can weaken the mechanism (−), as in Table 7.}}
```

**Justificativa**: a legenda passa a explicar a notação da figura nova (F08). Ligações conforme a Tabela 7: 15, com B2 (−), C3\* e E3\*.

## T06-A2 — Figura 5 (AF2), legenda

| Campo | Valor |
|---|---|
| Achado | T06-F01, T06-F08 |
| Lote | 2 |
| Localização | 7.1, legenda da Figura 5 |
| Ação | substituir-parcial |
| Estado | aplicado em 2026-10-20 (legenda e imagem) |

```original
5. {{Network-informed associating (AF2)}}
```

```novo
5. {{Mechanisms fed by network-informed associating (AF2), grouped by block (Section 6). Solid lines mark direct links and dashed lines indirect links, as in Table 7.}}
```

**Justificativa**: notação da figura nova. Ligações: B1, B5\*, B6\*, B7, D3\*, D4\*.

## T06-A3 — Figura 6 (AF3), legenda

| Campo | Valor |
|---|---|
| Achado | T06-F01, T06-F08 |
| Lote | 2 |
| Localização | 7.1, legenda da Figura 6 |
| Ação | substituir-parcial |
| Estado | aplicado em 2026-10-20 (legenda e imagem) |

```original
6. {{Asymmetric following (AF3)}}
```

```novo
6. {{Mechanisms fed by asymmetric following (AF3), grouped by block (Section 6). Solid lines mark direct links and dashed lines indirect links, as in Table 7.}}
```

**Justificativa**: notação da figura nova. Ligações: B1, B2, B4\*, B5\*, B6\*, C5, D3\*, D4\*.

## T06-A4 — Figura 7 (AF4), legenda

| Campo | Valor |
|---|---|
| Achado | T06-F01, T06-F08 |
| Lote | 2 |
| Localização | 7.1, legenda da Figura 7 |
| Ação | substituir-parcial |
| Estado | aplicado em 2026-10-20 (legenda e imagem) |

```original
7. {{Social quantification (AF4)}}
```

```novo
7. {{Mechanisms fed by social quantification (AF4), grouped by block (Section 6). Solid lines mark direct links and the dashed line an indirect link, as in Table 7.}}
```

**Justificativa**: notação da figura nova. Ligações: B4\*, B9, D2, E1, E2, E3, G3.

## T06-A5 — Figura 8 (AF5), legenda

| Campo | Valor |
|---|---|
| Achado | T06-F01 |
| Lote | 2 |
| Localização | 7.1, legenda da Figura 8 |
| Ação | substituir-parcial |
| Estado | aplicado em 2026-10-20 (legenda e imagem) |

```original
8. {{Replicability (AF5)}}
```

```novo
8. {{Mechanisms fed by replicability (AF5), grouped by block (Section 6). All three links are direct, as in Table 7.}}
```

**Justificativa**: ligações B9, D6, E2, todas diretas.

## T06-A6 — Figura 9 (AF6), legenda

| Campo | Valor |
|---|---|
| Achado | T06-F01 |
| Lote | 2 |
| Localização | 7.1, legenda da Figura 9 |
| Ação | substituir-parcial |
| Estado | aplicado em 2026-10-20 (legenda e imagem) |

```original
9. {{Audience segmentation (AF6)}}
```

```novo
9. {{Mechanisms fed by audience segmentation (AF6), grouped by block (Section 6). All seven links are direct, as in Table 7.}}
```

**Justificativa**: ligações B2, B4, B7, C5, D5, F2, F4, todas diretas. O título da figura antiga era "Context collapse", que a 7.2 trata como o extremo baixo desta affordance.

## T06-A7 — Figura 2 (framework), legenda

| Campo | Valor |
|---|---|
| Achado | T06-F04, T06-F07 |
| Lote | 1 |
| Localização | 5.1, legenda da Figura 2 |
| Ação | substituir-parcial |
| Estado | aplicado em 2026-10-20 |

```original
actors that {{exploit mechanisms and shape outcomes, and a feedback loop from outcomes to features.}}
```

```novo
actors that {{enact or exploit mechanisms and shape outcomes, and a feedback loop from outcomes to features, whose closing points are detailed in Figure 3.}}
```

**Nota (2026-10-20, depois da aplicação)**: a imagem nova da Figura 2 foi substituída no documento por um humano, que voltou a imagem original (objeto `kix.1c4i1lkgfh6l`, 365 × 297 pt). O usuário pediu que a Figura 2 não seja alterada. A legenda (este ajuste) e a frase T06-A9 continuam aplicadas, em amarelo.

**Justificativa**: a figura nova usa "enact or exploit", como a 5.1 ("actors enact or exploit mechanisms and shape the outcomes these produce") e a 5.3. A remissão à Figura 3 liga as duas figuras do loop (F04). Loop desenhado pela opção (a) de D1.

## T06-A8 — Figura 3 (fechamentos do loop), legenda

| Campo | Valor |
|---|---|
| Achado | T06-F03 |
| Lote | 1 |
| Localização | 5.2, legenda da Figura 3 |
| Ação | substituir-parcial |
| Estado | aplicado em 2026-10-20 |

```original
3. {{Three concrete points where the feedback loop closes.}}
```

```novo
3. {{Three points where the feedback loop closes (Section 5.2). In each chain, a mechanism changes the behavioral data used by the features that realize an affordance, and the affordance then feeds a mechanism again. Mechanism boxes are colored by block (Section 6).}}
```

**Justificativa**: a figura nova mostra cadeias de três passos (D5 → AF2 → B1, E1 → AF1 → B8, D3 e D4 → AF4 → D3 e D4), como a 5.2. A legenda diz como ler a cadeia e as cores.

## T06-A9 — 5.2, frase que liga a Figura 2 à Figura 3

| Campo | Valor |
|---|---|
| Achado | T06-F04 |
| Lote | 1 |
| Localização | 5.2, parágrafo "Figure 2 also represents an explicit feedback loop…", depois da última frase |
| Ação | inserir-apos |
| Estado | aplicado em 2026-10-20 |

```original
this article identifies three specific points where this loop closes, detailed in Figure 3.
```

```novo
At each point, a mechanism changes the behavioral data that the features behind an affordance use, such as the interactions on which recommendation and ranking systems are trained or the visible counts of reactions, and the affordance then feeds a mechanism again.
```

**Justificativa**: F04. A Figura 2 desenha o loop de Outcomes para Features, e os três pontos vão de um mecanismo a uma affordance. A frase explicita a passagem (D1, opção a) e resume o que os três parágrafos seguintes da 5.2 já dizem: o *spiral of silence* "alters the behavioral data on which the recommendation systems … are trained", o algoritmo "learns to prioritize" o conteúdo que engaja, e as posições populares "receive more visible likes and shares". Sem referência nova.

## T06-A10 — Figura 10 (AF7), legenda

| Campo | Valor |
|---|---|
| Achado | T06-F01 |
| Lote | 3 |
| Localização | 7.1, legenda da Figura 10 |
| Ação | substituir-parcial |
| Estado | aplicado em 2026-10-20 (legenda e imagem) |

```original
10. {{Constraint affordance (AF7)}}
```

```novo
10. {{Mechanisms fed by the constraint affordance (AF7), grouped by block (Section 6). Both links are direct, as in Table 7.}}
```

**Justificativa**: ligações A4 e F3, diretas. A figura antiga tinha "A5" e "Low-context communication".

## T06-A11 — Figura 11 (AF8), legenda

| Campo | Valor |
|---|---|
| Achado | T06-F01, T06-F08 |
| Lote | 3 |
| Localização | 7.1, legenda da Figura 11 |
| Ação | substituir-parcial |
| Estado | aplicado em 2026-10-20 (legenda e imagem) |

```original
11. {{Identifiability (AF8)}}
```

```novo
11. {{Mechanisms fed by identifiability (AF8), grouped by block (Section 6). All six links are direct, as in Table 7.}}
```

**Justificativa**: ligações B2, B7, C5, F1, F2, G3. Saem o rótulo "cheap fake accounts" em AF8 → F2, que contradizia a 7.1 (F08), e o "M5".

## T06-A12 — Figura 12 (AF9), legenda

| Campo | Valor |
|---|---|
| Achado | T06-F01, T06-F08 |
| Lote | 3 |
| Localização | 7.1, legenda da Figura 12 |
| Ação | substituir-parcial |
| Estado | aplicado em 2026-10-20 (legenda e imagem) |

```original
12. {{Frictionless continuation (AF9)}}
```

```novo
12. {{Mechanisms fed by frictionless continuation (AF9), grouped by block (Section 6). Links as in Table 7.}}
```

**Justificativa**: ligações A2, B8, C7, C8, desenhadas como diretas, conforme a Tabela 7. A legenda não diz "direct" porque o texto da 7.1 chama as quatro de indiretas ("all follow from the same indirect principle"): pendência 2 do relatório, para os autores. Se a decisão for "indiretas", basta regenerar a figura e acrescentar o asterisco na Tabela 7.

## T06-A13 — Figura 13 (AF10), legenda

| Campo | Valor |
|---|---|
| Achado | T06-F01, T06-F08 |
| Lote | 3 |
| Localização | 7.1, legenda da Figura 13 |
| Ação | substituir-parcial |
| Estado | aplicado em 2026-10-20 (legenda e imagem) |

```original
13. {{Platform governance (AF10)}}
```

```novo
13. {{Mechanisms fed by platform governance (AF10), grouped by block (Section 6). Solid lines mark direct links and dotted lines links whose sign depends on how the feature is designed (±), as in Table 7.}}
```

**Justificativa**: ligações A2 (±), C5 (±), G1, G4, G5. A figura antiga não tinha as duas ligações (±) e usava "Deplatforming & migration".

## T06-A14 — Figura 14 (AF11), legenda

| Campo | Valor |
|---|---|
| Achado | T06-F01 |
| Lote | 3 |
| Localização | 7.1, legenda da Figura 14 |
| Ação | substituir-parcial |
| Estado | aplicado em 2026-10-20 (legenda e imagem) |

```original
14. {{Membership (AF11)}}
```

```novo
14. {{Mechanisms fed by membership (AF11), grouped by block (Section 6). All three links are direct, as in Table 7.}}
```

**Justificativa**: ligações B2, B3, B10. A figura antiga se chamava "Group formation" (a 9.1 trata a formação de comunidades como resultado) e não tinha B2.

## T06-A15 — Figura 15 (rede bipartida), legenda

| Campo | Valor |
|---|---|
| Achado | T06-F02 |
| Lote | 3 |
| Localização | fim da 7.3, legenda da Figura 15, depois da frase atual |
| Ação | inserir-apos |
| Estado | aplicado em 2026-10-20 (legenda e imagem) |

```original
and the seven blocks of mechanisms (right).
```

```novo
Line width shows how many mechanisms of the block the affordance feeds, from one to four, and color identifies the block. Dashed lines mark links that are all indirect. Links as in Table 7.
```

**Justificativa**: a frase atual já descreve a figura nova (11 affordances × 7 blocos). O acréscimo explica espessura, cor e tracejado. A figura antiga tinha 9 blocos (M e H) e nomes antigos. A posição da figura (antes do título da Seção 8, que a cita primeiro, T06-I01) não muda neste lote: mover imagem e legenda exige riscar e reinserir a legenda, e fica para os autores ou para um ajuste à parte.

## T06-A16 — Figura 1 (identificação da literatura), legenda

| Campo | Valor |
|---|---|
| Achado | T06-F05 |
| Lote | 4 |
| Localização | 4.3, legenda da Figura 1 |
| Ação | substituir-parcial |
| Estado | aplicado em 2026-10-20 (legenda e imagem) |

```original
1. {{Literature identification process used in this article.}}
```

```novo
1. {{Literature identification process used in this article. The first list was compiled by citation chaining from the four anchor works (Section 4.3, Appendix A.1), and the second survey of the Lens database tested it and added mechanisms (Appendix A.2). Together they yield the 42 mechanisms of Section 6.}}
```

**Justificativa**: F05. A figura nova mostra as duas fontes que a 4.3 (último parágrafo) e o Apêndice A descrevem, com as quatro obras âncora nomeadas (corrige T01-F11). Não traz iteração nem critério de parada, que dependem de T01-D2. Por decisão do usuário (2026-10-20), a Figura A1 não é alterada.

## Log de troca de imagens

| Data | Figura | Arquivo | Objeto antigo | Objeto novo | Revisão antes | Revisão depois |
|---|---|---|---|---|---|---|
| 2026-10-20 20:38 | 4 | `fig04-AF1.png` | `kix.cidyrrmh8np0` | `kix.9pu02ffw52kw` | `AHj4eMQr3oaUEjv9nbry5r0NDImy1qXu2QCq5x7bzrNkbITxnYPdh6KehMy7pSWiF0EJFHQIX3p28uNKKlbsPqYgScC5n82jEnF1TqXHyGASoxc` | `AHj4eMRfGOzw2CZDdngLcrh8Anx-zve6gZRfpMfolreWdUNSfeRwlgLloLoDqfCGSPAYtpBl_U1_h48kzAuyN7Zdl50-xNxXl47sFJ6jXFnt9cA` |
| 2026-10-20 20:39 | 5 | `fig05-AF2.png` | `kix.jx75b9or8698` | `kix.whee6ok5b2va` | `AHj4eMQ9ope3QmlibCt24jMC9pWC9DYGZIHP46lDutBB1oF6mRw0ngihRNY3XXQpP1cQYOfSPm9S8k42Nv5Y1NivJrCdFGCEE-U4MnY6s0yPKz4` | `AHj4eMSzunOMuWX5nPWs985sfg-r23b9fQY3ytlhppLr_nCCboazEMdZgbBkK3zE3XCvkzcPPTunJGP_cfd2UaQF2BFGhMpiakIOzcsojR1urOg` |
| 2026-10-20 20:39 | 6 | `fig06-AF3.png` | `kix.kvxnv7q98k3a` | `kix.qh70ej5uoz5e` | `AHj4eMSzunOMuWX5nPWs985sfg-r23b9fQY3ytlhppLr_nCCboazEMdZgbBkK3zE3XCvkzcPPTunJGP_cfd2UaQF2BFGhMpiakIOzcsojR1urOg` | `AHj4eMTE7CyPgRuuIRvFWnN5eSobUyRUhRRD1Kz3UmDzzEJz4IVzIiio1M_S_OMtFQJ89dZpKiuFLWcmCVeh0mzDMrG5V10y7CQa6sCmxeNQ614` |
| 2026-10-20 20:39 | 7 | `fig07-AF4.png` | `kix.18d4bmb52etc` | `kix.iahpbo9czc8o` | `AHj4eMTE7CyPgRuuIRvFWnN5eSobUyRUhRRD1Kz3UmDzzEJz4IVzIiio1M_S_OMtFQJ89dZpKiuFLWcmCVeh0mzDMrG5V10y7CQa6sCmxeNQ614` | `AHj4eMTWT0sPh4AtLkwazzffTVDi7xBunZsO-BJjHd3ORSAWowo649yr3otaPloMDtUMkT6d_0kEcsQvwIwO0nMqxnjQFrVL26v1k-x7FNGvuFU` |
| 2026-10-20 20:39 | 8 | `fig08-AF5.png` | `kix.5vc042tzzv4r` | `kix.3u1hfhjfhnat` | `AHj4eMTWT0sPh4AtLkwazzffTVDi7xBunZsO-BJjHd3ORSAWowo649yr3otaPloMDtUMkT6d_0kEcsQvwIwO0nMqxnjQFrVL26v1k-x7FNGvuFU` | `AHj4eMRxYn9l9ES7W693dRBGBo8Q0xCevczVZCeuaAqKguenpMAaXQ1AsVHdX0h--QCW1Kk-TRXBDMq1HMf_NhYYQn6rz-V98LyK2WX6bpFJlbQ` |
| 2026-10-20 20:40 | 9 | `fig09-AF6.png` | `kix.dws3m4v2n1go` | `kix.e5hcwfilcyjy` | `AHj4eMRxYn9l9ES7W693dRBGBo8Q0xCevczVZCeuaAqKguenpMAaXQ1AsVHdX0h--QCW1Kk-TRXBDMq1HMf_NhYYQn6rz-V98LyK2WX6bpFJlbQ` | `AHj4eMQ6hwCfdW467IC8tU6g9EKPfVtgfSlB0PPG9OhUu7f_hGbmETdoLLmHD-_oAKPCCuKV0ViGZHvd-qNrtnmNmFheewc02vA3ePYkz41PXKk` |
| 2026-10-20 20:43 | 2 | `fig02-framework.png` | `kix.a2jlrj5wklde` | `kix.yvau1qu7t4nz` | `AHj4eMTTr338KxkEuWj71JH8QrvKCSTf7To5KlQJu3KxNWMgj8_ZXaMgPkEPOR7X0hlbglYZhfwZx24igDV4PE4dgRXAs4AA3ItpJCEItAIMbD4` | `AHj4eMRm3Skn8cqzH8UfS7qj7raU1QvTSzJqNtfOiBlgNbfLO4CWK2KX99O92MDa8hQWOikunurS8avwo8xzf7Xu94m2msWNtZow53fCoyYqImQ` |
| 2026-10-20 20:43 | 3 | `fig03-loop-closures.png` | `kix.4gq9t5r9vx1e` | `kix.noggmy8gu2q3` | `AHj4eMRm3Skn8cqzH8UfS7qj7raU1QvTSzJqNtfOiBlgNbfLO4CWK2KX99O92MDa8hQWOikunurS8avwo8xzf7Xu94m2msWNtZow53fCoyYqImQ` | `AHj4eMRlKdkydwEXBkVgUEENoB7qlIsTK5PGueJIpu0hzWij9MJe4angEU1y3vBUG6RQN6ihAzaS-RGb9cGdinw0E9OMcZmfeXh3bA-vG3NbaVY` |
| 2026-10-20 20:46 | 10 | `fig10-AF7.png` | `kix.csntyg1k2e2` | `kix.b668g9uqm83x` | `AHj4eMSyLVUfkgAlJZt3x33sJFBsH6wHEvFALgd3e_CVjTIr521boqUHR2YFypOUaHfvNfYX6nlACHF6rM6w97USjAgqOf3SmpwX-dDZWoSB6ag` | `AHj4eMQORxnereSidZc_KlmvaMrImVh6el8w32xswoc0x-ckxSPqCXVRem9_0Ua7eC-7iXlIE-9FeT8U6nyXnGd5ArOadTzHuNnHI3p_sZ38U0g` |
| 2026-10-20 20:46 | 11 | `fig11-AF8.png` | `kix.h0bmxrxhlkkh` | `kix.5frqpwkfss8j` | `AHj4eMQORxnereSidZc_KlmvaMrImVh6el8w32xswoc0x-ckxSPqCXVRem9_0Ua7eC-7iXlIE-9FeT8U6nyXnGd5ArOadTzHuNnHI3p_sZ38U0g` | `AHj4eMQ2ulgRsJMf0OXkKtvV4Wmb0m59jqSVb4myTuybCfWHjAsvlKnIATgJcjmnF3lcxd2sS-94erdoUkUv3O9FYxzCyrf1MIzNVZ5tSMvJEzs` |
| 2026-10-20 20:47 | 12 | `fig12-AF9.png` | `kix.bi42cd7z2s9b` | `kix.51a5dma961gu` | `AHj4eMQ2ulgRsJMf0OXkKtvV4Wmb0m59jqSVb4myTuybCfWHjAsvlKnIATgJcjmnF3lcxd2sS-94erdoUkUv3O9FYxzCyrf1MIzNVZ5tSMvJEzs` | `AHj4eMTDq371UzRiHkBKrgf9TEI7YDJuO5B6Ty2DebTCom7vXD_FTM0glrT2SYCw4_f3l8VOl7AUQG21CjxACipLThAO7gDhUeuJVC1b0ZDvLwM` |
| 2026-10-20 20:47 | 13 | `fig13-AF10.png` | `kix.m38p4gecdnvt` | `kix.iqjh4gdxrjz3` | `AHj4eMTDq371UzRiHkBKrgf9TEI7YDJuO5B6Ty2DebTCom7vXD_FTM0glrT2SYCw4_f3l8VOl7AUQG21CjxACipLThAO7gDhUeuJVC1b0ZDvLwM` | `AHj4eMQ2FhniMkHhtY1sO0GWfpysR-cmMpGdMFB9jUolAX7yHFSL61rtq5cAcooHJii8m-dMamTo6jmHhaXtEyLL49ZHf9cc6tPuiKCjCbzV4Qs` |
| 2026-10-20 20:47 | 14 | `fig14-AF11.png` | `kix.urqdbjwl4gr4` | `kix.lwwyw8p3jwki` | `AHj4eMQ2FhniMkHhtY1sO0GWfpysR-cmMpGdMFB9jUolAX7yHFSL61rtq5cAcooHJii8m-dMamTo6jmHhaXtEyLL49ZHf9cc6tPuiKCjCbzV4Qs` | `AHj4eMRm_vfaHKR68DbIfCybZ9rY8XJ6ySaeTDvHITnAg9PR9DsYmLSE6tksn42MvC2NegkSyjtU5ViQvMEXgC6hGfRkuq13cuw0CXFrH7Hb904` |
| 2026-10-20 20:47 | 15 | `fig15-bipartite.png` | `kix.ka5ve8wsytrr` | `kix.gm1b31jqj3gw` | `AHj4eMRm_vfaHKR68DbIfCybZ9rY8XJ6ySaeTDvHITnAg9PR9DsYmLSE6tksn42MvC2NegkSyjtU5ViQvMEXgC6hGfRkuq13cuw0CXFrH7Hb904` | `AHj4eMSLrMURsLSOY7QWdvsCF4YQSdA1vPEx2xh-nvW5O8lt7CusygdD4AW2i5p74YKhKR7YFS8jgTisYcgZq-tpzdYLucFdrfr77MnS9iDTKB8` |
| 2026-10-20 20:52 | 1 | `fig01-identification.png` | `kix.19dmvr8xfyzp` | `kix.ai87x7y840lt` | `AHj4eMR_5VfOE49ps4xugv3x_p0C-L-bGRJcPMCq7upsAR1n1UorOseKJltVuAwvCISng0KnM_9A3xr-f77pjNM4OOS8KWpRET0b1c5s9B0rW48` | `AHj4eMR_tkgS7WGJqK7dRS0FEe4qqQm4euIL9OKP-os97Vuc1kRrkZpG4szMXKtxjvW7qlO_BqnayCqmhEXv6OvRAi7FOUVhtiOeNuod5hL1Pjg` |

## Log de aplicação

| Data | Documento | Aplicados | Pulados | Revisão antes | Revisão depois |
|---|---|---|---|---|---|
| 2026-10-20 20:40 | `13O5Uco9-ItlpHioS_M_tsUr8UbqxppoQ2bx1fBmQ00g` | T06-A1, T06-A2, T06-A3, T06-A4, T06-A5, T06-A6 | — | `AHj4eMQ6hwCfdW467IC8tU6g9EKPfVtgfSlB0PPG9OhUu7f_hGbmETdoLLmHD-_oAKPCCuKV0ViGZHvd-qNrtnmNmFheewc02vA3ePYkz41PXKk` | `AHj4eMRI5cxVAtKSTVGeoe4P70A-8Xiun-_3hEALE0-S6jUX1M1AMKn_xE0StTN23daMRlow7yNkepjzTm0CUSMrje5a20yI29l1XN4KU5aRm3A` |
| 2026-10-20 20:43 | `13O5Uco9-ItlpHioS_M_tsUr8UbqxppoQ2bx1fBmQ00g` | T06-A7, T06-A8, T06-A9 | — | `AHj4eMRlKdkydwEXBkVgUEENoB7qlIsTK5PGueJIpu0hzWij9MJe4angEU1y3vBUG6RQN6ihAzaS-RGb9cGdinw0E9OMcZmfeXh3bA-vG3NbaVY` | `AHj4eMSyLVUfkgAlJZt3x33sJFBsH6wHEvFALgd3e_CVjTIr521boqUHR2YFypOUaHfvNfYX6nlACHF6rM6w97USjAgqOf3SmpwX-dDZWoSB6ag` |
| 2026-10-20 20:47 | `13O5Uco9-ItlpHioS_M_tsUr8UbqxppoQ2bx1fBmQ00g` | T06-A10, T06-A11, T06-A12, T06-A13, T06-A14, T06-A15 | — | `AHj4eMSLrMURsLSOY7QWdvsCF4YQSdA1vPEx2xh-nvW5O8lt7CusygdD4AW2i5p74YKhKR7YFS8jgTisYcgZq-tpzdYLucFdrfr77MnS9iDTKB8` | `AHj4eMS8ILBI0oEsoSwFiE8RDob67U0Wt-nh5x9J6lWicuwEA_7rqK6Nxu47_0S7r6y-1Ewh4CQFvIYudEPwhmR2YXcRKRdZYS96nPQunvjLln8` |
| 2026-10-20 20:52 | `13O5Uco9-ItlpHioS_M_tsUr8UbqxppoQ2bx1fBmQ00g` | T06-A16 | — | `AHj4eMR_tkgS7WGJqK7dRS0FEe4qqQm4euIL9OKP-os97Vuc1kRrkZpG4szMXKtxjvW7qlO_BqnayCqmhEXv6OvRAi7FOUVhtiOeNuod5hL1Pjg` | `AHj4eMQPcrYKfdaJlGHrT_CbLfPx1VtKhGghGcZnULqRFWn0lNA2nS408uB9GziL5dXfr9dCz9Y5pw8sag27-7nEUi_DokAoOMFBqmc67Hja_ds` |
