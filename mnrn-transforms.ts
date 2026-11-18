import { QuartzTransformerPluginInstance } from "./quartz/plugins/types"

/**
 * Ajustes de renderização do site MNRN. Rodam só no build do Quartz;
 * os arquivos em mnrn/ não mudam (os agentes continuam usando os caminhos raw/).
 *
 * 1. Escapa o "$" de moedas (R$, US$). O plugin obsidian-flavored-markdown ativa
 *    sempre a sintaxe de matemática $...$, e dois "R$" na mesma linha viravam fórmula.
 * 2. Remove o prefixo da pasta local "raw/" (e subpastas, como "fila/") das
 *    referências a fontes, porque essa pasta não existe no site.
 *
 * Blocos de código cercados (``` ou ~~~, como os diagramas Mermaid) e o
 * frontmatter YAML ficam intactos.
 */

const FENCE = /^\s{0,3}(`{3,}|~{3,})/
const INLINE_CODE = /(`[^`]*`)/
const CURRENCY_DOLLAR = /(?<=[A-Z])\$/g
const RAW_PREFIX = /(^|[\s(`"'[])raw\/(?:[^/\s`]+\/)*/g

function escapeCurrency(line: string): string {
  return line
    .split(INLINE_CODE)
    .map((part, i) => (i % 2 === 1 ? part : part.replace(CURRENCY_DOLLAR, () => "\\$")))
    .join("")
}

export function transformMnrnSource(src: string): string {
  const lines = src.split("\n")
  let start = 0
  if (lines[0]?.trim() === "---") {
    const end = lines.findIndex((line, idx) => idx > 0 && line.trim() === "---")
    if (end > 0) start = end + 1
  }

  let fence: string | null = null
  for (let i = start; i < lines.length; i++) {
    const match = lines[i].match(FENCE)
    if (fence) {
      if (match && match[1][0] === fence[0] && match[1].length >= fence.length) fence = null
      continue
    }
    if (match) {
      fence = match[1]
      continue
    }
    lines[i] = escapeCurrency(lines[i]).replace(RAW_PREFIX, "$1")
  }
  return lines.join("\n")
}

export const MnrnSiteTransforms: QuartzTransformerPluginInstance = {
  name: "MnrnSiteTransforms",
  textTransform: (_ctx, src) => transformMnrnSource(src),
}
