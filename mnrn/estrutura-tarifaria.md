# Estrutura Tarifária — Anexo 4 do Edital

**Resumo**: Detalhamento técnico da estrutura tarifária do Lote Nova Raposo conforme Anexo 4 do Edital de Concorrência Internacional nº 02/2024. Documento que confirma a instalação de **13 pórticos free flow bidirecionais** ao longo do sistema, define a tarifa quilométrica base de R$ 0,1477/km (março/2024) e estabelece fórmulas de cobrança, requalificação tarifária por etapa de obras, descontos e isenções.

**Fontes**: `raw/2024 09 NFMA D06b_LOTE 1 - Anexo 04 - Estrutura Tarifária.pdf`

**Última atualização**: 2026-05-14

---

## Os 13 pórticos do Sistema Automático Livre (free flow)

A confirmação técnica de que o sistema final terá **13 pórticos** bidirecionais — número maior do que os "5 pontos" da [[noticia-fato-mpsp|Notícia de Fato]], os "6 pórticos" da [[materia-estadao-2024|matéria do Estadão]] e os "seis pontos de pedágio" do [[abaixo-assinado|abaixo-assinado]] — está neste Anexo 4 (fonte: 2024 09 NFMA D06b).

| Código | Rodovia | km | Localização (lat/lng) |
|--------|---------|----|-----------------------|
| P01 | SP-270 | 11,81 | -23,5757432, -46,7191546 |
| P02 | SP-270 | 15,11 | -23,5860703, -46,7480622 |
| P03 | SP-270 | 19,76 | -23,5876541, -46,7914292 |
| P04 | SP-270 | 24,70 | -23,5921020, -46,8353318 |
| P05 | SP-270 | 29,00 | -23,5952178, -46,8729510 |
| P06 | SP-280 | 14,52 | -23,5230435, -46,7613117 |
| P07 | SP-280 | 20,545 | -23,5102610, -46,8152865 |
| P08 | SP-280 | 25,20 | -23,5046144, -46,8624619 |
| P09 | SP-280 | 29,18 | -23,5072716, -46,9012250 |
| P10 | SP-280 | 33,42 | -23,5189112, -46,9405861 |
| P11 | SP-029 | 34,60 | -23,5346393, -46,9386974 |
| P12 | SP-029 | 29,60 | -23,5722139, -46,9248290 |
| P13 | Trecho Cotia–Embu das Artes | 4,60 | -23,6309100, -46,9059746 |

Todos os pórticos são **bidirecionais** — cobram em ambos os sentidos.

### Pórticos podem ser reposicionados
- Em até 200 metros sem autorização da ARTESP
- Acima disso, com aprovação prévia do Poder Concedente

### Cobrança no eixo e marginais
Nos pórticos **P06, P07, P08, P09 e P10** (SP-280), a cobrança será realizada **tanto no eixo (vias expressas) quanto nas vias marginais**. Esse ponto é especialmente sensível ao Movimento porque desmente a tese governamental de que "as marginais não terão pedágio".

## Fase de transição (antes do Sistema Automático Livre)

Até a implantação dos 13 pórticos, operam **3 praças de pedágio existentes**:

| Praça | Rodovia | Cobrança | Sentido | km |
|-------|---------|----------|---------|-----|
| Osasco (P08 original) | SP-280 | Unidirecional | Oeste | 18,920 |
| Barueri (P08) | SP-280 | Unidirecional | Leste | 20,545 |
| Itapevi (P10) | SP-280 | Unidirecional | Oeste | 33,420 |

(fonte: 2024 09 NFMA D06b)

## Tarifa quilométrica base

- **R$ 0,1477/km** — bidirecional, pista simples, data-base março/2024
- **Reajuste anual pelo IPCA** (Fórmula 3)
- Cobrança AVI (Sistema de Cobrança Eletrônica): **desconto mínimo de 5%**
- Pagamento via Plataforma (sem AVI) no Sistema Automático Livre: **sem desconto**

## Requalificação Tarifária (incrementos por etapa de obras)

A concessionária **eleva a tarifa quilométrica** conforme conclui as obras:

| Tipo de obra concluída | Incremento na TQ |
|------------------------|------------------|
| Duplicação | **+40%** |
| Faixas adicionais em pista simples | +10% |
| Faixas adicionais em pista dupla | **+61%** |

Esses incrementos aplicam-se **trecho a trecho** após vistoria da ARTESP. Significa que ao longo da concessão a tarifa por km pode mais que duplicar em determinados trechos.

## Classificação de veículos e multiplicadores

| Cat. | Tipo | Eixos | Multiplicador |
|------|------|-------|---------------|
| 1 | Automóvel, caminhoneta, triciclo, furgão | 2 | **1** |
| 2 | Caminhão leve, microônibus, ônibus, caminhão trator, furgão | 2 | 2 |
| 3 | Caminhão trator, caminhão trator com semi reboque e ônibus | 3 | 3 |
| 4 | Caminhão com reboque, caminhão trator com semi reboque | 4 | 4 |
| 5 | Idem | 5 | 5 |
| 6 | Idem | 6 | 6 |
| 7 | Automóvel ou caminhonete com semi reboque | 3 | 1,5 |
| 8 | Automóvel ou caminhonete com reboque | 4 | 2 |
| 9 | Motocicleta, motoneta, bicicleta a motor | — | **0 (isento)** |
| — | Veículos oficiais SP, Forças Armadas, Polícia Militar | — | 0 |

Adicional: **2× tarifa por tonelada acima de 57 toneladas** de peso total (exceto "rodotrem"/"treminhão").

## Fórmulas de cálculo

### Tarifa Básica de Pedágio (Fórmula 1)
```
TBPt = (TQt × TCPs,t + 1,1×TQt × TCPsFA,t + 1,4×TQt × TCPd,t + 1,61×TQt × TCPdFA,t)
TPt = TBPt × Multiplicador
```
Onde TCP é o **Trecho de Cobertura de Pedágio**.

### Tarifa Devida (Fórmula 4) — vinculada à qualidade do serviço
```
TBDPt = (0,90 + 0,10 × IQD) × TBPt
TDPt = TBDPt × Multiplicador
```
Onde IQD é o **Índice de Qualidade e Desempenho** (de 0 a 1) — a tarifa devida representa **entre 90% e 100%** da tarifa cobrada conforme a qualidade do serviço.

## Trechos de Cobertura de Pedágio (TCP) após Sistema Automático Livre

| Pórtico | Rodovia | km início | km fim | Extensão |
|---------|---------|-----------|--------|----------|
| P01 | SP-270 | 10,940 | 14,050 | 3,11 |
| P02 | SP-270 | 14,050 | 17,650 | 3,60 |
| P03 | SP-270 | 17,650 | 21,830 | 4,18 |
| P04 | SP-270 | 21,830 | 27,590 | 5,76 |
| P05 | SP-270 | 27,590 | 34,065 | 6,475 |
| P06 | SP-280 | 13,290 | 16,140 | 2,85 |
| P07 | SP-280 | 16,140 | 20,990 | 4,85 |
| P08 | SP-280 | 20,990 | 26,660 | 5,665 |
| P09 | SP-280 | 26,660 | 32,250 | 5,59 |
| P10 | SP-280 | 32,250 | 54,140 | 21,89 |
| P11 | SP-029 | 32,580 | 38,600 | 6,023 |
| P12 | SP-029 | 38,600 | 43,700 | 5,10 |
| P13 | Cotia–Embu das Artes | 0 | 16,500 | 16,50 |
| **Total cobrado** | | | | **~91,5 km** |

## Desconto do Usuário Frequente (DUF)

Aplicável às Categorias 1, 7 e 8 **com AVI**:
- **11ª passagem do mês** no mesmo pórtico/praça/sentido: **10% de desconto**
- **21ª passagem do mês** no mesmo pórtico/praça/sentido: **20% de desconto**

Sem desconto para usuários do Sistema Automático Livre que pagam via plataforma sem AVI. A perda de receita pelo DUF é compensada pelo Poder Concedente (Compensação DUF — Apêndice D).

## Isenções

São isentos do pagamento:
- Veículos do Poder Concedente e ARTESP
- Comando de Policiamento Rodoviário da PM-SP
- Atendimento público de emergência (Bombeiros, ambulâncias)
- Forças militares em manobra
- Motocicletas, motonetas e bicicletas a motor
- Veículos oficiais dos Poderes Executivo, Legislativo, Judiciário, MP e Defensoria do Estado de SP (cadastrados no GCTI)

## Implicações para o Movimento

1. **A confirmação de 13 pórticos** (não 5 ou 6) torna explícito que o cordão de pedágios é mais denso do que se anunciou inicialmente — ver [[tarifas-pedagio]].
2. **Cobrança nas marginais** (P06–P10): contradiz a alegação de que apenas as vias expressas seriam pedagiadas (ver [[noticia-fato-mpsp|Notícia de Fato — vias marginais não pedagiadas]]).
3. **Requalificação tarifária de até +61%**: a tarifa de pedágio pode mais que duplicar em alguns trechos quando os investimentos forem concluídos.
4. **Categoria 1 com multiplicador 1**: o pedágio recai majoritariamente sobre **automóveis particulares de moradores** — exatamente o público que utiliza diariamente a Raposo Tavares como via urbana.
5. **DUF limitado a categorias 1, 7 e 8 com AVI**: usuários que não aderirem ao AVI ficam de fora dos descontos, criando barreira adicional aos mais pobres.

## Páginas relacionadas

- [[edital-lote-1]]
- [[tarifas-pedagio]]
- [[projeto-nova-raposo]]
- [[atores-institucionais]]
- [[noticia-fato-mpsp]]
- [[carta-aberta-bndes]]
- [[por-que-dizemos-nao]]
