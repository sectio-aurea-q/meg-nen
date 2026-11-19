# `heavy_solvent`, and two points of the `heavy_other` count — 18 November 2026

## Why

On 18 November 2026 two referees of an analysis of the collection (the pairing of single values with temperature
series) found that the fields of rule 13 do not see the isotope of the solvent. The referees are runs of the
model, as on 16 November. M0271 and M0006 are primary effects measured in heavy water; both passed the comparison
of pressure, cosolvent, `heavy_other` and branch with a series measured in ordinary water, and were kept apart
only by side rules of that analysis. The referees also pointed at two codings of `heavy_other` that do not follow
from its definition.

## The new field

`heavy_solvent`, in `measurements.csv` and `temperature.csv`, after `heavy_other`: heavy water as the solvent of
both the light and the heavy reaction, where the row says so. `D2O`, or `D2O <amount> %` for a mixture; empty
means ordinary water, none stated. The field stays empty for `solvent` effects and for effects that change
substrate and solvent together: there heavy water is the isotope substitution itself and stands in
`labelled_position`. `tools/validate.py` checks the form and that a solvent effect leaves the field empty.

## How it was coded

Once, by the curator, not by two coders. `search.py` searches `labelled_position`, `conditions`, `notes`,
`as_printed` and `location` of every row of both tables for the spellings of heavy water: D2O and 2H2O with and
without subscripts, deuterium oxide, heavy water, deuterated water, buffer, solvent, medium or solution, pD, p2H
and pL as words, solvent isotope, proton inventory. `hits.csv` lists every row with a hit and the decision.

- 46 rows have a hit. 43 are solvent effects (32 values, 11 series); the field stays empty by definition. The
  word list finds every solvent effect of the collection; the script stops if it misses one.
- Three other rows have a hit:
  - M0006 (primary): the conditions give D2O as the solvent for NADH and NAD2H alike. `D2O`.
  - M0271 (primary): the same reaction in MOPS-2H2O. `D2O`.
  - M0009 (`other`, a double isotope effect): NADH in H2O against NAD2H in D2O. The solvent is part of the
    substitution. Empty.
- No temperature series is filled.

A row whose text does not mention heavy water cannot be coded as heavy water from the row alone. The search is
therefore the whole coding, and the only judgement lies in the three hits above. For that reason, and because the
outcome is two rows, no second blind coding was made. This departs from the practice of rules 12 and 13 and is
stated here for that reason. No source was read again.

## `heavy_other`: two points of the count settled

1. **M0026 and T0021** ("dideutero linoleic acid (Fig. 1 caption; the text names no position)", primary), from
   `nd` to 1. On 16 November coder 1 wrote `nd` ("position not named") and coder 2 wrote 1 ("counted 2 D minus
   transferred"); the record settled for `nd`. The field counts positions, and the count does not depend on where
   the second deuterium sits: the row is a primary effect, so one of the two deuteriums is the transferred one and
   exactly one further position is labelled. Settled now for coder 2.
2. **M0140–M0179** ("all H (perdeutero-LA, D-LA)", 40 primary values of doi 10.1074/jbc.ra119.010826), from `nd`
   to 30. On 16 November both coders wrote `nd` ("number of positions not stated in row"), as the instruction
   asked, and the record listed the 40 rows as not done. The same substrate is counted 30 wherever the row prints
   the number (M0096, M0097, M0221–M0232, M0284; T0059, T0060, T0069, T0070, T0154). Settled: a substrate that the
   row calls labelled in all its hydrogens is counted from its formula. Linoleic acid has 31 carbon-bound
   hydrogens; the carboxyl hydrogen exchanges with the solvent and is not counted; less the transferred one, 30.
   This uses the formula of the named compound, not knowledge of the paper. Rows that say only "D-linoleic acid
   (not further specified)" (T0121–T0132) or "not stated in the main text" stay `nd`.

`changes.csv` lists the 44 changed cells: 2 `heavy_solvent`, 42 `heavy_other`.

After the change, primary isotope effects: 0: 276, 1: 84, 2: 20, 5: 3, 8: 11, 30: 55, nd: 9. Primary temperature
series: 0: 101, 1: 22, 2: 7, 8: 2, 30: 5, nd: 25. No value, error or other field changes.

`SCHEMA.md` now also says what the number is not: it counts positions and gives neither the size of their
contribution nor its direction. In intramolecular competition within one CH2D group the further deuterium is on
the light path, so its secondary effect divides the measured value where in a dideuterated substrate it
multiplies it.

## Not covered by any field

- A solvent isotope effect measured with a labelled substrate (M0008; M0276–M0280). The label that is the same in
  both reactions stands in `conditions` or `labelled_position`.
- A secondary effect measured with deuterium in the transferred position (for example M0465 and M0469), and other
  designs with more than one label.
- The cryogenic buffer of the POR series (T0035–T0045) is still not named in the rows, as noted on 16 November.
- Whether a single value and a temperature series of the same paper come from the same set of measurements.
- Whether a single value was measured or calculated from the fit of the series.

## Files

- `search.py`: the search; run it with `python3 search.py`.
- `hits.csv`: the 46 rows with a hit and the decision on each.
- `changes.csv`: the 44 changed cells with the reason.
