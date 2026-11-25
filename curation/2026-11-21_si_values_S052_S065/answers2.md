# Reader ai-2: answers (S052, S065)

## a. S052: captions, footnotes and units of Tables S2, S3, S4

- **Table S2** (SI p. S3): "Table S2. Temperature dependence of the rate constant for hydride transfer (kH) during catalysis by BsDHFR and its variants at pH 7."
- **Table S3** (SI p. S4): "Table S3. Temperature dependence of the rate constant for deuteride transfer (kD) during catalysis by BsDHFR and its variants at pH 7."
- **Table S4** (SI p. S5): "Table S4. Temperature dependence of the kinetic isotope effect (KIE) on hydride transfer during catalysis by BsDHFR and its variants at pH 7."
- **Footnotes:** each of the three tables has exactly one footnote, inside the table frame: "nd: not determined." There are no other footnotes and no symbols on any cells.
- **Units:** the header over the columns reads "kH (s-1)" in Table S2 and "kD (s-1)" in Table S3, so the unit is s⁻¹. Table S4 is headed "KIE" with no unit. The temperature column is headed "T (ºC)".
- **Header detail:** in Table S3 the last column is printed "BsDHFR-P122EP129D" (no slash). Tables S2 and S4 print "BsDHFR-P122E/P129D". In the CSV this column is still coded P122E/P129D, and the 5 C row of S3 carries a remark about it.

## b. S052: meaning of ± and number of measurements

**Not stated.** The SI (pp. S1–S5) has no statement on the errors. The article's Methods describe only the procedure for kH: "Pre-steady-state kinetic experiments were performed on a Hi-Tech Scientific stopped-flow spectrophotometer." and "To analyze the kinetic data, a single-exponential fit was used." (Kinetic Measurements section). Neither source says whether ± is an SD, an SE or a fit error, or how many shots or repeats were made.

## c. S052: Table S4 KIE at 20 °C compared with Table 5 "KIE (20 °C)" of the article

Table 5 caption: "kH and KIE Values at 20 °C and Activation Parameters for Hydride Transfer Catalyzed by BsDHFR and Its Variants at pH 7".

| enzyme | Table S4, 20 °C | Table 5, KIE (20 °C) | same? |
|---|---|---|---|
| BsDHFR | 3.44±0.17 | 3.44 ± 0.17 | yes |
| L20M | 2.80±0.16 | 2.80 ± 0.16 | yes |
| A104Q | 2.00±0.19 | 2.00 ± 0.19 | yes |
| L20M/A104Q | 1.90±0.08 | 1.90 ± 0.08 | yes |
| P122E | 2.02±0.12 | 2.02 ± 0.12 | yes |
| P129D | 2.05±0.10 | 2.05 ± 0.10 | yes |
| P122E/P129D | 1.89±0.08 | 1.89 ± 0.08 | yes |

All seven values and errors are identical. The kH (20 °C) column of Table 5 is also identical to Table S2 at 20 °C (102±5, 16.7±0.1, 125±8, 19.0±0.1, 84.8±3.7, 86.4±3.8, 92.2±3.3).

## d. S065: caption and footnotes of Table S1; meaning of ±

- **Caption** (SI p. S2), quoted in parts:
  - "Table S1. KIE values for reaction of TaCPa2E with saturating concentrations of CDP-Glc or CDP-[2-2H]Glc in the temperature range of 293.15 - 353.15 K (20-80 °C)."
  - "VH: initial reaction rate of CDP-Glc (min-1) and VD: initial reaction rate of CDP-[2-2H]Glc (min-1). The pH was 7.5."
- **Column headers:** "T (K)" and "KIE (VH VD-1)".
- **Footnotes:** none.
- **Meaning of ±:** the SI does not say for Table S1. The article gives two indirect statements:
  - Methods: "Repeated measurements ( N ≥ 4) at a single saturating substrate concentration gave k cat values determined with high precision. The KIEs ( Table S1 ) were obtained as the ratio of the k cat …"
  - Figure 4 caption, which plots the same KIE against T: "error bars show the associated S.D. ( N = 4)".
- **Conclusion:** ± is most likely the S.D. with N = 4 (Methods say N ≥ 4). This is inferred from the article, not stated in Table S1. How the S.D. of a ratio was propagated is not stated.

## e. S065: Table S1 at 20, 60 and 80 °C compared with Dkcat of Table 1 of the article

| T | Table S1 KIE (VH/VD) | Table 1 Dkcat | Table 1 Dkcat/KM |
|---|---|---|---|
| 20 °C (293.15 K) | 2.20 ± 0.75 | 2.20 ± 0.75 | 2.06 ± 0.67 |
| 60 °C (333.15 K) | 4.29 ± 0.28 | 4.30 ± 0.30 | 3.80 ± 0.40 |
| 80 °C (353.15 K) | 3.34 ± 0.09 | 3.34 ± 0.09 | 3.19 ± 0.24 |

- **Comparison:** the values are identical at 20 and 80 °C. At 60 °C they differ slightly (4.29 ± 0.28 against 4.30 ± 0.30). The article text also gives 60 °C as "4.3 ± 0.3 ( N = 4)" (noncompetitive KIE, Figure S1).
- **Different determinations?** Yes, the source describes two different procedures:
  - Table 1, footnote a: "The KIEs on k cat ( D k cat ) and on k cat / K M ( D k cat / K M ) were obtained by a global nonlinear fit to the data for both isotopologue substrates."
  - Table S1, Methods: "obtained as the ratio of the k cat for enzymatic reaction with the light ( 1 H) and heavy ( 2 H) isotope", from repeated measurements at one saturating concentration (N ≥ 4).
  - Methods also compare the two: "the KIEs on k cat determined from fits of eq 6 to the data were in excellent agreement (± 5%) with the corresponding KIEs determined from (repeated) measurements at a single saturating substrate concentration."
- **Caveat:** the source does not use the words "different determinations". Despite these descriptions, the values at 20 and 80 °C are identical to the last digit, including the errors.
