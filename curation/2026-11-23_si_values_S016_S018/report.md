# Single values from the supporting information of S016 and S018 — 23 November 2026

## What

Rules 4a and 4b. The values come from the transcriptions of the same day
(`curation/2026-11-23_S016_supporting_information/`, `curation/2026-11-23_S018_supporting_information/`), in each case
two readings blind to each other that agree in every cell. `build_rows.py` reads the first transcription, checks it
once more against the second and writes the rows.

| source | table | isotope effects | rate constants |
|---|---|---|---|
| S016 (Sharma & Klinman 2008) | SI Table S2 | 7 on kcat (15–50 °C without 30 °C) and 8 on kcat/KM | 16 (kcat with H and with D at 8 temperatures) |
| S018 (Nagel et al. 2012) | SI Table S5 | 34 on kcat | 79 (40 with H, 39 with D) |

The collection now holds 727 isotope effects and 455 rate constants.

## Decisions

1. **A value that the article prints as well is not entered a second time** (as on 21 November). S016: D kcat at 30 °C
   is M0026. S018: Table 1 of the article is headed "at 30 °C"; for L176G, L176Δ and V260A it prints the row at 30 °C
   of Table S5, for L176V and L176A Table S5 has no row at 30 °C and Table 1 prints the row at 28.5 °C (same D kcat,
   and the error of Table 1 is the one propagated from the rate constants of that row). These five rows are read as
   the determinations already held (M0029–M0033); a note on each says so. The temperature of M0029 and M0030 stays
   30 °C as printed in the article.
2. **The error of D kcat in SI Table S5 of S018.** The column "Error" of D kcat is not an absolute error. For all five
   values that Table 1 prints, the absolute error of Table 1 equals the error propagated from kcat (H) and kcat (D) of
   the same row of Table S5 (the script asserts this), and "Error" matches the relative error. For the 34 new values
   the `error` is therefore propagated from the two rate constants of the row; `as_printed` keeps the printed pair
   (value, Error) and the note of each row says that the error is a calculation of the curation and names the rate
   constants.
3. **The error of D kcat in SI Table S2 of S016** is entered as printed. It is smaller than the propagated error
   (the note of each row gives that number); what it is, is not stated, and Table 1 of the article prints the same
   small error for the value at 30 °C.
4. **S016: the values are those without the O2 correction** that the SI describes (Table S1); conditions and notes
   say so, and the note of each protio rate constant gives the factor of Table S1 at its temperature.
5. S018: Table S5 prints no unit; s-1 as for kcat in Table 1 of the article. KM of S016 Table S2 is not held in the
   collection; the note of each kcat/KM row quotes it.
6. `tools/validate.py`: the check "the quotient of the rate constants reproduces the isotope effect within 10 %" now
   allows for the rounding of the printed rate constants (half a unit of the last digit). Without it V260A at 10 °C
   fails (0.04/0.011 = 3.64, printed 4.04; kcat (H) has one digit).

## Check

`tools/validate.py` passes: 727 isotope effects, 455 rate constants; 211 quotients of rate constants agree with the
isotope effect of the same row.
