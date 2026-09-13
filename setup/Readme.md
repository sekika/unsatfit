# Documentation PDF setup

Install the Git hook once for each local clone:

```sh
cd tools/minitype-pdf
npm install
cd ../..
make -C setup
```

The PDF tool intentionally has no lockfile: each `npm install` resolves the
latest releases of minitype and its PDF dependencies.  Run it again before a
PDF rebuild to pick up security and feature updates.

When a committed `docs/*.md` file is added, changed, moved, or deleted, the
pre-commit hook regenerates its PDF (and any missing documentation PDFs) and
stages `pdf/` automatically.  The hook stops if `docs/` has unstaged changes,
so the committed Markdown and generated PDFs always agree.

Generate PDFs without committing:

```sh
node tools/minitype-pdf/generate-pdfs.mjs --missing
node tools/minitype-pdf/generate-pdfs.mjs --all
```

The generated file corresponding to `docs/code.md` is `docs/pdf/code.pdf`; its PDF
contains a clickable source link to `https://sekika.github.io/unsatfit/code.html`.
The top page `docs/index.md` is generated as `docs/pdf.pdf`.

`pdf: false` in a document's YAML front matter excludes it from both generation
and the View PDF link.  Documents containing interactive HTML outside a code
example are also excluded.
