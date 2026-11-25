# Decisions taken (by the model on the curator's behalf; rule 3)

1. **M0359–M0371 (intrinsic values of S013, SI Table 2S).** Coder 1: `conflicting`; coder 2: `se` for these 13 and
   `conflicting` only for M0358. The notes of all 14 rows quote the same two statements of the source: its
   introduction calls the errors of the tables standard errors, and its text calls the ± of one value of the same
   table (9.44 ± 0.29, M0358) a 95 % confidence interval. If that one value's ± is a 95 % interval, the statement
   about the table cannot be taken at face value for the other rows either. Entered as `conflicting` for all 14,
   in line with the decision of this morning's record (`2026-11-12_si_reading_S013_S019_S040_S041/resolution.md`,
   point 3: "Not settled").
2. **M0210–M0214.** Coder 2 gave `>=15` from "at least 15 averaged shots"; coder 1 left it empty. Shots averaged
   into one trace are not independent measurements of the value. Left empty.
3. **Points both coders flagged and coded alike** (kept as coded):
   - M0052–M0054: no ± printed, so `none`, although a footnote speaks of relative errors under 2 %.
   - M0098–M0102: `se`, propagated from rate constants with standard errors; `n_measurements` 2 is the number of
     duplicates of those rate constants. M0103 (duplicates and triplicates mixed): no number.
   - M0104: `not_recorded`; the standard deviation the notes mention belongs to the rate constants, and the notes
     do not say that it was propagated.
   - M0249, M0250: "n > 3" written as `>=4`.
   - M0294–M0297: `n_measurements` counted from the individual experiments listed in `notes`.
   - M0079: `other`; 3 is the number of enzyme preparations.
4. **Not done.** `temperature.csv` has three error fields per row and is not coded yet. The 107 `not_recorded` rows
   are to be closed from the sources.
