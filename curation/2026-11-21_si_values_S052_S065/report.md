# Single values from the supporting information of S052 and S065 — 21 November 2026

## Why

The reading of this afternoon (`curation/2026-11-21_n_temperatures/`) found that the supporting information of
S052 (Guo et al. 2014, Biochemistry, 10.1021/bi500238q) and of S065 (Rapp et al. 2022, ACS Catalysis,
10.1021/acscatal.2c00257) prints the isotope effect at each temperature, where the articles give the fitted
Arrhenius parameters and one or three single values. Rules 4a and 4b allow such values.

## Files

- `bi500238q_si_001.pdf` and `cs2c00257_si_001.pdf`, from the supplementary-files service of Europe PMC
  (PMC4065160 and PMC9207888), fetched on 21 November 2026.

## How

One instruction (`instruction.md`), two readers blind to each other (`reading1.csv`, `reading2.csv`; answers to
the side questions in `answers1.md`, `answers2.md`); the readers are runs of the model. They typed from the PDF
pages, not from extracted text. The readings agree in all 220 cells (153 with a value, 57 printed "nd", 10 of
S065). `build_rows.py` makes the rows from them and refuses to run if a cell differs.

## What was entered

- S052, SI Tables S2 (kH) and S3 (kD): 102 rate constants of seven enzymes (BsDHFR and six variants) at six to
  nine temperatures, R0259–R0360.
- S052, SI Table S4 (KIE): 44 isotope effects, M0628–M0671. The seven values at 20 °C are the numbers of Table 5
  of the article (M0203–M0209), value and error; they are not entered a second time, and the notes of those rows
  say so and name the rate constants.
- S065, SI Table S1 (VH/VD at one saturating concentration): 7 isotope effects at 25, 30, 35, 40, 45, 50 and
  70 °C, M0672–M0678. Not entered a second time: 20 and 80 °C (the same value and error as Table 1 of the
  article, M0265 and M0269) and 60 °C (4.29 ± 0.28 against 4.30 ± 0.30 in Table 1, M0267, read as the same
  determination with more digits). The 40 °C value, 6.13 ± 0.19, is the maximum the text prints as 6.1 (M0283).

## Checks

- `tools/validate.py`: all rows pass; the ratio kH/kD reproduces the isotope effect of the same temperature within
  10 % in all 51 new cases (166 ratios instead of 115); 141 series/value pairs instead of 134.
- Counts: 678 isotope effects (317 of them from supporting information), 175 temperature series, 360 rate
  constants.

## Limits

- S052 states neither what the ± is nor the number of measurements. Three cells are printed unevenly (12.4±0.29,
  25.7±0.36, 29.6±6) and entered as printed. In Table S3 the last column is headed BsDHFR-P122EP129D.
- S065: Table S1 does not say what the ± is; the Methods speak of N ≥ 4 repeated measurements and the Figure 4
  legend of S.D. with N = 4 for the same profile. The article describes Table 1 (global fit) and Table S1 (single
  concentration) as two procedures, yet prints the same numbers at 20 and 80 °C; both readers flag this.
- The series of S052 (T0104–T0110) still have no printed fit range; which of the tabulated temperatures entered
  the fits of Table 5 is not stated.
