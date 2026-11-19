# `value_origin` — 19 November 2026

## Why

On 18 November 2026 two referees of an analysis of the collection (the pairing of single values with temperature
series, GUTACHTEN6) found that some single values are not measured at their temperature but calculated: the six
KE07 values (M0259–M0264) come from the same Arrhenius fit as the slope they were paired with, and M0104 is a rate
constant extrapolated to 0 bar. Until now this stood only in `notes`. A search of the text fields showed that many
more rows say how the source obtained the number (Northrop method, Swain–Schaad relation, commitment correction,
correction for isotopic purity, viscosity or iron content). The collection therefore gets one field for it.

## The new field

`value_origin`, in `measurements.csv`, after `heavy_solvent`: how the source obtained the printed number.

| value | meaning |
|---|---|
| `ratio` | the ratio of two quantities measured for the light and the heavy isotope, or a competitive measurement of both in one mixture, as the source reports it; each quantity may come from a kinetic fit of the source's own data at that temperature |
| `corrected` | a measured ratio that the source then corrected (isotopic impurity, deuterium abundance, solvent viscosity, iron content of the enzyme, statistical factor) |
| `combined` | calculated by the source from other isotope effects or kinetic parameters (Northrop method from H/T and D/T, Swain–Schaad relation, commitment correction, product of primary and secondary effects, equations applied to observed effects) |
| `fit_T` | calculated by the source from the fit of a temperature series and stated at one temperature |
| `extrapolated` | extrapolated by the source beyond its measured conditions |
| `nd` | the reading does not allow a decision |

If two apply, the later step counts: a corrected value that is then combined is `combined`; `fit_T` and
`extrapolated` count over everything else. `tools/validate.py` checks that every row carries one of the six values.
`temperature.csv` does not get the field: every series is a fit by definition.

## How it was coded

Twice, from the rows themselves, by two coders blind to each other, as for rules 12 and 13 (`instruction.md`). The
coders are runs of the model, as on 16 November. They saw only the text of each row (`labelled_position`,
`conditions`, `location`, `as_printed`, `notes`, and `kind`, `method`, `quantity`) and no source; no source was
read again for this coding.

- The two codings agree on 514 of 520 rows (98.8 %; Cohen's κ = 0.974).
- Six rows differ (M0080–M0083, M0257, M0520). All six are isotope effects that the source takes from the
  partition between two products of one reaction (benzylic against aromatic hydroxylation, or metabolic
  switching), with the light and the heavy substrate in separate reactions. Coder 1 wrote `ratio`, coder 2
  `combined`. Settled for `ratio`: the source divides two measured product partition ratios, and no other isotope
  effect enters. That the partition ratio stands for a ratio of rate constants is the source's model and is not
  coded here.
- `comparison.csv` lists all 520 rows, both codings and the decision.

Result: `ratio` 368, `combined` 127, `corrected` 18, `fit_T` 6 (M0259–M0264, KE07), `extrapolated` 1 (M0104),
`nd` 0. By `kind`: of the 140 intrinsic values 124 are `combined`, 15 `ratio` (intrinsic by the source's argument,
for example an intramolecular competition or a step the source shows to be rate-limiting) and 1 `corrected`
(M0055); of the 380 observed values 353 are `ratio`, 17 `corrected`, 6 `fit_T`, 3 `combined`, 1 `extrapolated`.

## Limits

- The coding reads the rows, not the sources. A row that presents its value as the measured isotope effect and
  says nothing of a further calculation is `ratio`; whether the source did more than it says is not known from the
  row. The human check of the rows that carry an analysis (GUTACHTEN6, open point 11) covers this field too.
- `combined` says that the number is calculated, not how good the calculation is. The assumptions of the Northrop
  method or of a commitment correction are the source's.
- No value, error or other field changes.

## Files

- `instruction.md`: the instruction both coders worked from.
- `coder1.csv`, `coder2.csv`: the two codings with the words of the row that decided each.
- `comparison.csv`: both codings, the field as entered, and the decision on each of the six differences.
