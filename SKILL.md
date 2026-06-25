---
name: writing-nature-papers
description: Use when drafting, revising, or pre-submission checking a manuscript for Nature Communications or a Nature-branded research journal — writing any section (title, abstract, introduction, results, discussion, methods, figures, references, declarations) in the journal voice with submission rules already applied, or verifying a finished .docx / Supplementary PDF before upload. Keywords: Nature Communications, "Here we show", figure caption 350 words, red-green colorblind, italic statistics, tracked changes, OOXML, supplementary information PDF, file size limit, data availability, author contributions.
---

# Writing Nature papers

## Overview

This skill writes submission-grade manuscripts for **Nature Communications** and other
Nature-branded research journals. It is built from a real accepted manuscript, distilled
into topic-agnostic templates.

**Core principle:** *Lead with the finding, quantify everything, hedge what is inferred
but stay decisive on the headline claim — and apply the journal's formatting rules while
you write, not afterward.* Every editorial rule is baked into the section guide where it
applies, so a correctly written section is already compliant. There is no separate
"checklist pass."

## How to use this skill

1. **Identify which part you are writing** and open exactly that file under `writing/`.
   Each file gives the paragraph-by-paragraph structure, sentence templates (with
   placeholders, not real content), the tense/voice to use, and the compliance rules
   embedded at the point they apply.
2. **Always keep `writing/00-voice-and-global-rules.md` in mind** — it holds the rules that
   apply to *all* prose (no novelty hype, soften claims, sparse "we", no emphasis
   formatting, abbreviation-on-first-use, no bullet lists, heading style).
3. **When drafting, turn the file's "Self-check" line into TodoWrite items** so nothing is
   skipped.
4. **Before upload only**, optionally run the mechanical sweep in `verification/` for
   artifact-level issues you cannot fix by writing (tracked changes left on, file size,
   stale Supplementary PDF, red-green pixels in finished figure images).

## Section router

| Writing this… | Open |
|---|---|
| Global voice + rules for all prose | `writing/00-voice-and-global-rules.md` |
| Title | `writing/01-title.md` |
| Abstract | `writing/02-abstract.md` |
| Introduction | `writing/03-introduction.md` |
| Results (+ how to describe a phenomenon, numbers, stats) | `writing/04-results.md` |
| Discussion | `writing/05-discussion.md` |
| Methods (+ equations, units, currency, availability headings) | `writing/06-methods.md` |
| Figures, tables, captions, maps, colour, artwork (main + SI) | `writing/07-figures-and-display.md` |
| References (main + SI reference list) | `writing/08-references.md` |
| Data/code availability, competing interests, funding, author contributions, affiliations | `writing/09-declarations-and-availability.md` |
| Final mechanical sweep before upload | `verification/verification-workflow.md` |

## At-a-glance rule map (which file owns each)

| Rule / threshold | Owner file |
|---|---|
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
| Tracked changes off, file size ≤ 30 MB upload, fresh SI PDF, cover letter ≤ 250-char summary | `verification/` |

## When NOT to use

- Journals with different house style (IEEE, Elsevier, ACS) — the structure transfers but
  the specific rules here are Nature-branded.
- Plotting the figures themselves — use **superpowers:academic-figure**.
- Low-level .docx manipulation mechanics — use **document-skills:docx**.
