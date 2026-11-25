# Number of temperatures, second round — 23 November 2026

## Why

The referees of the analysis of 23 November 2026 (internal review) asked again for `n_temperatures` of the series tested with a
printed slope. Fourteen of them were still empty. This round covers the sources that lie in the source folder: S016,
S018, S024, S057, S059 and S061 (15 series: T0021, T0022–T0025, T0051, T0115–T0120, T0133, T0134, T0138). The series
of S001 (T0154, T0155) and S004 (T0168) are closed sources and follow separately. S027 (T0059, T0060) was read on
21 November and stays empty.

## How

- One task (`task.csv`), two readers blind to each other (`reading1.csv`, `reading2.csv`, `answers1.md`,
  `answers2.md`, in German); the readers are runs of the model. They read the article and, where it lies in the
  folder, the supporting information (S057: oc7b00142_si_001.pdf; S059: SI Appendix; S061: figure package).
- Only what is printed counts: a stated number, a list, a table with one row per temperature, or range and step.
  Points in a figure are not counted (rule 4).
- New on this day (decision of the curator): where a source prints only a lower bound ("at least seven
  temperatures"), `n_temperatures` takes the form `>=7`, as `n_measurements` already does. SCHEMA.md and
  `tools/validate.py` changed accordingly.
- The two readings agree on all 15 series. Table S7 of S057 was compared once more with the PDF text after the
  comparison.

## Result

| series | source | `n_temperatures` | basis |
|---|---|---|---|
| T0115, T0116, T0117, T0118, T0120 | S057 | 8 | SI Table S7: one row per temperature, 10–45 °C in steps of 5, for H and D |
| T0119 | S057 | 7 | SI Table S7: Y317L has no row at 10 °C (15–45 °C) |
| T0133, T0134 | S059 | >=7 | SI Appendix, Methods: "at least seven temperatures for each variant"; range 10–40 °C, no step printed for the kinetics |
| T0021 | S016 | empty | only the range 15 to 50 °C (Table 1, footnote a); SI not in the folder |
| T0022–T0025 | S018 | empty | nothing printed in the article; the values per temperature are in SI Tables S2–S5, not in the folder |
| T0051 | S024 | empty | neither number nor range printed; three preparations fitted separately and averaged (note 31) |
| T0138 | S061 | empty | only the range 5.3–20 °C; Fig. 9A shows six points per isotope, which is not a printed number |

## Remarks of the readers

- S057: the article (Table 1, footnote b) says the fit runs over "7 to 8 (depending on mutant) temperatures"; the
  rows of Table S7 match that. The source does not say in so many words that every row entered the fit.
- S057, Y317S: Table S7 prints kcat(H) = 83 s-1 at 30 °C, Table 1 prints 330 s-1. Table S7 is not corrected for the
  iron content, Table 1 is; the source gives no reason for a factor of four (1.1 to 1.3 for the other variants).
- S059: "at least seven" is printed for Ea(H). Table 1, footnote *, says the temperature data were reported before
  (ref. 35 of the source), which is not in the folder. The "5 °C intervals" of the SI belong to the fluorescence
  spectra, not to the kinetics.
- S018: the PMC version of Table 2 has no column A_H/A_D for the L176 variants.

## Open

- SI of S016 and S018 (not downloaded yet); S001 and S004 (closed sources); ref. 35 of S059.
- The analysis scripts (`schritt3_*.py`) read `n_temperatures` as a number and treat `>=7` as not stated until the
  next version, which will use the lower bound.
