# Single values from the supporting information of S057 and S058 — 19 November 2026

## Why

Two referees of an analysis of the collection (internal review of 18 November 2026, point 5) asked that single values be
used where a source prints them, instead of one value and a printed slope. The readings of today found two
supporting-information files that print the isotope effect and both rate constants at every temperature:

- S058 (Hu et al. 2016, 10.1002/anie.201603592), SI Tables S3 (WT), S4 (I553V), S5 (L546A): kcat-H, kcat-D and
  Dkcat at 288, 293, 298, 303 and 308 K and at 1, 344, 688 and 1034 bar. File
  NIHMS817928-supplement-Supporting_Information.docx, downloaded by the curator from PMC5040518.
- S057 (Offenbacher et al. 2017, 10.1021/acscentsci.7b00142), SI Table S7: kcat(H), kcat(D) and Dkcat of WT,
  S749A, S749G, Y317S, Y317L and Y317F at 10 to 45 °C (Y317L from 15 °C). File oc7b00142_si_001.pdf from the
  supplementary-files service of Europe PMC (PMC5492416).

Rules 4a and 4b allow such values.

## How

Two readers blind to each other (ai-1, ai-2; runs of the model) typed the tables from the text of the files
(`instruction.md`; `reading1.csv`, `reading2.csv`): 107 rows, 642 cells. **The two readings agree in every cell.**
`build_rows.py` in this folder turns reading 1 into the rows that were entered; no number is changed on the
way.

## What was entered

- 107 isotope effects (M0521–M0627): 60 of S058, 47 of S057. `value_origin` is `ratio`, `heavy_other` 30,
  `pH` 9.0; the S058 rows carry `pressure_bar`.
- 214 rate constants (R0045–R0258), one for each isotope of each row.
- `rates.csv` gets the field `pressure_bar` (empty in the 44 older rows), because the rate constants of S058
  differ only by pressure; the check of rule 4b and the check of rule 10 now also compare `pressure_bar`.

## Read with care

- **Temperature.** S058 prints kelvin without decimals (288 … 308 K) and its text gives 15 to 35 °C; the rows
  carry 288.15 … 308.15 K, like the series of the same source.
- **Units.** Table S3 of S058 prints no unit, Table S4 prints s-1 only for kcat-D, Table S5 prints s-1 for kcat-H and
  **10-2 s-1 for kcat-D**. The rate constants are entered as printed with the unit of their block (`s-1` where
  none is printed, said in `notes`; `10-2 s-1` for kcat-D of L546A). The validator compares only rate constants of
  the same unit, so it does not check the L546A ratios; they were checked here by hand (next point).
- **Two cells of Table S5 do not follow from the printed rate constants** (L546A, 293 K): at 1 bar 7.17 / 0.0557 =
  128.7 against the printed 124; at 344 bar 7.07 / 0.0660 = 107.1 against 116. All other 105 isotope effects agree
  with the ratio of the printed rate constants within 3 %. The two values are entered as printed, with a note.
- **Meaning of the ±.** S058 does not say what the parentheses are (`not_stated`). S057: mean ± s.e.m. of three
  measurements (SI, kinetics section), entered as `se`, n = 3.
- **Iron.** Table S7 of S057 calls its rate constants not corrected for iron content, while Table 1 of the article
  is corrected. The 30 °C values of Table S7 therefore stand beside M0239–M0244 and are not duplicates: e.g. WT
  56.7 (1.5) in Table S7 against 57 (2) in Table 1.
- Nothing is fitted or derived from these rows here.
