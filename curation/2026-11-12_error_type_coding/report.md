# Coding of `error_type` and `n_measurements` — 12 November 2026

New fields in `measurements.csv` and `rates.csv` (CURATION.md rule 12). Reason: the reporting standard of the field
(K. Francis and A. Kohen, "Standards for the reporting of kinetic isotope effects in enzymology", Perspectives in
Science 1, 2014) asks that every reported error say whether it is a standard deviation or a standard error, and from
how many measurements. The collection held this only as free text in `notes`.

## What was coded, and from what
All 500 rows (456 isotope effects, 44 rate constants). **No source was read again.** Each coder saw, for every row,
only the fields `value`, `error`, `as_printed`, `location`, `conditions`, `notes` and `doi`, and the task in
`task.md`. The fields therefore say what the collection has recorded about the error, not more.

- **Coder 1 (`ai-1`)** and **coder 2 (`ai-2`)**: two separate runs of the same model, neither saw the other.
  Their files are kept as returned: `coding1.csv`, `coding2.csv` (with the words of the row each relied on).
- Blind is not independent: same model, same rows, same task (rule 2).

## Result (`final_coding.csv`)

| `error_type` | isotope effects | rate constants |
|---|---|---|
| `not_stated` — the row says the source does not say what the ± is | 206 | 0 |
| `not_recorded` — the row is silent | 107 | 0 |
| `se` | 48 | 44 |
| `ci95` | 44 | 0 |
| `sd` | 21 | 0 |
| `none` — no error printed | 15 | 0 |
| `conflicting` | 14 | 0 |
| `other` | 1 | 0 |

`n_measurements` is set in 78 isotope-effect rows and in all 44 rate rows.

For 313 of the 441 isotope effects that carry an error, the collection cannot say what kind of error it is: in 206
because the source, as read, does not say; in 107 because the earlier readings did not record it. The second group
needs the sources to be opened again.
