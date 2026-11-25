# S016 (Sharma & Klinman 2008): supporting information read — 23 November 2026

## Why

T0021 (SLO-1 Leu546Ala/Ile553Ala) had no `n_temperatures`; the article prints only the range 15 to 50 °C and refers
to the supporting information.

## Source

`S016_Sharma2008_JACS_SI_Seitentext_2026-11-23.txt`: the text of NIHMS91462-supplement-1_si_001.pdf (PMC2671078),
copied by the curator from the PDF opened in the browser on 23 November 2026 and kept unchanged with a header on its
origin. The PDF itself is not in the source folder yet.

## How

One task (`task.md`), two readers blind to each other; the readers are runs of the model. Each transcribed Tables S1
and S2 (`reading1_tableS*.csv`, `reading2_tableS*.csv`), read the number of temperatures (`reading1.csv`,
`reading2.csv`), recomputed the Arrhenius fits and wrote remarks (`answers1.md`, `answers2.md`, in German). The two
transcriptions agree in every cell (8 rows each); both readings give the same number.

## Result

- **`n_temperatures` of T0021 is 8**: SI Table S2 prints one kcat(H) and one kcat(D) at each of 15, 20, 25, 30, 35,
  40, 45 and 50 °C, the range of Table 1, footnote a. The source does not say in so many words that all eight entered
  the fit and names no exclusion.
- **The numbers of Table 1 are the uncorrected ones.** The SI says that all data were "corrected to O2 saturation as
  needed" (Table S1: a factor of 1.022 to 1.195 on the protio rate, depending on temperature) and that the errors of
  kcat "were used to weight the exponential Arrhenius fit". Table S2 is headed "Empirical rate constants". Both
  readers recomputed the fits on their own (a recalculation, not a printed statement) with the same outcome: only the
  unweighted linear fit of ln kcat against 1/T over all eight temperatures with the values of Table S2 as printed
  gives Table 1 (Ea(H) 3.77, ΔEa 2.86, A_H 1.09 × 10^3, A_H/A_D 1.05; printed 3.8, 2.8, 1.1 × 10^3, 1.05; the printed
  2.8 equals the difference of the rounded 6.6 and 3.8). With the factors of Table S1 on kcat(H), or with weights,
  E_a(H) and A_H are missed (weighted and corrected: 3.36, 3.10, 586, 0.77). The printed errors of the fitted
  quantities are met by no variant.
- kcat 2.21 (0.09) and D kcat 128 (3) at 30 °C in Table 1 are the values of Table S2 as printed; with the factor
  1.116 of Table S1 they would be 2.47 s-1 and 143. The entry M0026 (128 ± 3) is therefore the value without the
  O2 correction. A note on M0026 and on T0021 says so.

## Remarks of the readers

- The error in parentheses of D kcat in Table S2 (1 to 3) is two to seven times smaller than the error propagated
  from kcat(H) and kcat(D) (2.9 to 7.5; at 30 °C (3) against 5.7). What the error is and the number of measurements
  are stated nowhere.
- D kcat at 50 °C is printed 91; 2.95/0.0321 = 91.9. D(kcat/KM) at 15, 30 and 45 °C lies one below the quotient
  (within the rounding of the inputs).
- Only the protio rate is corrected for O2 (the deuterio substrate is taken as saturated at all temperatures); the
  correction for the iron content applies to both and changes neither E_a nor the isotope effect; the source does
  not say whether Table S2 contains it.
- kcat/KM 0.11 (0.02) of Table 1 fits the corrected value (0.114) rather than the uncorrected one (0.102); not
  decidable.
- Misprints of the article: footnote d "Ea(D) − ΔEa(H)"; "octadecanoic"; "nearly temperature-dependent KIEs" for the
  wild type; "one hundred fifty-fold" where Table 1 gives about 130-fold.
- A single line "6" in the copied text is the footnote mark of the fitting program, not a number of rates.

## Open

- The single values of Table S2 (8 isotope effects on kcat, 8 on kcat/KM, 16 rate constants) are not entered yet;
  the meaning of the error of D kcat has to be settled first, as for S018.
- The PDF of the SI for the source folder.
