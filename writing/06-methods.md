# 06 — Methods

## Role

Let an independent group reproduce the study. Methods are exhaustive but ordered, with
detail pushed to the Supplementary Information. This file also owns **equation, unit, and
availability-heading** rules as they apply in Methods.

## Subsection order (functional, topic-agnostic)

Use one-level subheadings, sentence case, in roughly this order — include only those that
apply:

1. **Experimental / scenario design** — define the matrix of conditions and which parameters
   differ from baseline. State each scenario and why it exists.
2. **Model / system architecture** — the overall framework: components, how they couple,
   what is *not* modelled and why. Reference the schematic figure here.
3. **Sample / unit selection** — the population, inclusion/exclusion criteria, final **N**,
   and the data sources used to define them (cited).
4. **Input data — primary variable(s)** — source platform, temporal and spatial resolution,
   period, derived-quantity equations, preprocessing.
5. **Input data — secondary / exposure / scenario data** — model name, scenario, variables,
   period; justify any **exclusions** explicitly and note the direction of any resulting
   bias.
6. **Core algorithmic method** — the objective and constraints as **numbered equations**;
   the solver, its **version**, settings, and tolerances.
7. **Reliability / robustness submodule** (if any) — failure/risk modelling, stochastic
   approach (e.g. Monte Carlo, ensemble size), and the threshold metric enforced.
8. **Primary outcome metric** — define the key indicator in explicit steps; state how to
   interpret positive vs negative values.
9. **Sensitivity analysis** — vary key assumptions over stated ranges; report that findings
   remain stable (or how they shift).
10. **Data availability** and **Code availability** — see `09` for exact wording.

## Per-subsection paragraph template

Open by stating what is presented, then: source (with citation) → resolution/period →
parameter values with units and justification → cross-reference to the Supplementary detail.
Pattern: "[Quantity] [was/were] [simulated/derived] using [source/platform][ref], at
[resolution] over [period]. [Parameter] was set to [value] ([justification]). Detailed
[formulation] is provided in Supplementary Method [N] / Supplementary Equations ([a]–[b])."

## Reproducibility specifics (baked in)

- **Numeric precision:** 2–4 significant figures, always with units (`80 m`, `3-hourly`,
  `1% MIP gap`, `USD kWh⁻¹`).
- **Name software and versions explicitly** (e.g. "[Solver] [v.X.Y.Z]", "[Language] [vX.Y]").
- **State assumptions with their rationale**, including what is excluded and why.
- **Trace every data input** to a repository or publication with a citation.

## Equations (baked in)

- Equations must be **editable** (Word OMML / MathML / LaTeX), **never images**.
- **Number every equation** parenthetically `(1)`, `(2)`, … and **reference it in text** as
  "equation (1)" or "equations (2)–(5)".
- **Define every symbol** immediately below its equation ("where [symbol] is […]").
- Italicise scalar variables; keep functions and multi-letter terms roman; bold non-italic
  for vectors (see `04`).
- Defer long constraint/balance sets to Supplementary Methods, with continued numbering.

## Units & currency (baked in)

Same as `04`: negative-exponent units (`kW m⁻¹`), consistent currency (`USD`), en-dash
ranges.

## Tense & voice

- **Past passive** for what was done ("profiles were simulated", "the model was implemented
  in [language]").
- **Present passive** for how the system/constraint works ("reliability is enforced through
  a constraint on [metric]").
- **Present active** allowed for abstract logical statements and scenario definitions.

## Linking out

- Results refer back here by subsection name ("see Methods, [Subsection]").
- Detail lives in Supplementary Methods 1…N and Supplementary Equations/Tables; reference
  them precisely.

## Self-check

Subsections in functional order, one level, sentence case? Every equation editable, numbered,
referenced, symbols defined? Solver/versions named, parameters with units to 2–4 sig figs?
Exclusions justified? Data/Code availability present (per `09`)? Tense past/present passive?
