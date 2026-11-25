# Number of temperatures of the series tested with a printed slope — 21 November 2026

## Why

Two referees of the analysis of 21 November noted that the error of a printed slope can only be put on the right
quantile when the number of temperatures behind it is known. Of the 28 series tested with a printed slope, 26 had
`n_temperatures` empty. The earlier readings had already noted for most of them that the main text does not state
the number.

## How

- Supporting information fetched from Europe PMC (supplementaryFiles service) for S027 (Carr & Klinman 2014),
  S052 (Guo et al. 2014), S061 (Anoz-Carbonell et al. 2020; the package holds figures only) and S065 (Rapp et al.
  2022).
- One task (`task.csv`), two readers blind to each other (`reading1.csv`, `reading2.csv`, in German); the readers
  are runs of the model. They read the article and the SI, compared the text of every table they relied on with
  the PDF, and agree on all twelve series.
- Only what is printed counts: a stated number, a list, a table with one row per temperature, or range and step.
  Points in a figure are not counted (rule 4).
- For S005 (T0171, T0172) and S051 (T0102) nothing was read anew; the number follows from what the readings of
  15 and 19 November had recorded in `notes`.

## Result

| series | source | `n_temperatures` | basis |
|---|---|---|---|
| T0104 | S052 | 9 | SI Tables S2, S3: 10–50 °C in steps of 5 |
| T0105, T0106, T0108, T0109 | S052 | 7 | 5–35 °C |
| T0107 | S052 | 8 | 5–40 °C |
| T0110 | S052 | 6 | 5–30 °C |
| T0150 | S065 | 4 | SI Table S1 lists 20, 25, 30, 35, 40 °C; the Fig. 3 legend omits 25 °C from the Arrhenius plot |
| T0151 | S065 | 4 | SI Table S1: 45, 50, 60, 70 °C |
| T0102 | S051 | 6 | SI Table S1 (reading of 19 November): 5–30 °C |
| T0171, T0172 | S005 | 7 | 5–35 °C at 5 °C intervals (the 40 °C point was not fitted) |
| T0059, T0060 | S027 | empty | only the ranges are printed |
| T0138 | S061 | empty | only the range is printed |

## Limits

- S052 and S051 do not say which of the tabulated temperatures entered the Arrhenius fit. The number entered is the
  number tabulated; `notes` say so, and the range of these series stays empty.
- S065: Table S1 is a table of VH/VD, not of kcat for each isotope; that the omission of 25 °C holds for both
  isotopes is not stated separately.
- Still empty among the 26: T0021 (S016), T0022–T0025 (S018) — SI not in hand; T0051 (S024), T0154, T0155 (S001),
  T0168 (S004) — number only countable from figures; T0133, T0134 (S059) — "at least seven"; T0059, T0060, T0138.

## Not entered yet

SI Table S4 of S052 (isotope effect at each temperature, seven variants) and SI Table S1 of S065 (VH/VD at ten
temperatures) hold single values under rule 4a.

## What changes (`changes.csv`)

`n_temperatures` filled in twelve series, a note appended in fifteen. No value, error or status changes.
