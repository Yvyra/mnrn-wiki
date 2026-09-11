# contexto_mnrn_wiki.md — Wiki do Movimento Nova Raposo, NÃO!

Base de conhecimento coletivo mantida pelo Claude Code.
Baseado no padrão LLM Wiki de Andrej Karpathy.


# Wiki do "Movimento Nova Raposo, Não"

Wiki do "Movimento Nova Raposo, Não" Base de conhecimento coletivo sobre movimento social contra a concessão da Rodovia Raposo Tavares, publicada em formato wiki. Segue o padrão *LLM Wiki* de Andrej Karpathy: páginas curtas interligadas por `[[wiki-links]]`, construídas a partir de fontes primárias em `raw/` e links via web scrapping.

## Propósito

Este wiki é uma base de conhecimento estruturada e interligada sobre o **Movimento Nova Raposo, NÃO!** — movimento de resistência contra o projeto de concessão da Rodovia Raposo Tavares (SP-270).
O Claude mantém o wiki. O humano cuida das fontes, faz perguntas e orienta a análise.

## Eixos

**Eixo 1**: Meio Ambiente (MP Meio Ambiente)
O Eixo Ambiental questiona a validade e a qualidade dos estudos do Anteprojeto por descumprir as exigências legais do Art. 6º, inciso XXIV da Lei de Licitações quanto à viabilidade socioeconômica, interesse público e detalhamento construtivo. Além disso, o Estudo Ambiental preliminar (Relatório IFC) apresenta graves omissões ao ignorar os impactos sobre áreas verdes, parques, microclima urbano e recursos hídricos, adotando premissas metodológicas da IFC inadequadas para a realidade de perímetros estritamente urbanos.

**Eixo 2**: Habitação e Urbanismo (MP Habitação e Urbanístico)
O Eixo de Habitação e Urbanismo aponta a incompatibilidade do projeto com o planejamento local, colidindo com as diretrizes do Estatuto da Cidade, da Lei de Zoneamento e do Plano Diretor Estratégico, além de carecer de convênios municipais integrados e de estudos para rotas alternativas e segurança viária. Soma-se a isso a ilegalidade da cobrança de pedágio em perímetro urbano, medida que restringe indevidamente a circulação interna local e viola a Política Nacional de Mobilidade Urbana ao sobrecarregar bairros residenciais e desestimular o transporte coletivo.

**Eixo 3**: O Eixo do Patrimônio Público e Interesses Difusos/Coletivos ataca os vícios de legalidade, governança e transparência do projeto, destacando a violação ao Art. 45 da Lei 14.133/2021 pela ausência de comprovação de ganho social e de um Programa de Necessidades claro. Essa fragilidade estende-se à insegurança jurídica nos processos de desapropriação — marcados pela falta de critérios temporais para ressarcimento e desamparo a ocupações irregulares — e a um grave déficit democrático, evidenciado pela realização de apenas duas audiências públicas, omissão nos relatórios de contribuições, falta de comunicação com a comunidade afetada e necessidade de judicialização para garantir o acesso a informações fundamentais.

Se a fonte tocar mais de um eixo, crie páginas em cada um e conecte-as por `[[wiki-links]]`.

Use a Legística (ciência da qualidade e da elaboração das leis) e a Avaliação de Impacto Legislativo (AIL) ex-ante e ex-post como método de análise — isso vale para qualquer eixo escolhido.

# Estrutura de pastas

```
raw/          fontes primárias imutáveis (PDFs, recortes de Diário Oficial, dados abertos)
wiki/         páginas markdown mantidas pelo Claude
  index.md                  índice geral
  log.md                    registro append-only de operações
  linha-tempo.md            cronologia de eventos
  noticias-relacionadas.md  registro de notícias de imprensa
  legislacao/               análises de normas vigentes e projetos de lei
  projetos/                 propostas de aperfeiçoamento (se houver eixo propositivo)
  assets/grafos/            grafos interativos (HTML) embutidos nas páginas via iframe
```

Regras fixas:

- Nunca modifique nada em `raw/`.
- Nomeie páginas em minúsculas com hífens: `impactos-ambientais.md`.
- Escreva em português claro e direto (pt-BR), salvo instrução em contrário.
- Se não conseguir ler um arquivo de `raw/`, mova-o para `raw/descarte/`.
- Quando não souber categorizar algo, pergunte ao usuário.

# Fluxo da wiki

Dispare o fluxo quando o usuário adicionar um arquivo em `raw/` ou fornecer uma URL de portal legislativo oficial.

Para executar a ingestão, use a skill `ingestao-wiki-legislativo`.

Passos, em ordem:

1. Leia a fonte inteira (o arquivo original, ou o texto extraído se houver alguma ferramenta de extração no projeto). Aplique OCR se for PDF digitalizado.
2. Mapeie as citações a outras normas. Siga cada citação até uma profundidade razoável (evite laço infinito).
3. Rastreie a vigência de cada norma citada nos portais oficiais — use a skill `pesquisa-legislacao` (cobre Prefeitura de SP, ALESP e Planalto; adapte ou substitua se o projeto tratar de outra esfera).
4. Crie a página de resumo. Norma vigente vai em `wiki/legislacao/`. Projeto de lei vai em `wiki/projetos/`.
5. Aplique a AIL e a bifurcação de eixos, se o projeto tiver eixos definidos.
6. Crie ou atualize uma página de conceito para cada entidade importante.
7. Gere o diagrama Mermaid ao final da análise (skill `gerador-diagrama-drawio`). Se a malha for densa, gere também o grafo interativo (skill `gerador-mapa-interativo-d3blocks`) — é ele que fica navegável na página publicada. Não gere bloco de código de outra linguagem (ex.: Cypher) como visualização: texto de código não renderiza nada ao ser lido, só o grafo interativo ou o diagrama Mermaid o fazem.
8. Atualize `wiki/index.md`, `wiki/log.md`, `wiki/linha-tempo.md` e `wiki/noticias-relacionadas.md`.

## Formato de página (padrão)

```markdown
# Título da Página

**Resumo**: Uma ou duas frases descrevendo esta página.

**Fontes**: Arquivos de raw/ dos quais esta página extrai informação.

**Última atualização**: Data.

---

Conteúdo. Títulos claros, parágrafos curtos. Vincule conceitos com [[wiki-links]].

## Páginas relacionadas

- [[conceito-relacionado-1]]
```

## Formato de análise legislativa

Para projetos de lei e normas, acrescente à página:

```markdown
## Identificação

- **Número**: XXX/AAAA
- **Autoria**: Nome do autor
- **Status**: em tramitação / aprovado / arquivado
- **Instância**: [câmara/assembleia/congresso — preencher conforme a esfera]

## O que propõe

Síntese objetiva do texto normativo em linguagem acessível.
Dispositivos ou princípios relevantes para o objetivo do estudo.

## Pontos de atenção ou lacunas

Disposições que enfraquecem o objetivo do estudo, brechas ou contradições internas.

## Atores envolvidos

Autores, relatores, entidades que apoiam ou se opõem à norma ou ao PL.
```

## Regras de citação

- Toda afirmação factual referencia sua fonte: `(fonte: nome-do-arquivo.pdf)`.
- Fonte de site legislativo: aponte o link direto para o Artigo, Parágrafo ou Inciso no HTML consultado.
- Se duas fontes divergirem, registre a contradição explicitamente na página.
- Afirmação sem amparo documental em `raw/`: marque `[verificar]`.

# Resposta a perguntas

1. Leia `wiki/index.md` para achar as páginas relevantes.
2. Leia essas páginas e sintetize a resposta.
3. Cite as páginas específicas do wiki que você usou.
4. Se a resposta não estiver no wiki, diga isso com clareza.
5. Se a resposta for valiosa, ofereça salvá-la como página nova.

# Auditoria (lint)

Quando o usuário pedir auditoria do wiki, reporte uma lista numerada com a correção sugerida para cada achado:

- Contradições entre páginas.
- Páginas órfãs (sem links de entrada de outras páginas).
- Conceitos citados em páginas que não têm página própria.
- Afirmações possivelmente desatualizadas por uma fonte mais recente.
- Páginas fora do formato padrão.

# Princípios de engenharia

## 1. Pense antes de codificar

Não presuma. Não esconda confusão. Explicite os tradeoffs. Declare suas premissas. Se houver múltiplas interpretações, apresente-as. Se houver uma abordagem mais simples, diga. Se algo não estiver claro, pare e pergunte.

## 2. Simplicidade em primeiro lugar

O mínimo de código que resolve o problema. Nada especulativo. Sem funcionalidades além do pedido, sem abstrações de uso único, sem "flexibilidade" não solicitada, sem tratamento de erro para cenários impossíveis. Se 200 linhas poderiam ser 50, reescreva.

## 3. Mudanças cirúrgicas

Mexa apenas no necessário. Não "melhore" código adjacente. Não refatore o que não está quebrado. Imite o estilo existente. Se notar código morto não relacionado, mencione — não delete. Remova imports e funções que as suas mudanças tornaram inúteis.

## 4. Execução orientada a objetivos

Transforme a tarefa em meta verificável. "Adicionar validação" vira "escreva testes para entradas inválidas, depois faça-os passar". "Corrigir o bug" vira "escreva um teste que o reproduz, depois faça-o passar". Para tarefas multi-etapa, declare um plano curto com a checagem de cada passo.


### Fontes regulatórias de partida

```
- **[Tipo] [Número]/[Ano]** — [ementa em uma linha].
- Histórico (revogados, rastrear só como elos de evolução temporal): [se houver].
```

Se o estudo for sobre legislação paulistana ou paulista, estes são os três portais de busca oficiais (municipal, estadual e federal) para localizar as normas-semente antes de preencher a lista acima:

- **Prefeitura de São Paulo (municipal)**: https://legislacao.prefeitura.sp.gov.br/
- **ALESP — Assembleia Legislativa de SP (estadual)**: https://www.al.sp.gov.br/norma/pesquisa
- **Presidência da República (federal)**: https://legislacao.presidencia.gov.br/

Adapte a lista de portais se o estudo tratar de outro município, estado, ou só da esfera federal.

# Skills do projeto

- **`ingestao-wiki-legislativo`** — executa o fluxo de ingestão de uma nova fonte de ponta a ponta: leitura, mapeamento de citações, AIL, páginas de resumo e de conceito, diagrama, índices.
- **`pesquisa-legislacao`** — pesquisa e rastreia normas nos portais oficiais (Prefeitura de SP, ALESP, Planalto — adaptar os portais se o estudo for de outro município/estado, ou federal apenas).
- **`gerador-diagrama-drawio`** — gera o diagrama Mermaid da análise, com código de cores (norma vigente, proposta de aperfeiçoamento, lacuna/alerta), pronto para o Draw.io.
- **`gerador-mapa-interativo-d3blocks`** — gera o grafo relacional interativo (HTML) da malha de normas, embutido na página via iframe, para quando a malha for densa demais para o diagrama estático.

## Como criar essas skills num novo projeto

Skills do Claude Code são locais a cada repositório: crie um arquivo `.claude/skills/<nome-da-skill>/SKILL.md` para cada uma, com frontmatter `name` e `description` (a description é o que o Claude usa para decidir quando invocar a skill sozinho) e instruções de execução no corpo. Para cada uma das quatro skills acima, o `SKILL.md` precisa cobrir:

1. **`ingestao-wiki-legislativo`** — o passo a passo da seção "Fluxo da wiki" deste arquivo (leitura, mapeamento de citações, AIL, criação de página, diagrama/grafo, atualização de índices), mais o "Formato de página" e as "Regras de citação".
2. **`pesquisa-legislacao`** — para cada portal oficial do estudo (adapte os 3 de São Paulo listados em "Fontes regulatórias de partida", ou troque pelos do município/estado/país do estudo): como a URL de cada norma é construída ou buscada, onde fica o texto consolidado/vigente, e como rastrear revogações e regulamentações a partir da página da norma.
3. **`gerador-diagrama-drawio`** — o código de cores por tipo de nó (ex.: norma vigente, proposta, lacuna) e a convenção de rótulo de aresta (ex.: `-->|revoga|`, `-->|regulamenta|`), para que todo diagrama Mermaid do projeto siga o mesmo padrão visual.
4. **`gerador-mapa-interativo-d3blocks`** — o formato de dados de entrada (um `DataFrame` com `source`, `target`, `weight`), a mesma paleta de cores da skill de diagrama, e a convenção de saída: salvar em `wiki/assets/grafos/<nome-da-página>.htm` e embutir na página com `<iframe src="assets/grafos/<nome-da-página>.htm" width="100%" height="600px" frameborder="0"></iframe>` (ajuste o `../` no `src` conforme a profundidade da página que embute o grafo). Use a extensão `.htm`, não `.html`: se o site for publicado com Quartz, ele remove a extensão `.html` de qualquer arquivo dentro de `content/` (trata como se fosse mais uma página), o que quebra o embed — `.htm` não sofre essa transformação.


# futuras implementações

- **`Varredura do gdrive do movimento`** - Para coleta de noticias, estudos, eventos e fotos
- **`Leitura do Contrato de Concessão`** - Fiscalização e ilegalidades que possam ser questionado
- **`Vistas de processos MP`** - Documentos grandes e complexos, com compressão de dados e dificil leitura. Verificar estratégias de ingestão.

