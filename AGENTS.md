# AGENTS.md — mnrn-wiki

Knowledge wiki about the **Movimento Nova Raposo, NÃO! (MNRN)**, a social movement opposing the 30-year private concession of Rodovia Raposo Tavares (SP-270 + SP-280 + SP-029) in São Paulo. Follows the Andrej Karpathy "LLM Wiki" pattern: short interlinked pages connected by `[[wikilinks]]`, built from primary sources in `raw/`.

This is primarily a **documentation repository**: `raw/` + `wiki/` are Markdown/PDF content written in Brazilian Portuguese (pt-BR). A small `uv`-managed Python environment exists for ingestion/analysis scripts (to live in `scripts/`). There is no git history yet.

`contexto_mnrn_wiki.md` is the operational playbook of this project — read it before doing any ingestion work. This file distills it; on conflict, `contexto_mnrn_wiki.md` wins.

## Repository Structure

```
raw/              Immutable primary sources (PDFs, press clippings). Never modified.
  descartes/      Quarantine for unreadable files
wiki/             Markdown pages maintained by the AI agent
  index.md        Master index: ingested sources + page directory
  log.md          Append-only operations log (one entry per ingestion session)
  linha-tempo.md  Chronology of events
  noticias-relacionadas.md  Press coverage registry
contexto_mnrn_wiki.md   Operational playbook (rules, flow, formats)
mapa_mental_mnrn.md     Mermaid mindmaps of the "auction postponement" analysis
pyproject.toml          uv manifest (Python deps); .python-version pins CPython 3.14.7
.gitignore              ignores .venv/, secrets, caches
.codewhale/             Agent tool state — ignore, never edit
```

Planned (not yet created) subdirectories per the playbook: `wiki/legislacao/` (analyses of laws), `wiki/projetos/` (bill analyses), `wiki/assets/grafos/` (interactive HTML graphs).

## Core Rules (non-negotiable)

- Never modify anything in `raw/`. If a file is unreadable, move it to `raw/descartes/`.
- Page filenames: lowercase, hyphen-separated (`impactos-ambientais.md`).
- Write wiki content in clear, direct pt-BR unless told otherwise.
- When you cannot categorize something, ask the user.
- The wiki has three analytical axes (Eixos): (1) Meio Ambiente, (2) Habitação e Urbanismo, (3) Patrimônio Público/Interesses Difusos. A source touching multiple axes gets one page per axis, cross-linked. Analysis should use Legística and Avaliação de Impacto Legislativo (AIL) ex-ante/ex-post methods.

## Ingestion Workflow

Triggered when the user adds a file to `raw/` or provides a URL of an official legislative portal. Steps, in order:

1. Read the whole source (OCR if it is a scanned PDF).
2. Map citations to other norms; follow each citation to reasonable depth (avoid infinite loops).
3. Track the validity of each cited norm on official portals: Prefeitura de SP (https://legislacao.prefeitura.sp.gov.br/), ALESP (https://www.al.sp.gov.br/norma/pesquisa), Planalto (https://legislacao.presidencia.gov.br/). Adapt portals for other jurisdictions.
4. Create the summary page. Current law → `wiki/legislacao/`; bill → `wiki/projetos/`.
5. Apply AIL and axis bifurcation.
6. Create or update one concept page per important entity.
7. Generate a Mermaid diagram at the end of the analysis. For dense normative webs, also generate an interactive d3blocks graph — save as `wiki/assets/grafos/<page-name>.htm` (extension `.htm`, NOT `.html` — Quartz strips `.html` from files under `content/`, breaking the embed) and embed via `<iframe src="assets/grafos/<page-name>.htm" width="100%" height="600px" frameborder="0">` (adjust `../` for page depth). Do not use other-language code blocks (e.g. Cypher) as visualization.
8. Update the four registry files: `wiki/index.md`, `wiki/log.md`, `wiki/linha-tempo.md`, `wiki/noticias-relacionadas.md`.

## Page Format

Every page follows this template:

```markdown
# Título da Página

**Resumo**: One or two sentences describing this page.

**Fontes**: raw/ files this page draws from.

**Última atualização**: Date.

---

Content. Clear headings, short paragraphs. Link concepts with [[wikilinks]].

## Páginas relacionadas

- [[related-concept-1]]
```

For legislative analyses (laws and bills), add these sections:

```markdown
## Identificação          (Número, Autoria, Status, Instância)
## O que propõe           (accessible synthesis of the normative text)
## Pontos de atenção ou lacunas  (provisions that weaken the study's goal, loopholes)
## Atores envolvidos      (authors, rapporteurs, supporting/opposing entities)
```

## Citation Rules

- Every factual claim cites its source inline: `(fonte: nome-do-arquivo.pdf)`.
- For legislative portals, link directly to the Article/Paragraph/Inciso in the consulted HTML.
- If two sources disagree, record the contradiction explicitly on the page.
- Claims without documentary support in `raw/` get marked `[verificar]`.

## Answering Questions

1. Read `wiki/index.md` to find relevant pages.
2. Read those pages and synthesize the answer.
3. Cite the specific wiki pages used.
4. If the answer is not in the wiki, say so clearly.
5. If the answer is valuable, offer to save it as a new page.

## Wiki Audit (the project's "lint")

When the user asks for a wiki audit, report a numbered list with a suggested fix for each finding:

- Contradictions between pages
- Orphan pages (no inbound links)
- Concepts referenced but lacking their own page
- Claims possibly outdated by a newer source
- Pages that deviate from the standard format

## Python Environment & Tooling

Wiki content has no build/test/lint. An isolated `uv` environment is provided for data/document scripts, pinned to CPython 3.14.7 via `.python-version`.

- Sync/install: `uv sync`
- Run a script: `uv run python scripts/<name>.py`
- Add a dependency: `uv add <package>` (commit `pyproject.toml` + `uv.lock`)
- Installed (2026-09-11): `pymupdf`, `pdfplumber`, `pandas`, `openpyxl`

Verification for this repo means: format-check edited pages against the templates above, confirm the four registry files were updated, and check that every `[[wikilink]]` target resolves to an existing `wiki/*.md` filename.

## Tips for AI Agents

- **Path drift**: `wiki/log.md` and `wiki/grandes-arquivos-pendentes.md` reference `raw/fila/`, which no longer exists — all files now sit at the `raw/` root. Trust `Get-ChildItem raw` over historical log entries.
- **Filenames in `raw/` contain spaces and accented characters** (e.g. `2024 09 NFMA D06b_LOTE 1 - Anexo 04 - Estrutura Tarif†ria.pdf`). Always quote paths in shell commands.
- **Huge PDFs**: the ACP is ~127 MB; the Parecer CAEX ~13.7 MB. Process large documents one per session, reading by page ranges. `wiki/grandes-arquivos-pendentes.md` tracks what remains unprocessed, with priority order and per-file strategies — consult it before starting a new ingestion.
- **Wikilink targets are kebab-case filenames** (`[[impactos-ambientais]]` → `wiki/impactos-ambientais.md`). A link whose target has no matching file is an audit finding.
- **Wikilink with alias syntax** is used: `[[movimento-de-resistencia|MNRN]]`.
- **Update registries together**: a new page is not "done" until `index.md`, `log.md`, and (when applicable) `linha-tempo.md` / `noticias-relacionadas.md` are updated.
- **`wiki/log.md` is append-only**: add a new dated entry at the top; never rewrite history.
- **Planned skills** (`ingestao-wiki-legislativo`, `pesquisa-legislacao`, `gerador-diagrama-drawio`, `gerador-mapa-interativo-d3blocks`) are described in `contexto_mnrn_wiki.md` but not yet present as `.claude/skills/*/SKILL.md` files. Follow the playbook's prose flow directly until they exist.
- **Dates** in pages use `YYYY-MM-DD`; registry tables use `YYYY-MM-DD` for ingestion dates.
- **Shell**: this machine runs PowerShell — use PowerShell syntax, not bash.
- **PyMuPDF**: use `import pymupdf`, not `import fitz` — the `fitz` alias is deprecated and warns on 1.28+.
- **Keep scripts out of `raw/` and `wiki/`**: automation lives in `scripts/` (created as needed); `raw/` stays source-only and `wiki/` stays content-only.
