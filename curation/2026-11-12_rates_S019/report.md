# Rate constants under rule 4b — source S019

12 November 2026. First rows of `data/rates.csv` (CURATION.md rule 4b, added today).

## File read
`bj3940259add.pdf`, supplementary material of Swanwick, Maglia, Tey and Allemann, Biochem. J. 2006, 394, 259
(doi:10.1042/bj20051464), from PubMed Central (PMC1386024) on 12 November 2026;
SHA-256 `ce306b477e92be27598eb7228d0682fc4d5b815bc4d9dd82344356f0ae1ac9ad`. The KIE columns of the same tables
were read and entered earlier today (`curation/2026-11-12_si_reading_S013_S019_S040_S041/`).

## The two readings
- **First reading (`ai-1`)**: from the text of the file (`pdftotext -layout`), 44 rate constants, `reading1_rates.csv`.
- **Second reading (`ai-2`)**: a separate run of the same model, which did not see the first reading or the tables
  of the collection; it read the text and page images at 200 dpi and reports that both agreed for every value.
  44 rate constants, `reading2_rates.csv`, as returned.
- Blind is not independent: both readings were made by the same model from the same file (rule 2).

## What the tables contain
- **Table 1**: "pre-steady state kinetic parameters at pH 7.0 for the reaction of NADPH and H2F catalysed by DHFR
  from E. coli", kH and kD in s-1 at 5 to 40 °C in steps of 5 °C: 16 values.
- **Table 2**: "steady state rates … for the reaction between NADPH/NADPD and H2F catalyzed by DHFR at pH 9.5",
  Rate (NADPH) and Rate (NADPD) in s-1 at 5 to 35 °C: 14 values.
- **Table 3**: "pre-steady state kinetic parameters at pH 7.0 … catalysed by G121V-DHFR", kH and kD in s-1 at 5 to
  35 °C: 14 values.
- All three captions: "All data points are the average of at least 6 measurements. The errors are standard errors
  of the mean (for one sigma)."

## Rows written
44 rows, R0001–R0044 (`rows_entered.csv`), all `verified`. No person has checked these rows.
`tools/validate.py`: in all 22 table rows the ratio of the two rate constants reproduces the isotope effect held
for the same step, quantity, pH and temperature within 10 %.
