# Supporting information of S058 read — 19 November 2026

## Why

The SI of S058 (Hu et al. 2016, Angew. Chem., 10.1002/anie.201603592) was the one file the round of this afternoon
(`curation/2026-11-19_si_reading_open_point_3/`) could not obtain. The curator downloaded it from PMC
(NIHMS817928-supplement-Supporting_Information.docx). It decides the label, buffer and pH of T0121–T0132.

## How

One set of questions (`questions.md`), two readers blind to each other (`reading1.md`, `reading2.md`); the readers
are runs of the model. They read the text of the .docx (tables included). They agree on every point.

## Result

- Heavy substrate: perdeutero linoleic acid (D-LA), isolated from algal fatty acid methyl esters (Cambridge Isotope
  Laboratories, U-D 97–98 %). No single position is named.
- 0.1 M borate, pH 9.0; the pH falls by about 0.3 up to about 1 kbar, which the source neglects. The kinetics
  section itself does not name the assay buffer; it follows from the neighbouring sections.
- 15, 20, 25, 30 and 35 °C at each of 1, 344, 688 and 1034 bar, as the rows already say.
- Ea from Arrhenius fits weighted by the errors of kcat; ΔEa = Ea(D) − Ea(H). The temperature of the Dkcat of
  Table 2 and an iron correction are not stated.

## What changes (`changes.csv`)

T0121–T0132 (the collection holds no single value of this source): `heavy_other` nd → 30, `pH` → 9.0,
`labelled_position` filled, a note added. No value, error or status changes.

## Not entered yet

SI Tables S3 (WT), S4 (I553V) and S5 (L546A) print kcat(H), kcat(D) and Dkcat with errors at five temperatures and
four pressures each: 60 isotope effects and 120 rate constants that rule 4a and 4b allow to enter. They need
their own two readings of the numbers. Both readers recomputed the tables and found three cells that do not agree
with the printed rates (Table S5, L546A, 293 K, 1 bar and 344 bar; Table S1, WT, 308 K, 1034 bar).
