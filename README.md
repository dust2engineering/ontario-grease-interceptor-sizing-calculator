# Ontario Grease Interceptor Sizing Calculator (OBC 7.4.4.3)

Calculates the design flow rate through a grease interceptor with the formula the Ontario Building Code itself prescribes in Sentence 7.4.4.3.(7), so the selected CSA B481-rated interceptor is never undersized for the fixtures it serves.

**Live web tool:** https://dust2engineering.github.io/ontario-grease-interceptor-sizing-calculator/web/

## How it works

- For each fixture: Q contribution = 0.75 × brim volume ÷ drain down time (60 s or 120 s); add any pump discharge. The 0.75 factor reflects a fixture filled to about 75% with contents displacing the rest.
- The interceptor's rated capacity (CSA B481.1 lard test or B481.2 oil test) must be at least Q; locate it as close as possible to the fixtures (7.4.4.3.(6)).
- Both worked examples reproduce published municipal examples (Halifax Water, City of Calgary) to the decimal.

## Data in this repository

- `grease-interceptor-data.json` — the 7.4.4.3.(7) formula, the OBC requirement sentences and the CSA B481 selection/maintenance points, from the 2024 Building Code Compendium Part 7, checked 2026-11-15.
- `grease_interceptor.py` — command-line calculator using the same formula.

## Command line

```bash
python3 grease_interceptor.py 60 0 170.5
```

## Worked examples

- [three-compartment-sink.md](examples/three-compartment-sink.md)
- [two-sinks-calgary.md](examples/two-sinks-calgary.md)

## Scope and limits

Preliminary design aid only. It does not replace the current Ontario Building Code, the Canadian Electrical Code or CSA B149.1, or the judgement of the designer of record. Verify all values against the Code in force for your project before submitting drawings for permit.

## About

Maintained by **Dust 2 Engineering Inc.** (Mississauga, Ontario) — building permit drawings
(architectural, HVAC, plumbing, sprinkler, electrical) for restaurants and small commercial
projects across the Greater Toronto Area, stamped by an Ontario P.Eng. Flat rate $3,500–$5,000.

Category: Plumbing. More free Ontario code tools: see the full index at
https://github.com/dust2engineering
