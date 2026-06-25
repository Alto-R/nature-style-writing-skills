# Verification scripts

Optional **pre-upload mechanical sweep** for a Nature-branded submission. These catch
artifact-level issues that cannot be fixed by writing (tracked changes left on, file size,
stale Supplementary PDF, red-green pixels, stray lists). They do **not** replace writing each
section correctly with the `writing/` guides — see `../verification-workflow.md`.

## Dependencies

| Need | For |
|---|---|
| Python 3.8+ | all scripts |
| `pandoc` on PATH | `extract_text.py` (docx→markdown) |
| `Pillow`, `numpy` | `check_figures.py` (pixel scan) |
| (standard library only) | `check_ooxml.py`, `check_deliverables.py` |

Install the optional ones: `pip install pillow numpy` and install pandoc from pandoc.org.
Missing dependencies or inputs produce a `SKIP`, never a crash.

## Run everything

```bash
python check_all.py --docx ../../Final_manuscript.docx \
                    --si ../../Supplementary.docx \
                    --si-pdf "../../Supplementary Information.pdf" \
                    --figdir ../../figure
```

## Run individually

```bash
python check_ooxml.py        --docx Manuscript.docx
python check_figures.py      --figdir figures/
python check_deliverables.py --files Manuscript.docx Supplementary.docx --si Supplementary.docx --si-pdf SI.pdf
python extract_text.py       --docx Manuscript.docx --dump extracted.md
```

## Output

Each line is tagged `[PASS] / [PARTIAL] / [FAIL] / [SKIP]`, and each script prints a summary
line. `check_all.py` rolls them into one `OVERALL` verdict and an exit code (0 PASS,
1 PARTIAL, 2 FAIL) for use in CI.

## Note on rendering to PDF

The scripts inspect existing files; they do not export PDFs. To render a .docx to PDF for
visual inspection, use Word COM (`ExportAsFixedFormat(path, 17)`) on Windows or
`libreoffice --headless --convert-to pdf file.docx`, then re-run `check_deliverables.py` /
`check_figures.py` on the output.
