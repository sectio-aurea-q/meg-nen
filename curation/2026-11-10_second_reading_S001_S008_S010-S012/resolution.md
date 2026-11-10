# Second reading of S001, S008, S010, S011 and S012 (10 November 2026)

First reading `ai-1`, second reading `ai-2`. These are five of the eight papers that the first source list had
marked as closed: the temperature dependence of the isotope effect on kcat in soybean lipoxygenase-1 and three
active-site mutants (S001), the intrinsic primary and the secondary isotope effects of the hydride transfer in
*E. coli* dihydrofolate reductase (S008), the Arrhenius prefactor ratios of a thermophilic alcohol dehydrogenase
above and below its 30 °C transition (S010), the observed and intrinsic H/T and D/T effects of the hydride transfer
in *E. coli* thymidylate synthase (S011), and the primary and secondary H/T and D/T effects of yeast alcohol
dehydrogenase (S012). The papers reached the author on 10 November 2026 as PDFs, on request, from the groups of two of the
corresponding authors; they are the published versions. S012 is a scan without a text layer and was read from page
images by both readers; for the other four, both readers checked every number against a page image as well as the
text layer. The supporting information was not read. The second reader worked from the PDFs alone, did not see the
first reading or the tables of the collection, and looked up UniProt and RCSB PDB for the enzymes. Files in this
folder:

- `reading2_measurements.csv`, `reading2_temperature.csv`, `reading2_enzymes.csv`, `report.md`: the second reading as
  delivered (`report.md` saved by the curator from the second reader's answer; shortened as it says)
- `comparison.md`: row-by-row comparison of both readings, before the decisions below

## Result

All 16 isotope effects and all 16 temperature series of the first reading have a partner in the second reading, and
every number agrees: value and error, prefactor ratio, ΔEa and their errors, temperature, pH, effect type, isotope
pair, quantity, method and kind. Four series differed in a field other than these numbers, and the second reading
held 14 further rows. Of the 32 rows, 28 are entered, all `verified`: M0284–M0297 and T0154–T0167. Four are not
entered (decision 1).

A first settlement of this block, made on the morning of 10 November and kept in the archive
`MEG-NEN_2026-11-10_10-44.zip`, had entered all 32 rows and held four of them at `single`. Two referee readings of
the note and the archive the same day led to the decisions below; the row numbers of that archive (M0284–M0299,
T0154–T0169) are therefore not those of the collection.

## Decisions

1. **S001, the rows WT-SLO and Leu546→Ala of Table 1: not entered (rule 1).** Both readings produced the two
   isotope effects and two series and agree on every number: KIE 81 (5) and 93 (9); Eact 2.1 (0.2) and 4.1 (0.4);
   ΔEact 0.9 (0.2) and 1.9 (0.6); AH/AD 18 (5) and 4 (4). Footnote e of the table sits on these two row labels and
   cites Rickert & Klinman, Biochemistry 1999, 38, 12218–12228. Rule 1 does not enter a value that a paper
   attributes to other work, and the collection has applied it to a citation mark of this kind before without
   reading the cited paper (S027: T0059 and T0060; S041–S045). The evidence within S001 points both ways. For the
   attribution: the Introduction gives "KIE on kcat (Dkcat = 81)" with a citation of that paper, which is the value
   of the WT row, and the Methods say that the "data for Leu546→Ala appeared in an earlier publication … but were
   not analyzed in detail for effects on the primary tunneling events". Against a plain reprint: the Introduction
   quotes Eact = 2.2 kcal/mol where Table 1 prints 2.1 (within the printed error of 0.2), the Methods describe a
   correction for subsaturating O2 applied in this work to WT-SLO and Ile553→Ala, and the Arrhenius parameters of
   Leu546→Ala may be a new analysis of the earlier data. That cannot be settled without the earlier paper. The rows
   are left out, the earlier paper is added to the reading list as S066 (not yet obtained), and the rows for
   Leu754→Ala and Ile553→Ala, which carry no footnote, say in `notes` that the other two were not entered.
2. **S012, individual experiments (14 rows only in reading 2): not entered.** Tables 2 and 3 print three or four
   experiments per effect and, starred, their average with its standard deviation. The collection holds the four
   averages (M0294–M0297) and lists the experiments in `notes`. Entering both would put the same measurements into
   the tables twice; where another source prints averages over several preparations (M0079), the collection also
   holds the average. Rule 4 now says so.
3. **S011, range and number of temperatures (T0165, T0166): 5–40 °C, four temperatures**, as in reading 2. The
   Results name 5, 20, 30 and 40 °C and the temperature axis of Fig. 2 prints 40, 30, 20 and 5; the Abstract says
   5–45 °C, which the body of the paper does not bear out. `notes` record the conflict.
4. **S010, ΔH‡ of the light isotope (T0163, T0164): not put into `Ea_light_kcal`**, as in reading 2. The values
   (23.6 ± 0.6 and 14.6 ± 0.3 kcal/mol at 30 °C) are enthalpies of activation. The Methods fit Arrhenius plots and
   the table reports the slopes as enthalpies, so these two rows are not counted as Eyring analyses.
5. **S008, the corrected secondary effects (M0289, M0290): `intrinsic`.** The source reports them as "corrected
   for the commitment" and calculates from them what it calls "an intrinsic 2° H/D KIE"; the word is not used of the
   two numbers themselves. Both readers entered them as intrinsic and flagged the call. Rule 5 now says that a value
   the source reports as corrected for the commitment is intrinsic, and `notes` quote the sentence.
6. **S008, values the source calculates (M0286, M0291): entered and marked.** The intrinsic primary H/D effect of
   3.5 ± 0.2 and the intrinsic secondary H/D effect of 1.13 are not measured with H against D; the source calculates
   them from its H/T and D/T effects and reports them as intrinsic effects of the step. The collection holds many
   intrinsic effects obtained by Northrop's method in the same way. `notes` say "calculated by the source, not
   measured", and rule 4 now distinguishes such values from a calculated prediction printed beside a measurement
   (the (kH/kT)calc columns of S012), which is not entered.
7. **S012, pH of the series (T0167): left empty.** The table captions give pH 8.5 for the 25 °C measurements; for
   the 0–40 °C series the source states none (its note 34 says only that the relation is similar to Table 2). Where
   another source stated no pH for the assays concerned (S031), the field was left empty too.
8. **Enzymes.** S001, S008 and S011 use enzymes already in the collection; nothing in those rows was changed. Two
   rows are new. `HTADH_GEOSE_WT`: both readings give the same enzyme, organism and strain (LLD-R); the accession
   P42328 and the entry 1RJW are from the second reading and are the ones the variants of this enzyme already
   carry. `YADH_YEAST_WT`: the source says only "yeast alcohol dehydrogenase", a commercial preparation; both
   readings agree on that. The second reader presumed *S. cerevisiae* ADH1 (P00330), which is not a statement of
   the source; `uniprot` and `ec` are left empty, `organism` says that the source names no species, and `notes` record the presumption.
9. **`as_printed`.** The first reading had abbreviated three kinds of entry ("A ratio" for AH/AT, "dEact" for
   ΔEact, kcal/mol for kcal mol−1) and reordered the sentence of S011; they now follow the print.

## Noted, nothing to decide

- **S001, Leu754→Ala.** The printed series gives 83 at 30 °C where the table prints a KIE of 112 (11). Both readers
  re-read the digits on the page image. The prefactor ratio is printed with one digit and an error as large as
  itself, "3 (3)"; a ratio of 4 would give 111. The row passes the convention check of `tools/validate.py`.
- **S001, transfer.** The source speaks of hydrogen-atom abstraction; the second reading wrote `H_atom`. The steps
  of soybean lipoxygenase-1 were already in the collection as `PCET`, from S002 and S016, and were not changed.
- **S008.** The observed primary V/K effects, H/T = 4.81 ± 0.06 and D/T = 1.65 ± 0.01, are printed for "a
  temperature range from 45 to 15 °C" and not for one temperature; under rule 11 they are not entered. The range of
  the intrinsic series, 5–45 °C, is not printed as such: it is put together from temperatures the text states, and
  `notes` say so. The sign of ΔEa is not defined in the source and was established by recomputation.
- **S012.** The Fig. 3 legend of the scan reads "3/3 kJ/mol"; the running text prints 3.3 ± 1.3 kJ/mol, and the
  series reproduces the ratio of the printed H/T and D/T effects (4.16 against 4.12 at 25 °C). The H/D series is
  itself obtained by the source from its H/T and D/T fits. The primary and secondary H/D effects of note 28 (3.9
  and 1.2 at 25 °C) are inputs to a correction, printed without origin, method or rate constant, and are not
  entered.
- **Convention check.** With the new rows `tools/validate.py` compares 64 series/value pairs (59 before); all agree
  within a factor of 3.
