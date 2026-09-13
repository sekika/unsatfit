import { existsSync, mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { mkdir, readdir, readFile, stat, writeFile } from "node:fs/promises";
import { createHash } from "node:crypto";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { PDFArray, PDFDict, PDFDocument, PDFName } from "pdf-lib";
import { Resvg } from "@resvg/resvg-js";
import { H, Q, b, box, color, fontSize, h1, image, inlineMath, math, mdFile, minitype, p, page, physical, ratio, rgb, sub, sup, url } from "@minitype/minitype";

const here = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(here, "../..");
const docsDirectory = path.join(root, "docs");
const fontDir = path.join(here, "node_modules/@minitype/minitype/fonts");
const siteUrl = "https://sekika.github.io/unsatfit";
const serifFont = { default: { font: "SourceHanSerifJP-Regular" }, latin: { font: "NOTONOTO35HS-Regular" } };
const sansFont = { default: { font: "SourceHanSansJP-Regular" }, latin: { font: "NOTONOTO35HS-Regular" } };
const style = {
  size: "A4", writingMode: "horizontal", padding: physical(20, 18, 24, 18),
  block: {
    paragraph: { font: serifFont, size: Q(10), lineHeight: H(18), firstIndent: Q(10) },
    h1: { font: "SourceHanSerifJP-Bold", size: Q(20), lineHeight: H(28) },
    h2: { font: "SourceHanSerifJP-Bold", size: Q(15), lineHeight: H(22) },
    code: { font: sansFont, size: Q(8), lineHeight: H(12), highlight: "atom-one-light" },
    li1: { indent: Q(15), firstIndent: Q(-12) }, li2: { indent: Q(15), firstIndent: Q(-12) }, li3: { indent: Q(15), firstIndent: Q(-12) },
    image: { align: "center", width: ratio(0.78) }, table: { textStyle: { size: Q(8) } },
  },
  gaps: [["fallback", "fallback", 0], ["paragraph", "h2", 8], ["h2", "paragraph", 4], ["fallback", "code", 3], ["code", "fallback", 3], ["fallback", "math", 3], ["math", "fallback", 3], ["fallback", "box", 3], ["box", "fallback", 3], ["image", "image", 5]],
};
const interactiveTags = new Set(["applet", "button", "canvas", "embed", "form", "iframe", "input", "object", "script", "select", "textarea"]);
const pdfLink = (href, body) => color(url(href, restoreInlineValue(body)), rgb(0, 82, 155));

function frontMatter(source) {
  const match = source.match(/^---\r?\n([\s\S]*?)\r?\n---\r?\n?/);
  const values = new Map();
  if (match) for (const line of match[1].split(/\r?\n/)) {
    const pair = line.match(/^([A-Za-z][\w-]*):\s*(.*?)\s*$/);
    if (pair) values.set(pair[1], pair[2].replace(/^(?:"(.*)"|'(.*)')$/, "$1$2"));
  }
  return { values, body: match ? source.slice(match[0].length) : source };
}

function fileIdentity(file) {
  const relative = path.relative(docsDirectory, file).replace(/\\/g, "/");
  const stem = relative.replace(/\.m(?:d|arkdown)$/i, "");
  const output = stem === "index" ? path.join(docsDirectory, "pdf.pdf") : path.join(docsDirectory, "pdf", `${stem}.pdf`);
  return { relative, stem, output, sourceUrl: `${siteUrl}/${stem}.html` };
}

function imagePath(src) {
  const resolved = path.resolve(docsDirectory, src.replace(/^\//, ""));
  if (!resolved.startsWith(`${root}${path.sep}`)) throw new Error(`Image is outside the repository: ${src}`);
  return resolved;
}

function pdfImage(src) {
  const source = imagePath(src);
  if (path.extname(source).toLowerCase() !== ".svg") return image(source);
  const name = createHash("sha256").update(source).digest("hex").slice(0, 16);
  const rasterized = path.join(root, "tmp", "pdfs", "rasterized-svg", `${name}.png`);
  if (!existsSync(rasterized)) {
    mkdirSync(path.dirname(rasterized), { recursive: true });
    writeFileSync(rasterized, new Resvg(readFileSync(source), { fitTo: { mode: "width", value: 1600 } }).render().asPng());
  }
  return image(rasterized);
}

function htmlAttribute(attributes, name) {
  const match = attributes.match(new RegExp(`\\b${name}\\s*=\\s*(?:"([^"]*)"|'([^']*)'|([^\\s"'=<>\\x60]+))`, "i"));
  return match?.[1] ?? match?.[2] ?? match?.[3] ?? "";
}

function restoreInlineHtml(value) {
  return value.split(/@@MINITYPE(SUB|SUP)([A-Za-z0-9_-]+)@@/).flatMap((part, index, parts) => {
    if (index % 3 === 0) return part ? [part] : [];
    if (index % 3 === 1) return [];
    const text = Buffer.from(part, "base64url").toString("utf8");
    return [parts[index - 1] === "SUB" ? sub(text) : sup(text)];
  });
}

function restoreInlineValue(value) {
  if (typeof value === "string") return restoreInlineHtml(value);
  if (Array.isArray(value)) return value.flatMap(restoreInlineValue);
  return value;
}

function normalizeHtml(source) {
  let fence;
  return source.split(/(\r?\n)/).map((line) => {
    const marker = line.match(/^\s*(`{3,}|~{3,})/);
    if (marker) fence = fence ? undefined : marker[1][0];
    if (fence && !marker) return line;
    return decodeHtmlEntities(line).replace(/<img\b([^>]*)\/?\s*>/gi, (tag, attrs) => {
      const src = htmlAttribute(attrs, "src");
      return src && !/^(?:[a-z][a-z0-9+.-]*:|\/\/)/i.test(src) ? `![${htmlAttribute(attrs, "alt")}](${src})` : tag;
    }).replace(/<(sub|sup)\b[^>]*>([\s\S]*?)<\/\1\s*>/gi, (_tag, name, text) =>
      `@@MINITYPE${name.toUpperCase()}${Buffer.from(text.replace(/<[^>]*>/g, ""), "utf8").toString("base64url")}@@`
    ).replace(/<a\b([^>]*)>([\s\S]*?)<\/a\s*>/gi, (tag, attrs, text) => {
      const href = htmlAttribute(attrs, "href");
      return href && !/^\s*javascript:/i.test(href) ? `[${text.replace(/<[^>]*>/g, "").trim()}](${href})` : tag;
    });
  }).join("");
}

function decodeHtmlEntities(value) {
  const named = {
    amp: "&", gt: ">", lt: "<", quot: "\"", apos: "'", times: "×",
    theta: "θ", sigma: "σ", lambda: "λ", omega: "ω", gamma: "γ",
  };
  return value.replace(/&(#x[\da-f]+|#\d+|[a-z]+);/gi, (entity, name) => {
    if (name[0] === "#") return String.fromCodePoint(Number(name[1].toLowerCase() === "x" ? `0x${name.slice(2)}` : name.slice(1)));
    return named[name.toLowerCase()] ?? entity;
  });
}

function normalizeMarkdown(source) {
  const supported = new Set(["bash", "go", "html", "javascript", "json", "python", "shell", "text"]);
  return source
    .replace(/{%\s*highlight\s+([\w+-]+)(?:\s+[^%]*)?%}\r?\n?/gi, (_match, language) => `\`\`\`${supported.has(language.toLowerCase()) ? language.toLowerCase() : "text"}\n`)
    .replace(/{%\s*endhighlight\s*%}\r?\n?/gi, "\`\`\`\n")
    .replace(/^(`{3,}|~{3,})([^\s]*)\s*$/gm, (line, fence, language) => language && !supported.has(language.toLowerCase()) ? `${fence}text` : line);
}

function mathMarkers(source) {
  const display = [], inline = [];
  let fence, open;
  const output = [];
  const inlineReplace = (line) => line.split(/(`[^`]*`)/).map((part, i) => i % 2 ? part : part.replace(/(?<![\\$])\$(?!\$)([^$\n]+?)(?<!\\)\$(?!\$)/g, (_m, latex) => `@@MINITYPEINLINE${inline.push(latex.trim()) - 1}@@`)).join("");
  const displayMarker = (latex) => `@@MINITYPEDISPLAY${display.push(latex.trim()) - 1}@@`;
  for (const line of source.split(/\r?\n/)) {
    const marker = line.match(/^\s*(`{3,}|~{3,})/);
    if (marker) { fence = fence ? undefined : marker[1][0]; output.push(line); continue; }
    if (fence) { output.push(line); continue; }
    if (open) {
      const end = line.indexOf("$$");
      if (end === -1) { open.push(line); continue; }
      open.push(line.slice(0, end));
      output.push("", displayMarker(open.join("\n")), "");
      open = undefined;
      const tail = line.slice(end + 2);
      if (tail.trim()) output.push(inlineReplace(tail));
      continue;
    }
    const start = line.indexOf("$$");
    if (start === -1) { output.push(inlineReplace(line)); continue; }
    const end = line.indexOf("$$", start + 2);
    if (end !== -1) {
      const before = line.slice(0, start), after = line.slice(end + 2);
      if (before.trim()) output.push(inlineReplace(before));
      output.push("", displayMarker(line.slice(start + 2, end)), "");
      if (after.trim()) output.push(inlineReplace(after));
    } else {
      const before = line.slice(0, start);
      if (before.trim()) output.push(inlineReplace(before));
      open = [line.slice(start + 2)];
    }
  }
  if (open) output.push(...open);
  return { source: output.join("\n"), display, inline };
}

function replaceMath(value, formulae) {
  if (Array.isArray(value)) return value.forEach((item) => replaceMath(item, formulae));
  if (!value || typeof value !== "object" || value.type === "code") return;
  if ((value.type === "text" || value.type === "list") && Array.isArray(value.lines)) value.lines = value.lines.map((line) => line.flatMap((item) => typeof item !== "string" ? [item] : item.split(/@@MINITYPEINLINE(\d+)@@/).flatMap((part, index) => index % 2 ? [inlineMath(formulae[Number(part)])] : part ? [part] : [])));
  Object.values(value).forEach((child) => replaceMath(child, formulae));
}

function replaceInlineHtml(value) {
  if (Array.isArray(value)) return value.forEach(replaceInlineHtml);
  if (!value || typeof value !== "object" || value.type === "code") return;
  if ((value.type === "text" || value.type === "list") && Array.isArray(value.lines)) value.lines = value.lines.map((line) => line.flatMap((item) => typeof item === "string" ? restoreInlineHtml(item) : [item]));
  Object.values(value).forEach((child) => replaceInlineHtml(child));
}

function replaceDisplay(blocks, formulae) {
  return blocks.flatMap((block) => {
    const marker = block.type === "text" && block.textType === "paragraph" && block.lines?.length === 1 && block.lines[0]?.length === 1 && typeof block.lines[0][0] === "string" ? block.lines[0][0].match(/^@@MINITYPEDISPLAY(\d+)@@$/) : null;
    return marker ? [math(formulae[Number(marker[1])].split(/\r?\n/), { size: Q(10) })] : [block];
  });
}

function excluded(metadata, body) {
  if (metadata.get("pdf") === "false") return "front matter sets pdf: false";
  const text = body.replace(/(^|\n)(`{3,}|~{3,})[^\n]*\n[\s\S]*?\n\2(?=\n|$)/g, "$1");
  for (const found of text.matchAll(/<\s*([A-Za-z][\w:-]*)\b[^>]*>/g)) if (interactiveTags.has(found[1].toLowerCase())) return `<${found[1]}> outside a code example`;
  return null;
}

async function removeSquareAnnotations(file) {
  const pdf = await PDFDocument.load(await readFile(file));
  for (const page of pdf.getPages()) {
    const ref = page.node.get(PDFName.of("Annots")); if (!ref) continue;
    const annotations = pdf.context.lookup(ref, PDFArray);
    for (let i = annotations.size() - 1; i >= 0; i -= 1) if (pdf.context.lookup(annotations.get(i), PDFDict).get(PDFName.of("Subtype"))?.asString() === "/Square") annotations.remove(i);
  }
  await writeFile(file, await pdf.save());
}

async function generate(file) {
  const source = await readFile(file, "utf8");
  const { values: metadata, body } = frontMatter(source);
  const identity = fileIdentity(file);
  const title = metadata.get("title") || body.match(/^#\s+(.+?)(?:\s+\{#.+\})?\s*$/m)?.[1] || identity.stem;
  const bodyWithoutTitle = body.replace(/^#\s+.+?(?:\s+\{#.+\})?\s*\r?\n+/, "");
  const prepared = mathMarkers(normalizeMarkdown(normalizeHtml(bodyWithoutTitle.replace(/{%\s*(?:raw|endraw|include[^%]*)\s*%}\r?\n?/gi, "").replace(/[\u0000-\u0008\u000B\u000C\u000E-\u001F\u007F]/g, ""))));
  const markdownFile = path.join(root, "tmp", "pdfs", "normalized", identity.relative);
  await mkdir(path.dirname(markdownFile), { recursive: true });
  await writeFile(markdownFile, prepared.source);
  const article = await mdFile(markdownFile, { image: (src) => pdfImage(src), link: (href, text) => pdfLink(href, text) });
  article.blocks = replaceDisplay(article.blocks, prepared.display);
  replaceMath(article.blocks, prepared.inline);
  replaceInlineHtml(article.blocks);
  const document = minitype([{ body: [
    h1(title, { align: "center", unnumbered: true }),
    p([["from ", fontSize([color([b("unsatfit")], rgb(0, 82, 155))], Q(14)), " document: ", pdfLink(identity.sourceUrl, identity.sourceUrl)]], { align: "right", font: sansFont, size: Q(11), firstIndent: 0 }),
    box(article.blocks, { columns: 2, columnGap: 7, splitable: true }),
    { type: "flow", position: "page", blockOffset: 283, inlineSize: 210, blocks: [p([[page]], { align: "center", firstIndent: 0, font: sansFont, size: Q(9) })] },
  ] }], structuredClone(style), { fontDir, outline: false, metadata: { title, author: "Katsutoshi Seki" } });
  const errors = (await document.getDiagnostics()).filter((item) => item.severity === "error");
  if (errors.length) throw new Error(JSON.stringify(errors, null, 2));
  await mkdir(path.dirname(identity.output), { recursive: true });
  await document.save(identity.output); await removeSquareAnnotations(identity.output);
  return path.relative(root, identity.output);
}

async function docFiles(directory = docsDirectory) {
  const result = [];
  for (const entry of await readdir(directory, { withFileTypes: true })) {
    const file = path.join(directory, entry.name);
    if (entry.isDirectory() && !["sample", "sample-wrc"].includes(entry.name)) result.push(...await docFiles(file));
    else if (entry.isFile() && /\.m(?:d|arkdown)$/i.test(entry.name)) result.push(file);
  }
  return result.sort();
}

const args = process.argv.slice(2), includeMissing = args.includes("--missing"), all = args.includes("--all");
const requested = new Set(args.filter((arg) => !["--missing", "--all"].includes(arg)).map((file) => path.resolve(root, file)));
if (!includeMissing && !all && requested.size === 0) { console.error("Usage: node generate-pdfs.mjs --all | --missing [docs/file.md ...]"); process.exit(2); }
let generated = 0, excludedCount = 0; const failures = [];
for (const file of await docFiles()) {
  const { values, body } = frontMatter(await readFile(file, "utf8")); const reason = excluded(values, body);
  if (reason) { excludedCount += 1; continue; }
  const missing = !(await stat(fileIdentity(file).output).then(() => true).catch(() => false));
  if (!(all || requested.has(file) || (includeMissing && missing))) continue;
  try { console.log(`Generating ${path.relative(root, file)}`); console.log(`  -> ${await generate(file)}`); generated += 1; }
  catch (error) { failures.push(`${path.relative(root, file)}: ${error.message}`); }
}
console.log(`PDF generation: ${generated} generated, ${excludedCount} excluded.`);
if (failures.length) { console.error(`Failed PDFs:\n${failures.join("\n")}`); process.exit(1); }
