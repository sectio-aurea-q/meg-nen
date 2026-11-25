# Reading of supporting information under rule 4a — sources S014 and S026

12 November 2026. First entry of values from supporting information (CURATION.md rule 4a, added the same day).

## Files read
| source | article | file | obtained | SHA-256 |
|---|---|---|---|---|
| S026 | Bandaria, Cheatum, Kohen, J. Am. Chem. Soc. 2009, 131, 10151–10155, doi:10.1021/ja902120t | `NIHMS132597-supplement-1_si_001.pdf` (3 pages) | PubMed Central, PMC2746013, supplementary material of the author manuscript, 12 November 2026 | `8de465300ffc3248214b3ac4743109c5e28166c1bf12c8c9ab098d6dff6aee02` |
| S014 | Wang, Goodey, Benkovic, Kohen, Phil. Trans. R. Soc. B 2006, 361, 1307–1315, doi:10.1098/rstb.2006.1871 | `rstb20061871s01.doc` (1 page of content) | PubMed Central, PMC1647312, electronic supplementary material, 12 November 2026 | `17b412d194a48888a0afc64d71a03efa3187c6b8706f37f985c756fdb10cfb94` |

The S026 file is the supplement deposited with the author manuscript in PubMed Central, not a download from the
publisher's site; whether the two are identical was not checked.

## The two readings
- **First reading (`ai-1`)**: from the text of the files (`pdftotext -layout` for the PDF, text export of the
  `.doc`), 12 November 2026, 07:13. Kept as `reading1_si.csv`.
- **Second reading (`ai-2`)**: a separate run of the same model, which did not see the first reading or the tables
  of the collection. It read each file twice, from the extracted text and from page images at 200 dpi, and reports
  that both agreed everywhere. Kept as `reading2_si.csv`, as returned.
- Blind is not independent: both readings were made by the same model from the same files (rule 2).

## What the files contain
- S026: Table S1 (an HPLC gradient, not entered); Table S2, "Observed V/K KIEs (with the standard deviation)",
  H/T and D/T at 5, 15, 25, 35, 45 °C; Table S3, "Intrinsic KIEs presented in Figure 4 in the main text",
  H/T, H/D and D/T at the same temperatures, with the note "calculated using the Northrop's method as described in
  the text. Reported errors are from all combinations of H/T and D/T observed KIEs for each temperature point.
  Errors were calculated at the 95% confidence interval."
- S014: Table 1, "Observed V/K KIEs", H/T and D/T at 5–45 °C; Table 2, "Intrinsic KIEs", H/T, H/D and D/T at the
  same temperatures. Neither table says what the ± is or how the values were calculated.

## Rows written
50 rows in `measurements.csv`, M0298–M0347 (`rows_entered.csv`): S026 25 (10 observed, 15 intrinsic),
S014 25 (10 observed, 15 intrinsic). All are `verified`: both readings produced each value and agree.
No person has checked these rows.
