# Second reading of S056–S060 (9 November 2026)

First reading `ai-1`, second reading `ai-2`. These five papers are block 4 of the second reading list: the C–H
activation of soybean lipoxygenase-1, in three double mutants of its substrate pocket (S056), in mutants of the
surface residue Y317 and of S749, which hydrogen-bonds to it (S057), under hydrostatic pressure up to 1034 bar
(S058) and in the network residues I552 and V750 (S059), and of the lipoxygenase of the rice-blast fungus
Magnaporthe oryzae with and without its sugar chains (S060). Both readers worked from the PMC pages of the papers,
saved on 9 November 2026 (S056, S057 and S059 as publisher versions, S058 and S060 as author manuscripts); the
published PDFs and the supporting information were not read. Both readers also had the PMC XML of the same five
manuscripts; the equations of S056 and S057 are images in the XML as well, and the only thing the XML added were the
two equations of S059, which hold no values. No number was taken from it. The second reader worked from these files
alone, did not see the first reading, and looked up UniProt and RCSB PDB again for every enzyme. Its instructions
repeated the rules of CURATION.md and SCHEMA.md and allowed the web only for these lookups. Files in this folder:

- `reading2_measurements.csv`, `reading2_temperature.csv`, `reading2_enzymes.csv`, `report.md`: the second reading as
  delivered (`report.md` saved by the curator from the second reader's answer; the list of its output files was
  shortened)
- `comparison.md`: row-by-row comparison of both readings, before the decisions below

## Result

All 29 isotope effects and all 23 temperature series of the first reading have a partner in the second reading, and
all of them agree in value, error, temperature, temperature range, number of temperatures, pH, quantity, method,
kind and isotope type. Both readings give the same UniProt entry, variant and PDB entries for all 8 new enzymes and
for the 6 existing SLO-1 variants these papers measure, and they name the same donor and acceptor atoms. Both
readers left out the same values: everything the papers take from other work (six of the seven rows of S056 Table 1,
the PNG and ENDO rows of S060 Table 1, the wild-type row of S059 Table 1, the earlier wild-type values quoted in
S057 and S059), the ratios of rate constants at pressure to ambient pressure in S058 Table 1 (which are not isotope
effects), the Arrhenius prefactors printed as A_H or ln A_H, the Eyring and free-energy rows, the hydrogen-exchange
and Stokes-shift activation energies, and everything that stands only in a figure or in the supporting information.
Decisions:

1. **Recollected wild type of S059 (second reading only, left out):** footnote † of S059 Table 1 gives kcat 359 (7)
   s−1, Dkcat 57 (2), Ea 2.4 (0.2) and ΔEa 1.1 (0.1) kcal/mol for the wild type, "recollected using the enzyme
   preparation of the present study". All four numbers are identical to the wild-type row of S057 Table 1, which
   S059 cites as its ref. 5 and which is entered as M0239 and T0115. The second reading entered them again and
   flagged the duplicate; they are left out, so the measurement is counted once. The notes of M0245, M0246, T0133
   and T0134 say so.
2. **Signs of ΔEa:** every paper of this block defines ΔEa = Ea(D) − Ea(H), the direction of this database, so all
   values are entered as printed, the same way by both readers: S056 in the text ("E a (D) – E a (H) = 3.5
   kcal/mol"), S057 in footnote d, S058 in footnote b, S059 in the text and S060 in footnote c. S060 is the one
   paper that contradicts itself: its Discussion once writes ΔEa = Ea(H) – Ea(D), against its own footnote. The
   footnote is followed, because the negative values of the table then mean a KIE that rises slightly with
   temperature, as the paper describes.
3. **Wild-type MoLOX of S060 (entered, flagged):** the wild-type row of Table 1 carries no source footnote, while
   the PNG and ENDO rows carry refs. 26 and 25, but the text credits "Dkcat ≈ 70, which is invariant with
   temperature" and Ea 9–10 kcal/mol for the wild type to ref. 26. Both readers entered the row and flagged it. It
   stays entered, since the table marks the cited rows and this one is not among them; the notes of M0247 and T0135
   say that it may be the same measurement as ref. 26. If that paper is ever read into MEG-NEN, the two rows must be
   compared.
4. **Perdeuterated substrate of S056 Table 2:** the competitive D(kcat/KM) values were measured with a 1:4 mixture
   of protio-LA and perdeutero-LA (2H31-LA), so every C–H of the heavy substrate is deuterated and the values
   contain secondary effects besides the primary one at C11. Both readings set `kie_type` to `primary`, as for the
   perdeutero values of S033 and S038 already in the database; the notes say what is labelled.
5. **Pressure (S058):** the schema has no pressure field, so the pressure stands in `conditions`, `location` and
   `as_printed` of each of the twelve series, as it does for the two series of morphinone reductase under pressure
   (T0062, T0063). The four L754A rows of Table 2 (entries 13–16) give no ΔEa, because the Ea(D) values were
   experimentally inaccessible, so they are not entered and L754A gets no row from this source.
6. **Transfer in S058 (judgement call, same in both readings):** S058 writes "C-H activation" and "H-transfer" and
   assigns no mechanism. Both readers entered PCET, which its own ref. 7a and the other four sources of this block
   state, and both say so in the notes.
7. **MoLOX (S060):** G4NAP4, as the source itself gives. UniProt files it under Pyricularia oryzae, the current name
   of M. oryzae, and the organism stays as the source names it. The source numbers the mature protein, 14 lower than
   UniProt at all eight glycosylation sites, the numbering of the crystal structure 5FNO; both readings checked
   this. From the second reading the EC field now carries all three numbers UniProt gives (1.13.11.-, 1.13.11.45,
   1.13.11.58) in place of the single 1.13.11.45 of the first reading, with a note that 1.13.11.45, linoleate
   11-lipoxygenase, is the one matching the C11 chemistry measured here. The GLN variant is entered as its eight
   point mutations.
8. **PDB entries:** both readings find no entry for the eight new variants except the wild-type MoLOX (5FNO, the
   Endo H-treated enzyme of S060 ref. 22, whose chain begins with EF in place of V15 and A16 of the signal
   peptide). The entries the papers name are added to the notes of the existing wild type: 3PZW (S057, S059), 1F8N
   (S058) and 5T5V (S059), which S059 calls the 300 K structure while its RCSB entry gives 293 K. The second reading
   also reports an eighth wild-type entity at RCSB, one more than the seven the verified row lists; the row is left
   as it is and the note says so.
9. **Judgement calls made the same way by both readers:** 30 °C for S056 Tables 1–3 (footnote a) and for S057
   Table 1 (footnote a); 10 and 30 °C and pH 9.0 or 7.0 for the twelve competitive values of S056 Table 2; the
   solvent isotope effects of S056 Table 3 as `solvent` on H2O over D2O at pD 9.0 (meter reading 8.6); 303 K for
   S059 (footnote †, the text writing 30 °C); 20 °C and pH 9.0 for S060 (footnote a); 10–45 °C for the S057 series
   (footnote b), with the number of temperatures left empty because the footnote says "7 to 8 (depending on
   mutant)"; 15–35 °C and five temperatures for S058 (text); 10–30 °C and seven temperatures for S060 (Methods);
   no pH and no labelled substrate for S057, S058 and S059, whose methods are in the supporting information; all
   rows `observed`, since no paper of this block calls a value intrinsic.

## Inconsistencies inside the papers

None of them changes an entered value. All were checked by the curator in the HTML or the XML.

- **S056:** the text credits the wild-type Dkcat (81) to ref. 13, the Table 1 footnote to ref. 19; the Discussion
  writes "mutations at positions 756, 564, and 553" where the paper's mutations are at 754, 546 and 553; the typos
  "Ile553Ala/ILeu754Ala" and "Leu546Ala/Leu754/Ala". The printed A_H/A_D of about 0.2 with ΔEa 3.5 kcal/mol gives a
  KIE of about 67 at 30 °C against the measured 85, which the "∼" covers.
- **S057:** none; the values repeated in the text match Table 1.
- **S058:** Table 1 prints the lower temperature of L754A as "208" K, which must be 288 K; the text writes "at 1.034
  bar" for 1034 bar; one cell reads "0.98 (0.03" without the closing bracket.
- **S059:** footnote * says the temperature-dependent data of I552A and V750A had been reported in ref. 35 and were
  only now analysed for Ea and ΔEa, while the table marks the row "This work"; the recollected wild type of footnote
  † is identical to S057 (point 1); the paper calls 5T5V the 300 K structure where RCSB gives 293 K.
- **S060:** footnote c defines ΔEa = Ea(D) – Ea(H) and the Discussion once writes it the other way round (point 2);
  the wild-type row carries no footnote although the text credits its values to ref. 26 (point 3); the text gives
  the Ea of GLN as "12 ± 0.7" and Table 1 as 12.1 ± 0.7, and the table value is entered; the kcat header carries
  footnote a twice and the ΔEa header a stray ",c"; "NeNGlyc" should read NetNGlyc.

## SCHEMA.md

No change. The pressure of S058 is recorded in `conditions`, `location` and `as_printed`, as for T0062 and T0063.

All 29 isotope effects, all 23 temperature series, the 8 new enzyme rows and the 8 new steps of S056–S060 are now
`verified`.
