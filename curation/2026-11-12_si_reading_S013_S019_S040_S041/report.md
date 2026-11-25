# Reading of supporting information under rule 4a — sources S013, S019, S040 and S041

12 November 2026. Second batch of values from supporting information (CURATION.md rule 4a).

## Files read
All from PubMed Central on 12 November 2026, as deposited there with the author manuscript or the article;
whether they are identical to the publishers' files was not checked.

| source | doi | file | PMC | SHA-256 |
|---|---|---|---|---|
| S013 | 10.1021/bi0518242 | `NIHMS63864-supplement-1si20051208_05.doc` | PMC2553318 | `4348f43ee703fb361aed3d90001b4821dd0a8c62cb8f680b86ac247d9a8ea0db` |
| S013 | 10.1021/bi0518242 | `NIHMS63864-supplement-2si20051208_05.pdf` (same content as the `.doc`) | PMC2553318 | `9b2d1cc971cc17b625e0a86caf89513a2b4361dccd1996f9760593b8b84422c5` |
| S019 | 10.1042/bj20051464 | `bj3940259add.pdf` | PMC1386024 | `ce306b477e92be27598eb7228d0682fc4d5b815bc4d9dd82344356f0ae1ac9ad` |
| S040 | 10.1021/ja400761x | `NIHMS476305-supplement-1_si_001.pdf` | PMC3674108 | `474a009af597a1cf268bb45c36c21a6a7b85e4290b7a78180bc27ceb57ac7c20` |
| S041 | 10.1021/ja103010b | `NIHMS217094-supplement-1_si_001.pdf` | PMC2912445 | `1473504006912e7de3c5112a4f1b84e1f79e566a0a9aa3237328ebdde3a38c14` |

## The two readings
- **First reading (`ai-1`)**: from the text of the files (`pdftotext -layout`; the `.doc` converted to PDF first).
  87 values, kept as `reading1_si.csv`.
- **Second reading (`ai-2`)**: a separate run of the same model, which did not see the first reading or the tables of
  the collection. It read each file from the extracted text and from page images at 200 dpi and reports that both
  agreed for every value. 112 values, because it transcribed both S013 files; kept as `reading2_si.csv`, as returned.
- Blind is not independent: both readings were made by the same model from the same files (rule 2).

## What the files contain
- **S013** (DHFR G121V): Table 1S observed H/T and D/T on V/K, Table 2S intrinsic H/T, H/D, D/T, each at 5–45 °C
  (printed from 45 down to 5 °C). Table 3S repeats the Arrhenius parameters of the article with standard errors and
  with 95 % confidence intervals; not entered (the parameters are in the collection from the article).
- **S019** (DHFR wild type and G121V): Table 1 pre-steady-state kH, kD and KIE at pH 7.0, 5–40 °C; Table 2
  steady-state rates and KIE at pH 9.5, 5–35 °C; Table 3 pre-steady-state kH, kD and KIE of G121V, 5–35 °C.
  Only the KIE columns are isotope effects; the rate constants have no field in the collection and are not entered.
- **S040** (thymidylate synthase, hydride transfer, 50 mM MgCl2): Table S2 observed H/T and D/T on kcat/KM,
  intrinsic H/T, H/D and D/T, and the commitment Cf, at 5, 15, 25 and 35 °C. Footnote a: "The intrinsic H/T KIE is
  numerically solved from Eq 8 in the main text, and the intrinsic H/D and D/T KIEs are calculated from the intrinsic
  H/T KIE using the Swain-Schaad relationship." Cf is not an isotope effect and is not entered.
- **S041** (thymidylate synthase, proton transfer): Table S1 observed H/T and D/T on V/K, Table S2 intrinsic H/T,
  H/D and D/T (Northrop's method, errors at the 95 % confidence level), at 5, 15, 25 and 35 °C.

## Rows written
80 rows in `measurements.csv`, M0348–M0427 (`rows_entered.csv`): S013 24, S019 17, S040 19, S041 20.
Seven of the 87 values were already in the collection from the articles themselves and were not entered a second
time (see `resolution.md`, point 1). All 80 rows are `verified`: both readings produced each value and agree.
No person has checked these rows.
