# minitype documentation PDFs

From this directory, install the Node.js dependencies once and generate PDFs:

```sh
npm install
npm run build
```

`npm run build` creates only missing files; `npm run rebuild` regenerates all
documentation PDFs. `docs/code.md`, for example, becomes `docs/pdf/code.pdf`;
the top page `docs/index.md` becomes `docs/pdf.pdf`, matching its GitHub Pages
URL.

All dependencies are declared as `latest` and the local `.npmrc` disables the
lockfile, so `npm install` resolves current releases rather than retaining an
old dependency graph.

The generator typesets the Markdown source on A4 pages with a two-column body,
embedded fonts, page numbers, blue clickable links, and a clickable source URL
such as `https://sekika.github.io/unsatfit/code.html`.  Repository images are
included, and SVG files are rasterized only in the ignored `tmp/pdfs/` work
area.  Inline and display TeX expressions are rendered by minitype.

The site layout links every eligible documentation page to its corresponding
PDF.  Add `pdf: false` in YAML front matter to suppress both generation and the
View PDF link.
