# mnrn-wiki

Wiki de conhecimento do **Movimento Nova Raposo, NÃO!** — movimento de resistência à concessão da Rodovia Raposo Tavares (SP-270 + SP-280 + SP-029).

Base de conhecimento em Markdown no padrão *LLM Wiki* (páginas curtas interligadas por `[[wikilinks]]`), publicada com [Quartz v4](https://quartz.jzhao.xyz/) a partir da pasta `wiki/`.

## Estrutura

- `wiki/` — páginas do wiki (conteúdo publicado).
- `raw/` — fontes primárias (PDFs). **Não publicadas**: ficam fora do repositório e são disponibilizadas via pasta pública do Google Drive.
- `scripts/` — ferramentas de ingestão/análise (Python, gerenciado com `uv`).
- `AGENTS.md` — guia para agentes de IA.
- `contexto_mnrn_wiki.md` — manual operacional do wiki (regras, fluxo de ingestão, formatos).

## Pré-requisitos

- Node.js 22+ (testado com v24) — para o Quartz.
- `uv` — opcional, apenas para os scripts em `scripts/`.

## Visualizando o wiki localmente (Quartz v5)

O Quartz v5 já está integrado neste repositório (código em `quartz/`, config em `quartz.config.yaml`). O conteúdo é a pasta `wiki/` (a flag `-d wiki` aponta o Quartz para ela).

```
npm install                      # primeira vez (ou npm ci)
npx quartz build -d wiki --serve # preview local
```

Abra http://localhost:8080.

Para gerar só o site estático (sem servidor): `npx quartz build -d wiki` (saída em `public/`).

O `baseUrl` já está configurado como `yvyra.github.io/mnrn-wiki` em `quartz.config.yaml`.

## Toolchain Python (ingestão)

O ambiente Python é gerenciado com `uv` (CPython 3.14.7):

```
uv sync
uv run python scripts/ingest_pdf.py raw/<arquivo>.pdf --max-pages 3
```

O ingestor extrai o texto do PDF em Markdown (com detecção de páginas digitalizadas e OCR opcional). Veja `AGENTS.md` e `contexto_mnrn_wiki.md` para o fluxo completo.

## Publicação (GitHub Pages)

- Repositório: `Yvyra/mnrn-wiki`.
- Deploy via GitHub Actions na branch `gh-pages`, com `baseUrl` = `/mnrn-wiki/`.
- URL: https://yvyra.github.io/mnrn-wiki/

## Privacidade

- `raw/`, `wiki/log.md` e `wiki/grandes-arquivos-pendentes.md` são mantidos fora do repositório (ver `.gitignore`).
