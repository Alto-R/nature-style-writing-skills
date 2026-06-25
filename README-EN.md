<div align="center">

# Writing Nature Papers 🧬

A Claude Code skill for **Nature Communications** and Nature-branded research journals: it distills hands-on writing experience across multiple Nature family journals — and the journals' real submission checklists — into *section-by-section writing guides + journal-voice rules + a pre-submission mechanical sweep*, so every section is already compliant the moment you write it.

[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-D97757?style=flat-square&logo=anthropic&logoColor=white)](#-how-to-use)
[![Markdown](https://img.shields.io/badge/Format-Markdown-000000?style=flat-square&logo=markdown&logoColor=white)](#)
[![Python](https://img.shields.io/badge/Verification-Python%203.8+-3776AB?style=flat-square&logo=python&logoColor=white)](#-pre-submission-mechanical-sweep)
[![Journal](https://img.shields.io/badge/Target-Nature%20family-006699?style=flat-square)](#-scope)

**[中文](README.md)** | **[English](README-EN.md)**

</div>

<br>

## 📑 Quick navigation

<div align="center">

| | | |
|:---:|:---:|:---:|
| [✨ Core principle](#-core-principle) | [🏗️ Layout](#️-layout) | [🚀 How to use](#-how-to-use) |
| [🧭 Section router](#-section-router) | [✅ Pre-submission sweep](#-pre-submission-mechanical-sweep) | [🎙️ Voice & global rules](#️-voice--global-rules) |
| [📐 Rule map](#-rule-map) | [🚫 Scope](#-scope) | [❓ FAQ](#-faq) |

</div>

<br>

## ✨ Core principle

> **Lead with the finding, quantify everything, hedge what is inferred but stay decisive on the headline claim — and apply the journal's formatting rules while you write, not afterward.**

Every editorial rule is baked into the section guide where it applies: a correctly written section is already compliant.

- **Section-by-section templates**: title / abstract / introduction / results / discussion / methods / figures / references / declarations — each with paragraph-by-paragraph structure, sentence templates (placeholders, not real content), tense/voice, and the compliance rules embedded at the point they apply.
- **Distilled from multiple sub-journal experiences**: built from the writing experience of several manuscripts actually accepted at Nature family journals stripped of topic-specific content into reusable, topic-agnostic templates. The rules come from first-hand experience of getting through review and into print, not second-hand summaries that have never been tested by publication.
- **Compliance rules from real checklists**: every threshold and formatting requirement is distilled from the journals' actual submission checklists — not invented — and embedded into the relevant section where it applies.
- **Writing equals compliance**: turn each file's "Self-check" line into TodoWrite items so nothing is skipped.
- **Pre-submission safety net**: optional verification scripts catch artifact-level issues you *cannot* fix by writing (tracked changes left on, oversized files, stale SI PDF, red-green pixels in figures).
- **Topic-agnostic**: the same voice and structure transfer to any quantitative-research manuscript.

## 🏗️ Layout

```text
writing-nature-papers/
├── SKILL.md                         Skill entry: overview + section router + rule-ownership map
├── writing/                         Section-by-section guides (compliant as you write)
│   ├── 00-voice-and-global-rules.md Global voice & rules (all prose — read first)
│   ├── 01-title.md                  Title
│   ├── 02-abstract.md               Abstract (≤ ~200 words, "Here we show")
│   ├── 03-introduction.md           Introduction
│   ├── 04-results.md                Results (phenomena / numbers / statistics)
│   ├── 05-discussion.md             Discussion
│   ├── 06-methods.md                Methods (equations / units / currency / availability headings)
│   ├── 07-figures-and-display.md    Figures, tables, captions, colour, layout (main + SI)
│   ├── 08-references.md             References (main + SI)
│   └── 09-declarations-and-availability.md  Data/code availability, competing interests, contributions
└── verification/                    Pre-submission mechanical sweep (optional, run once before upload)
    ├── verification-workflow.md     Workflow notes + manual cross-consistency checklist
    └── scripts/                     Python verification scripts
        ├── check_all.py             Combined run, prints PASS / PARTIAL / FAIL
        ├── check_ooxml.py           Tracked changes / equation editability / bold / lists / field codes
        ├── check_figures.py         Red-green co-occurrence + greyscale distinguishability
        ├── check_deliverables.py    File sizes / stale SI PDF
        └── extract_text.py          docx→md text sanity scan
```

## 🚀 How to use

This is a **Claude Code skill**, not standalone software. In a Claude Code session where the skill is installed, it triggers automatically when you set out to draft, revise, or pre-submission-check a Nature-branded manuscript; you can also invoke it by stating your intent.

Workflow:

1. **Identify which part you are writing** and open exactly that file under `writing/`. Each file gives paragraph-by-paragraph structure, sentence templates, the tense/voice to use, and the compliance rules embedded at the point they apply.
2. **Always keep `writing/00-voice-and-global-rules.md` in mind** — it holds the rules for *all* prose (no novelty hype, soften absolute claims, sparse "we", no emphasis formatting, abbreviation-on-first-use, no bullet lists, heading style).
3. **When drafting, turn the file's "Self-check" line into TodoWrite items** so nothing is skipped.
4. **Before upload only**, optionally run the mechanical sweep in `verification/` for artifact-level issues you cannot fix by writing.

## 🧭 Section router

| Writing this… | Open |
| --- | --- |
| Global voice + rules for all prose | `writing/00-voice-and-global-rules.md` |
| Title | `writing/01-title.md` |
| Abstract | `writing/02-abstract.md` |
| Introduction | `writing/03-introduction.md` |
| Results (+ how to describe a phenomenon, numbers, stats) | `writing/04-results.md` |
| Discussion | `writing/05-discussion.md` |
| Methods (+ equations, units, currency, availability headings) | `writing/06-methods.md` |
| Figures, tables, captions, maps, colour, artwork (main + SI) | `writing/07-figures-and-display.md` |
| References (main + SI reference list) | `writing/08-references.md` |
| Data/code availability, competing interests, funding, contributions, affiliations | `writing/09-declarations-and-availability.md` |
| Final mechanical sweep before upload | `verification/verification-workflow.md` |

## ✅ Pre-submission mechanical sweep

The writing guides make the prose compliant *while you write*. This sweep is a safety net for **artifact-level** problems you cannot fix by writing — things that depend on the finished file (tracked changes accidentally left on, file size, a stale exported PDF, red-green pixels in a rendered image). **Run it once, just before upload.**

```bash
cd verification/scripts
python check_all.py --docx ../../Final_manuscript.docx \
                    --si ../../Supplementary.docx \
                    --si-pdf "../../Supplementary Information.pdf" \
                    --figdir ../../figure
```

What each script checks:

| Script | Checks | Why it must be post-hoc |
| --- | --- | --- |
| `check_ooxml.py` | tracked changes left on; OMML (editable) vs image equations; bold in body paragraphs; bullet/numbered lists; field codes (PAGE/NUMPAGES) | depends on the saved .docx internals |
| `check_figures.py` | red-green co-occurrence and greyscale-distinguishability of finished figure PNGs | depends on the rendered image pixels |
| `check_deliverables.py` | file sizes vs limits (30 MB upload, 50 MB figure); stale SI PDF | depends on files on disk and their timestamps |
| `extract_text.py` | pandoc docx→md; normalises full-width `（N）`→`(N)`; flags `kW/m`-style slash units, "on request" data statements, over-length abstract | a sanity scan of the exported text |
| `check_all.py` | runs the above and prints a combined PASS / PARTIAL / FAIL summary | — |

Dependencies: `python-docx`, `PyMuPDF` (`fitz`), `Pillow`, and `pandoc` on PATH; `pywin32` only if you pass `--word-com` on Windows to render/export via Word. Scripts degrade gracefully when an optional dependency or input is missing (they report `SKIP`, not crash). Exit codes: `0` PASS, `1` PARTIAL, `2` FAIL — usable in CI.

> This is **not** a substitute for writing correctly. If the sweep flags a prose issue, fix it in the owning `writing/` guide's terms, not with a patch here.

## 🎙️ Voice & global rules

A Nature-branded research paper reads like a confident, precise, slightly austere expert who never oversells. Five habits produce it:

1. **Lead with the finding, not the method** — state *what is true* first; the apparatus that established it comes second or in Methods.
2. **Quantify everything** — replace adjectives with numbers and units; give a distribution (mean, median, spread), not just a central value.
3. **Compare explicitly** — a number alone is inert; anchor it ("about k times that of the reference group", "x% of the sample").
4. **Hedge what is inferred, stay decisive on the headline** — use *indicate / suggest / likely* for mechanisms and projections; state the central result plainly.
5. **Topic sentence first** — each paragraph opens with the sentence that states its point.

## 📐 Rule map

| Rule / threshold | Owner file |
| --- | --- |
| Abstract ≤ ~200 words, no references, no undefined acronyms, "Here we show" | `02` |
| Introduction final paragraph in present tense, introduces the study | `03` |
| One level of subheadings; sentence case; no terminal punctuation in headings | `04`, `06`, `00` |
| Italic scalar symbols (*β*, *p*, *R*, *R²*, *n*); roman multi-letter functions/abbrevs | `04` |
| Units as negative exponents (`kW m⁻¹`, not `kW/m`); currency consistent (USD) | `04`, `06` |
| Equations editable, numbered `(1)`, referenced as "equation (1)" | `06` |
| Figure/table caption ≤ 350 words, self-contained (define every acronym/symbol/colour) | `07` |
| ≤ 10 main display items; each fits one A4 page; Arial 5–7 pt; ≥ 300 dpi; vector where possible | `07` |
| No red-green pairs; maps show latitude/longitude; multi-panel labels **a, b, c**; key inside image | `07` |
| References in citation order, complete, Nature format; SI list self-contained | `08` |
| Data availability specific (never "on request"); code via Zenodo DOI | `09` |
| Author contributions use initials, never "all authors" | `09` |
| No novelty/exaggeration words; soften absolute claims; sparse "we"; no emphasis formatting; no bullets | `00` |
| Tracked changes off, upload file ≤ 30 MB, fresh SI PDF, cover letter ≤ 250-char summary | `verification/` |

## 🚫 Scope

For drafting, revising, and pre-submission checking manuscripts for **Nature Communications** and other Nature-branded research journals.

When **not** to use:

- **Journals with a different house style** (IEEE, Elsevier, ACS) — the structure transfers, but the specific rules here are Nature-branded.
- **Plotting the figures themselves** — use the **superpowers:academic-figure** skill.
- **Low-level .docx manipulation mechanics** — use the **document-skills:docx** skill.

## ❓ FAQ

### Is this a program or documentation?

A Claude Code **skill** — primarily structured Markdown writing guides, plus an optional set of Python verification scripts. It does not write your paper's content for you; it constrains Claude so each section is compliant as it is written.

### Do I have to run the verification scripts?

No. The writing guides already make the prose compliant as you write; the scripts are an optional, run-once safety net for artifact-level issues before upload.

### What if `pandoc` or `Pillow` is missing?

Scripts degrade gracefully: a missing optional dependency or input reports `SKIP` rather than crashing.

### The sweep flagged a prose wording issue — do I fix it in the script?

No. Go back to the owning `writing/` guide and fix it in the source, in that guide's terms. The scripts only report; they do not rewrite.
