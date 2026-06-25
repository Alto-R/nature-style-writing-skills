# Verification — final mechanical sweep (optional, pre-upload only)

The writing guides make the prose compliant *while you write*. This sweep is a safety net
for **artifact-level** problems you cannot fix by writing — things that depend on the
finished file (tracked changes accidentally left on, file size, a stale exported PDF,
red-green pixels in a rendered image). Run it once, just before upload.

> This is **not** a substitute for writing correctly. If the sweep flags a prose issue, fix
> it in the owning `writing/` guide's terms, not with a patch here.

## Quick start

```bash
cd verification/scripts
python check_all.py --docx ../../Final_manuscript.docx \
                    --si ../../Supplementary.docx --si-pdf "../../Supplementary Information.pdf" \
                    --figdir ../../figure
```

Each script also runs standalone with `--help`. Dependencies: `python-docx`, `PyMuPDF`
(`fitz`), `Pillow`, and `pandoc` on PATH; `pywin32` only if you pass `--word-com` on Windows
to render/export via Word. Scripts degrade gracefully when an optional dep or input is
missing (they report SKIP, not crash).

## What each script checks

| Script | Checks | Why it must be post-hoc |
|---|---|---|
| `check_ooxml.py` | tracked changes left on; OMML (editable) vs image equations; bold in body paragraphs; bullet/numbered lists; field codes (PAGE/NUMPAGES) | depends on the saved .docx internals |
| `check_figures.py` | red-green co-occurrence and greyscale-distinguishability of finished figure PNGs | depends on the rendered image pixels |
| `check_deliverables.py` | file sizes vs limits (30 MB upload, 50 MB figure); stale SI PDF (PDF older than its .docx, or key values differ) | depends on files on disk and their timestamps |
| `extract_text.py` | pandoc docx→md; normalises fake full-width `（N）`→`(N)`; flags `kW/m`-style slash units, "on request" data statements, abstract over length | a sanity scan of the exported text |
| `check_all.py` | runs the above and prints a combined PASS / PARTIAL / FAIL summary | — |

## Inspection techniques (reusable, behind the scripts)

- **OOXML unpack:** a .docx is a ZIP; inspect `word/document.xml`. `<w:ins>`/`<w:del>` =
  tracked changes; `<m:oMath>` = editable equation, `<a:blip>` inside a math context = image
  equation; `<w:numPr>`/`ListParagraph` = a list; `<w:instrText>` are field codes (don't
  mistake them for insertions).
- **pandoc caveat:** pandoc emits fake full-width brackets `（N）` for some equation numbers
  and may drop OMML — always confirm equations in the real .docx, not the markdown.
- **Run-level italics:** statistical scalars must be their own italic run; fixing them means
  splitting runs in OOXML or via `python-docx`/Word COM, not italicising whole phrases.
- **Render to PDF:** Word COM `ExportAsFixedFormat(path, 17)` on Windows, or
  `libreoffice --headless --convert-to pdf`, then inspect with PyMuPDF (`fitz`).
- **Greyscale colour test:** convert a figure to greyscale; if two categories become
  indistinguishable, the colour pair fails the colour-blind check.

## Cross-consistency checks (manual — scripts can't judge these)

Scripts catch the mechanical issues; these need a human/agent read:

- **Text ↔ figure counts:** every "Fig. N[panel]" referenced exists with that panel; every
  cited Supplementary Table/Note exists; a count stated in prose matches the figure it cites.
- **Main ↔ SI consistency:** the same metric reported in both places uses the same number or
  range; a value isn't "98–100%" in one place and "97–98%" in another without explicit
  context.
- **Terminology:** one name per device/concept throughout (don't alternate two acronyms for
  the same thing); subscripts in equations match the symbols used in tables.
- **Abbreviation discipline:** defined once in the body; re-defined in each caption/table.

## Pre-submission auxiliary files (logistics reminder)

Not writing rules, but required at upload:

- **Supplementary Information** as a **single fresh PDF** (re-exported after the last edit),
  with a table of contents and page numbers; tracked changes removed.
- **Cover letter** including a third-person summary of the findings **≤ 250 characters**
  (incl. spaces) for website/e-alerts.
- **Third-party content statement**: declare any third-party images/data and the tools used
  to create figures; if BioRender was used, hold a publication licence and attribute it in
  the legend; declare whether generative AI created/edited any image.
- **Inventory of supporting information** (.docx) listing every SI figure/table/note, matching
  the SI PDF exactly.
- **File sizes:** keep each upload ≤ ~30 MB (use repositories for large data); embedded
  full-resolution images are the usual cause of an oversized Supplementary file.
