# Sources read again for open point 3 — 19 November 2026

## Why

On 18 November 2026 two referees of an analysis of the collection (internal review) listed rows whose fields could not
be filled from the row alone: the label, buffer, pH and fitted range of the lipoxygenase series coded `nd`, the
origin of slope and single value in T0133 and T0134, the buffer of the POR series, the label of T0069 and T0070,
the fitted range of T0103, and whether the wild-type MoLOX value (M0247) belongs to its source (rule 1).

## How

Seven questions (`questions.md`) were put to the main text of seven sources (S022, S033, S051, S057, S058, S059,
S060) by two readers blind to each other (`reading1.md`, `reading2.md`). The readers are runs of the model, as
before. They read the PMC full text held by the curator: main text, tables with footnotes, figure legends, Methods.
No supporting information was read.

## Result

The two readings agree on every question. Nothing they found contradicts a value of the collection.

| question | rows | both readings |
|---|---|---|
| Q1, S057 | T0115–T0120 | heavy substrate, buffer and pH not in the main text (SI); fits 10–45 °C; Dkcat at 30 °C; all six rows are of this work |
| Q2, S058 | T0121–T0132 | substrate only "D-LA"; buffer and pH not in the main text (SI); fits 15–35 °C, five temperatures |
| Q3, S059 | T0133, T0134 | heavy substrate, buffer, pH and fitted range not in the main text (SI); Dkcat at 303 K; footnote *: the temperature-dependent kinetics were reported in ref. 35 and analysed for Ea and ΔEa here; footnote †: kcat and Dkcat from this work. Slope and single value therefore need not come from one set of measurements |
| Q4, S022 | T0035–T0046 | buffer and cryo-solvent of the hydride-transfer measurements not in the main text ("as described previously", ref. 12); whether the solvent is the same above and below −27 °C is not stated; Table 1 at 25 °C |
| Q5, S033 | T0069, T0070 | the source contradicts itself: the Fig. 3 legend names perdeuterated D31-LA, Table 2 footnote b names 11,11-D2-LA, and the Ea(D) of Table 2 reproduce the ΔEa quoted from Fig. 3; Methods name both substrates |
| Q6, S051 | T0103, M0202 | fitted range not in the main text (SI); the fall of the KIE below 5 °C (1.98 ± 0.13 at 1 °C, not shown) stands with the steady-state series at pH 9, the series T0103 belongs to |
| Q7, S060 | M0247 | the WT row carries no reference footnote (only PNG and ENDO do), the table never says "this work", and the text credits Dkcat ≈ 70 and Ea 9–10 kcal/mol of WT to ref. 26 |

## What changes in the collection

- T0069 and T0070: `heavy_other` from 30 to `nd`, and `labelled_position` now names both statements of the source.
  Until now the rows followed the figure legend. Both readings find the contradiction unresolved in the main text;
  by rule 13 a count the reading does not allow is `nd`. `changes.csv` lists the four cells.
- No other field changes. For Q1–Q4, Q6 and Q7 the rows already say what the main text says; this reading confirms
  their notes by a second, blind pair of readers.

## Still open — it needs the supporting information or another paper

1. S057, S058, S059: heavy substrate (positions), buffer and pH; S059 also the fitted range. Until then
   T0115–T0134 stay `nd`.
2. S022: the buffer and cryo-solvent of the hydride-transfer measurements (ref. 12 of the source).
3. S051: the fitted range of both series.
4. S033: which substrate the Arrhenius series used; only the authors or the SI can say.
5. S060: whether the WT row was measured again; ref. 26 has to be compared (rule 1).

Seen on the way, outside the questions: S059 footnote † prints for WT the same four numbers as the WT row of S057
Table 1; S060 defines ΔEa in the Discussion with the opposite sign to footnote c of its Table 1 (the collection
follows the footnote); S058 Table 1 prints 208 K for L754A where the other rows have 288 K.
