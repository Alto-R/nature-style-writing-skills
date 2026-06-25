# 04 — Results

## Role

Present findings in a fixed order, each subsection making one quantified point and pointing
at its figure. This file also owns the **number, unit, and statistics conventions** and the
**describe-a-phenomenon template** (they live here because this is where you use them most).

## Results discipline

> Results should make the reader trust the measurement before asking them to care about the
> meaning.

Results report what was measured, estimated, compared or tested — not why the study matters.
Keep the prose close to the data; significance, policy and broad implications belong in the
Introduction and Discussion (per `03`, `05`).

- **Finding-first, not narrative-first.** Open every subsection and paragraph with the
  result, not a motivation or broad claim. Prefer "[quantity] reaches [value] under
  [scenario/constraint]" over "to solve [big problem], this shows [broad solution] is
  possible".
- **Open with finding-narration, not editorialising.** Prefer result-stating openers — "The
  results show…", "Under the baseline scenario…", "Across sensitivity cases…", "This estimate
  decreases / increases under…", "The spatial distribution is concentrated in…" (cast in
  objective voice per `00`; "we quantify / we find" only sparingly). Avoid interpretive or
  promotional openers — "This reveals…", "This highlights the importance of…", "This opens a
  new pathway…", "This suggests a paradigm shift…", "This provides a bridge to…".
- **Report results, not importance.** Answer what was estimated, under what assumptions, at
  what magnitude, against what benchmark, how it varies (across space, time, groups or
  scenarios) and how robust it is. Do not answer at length why the topic matters, what
  society should do, or how the field changes — move those sentences out.
- **No rhetorical or metaphorical framing.** Drop slogans and promotional language ("turning
  point", "game-changing", "unlocking potential", "paradigm shift"). Replace with measurable
  language: "increases by [x]%", "decreases from [a] to [b]", "is concentrated in [units]",
  "exceeds [benchmark] under [scenario]", "remains robust across [sensitivity cases]".
- **Bounded interpretation only.** Interpretation must tie directly to the reported result.
  Prefer "this pattern is consistent with [mechanism] because [measured driver] varies with
  [outcome]" over "this shows [broad conclusion]"; prefer "under [constraint], A has a lower
  [metric] than B" over "A is the better solution".
- **Claims proportional to evidence.** Do not generalise past the analysis boundary. Every
  strong statement names its scope — scenario, spatial unit, temporal horizon, system
  boundary, and binding constraint. If a sentence would be false outside the model boundary,
  put the boundary in the sentence.
- **Embed the limit, never declare it.** A scope limit or exclusion must ride *inside* the
  result sentence — carried by the metric's name, the comparison object, the model-boundary
  phrase, or a subordinate clause — not stated as a standalone clarifying sentence. Defensive
  constructions that spell out what a result is *not* ("This comparison does not include…",
  "These comparisons reflect […], rather than […]", "This does not assume…") read like a
  reviewer response, not a finding; the qualifying detail belongs in Methods or the figure
  caption (per `06`, `07`), while the result sentence carries the boundary in its own terms.
  When a draft contains such a sentence, fold each excluded condition into a qualifier and
  delete the standalone clause.
- **Association, not causation, unless identified.** Default to "is associated with /
  correlated with / consistent with / varies with / concentrated in / coincides with";
  reserve "driven by / results from / caused by / proves / demonstrates" for cases where the
  analysis identifies causality.
- **Downgrade over-strong terms.** Replace a value-laden adjective with the measured property
  plus its accounting boundary; "huge potential" → "[value] [unit] of technical/economic
  potential"; "transformative" → delete unless a quantified comparison supports it.

**Results-only rewrite rule.** Any sentence that mainly answers "why this matters" should be
rewritten to answer "what the analysis shows". E.g. "this reveals a major opportunity to
transform [system]" → "under the baseline scenario, [n] cases meet [criterion], corresponding
to [value] [unit]". When revising, **preserve every number, figure reference and core
result, and reorder rather than discard** — introduce no result or judgement not supported by
the source text, and add no promotional summary.

**Limit-folding rewrite rule.** When a sentence exists only to fence off a result, dissolve it
into the result it qualifies. Each excluded condition becomes a word or clause; nothing is
lost, but the prose stops sounding like a rebuttal. The recurring repairs:

- *Exclusion → into the metric's name.* "This [estimate] does not include [excluded
  component], and does not assume [optimistic condition]." → "Measured as [bounding
  qualifier — e.g. a one-off, [timescale]-resolution] [metric], [quantity] exceeds
  [benchmark] (Fig. [N])." The two exclusions now ride in "[bounding qualifier]".
- *"Rather than" comparison → into the boundary clause.* "These comparisons reflect [metric]
  under [constraint], rather than [metric] for [other setting]." → "Under [constraint],
  [case A] shows a lower [metric] than [case B] (Fig. [N])." Drop the "rather than…"; the
  "under [constraint]" clause already bounds what is compared, and the "not [other setting]"
  caveat, if it is needed at all, goes to Methods or the caption.
- *Caveat → into a subordinate clause.* "This result holds only when [condition]." →
  "When [condition] holds, [quantity] reaches [value]." Same content, but now it is a finding,
  not a disclaimer.

## Structure

- Organise Results into **subsections, one analytical dimension each**, ordered from the
  primary finding outward (e.g. baseline pattern → who is affected → an added factor → a
  hopeful factor and its limit). Subheadings are **one level only**, sentence case, no end
  punctuation (per `00`).
- Subheadings are themselves mini-claims, but **result-type, not promotional.** State the
  measured finding, not its significance or a selling hook. "[Driver] is insufficient to
  [close the gap]" reads better than the bare topic "Effect of [driver]"; and a finding such
  as "[Quantity] [rises / falls] with [factor]" is preferred over promotional framing such as
  "A [transformative / promising] pathway to [goal]". If the heading would still read as true
  outside the analysis, it is too broad — tie it to what was measured.
- **One core finding per paragraph** (per `00`). Do not mix resource scale, spatial
  distribution, mechanism, robustness and policy meaning in a single paragraph; if a paragraph
  carries more than one finding, split it.

## Per-paragraph build

Each results paragraph follows the same arc:

1. **Topic sentence = the finding.** "[Substantial / pronounced] [pattern] [is evident /
   emerges] in [quantity] (Fig. [N]a)."
2. **Summary statistics.** Give the distribution, not just a mean: "[mean] ± [SD], with a
   median of [value] and a range of [a–b], indicating [substantial heterogeneity / a skew]."
3. **Explicit comparison / benchmark.** "[Subgroup] reach [value], about [k] times that of
   [reference group] ([value])," or "[x]% of the sample exceed [threshold]".
4. **Bounded mechanism or heterogeneity.** Tie the pattern only to variables analysed in the
   paper, in restrained language — "is associated with", "is consistent with", "varies with",
   "is concentrated in". Often via a regression: "[Outcome] is mainly associated with
   [driver 1] and [driver 2] (*β* = [value], *R*² = [value], *p* < [threshold])." Do not
   infer broad institutional, political or societal causes here — those belong in the
   Discussion (per `05`).
5. **Figure reference** in parentheses at the clause end: `(Fig. 2b)` — abbreviate "Fig.",
   never "Figure" mid-text.

## Describe-a-phenomenon template (reusable everywhere)

> **definition / model boundary → quantified observation → benchmark/comparison → bounded
> mechanism or heterogeneity → figure reference**

Example shape (placeholders): "Within [model boundary], [group] show [magnitude with units],
about [k] times that of [reference] ([magnitude]), a pattern consistent with [driver]
(Fig. [N])."

## Number, unit, and statistics conventions (baked in)

- **Distributions, not point values:** report mean ± SD *and* median *and* range where you
  can.
- **Units use negative integer exponents or "per":** `kW m⁻¹`, `USD kWh⁻¹`, `mg L⁻¹`,
  `g m⁻²` — **never** `kW/m` or `mg/L`. "per capita", "per hour" are fine in words.
- **Currency consistent:** pick `USD` and use it throughout; do not alternate with `$`.
- **Ranges** use an en-dash, no spaces: `6–10%`, `USD 500–624`. Lists of years use "and":
  "2030, 2040 and 2050".
- **Sample sizes and percentages:** "(*n* = [N], [x]% of the sample)". Use words for very
  small/rough fractions ("fewer than 1%", "about half").
- **Statistical symbols are italic, multi-letter names are roman.** Italicise scalar
  symbols: *β, p, R, R², n, σ, μ, t, F*. Keep upright (roman): functions and multi-letter
  abbreviations — `log`, `sin`, `GDP`, `VIF`, `CV`, and unit letters. Numerals and
  operators (`=`, `±`, `<`) stay roman. In figures, significance stars: `*p* < 0.05,
  **p* < 0.01, ***p* < 0.001`.
- **Hedge inferences, assert the headline.** Mechanisms and projections take *indicate,
  suggest, is associated with, likely*; the central finding is stated plainly.

## Voice

- Largely objective/passive: "the analysis reveals", "these results indicate". **Avoid
  repeated "we find / we observe"** (per `00`) — say what the data show, not that you saw it.
- Present tense for patterns and interpretation.

## Self-check

One-level subheadings as mini-claims? Does each paragraph open with a finding (not a
motivation)? Each paragraph: topic sentence → distribution stats → explicit comparison →
bounded mechanism → `(Fig. N)`? Any metaphor, slogan or "why it matters" claim to delete or
move to the Discussion? Does every strong claim name its scope (scenario, unit, horizon,
boundary)? Are scope limits folded *into* the result sentence (metric name, comparison object,
boundary phrase, subordinate clause) rather than stated as standalone "does not include… /
reflects… rather than…" sentences? Association language unless causality is identified? All units as negative
exponents, currency consistent, ranges en-dashed? Scalar stats italic, abbreviations roman?
"we" near zero in this section?
