# Second reading of S046–S050 (8 November 2026)

First reading `ai-1`, second reading `ai-2`. These five papers are block 2 of the second reading list: the hydride
transfer of two thymidylate synthase variants and of E. coli and human dihydrofolate reductase variants. Both readers
worked from the PMC pages of the papers, saved on 8 November 2026 (S046, S047 and S049 as author manuscripts, S048
and S050 as publisher versions); the published PDFs and the supporting information were not read. The saved pages
lost the equations, which PMC renders with MathJax or shows as images, so both readers also had the PMC XML of the
same five manuscripts and used it only for those; no number was taken from it. The equations of S048 and S050 are
images in both; the curator read them from the images on the PMC page. The second reader worked from these files
alone, did not see the first reading, and looked up UniProt and RCSB PDB again for every enzyme. Its instructions
repeated the rules of CURATION.md and SCHEMA.md, allowed the web only for these lookups, and asked it to treat an
isotope-labelled ("heavy") enzyme as a construct of its own. Files in this folder:

- `reading2_measurements.csv`, `reading2_temperature.csv`, `reading2_enzymes.csv`, `report.md`: the second reading as
  delivered (`report.md` saved by the curator from the second reader's answer; the list of its output files was
  shortened)
- `comparison.md`: row-by-row comparison of both readings, before the decisions below

## Result

All 11 isotope effects and all 13 temperature series of the first reading have a partner in the second reading, and
all of them agree in value, error, temperature, temperature range, pH, quantity, method and kind; neither reading
has rows the other lacks. Both readings give the same UniProt entry, EC number, variant and PDB entries for all 13
enzymes. Both readers left out the same values: everything the papers mark as taken from other work (the wild-type
columns and rows of S046 Tables 2 and 4, S047 Table 1, S048 Table 3, S049 Table 1 and S050 Table 2, the l-DHFR Dkhyd
of S048 and the E. coli columns of S049), the heavy-enzyme ratios of S048 (h-KIE, light over heavy enzyme, which
SCHEMA.md excludes), the QM/MM KIEs of S046, the DADs fitted to a tunnelling model, and the per-temperature KIEs and
commitments, which stand only in figures and the supporting information. Decisions:

1. **Wild-type human DHFR in S049 and S050 (left out by both readers):** S049 says that the wild type was measured
   with the mutants, but its Fig. 2 legend gives ref. 44 for the wild-type data, and S050 gives ref. 2 for the same
   row. Both refer to S037 (Francis et al. 2016), whose values (A_H/A_T 6.6 ± 0.8, ΔEa −0.1 ± 0.1 kcal/mol, pH 9.0)
   are already T0078 and equal the printed ones. Nothing is added.
2. **Signs of ΔEa:** all values are entered as printed and read as Ea(heavy) − Ea(light), the same way by both
   readers. S046: Eq. 2 in the XML has exp(ΔEa,T−H/RT), the text writes ΔEa,T-H; the Table 2 row reads ΔEa,H-T.
   S047: the row label reads ΔEaT-H; the paper prints no Arrhenius equation. S049: the text defines ΔEa(T-H) as
   Ea(T) − Ea(H). S048 and S050: the equations as printed (images) have exp(−ΔEa/RT), which would invert the sign;
   with A_H/A_T far below 1 (S048 5–25 °C, S050 F32M and F32L) only Ea(T) − Ea(H) gives a normal KIE.
3. **Dkhyd of the heavy enzyme (S048, M0200):** both readings enter 25 °C, from the title of Table 2, and pH 9, from
   the Methods, although the same title says pH 7: the intrinsic KIEs come from the competitive experiments, which
   ran at pH 9.
4. **Heavy E. coli DHFR (S048):** entered as its own enzyme row, `DHFR_ECOLI_HEAVY`, like the heavy human enzyme of
   S037; the light enzyme (l-DHFR) is the wild type, and its Dkcat and Dkburst go to `DHFR_ECOLI_WT_NADPH`.
5. **Steps:** twelve new steps, all hydride transfers. Both readings name the same donor and acceptor; the wording
   of the existing TS and DHFR steps is kept (reading 2: "MTHF C6", "exocyclic methylene C7 of intermediate E",
   "DHF C6"). The si face stays a statement of S013 and S015.
6. **PDB entries:** both readings find 4QLE for I14A (it cites another paper) and no entry for the other eleven
   variants. From the second reading the notes now also name the entries the papers show: 1TRG and the N177A entry
   1BQ1 (S046 Fig. 1), 1RX2 (S047, S048, S049) and 1RX4 (S048); the curator checked at RCSB that 1RX2 and 1RX4 carry
   D37 where P0ABQ4 has N37.
7. **Judgement calls made the same way by both readers:** the temperatures of S046 Table 4, printed as 278 to
   308 K, entered as 278.15 to 308.15 K from the Methods (5, 15, 25 and 35 °C); four temperatures and pH 7.5 for
   S046 from the Methods; no temperature range, number of temperatures or pH for S047 and no temperature range for
   S049 and S050, none being stated in the main text; Dkburst of S048 as `single_turnover`; the Table 2 value of the
   S050 triple mutant (± 0.2) rather than the text's ± 0.05.

## Inconsistencies inside the papers

None of them changes an entered value. All were checked by the curator in the HTML, the XML or the images.

- **S046:** the Table 2 row reads ΔEa,H-T, Eq. 2 and the text ΔEa,T-H. The N177D parameters of Table 2 and its
  intrinsic KIEs in Table 4 fit together (about 23 at 278 K and 15 at 308 K).
- **S047:** the * in the row label ΔEaT-H* is not explained.
- **S048:** Eq. 2 as noted in point 2; the title of Table 2 says pH 7 for the Dkhyd column, whose values come from
  experiments at pH 9; at 25 °C, where both fits of Table 3 meet, the 5–25 °C parameters give a KIE of about 10, the
  25–45 °C parameters about 6.6 and Dkhyd 3.88 by the Swain–Schaad relation of the Methods about 7; the DAD error
  ± 0.0008 Å of Table 3 looks misprinted (not entered).
- **S049:** the text says the wild type was measured in this study, while the Fig. 2 legend cites ref. 44 for it
  (point 1); the text and the Fig. 2 legend name the panels the other way round; the text writes "S14V" for S145V
  and prints the definition of ΔEa(T-H) with unbalanced brackets.
- **S050:** the printed F32L parameters (A_H/A_T 0.1 ± 0.1, ΔEa 6.5 ± 0.3 kcal/mol) give a KIE of about 6 × 10^3 at
  25 °C, so one of them is misprinted; the Abstract writes F28, F28M and F28L for F32, F32M and F32L (residue 28 of
  P00374 is Leu); for the triple mutant the text gives ΔEa −0.01 ± 0.05 kcal/mol and a DAD of 3.09 Å, Table 2
  ± 0.2 and 3.10 Å; the text cites Table 1 for values of Table 2; the Fig. 2 legend writes F3M; the text dates the
  F32M form to about 797 million years ago, Table 1 the F32 event to about 499; the Introduction speaks of deleting
  26PP while the variant is named Δ26-PPLR, so which residues the deletion removes is set by SI Table S1 (not read).

## SCHEMA.md

No change.

All 11 isotope effects, all 13 temperature series, the 12 new enzyme rows and the 12 new steps of S046–S050 are now
`verified`.
