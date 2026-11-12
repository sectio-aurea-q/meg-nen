# Coding task: what kind of error is the printed ±, and from how many measurements?

Input: `zeilen.csv` — 500 rows of a curated database of enzyme kinetic isotope effects (456 rows from
measurements.csv, 44 from rates.csv). Each row is one published value. `error` is the printed ± (empty if the source
prints none). `as_printed`, `location`, `conditions` and `notes` were written by earlier readers of the source and
are the ONLY evidence you may use. You do not have the papers and must not look them up.

For every row decide two things, strictly from what the row itself says:

## error_type — one of
- `none`          the `error` field is empty.
- `sd`            the row says the ± of THIS value is a standard deviation.
- `se`            the row says it is a standard error (standard error of the mean, s.e.m., standard error of a fit).
- `ci95`          the row says it is a 95 % confidence interval/level/limit.
- `other`         the row states another defined meaning (e.g. a range of duplicates, a propagated error whose inputs
                  are of mixed or unnamed type, "relative error under 2 %"). Say which in `evidence`.
- `conflicting`   the row reports that the source gives two different meanings for the same ±.
- `not_stated`    the row explicitly says the source does not say what the ± is.
- `not_recorded`  the row is silent about the meaning of the ±. (Silence is NOT `not_stated`.)

Rules:
1. The statement must be about the ± of the value in this row. A statistic mentioned for some other number
   (a rate constant quoted in the notes, another table, a fit parameter) does not count, unless the row says the
   KIE's error was propagated from those — then code what the row says of the propagated error; if it only names the
   type of the inputs, code that type and write "propagated from …" in `evidence`.
2. If a row says the error is of type X "(Methods)" or "(caption)" or "(footnote)", that counts.
3. When in doubt between a type and `not_recorded`, choose `not_recorded`.

## n_measurements
The number of measurements/experiments behind THIS value as the row states it: an integer (`3`), or with a prefix
when the row says "at least" (`>=6`). Empty if the row does not say, or says it only for something else.
If the row gives experiments and points per experiment (e.g. "at least 3 independent experiments with at least 4
points each"), give the number of independent experiments and put the rest in `evidence`.

## Output
Write `kodierung.csv` in your own directory with the header
`row_id,error_type,n_measurements,evidence`
one line per input row, same order, all 500 rows. `evidence` = the few words of the row you relied on (at most 15
words, quoted from `notes`/`conditions`), empty for `none` and `not_recorded`.
You may use a script for a first pass, but every row with a non-empty `error` must then be checked by reading its
notes; many rows share identical notes, so group them. Report at the end: counts per code, the number of rows you
changed after the first pass, and the row_ids you found hard, with one line each.
