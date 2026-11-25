# Second reading of S051–S055 (9 November 2026)

First reading `ai-1`, second reading `ai-2`. These five papers are block 3 of the second reading list: the hydride
transfer of dihydrofolate reductase from the deep-sea bacterium Moritella profunda (S051) and from the moderate
thermophile Geobacillus stearothermophilus with six variants (S052), of E. coli and human DHFR at five temperatures
(S053), and of recombinant formate dehydrogenase from Candida boidinii (S054) with its variants V123A and V123G
(S055). Both readers worked from the PMC pages of the papers, saved on 9 November 2026 (S051 and S052 as publisher
versions, S053, S054 and S055 as author manuscripts); the published PDFs and the supporting information were not
read. Both readers also had the PMC XML of the same five manuscripts and used it only for the equations; no number
was taken from it. The second reader worked from these files alone, did not see the first reading, and looked up
UniProt and RCSB PDB again for every enzyme. Its instructions repeated the rules of CURATION.md and SCHEMA.md and
allowed the web only for these lookups. Files in this folder:

- `reading2_measurements.csv`, `reading2_temperature.csv`, `reading2_enzymes.csv`, `report.md`: the second reading as
  delivered (`report.md` saved by the curator from the second reader's answer; the list of its output files was
  shortened)
- `comparison.md`: row-by-row comparison of both readings, before the decisions below

## Result

All 19 isotope effects and all 12 temperature series of the first reading have a partner in the second reading, and
all of them agree in value, error, temperature, temperature range, number of temperatures, pH, quantity, method and
kind. Both readings give the same UniProt entry, EC number, variant and PDB entries for all 11 new enzymes and for
the two existing wild types that S053 measures, and they name the same donor and acceptor atoms. Both readers left
out the same values: everything the papers take from other work (the EcDHFR and TmDHFR columns of S051 Table 1, the
commercial-enzyme values that S054 cites from ref. 2, the WT row of S055 Table 1), values shown only in figures or
in the supporting information (KIEs at further temperatures, in cosolvents and with salts in S051 and S052, the
per-temperature intrinsic KIEs of S054 and S055), the Eyring and free-energy rows of S051 Table 1, and the
crystallographic donor–acceptor distances of S055. Decisions:

1. **α-Secondary KIEs of S051 (second reading only, left out):** the text gives "average observed values of 1.065 ±
   0.022 for EcDHFR and 1.044 ± 0.011 for MpDHFR", temperature independent, at pH 7 under single-turnover
   conditions. They are averages over temperatures that only the supporting information lists, so they stand at no
   temperature; SCHEMA.md enters one isotope effect at one temperature, and `temperature_K` is required. As with the
   single KIEs of S045 (block 1), they are not entered.
2. **Signs of ΔEa:** all values entered as Ea(heavy) − Ea(light), the same way by both readers. S051: Table 1 prints
   Ea H and Ea D, so its ΔEa is Ea(D) − Ea(H) (28.1 − 21.6 = 6.5, printed 6.6); the pH 9 value in the text is read the
   same way. S052: ΔEa is not defined and Ea D not printed; only Ea(D) − Ea(H) reproduces the KIE at 20 °C in all
   seven rows. S054: the label ΔEaT-H. S055: the label ΔE H-T, positive with AH/AT below 1, gives a normal KIE only as
   Ea(T) − Ea(H) (about 17 and 15 at 25 °C). None of the five papers prints an Arrhenius equation.
3. **pH of the human KIEs of S053 (left empty by both readers):** the text says only "at high pH". The E. coli KIEs
   were collected at pH 9.0 "for the sake of comparison", and the second reader notes that the human kNADPH at
   25 °C (25 ± 0.3 s−1) equals the Table 4 rate at pH 9.00; pH 9.0 is likely but not stated.
4. **BsDHFR (S052):** both readings give Q5KZ26. No active UniProtKB entry carries the sequence of 1ZDR, the apo
   structure the paper shows (UniParc UPI00005AB3BA; its UniProtKB entries are all deleted); RCSB maps 1ZDR to
   Q5KZ26, which UniProt files under G. kaustophilus HTA426 and which has R64 where 1ZDR has G64. The organism stays
   as the paper names it. 1ZDR is the only PDB entry for the wild type, none exists for the variants.
5. **Recombinant FDH (S054, S055):** the recombinant isozyme (CbFDH_iso2) gets its own enzyme row, `FDH_CANBO_REC`
   (A0A0A1EQY0), separate from the commercial mixture of isozymes in `FDH_CANBO_WT` (O13437, S026); the V123
   variants are made from it (their structures 6D4B and 6D4C map to A0A0A1EQY0). The notes of `FDH_CANBO_WT`,
   `FDH_CANBO_HALFHEAVY` and `FDH_CANBO_HEAVY` now point to the new rows.
6. **Correction to the first reading:** its notes called ref. 29 of S055 the paper S054. Ref. 29 is S026 (Bandaria et
   al. 2009, the commercial enzyme), S054 is ref. 32; the notes of `FDH_CANBO_V123A`, `FDH_CANBO_V123G`, T0112 and
   T0113 are corrected.
7. **Steps:** eleven new steps, all hydride transfers; both readings name the same donor and acceptor atoms, and the
   wording of the existing DHFR and FDH steps is kept. S052 does not say which face of NADPH its NADPD labels; S053
   makes R-[4-2H]-NADPH by the same method (T. brockii ADH and d8-2-propanol).
8. **PDB entries named in the papers** are added to the notes of the existing wild types: 1RX2 (S051, S052) for
   `DHFR_ECOLI_WT` and 4M6J (S053) for `DHFR_HUMAN_WT`.
9. **Judgement calls made the same way by both readers:** 1.98 ± 0.13 of S051 as a steady-state KIE on kcat at pH 9
   and 1 °C (from the paragraph on the pH 9 measurements); no temperature range for S051 and S052, none being stated
   in the main text; the S052 KIEs at 20 °C; pH 9.0 for the E. coli KIEs of S053 from the Results; the S053 KIEs as
   `single_turnover`, `noncompetitive`, `observed`; 5, 15, 25, 35 and 45 °C and pH 7.5 for S054 and S055 from their
   Methods.

## Inconsistencies inside the papers

None of them changes an entered value. All were checked by the curator in the HTML or the XML.

- **S051:** ΔEa is printed as 6.6 ± 3.4 kJ/mol, Ea D − Ea H gives 6.5; the EcDHFR data are credited to ref. 36 in
  Table 1 and to ref. 37 in the Fig. 1 legend.
- **S052:** the text lists "Phe31, Lys31" among the substrate-binding residues; the second is K32 in 1ZDR.
- **S053:** the printed KIEs of Table 3 differ slightly from the ratios of the printed rates (3.01, 3.20 and 2.97
  against 3.02, 3.19 and 2.96), those of Table 5 more (2.79 against 2.9 at 15 °C, 1.33 against 1.4 at 45 °C),
  perhaps from averaging per trial; the E. coli rate at 25 °C and pH 9 is 30.0 s−1 in Table 3 and 25 ± 1 s−1 at pH
  8.99 in Table 2; the E. coli rates of Table 3 do not rise monotonically (31.8 at 15 °C, 30.0 at 25 °C); the pH of
  the human KIEs is not stated (point 3).
- **S054:** refs. 2 and 6 are the same paper (S026); it quotes the commercial-enzyme values of S026 as AH/AT 6.1 ±
  0.5 and ΔEa −0.02 ± 0.05 kcal/mol, where S026 prints ± 0.8 and ± 0.08 (T0056); EC 1.2.1.2 is printed, UniProt
  gives 1.17.1.9.
- **S055:** the WT row of Table 1 is marked "From Ref 29" (S026), but its values (AH/AT 7 ± 2, ΔE 0.0 ± 0.2
  kcal/mol) are those of the recombinant enzyme of S054 (6.8 ± 2.0, 0.01 ± 0.2), not those of S026 (6.1 ± 0.8,
  −0.02 ± 0.08); the Methods also say WT and variants were expressed and purified "using the procedure in Ref. 29";
  the Introduction gives the UniProt code O13437, while the paper's structures map to A0A0A1EQY0; the text once
  writes "DE H-T".
- **Across sources:** S032 quotes the ΔEa of the light recombinant enzyme from S054 as 0.05 ± 0.10 kcal/mol (T0067
  notes); S054 prints 0.01 ± 0.2.

## SCHEMA.md

No change.

All 19 isotope effects, all 12 temperature series, the 11 new enzyme rows and the 11 new steps of S051–S055 are now
`verified`.
