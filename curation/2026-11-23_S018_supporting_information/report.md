# S018 (Nagel et al. 2012): supporting information read — 23 November 2026

## Why

The series T0022–T0026 (ht-ADH variants, upper branch above the break) had no `n_temperatures` and no E_a(H). The
article refers to the supporting information for the values per temperature.

## Source

`S018_Nagel2012_Biochemistry_SI_Seitentext_2026-11-23.txt`: the text of NIHMS376254-supplement-1_si_001.pdf
(PMC3498984), copied by the curator from the PDF opened in the browser on 23 November 2026 and kept unchanged with a
header on its origin. Europe PMC was not reachable on that day and PubMed Central does not serve the file to a script.
The PDF itself is not in the source folder yet.

## How

One task (`task.csv`), two readers blind to each other; the readers are runs of the model. Each transcribed
Tables S1 to S5 (`reading1_tableS*.csv`, `reading2_tableS*.csv`), read the number of temperatures of the upper branch
(`reading1.csv`, `reading2.csv`) and wrote remarks (`answers1.md`, `answers2.md`, in German). All numbers of the five
tables agree cell by cell (40 rows in Table S5, 6 each in S1 and S2, 8 each in S3 and S4); the two readings differ only
in the wording of the remark on the brackets of the WT row. Both readings give the same `n_temperatures`.

## Result

- The printed ΔE_a of the upper branch (SI Table S2) equals Table 2 of the article and the entries of the database for
  all five series. Nothing changed there.
- **E_a(H) of the upper branch** is printed only in SI Table S2 and is entered now (`Ea_light_kcal`, `Ea_light_error`):
  L176V 18.6 ± 0.6, L176A 15.9 ± 0.5, L176G 16.6 ± 0.5, L176Δ 13.5 ± 0.4, V260A 14.2 ± 1.0. Tables S1 and S2 print no
  unit; kcal/mol follows from Table 2 of the article.
- **`n_temperatures`** is entered as a lower bound for all five series:

| series | variant | temperatures of Table S5 above the break | entered |
|---|---|---|---|
| T0022 | L176V | 33, 37.5, 42, 45, 52 °C (break 30 °C, no point at 30 °C) | >=5 |
| T0023 | L176A | 33, 37.5, 45, 52 °C (no point at 30 °C) | >=4 |
| T0024 | L176G | 37.5, 46, 52 °C, and a point at 30 °C itself | >=3 |
| T0025 | L176Δ | 40, 50, 60 °C, and a point at 30 °C itself | >=3 |
| T0026 | V260A | 45, 50, 58 °C (break 40 °C, Table 2 footnote a; no point at 40 °C) | >=3 |

  The source prints neither the ranges of the fits nor to which branch a point at the break belongs. Both readers
  recomputed the fits from Table S5 on their own (not a printed statement): for L176G and L176Δ a weighted fit that
  includes the point at 30 °C gives the numbers of Table S2 to the printed digit, and the same point also fits the
  lower branch; for L176A and V260A the fit with the point next to the break (28.5 and 38 °C) lies closer to
  Table S2; for L176V it is undecided. The count above the break is therefore a lower bound in every case (decision
  of the curation on 23 November 2026).

## Remarks of the readers

- D kcat of Table S5 equals kcat(H)/kcat(D) within rounding in all 39 rows with numbers; the widest gap is V260A at
  10 °C (0.04/0.011 = 3.64, printed 4.04; kcat(H) has one significant digit there).
- **The "Error" of D kcat in Table S5 is not the propagated absolute error.** Table 1 of the article prints for the
  same values the propagated ones (L176Δ, 30 °C: 4.4 ± 1.4 against 4.4 ± 0.3 in Table S5); in size the column of Table
  S5 matches the relative error. What the ± is and the number of measurements are stated nowhere.
- Table 1 is headed "at 30 °C"; for L176V and L176A Table S5 has no row at 30 °C and the values of Table 1 are those
  of the rows at 28.5 °C.
- WT: the text gives 0.1 kcal/mol with a reference to Table 2, which prints 0.2 (±0.2) as Ea(T) − Ea(H); 0.1 stands
  only in SI Table S2.
- SI Table S1, L176V: 30.0 − 27.5 = 2.5, printed 2.4. SI Table S2, L176A: 17.2 − 15.9 = 1.3, printed 1.4 (as in
  Table 2).
- Table S5 itself prints no pH, buffer or units; pH 7.0 follows from the article.

## Open

- The single values of Table S5 (39 isotope effects, 79 rate constants) and the lower branch (Table S1) are not
  entered yet. Before they are, the meaning of the "Error" column of D kcat has to be settled (see above).
- The PDF of the SI for the source folder; the SI of S016.
