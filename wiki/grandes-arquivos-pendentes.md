# Arquivos Pendentes de Processamento

**Resumo**: Lista de arquivos da pasta `raw/` que não puderam ser processados nesta sessão de ingestão devido a limites de memória/contexto disponíveis. Estes arquivos devem ser ingeridos em sessões futuras, idealmente um por vez para permitir análise detalhada.

**Última atualização**: 2026-05-14

---

## Critério de pendência

Foram registrados como pendentes arquivos que:
- Excedem capacidade de processamento integral em uma sessão (> ~10 MB de conteúdo PDF rico)
- Têm muitas páginas com conteúdo técnico denso
- Não foram lidos por restrição de contexto disponível ao final da sessão

## Lista de arquivos pendentes

### Documentos jurídicos (pasta `raw/fila/`)

#### 1. ACP Nova Raposo (Ação Civil Pública)
- **Arquivo**: `raw/fila/1500561-14.2025.8.26.0053 ACP Nova Raposo.pdf`
- **Tamanho**: ~127 MB (arquivo extremamente grande)
- **Tipo**: Ação Civil Pública relativa ao Projeto Nova Raposo, autos 1500561-14.2025.8.26.0053 da 8ª Vara da Fazenda Pública (53 = código TJSP da Fazenda)
- **Prioridade**: **ALTA** — documento jurídico central
- **Estratégia sugerida**: processar em partes (capa, pedidos, fundamentação, anexos), sessões separadas

#### 2. Cautelar Antecedente Nova Raposo — ✅ PROCESSADO em 2026-05-14
- **Arquivo**: `raw/2024 11 CAUTELAR ANTECEDENTE - NOVA RAPOSO.pdf` (caminho real: `raw/` raiz, não `raw/fila/`)
- **Tamanho**: ~1,6 MB / 52 páginas
- **Tipo**: Ação Cautelar Antecedente da Bancada Feminista do PSOL — ajuizada 27/11/2024
- **Página wiki**: [[cautelar-antecedente-2024]]

#### 3. Processo 1120375-77.2025.8.26.0053
- **Arquivo**: `raw/fila/1120375-77.2025.8.26.0053.pdf`
- **Tamanho**: ~2 MB
- **Tipo**: Processo judicial relativo ao Projeto, autos 1120375-77.2025.8.26.0053
- **Prioridade**: **ALTA**

#### 4. Parecer CAEX MPSP
- **Arquivo**: `raw/fila/2025 09 Parecer CAEX Nova Raposo IC 048200005712024 MP PJMAC ate 250925-718-786_ParecerCAEX.pdf`
- **Tamanho**: ~13,7 MB
- **Tipo**: Parecer do Centro de Apoio à Execução (CAEX) do MPSP no Inquérito Civil IC 0482.0000571/2024
- **Data**: setembro/2025 (até 25/09/2025)
- **Prioridade**: **ALTA** — documento técnico-jurídico oficial do MPSP
- **Estratégia sugerida**: processar em sessão dedicada com leitura por trechos (`pages: 1-30`, `pages: 31-60`...)

#### 5. Lei 14.133/2021 (Nova Lei de Licitações) — Reader View
- **Arquivo**: `raw/fila/L14133 __ Reader View.pdf`
- **Tamanho**: ~1,8 MB
- **Tipo**: Reader view da Lei Federal 14.133/2021 (Nova Lei de Licitações), aplicada à concessão
- **Prioridade**: MÉDIA — texto legal já disponível em planalto.gov.br

### Apresentações do Seminário de Mobilidade (abril/2025)

Apenas 1 das 5 apresentações foi processada (Nestor — Linha 22-Marrom). As demais permanecem pendentes:

#### 6. Apresentação Elio — Pedágio e Controle de Demanda
- **Arquivo**: `raw/fila/2025-04 - Apresentação Seminário Mobilidade - Elio Pedágio Controle Demanda.pdf`
- **Tamanho**: ~2,5 MB
- **Prioridade**: ALTA (tema central do Projeto)

#### 7. Apresentação Felipe — Clima, Mobilidade e Cidades
- **Arquivo**: `raw/fila/2025-04 - Apresentação Seminário Mobilidade - Felipe Clima Mobilidade Cidades.pdf`
- **Tamanho**: ~3,7 MB
- **Prioridade**: ALTA

#### 8. Apresentação Horácio — Análise e Reflexões da Proposta Nova Raposo
- **Arquivo**: `raw/fila/2025-04 - Apresentação Seminário Mobilidade - Horácio Analise e Refelxões Proposta Nova Raposo.pdf`
- **Tamanho**: ~1,3 MB
- **Prioridade**: **MUITO ALTA** — análise dirigida especificamente ao Projeto

#### 9. Apresentação Marta — Estudo de Caso Barcelona
- **Arquivo**: `raw/fila/2025-04 - Apresentação Seminário Mobilidade - Marta Estudo de Caso Barcelona.pdf`
- **Tamanho**: ~21 MB (apresentação grande com muitas imagens)
- **Prioridade**: MÉDIA (referencial internacional)

### Apresentação do Seminário ALESP — Sustentabilidade Ameaçada

#### 10. Seminário ALESP — Sustentabilidade Ameaçada na Zona Oeste de SP/RMSP
- **Arquivo**: `raw/fila/SEminário ALESP - Sustentabilidade Ameaçada na Zona Oeste de São Paulo-RMSP - Rev.pdf`
- **Tamanho**: ~2,3 MB
- **Tipo**: Apresentação do 1º Seminário Técnico do Movimento (eixo Meio Ambiente)
- **Cobertura em vídeo**: youtube.com/live/EeH-wpZA7ZE
- **Prioridade**: ALTA

## Status do processamento desta sessão (2026-05-14)

### Pasta `raw/` (raiz) — TODOS PROCESSADOS

| Arquivo | Status | Página(s) wiki |
|---------|--------|----------------|
| D00 Notícia de Fato | ✅ | [[noticia-fato-mpsp]] |
| D01 Matéria Estadão | ✅ | [[materia-estadao-2024]] |
| D02 Lista organizações + Nota Repúdio | ✅ | [[nota-repudio]], [[organizacoes-integrantes]] |
| D03 Abaixo-assinado Change.org | ✅ | [[abaixo-assinado]] |
| D04 Ofício Secretaria Parcerias | ✅ | [[oficio-secretaria-parcerias]] |
| D05 Ofício ARTESP + Resposta | ✅ | [[oficio-artesp]] |
| D06a Edital LOTE 1 | ✅ | [[edital-lote-1]] |
| D06b Estrutura Tarifária | ✅ | [[estrutura-tarifaria]] |
| D07 Relatório Preliminar Impactos | ✅ | [[relatorio-preliminar-impactos-ambientais]] |
| D08 Parques Adjacentes | ✅ | [[parques-adjacentes]] |
| D09 Texto Base Conferência das Cidades | ✅ | [[texto-base-conferencia-cidades]] |

### Pasta `raw/fila/` — 3 de 13 processados

| Arquivo | Status |
|---------|--------|
| 1031_artigo (Tecnologia Metroferroviária) | ✅ [[artigo-projeto-populacao]] |
| 2025-04 Seminário Mobilidade - Nestor (Linha 22) | ✅ [[seminario-mobilidade]] |
| AUDIENCIA ALESP 25NOV | ✅ [[audiencia-alesp-novembro-2024]] |
| 1120375-77.2025.8.26.0053 | ⏸ Pendente (ver lista acima) |
| ACP Nova Raposo (1500561-14) | ⏸ Pendente — **arquivo de 127 MB** |
| Cautelar Antecedente (2024 11) | ✅ [[cautelar-antecedente-2024]] (estava em `raw/`, não em `raw/fila/`) |
| Parecer CAEX (2025 09) | ⏸ Pendente — **arquivo grande, 13,7 MB** |
| Seminário Mobilidade - Elio | ⏸ Pendente |
| Seminário Mobilidade - Felipe | ⏸ Pendente |
| Seminário Mobilidade - Horácio | ⏸ Pendente |
| Seminário Mobilidade - Marta Barcelona | ⏸ Pendente — **arquivo grande, 21 MB** |
| L14133 Reader View | ⏸ Pendente |
| Seminário ALESP Sustentabilidade | ⏸ Pendente |

## Recomendação para próxima sessão de ingestão

**Ordem sugerida** (do mais prioritário ao menos prioritário):

1. **Cautelar Antecedente Nova Raposo (nov/2024)** — pequeno, ação judicial precoce
2. **Parecer CAEX MPSP (set/2025)** — em sessão dedicada, leitura por páginas
3. **Processos 1120375-77 e ACP 1500561-14** — em sessões separadas
4. **Apresentação Horácio (Seminário Mobilidade)** — análise direta do Projeto
5. **Apresentação Elio (Pedágio)** — tema central
6. **Apresentação Felipe (Clima)**
7. **Apresentação Marta (Barcelona)** — em sessão dedicada por ser grande
8. **Seminário ALESP Sustentabilidade**
9. **L14133 (Lei das Licitações) — Reader View** — pode ser dispensável

## Páginas relacionadas

- [[index]]
- [[log]]
- [[noticia-fato-mpsp]]
- [[seminario-mobilidade]]
