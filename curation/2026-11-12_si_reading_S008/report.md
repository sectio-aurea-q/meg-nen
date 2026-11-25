# Reading of supporting information under rule 4a — source S008

12 November 2026. Third batch of values from supporting information (CURATION.md rule 4a).

## Files read
Supporting information of Sikorski et al., J. Am. Chem. Soc. 2004, 126, 4778–4779 (doi:10.1021/ja031683w), fetched
from pubs.acs.org by the curator on 12 November 2026. Three files, two pages each, same wording, same two tables,
same 30 values; they differ in rendering only.

| file | SHA-256 | remark |
|---|---|---|
| `ja031683w_si_001.pdf` | `94519983be2dea459ed1fbc84f27f07f949b492664494ddd04c8905a244710be` | ± printed correctly; the one transcribed |
| `ja031683w_si_002.pdf` | `a08409506fc42297f903072499a2e128c676084b5af86e7072ae3db0afd6d2ed` | ± rendered as an en dash, "2°" as "2ß" |
| `ja031683w_si_002-2.pdf` | `4dd9b101820fc848879cf7fed57e0d30b3a8bd21f26828c7abbd91e1c6f5cd55` | as `_002`, with a download stamp in the margin |

## The two readings
- **First reading (`ai-1`)**: from the text of the files (`pdftotext -layout`). 30 values, kept as `reading1_si.csv`.
- **Second reading (`ai-2`)**: a separate run of the same model, which did not see the first reading or the tables of
  the collection. It read each of the three files from the extracted text and from page images at 200 dpi and reports
  that both agreed for every value and that the three files agree. 30 values, kept as `reading2_si.csv`, as returned.
- Blind is not independent: both readings were made by the same model from the same files (rule 2).

## What the files contain
- Conditions: "All experiments were performed in MTEN Buffer (50 mM MES, 25 mM TRIS, 25 mM EtOH-NH2 and 100 mM NaCl)
  at pH = 9.0, 70 µM NADPH, and a 200 fold excess of H2F. The pH was adjusted at the experimental temperature".
  The µ is present only in the text layer of the first file; no page image shows it.
- **Table 1**, "Observed V/K KIEs": observed D/T and H/T at 45, 35, 25, 15, 10 and 5 °C. "For 1° KIE (Table 1) all
  data points are from at least 3 independent experiments with at least 4 points from each experiment." What the ±
  is, the file does not say.
- **Table 2**, "Intrinsic KIEs calculated using the Northrop method": intrinsic H/T, H/D and D/T at the same six
  temperatures. Footnote a: "Reported errors are from all combinations of H/T and D/T observed KIEs for each
  temperature point. Errors were calculated at the 95% confidence interval."
- On the method: "The Northrop procedure assumes that the reaction has no reverse commitment (or that EIE=1) and that
  the Swain Schaad relationship holds for intrinsic 1° KIEs even if tunneling is involved." The exponent is 3.34.
- In the running text: the observed secondary D/T KIE 1.058 ± 0.003, already in the collection from the article (M0288).

## Rows written
29 rows in `measurements.csv`, M0428–M0456 (`rows_entered.csv`): 12 observed (Table 1), 17 intrinsic (Table 2).
One of the 30 values was already in the collection from the article and was not entered a second time (M0286; see
`resolution.md`, point 1). All 29 rows are `verified`: both readings produced each value and agree.
No person has checked these rows.

## Checks made on the entered values (not entered anywhere)
- Weighted Arrhenius fits of the six intrinsic values give AH/AT 7.4, AH/AD 4.0, AD/AT 1.8 and Ea(heavy) − Ea(light)
  of −0.11, −0.07 and −0.02 kcal/mol; the article prints 7.4 ± 4, 4.0 ± 1.5, 1.8 ± 0.3 and −0.1 ± 0.3, −0.07 ± 0.2,
  −0.03 ± 0.09 (T0156–T0158). The table is the one behind the article's fit.
- ln(H/T)/ln(D/T) of the intrinsic values is 3.33–3.36 at five temperatures, as the method prescribes, and 3.18 at
  10 °C, where the three printed values also do not multiply up (3.72 × 1.75 = 6.51 against 5.91). Entered as printed.
- A quadratic term in 1/T is not resolved in any of the three intrinsic series (0.2 to 0.4 standard errors).
