# Rule 13 coding — 16 November 2026

New fields `pressure_bar`, `cosolvent`, `heavy_other` (measurements.csv and temperature.csv) and `T_break_K`,
`branch` (temperature.csv). Coded from the rows themselves (`labelled_position`, `conditions`, `notes`,
`as_printed`, `location`) by two coders blind to each other; no source was read again. Reason: on 16 Nov 2026 two
referees of Schritt 3 found single values paired with temperature series across 1 bar / 2 kbar, across a break
and across the regime below 5 °C, and primary rows that carry secondary labels.

## Agreement
- `pressure_bar` and `cosolvent`: complete agreement (16 and 13 rows filled).
- `T_break_K`/`branch`: agreement except T0092/T0093 (coder 2: break 298.15, high/low; coder 1: none). Settled
  for coder 2: the row says the source fits "both ranges" (5–25 °C and 25–45 °C) separately.
- `heavy_other`: 166 differences, of two kinds only:
  1. Remote 14C reporter labels (competitive tritium method). Coder 1 counted them, coder 2 partly. Settled: the
     field counts hydrogen positions only; a remote 14C reporter is placed where it carries no isotope effect.
     All such rows are 0, including 31 rows where both coders had written 1 (rule clarified in CURATION.md 13).
  2. Competitive tritium rows where coder 1 wrote `nd` ("reporter label position not stated") and coder 2 `0`.
     Settled for 0: with the reporter not counted, only the transferred position differs.
- M0026, T0021 ("dideutero linoleic acid", positions not named): `nd` (coder 1), not 1.
- M0294, M0295 (benzyl alcohol, 14C ring reporter): 0.

## Result
Primary isotope effects: heavy_other 0: 276, 1: 83, 2: 20, 5: 3, 8: 11, 30: 15, nd: 50.
Primary temperature series: 0: 101, 1: 21, 2: 7, 8: 2, 30: 5, nd: 26.
Pressure stated: 2 values, 14 series. Cosolvent: 6 values, 7 series. Broken plots: 21 series (2 with `T_break_K` nd).

## Not done
- Cosolvent of the POR cryogenic buffer (T0035–T0045) is not named in the rows; left empty. Source to be read.
- 40 rows say only "perdeutero linoleic acid" (`nd`).
