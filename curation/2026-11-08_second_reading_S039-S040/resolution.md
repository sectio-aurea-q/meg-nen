# Second reading of S039–S040 (8 November 2026)

First reading `ai-1`, second reading `ai-2`. Both readers worked from the PMC pages of the two papers, saved on
8 November 2026 (both author manuscripts); the published PDFs and the supporting information were not read. The saved
pages lost the equations and some symbols in table headers, which PMC renders with MathJax, so both readers also had
the PMC XML of the same two manuscripts, fetched the same day, and used it only for those; no number was taken from
it. The second reader worked from these files alone, did not see the first reading, and looked up UniProt and RCSB
PDB again for every enzyme. Its instructions repeated the rules of CURATION.md and SCHEMA.md and allowed the web only
for these lookups. Files in this folder:

- `reading2_measurements.csv`, `reading2_temperature.csv`, `reading2_enzymes.csv`, `report.md`: the second reading as
  delivered (`report.md` saved by the curator from the second reader's answer; the list of its output files was
  shortened)
- `comparison.md`: row-by-row comparison of both readings, before the decisions below

## Result

All 4 rows of the first reading (2 isotope effects, 2 temperature series) have a partner in the second reading, and
all of them agree in value, error, temperature, pH, Arrhenius parameters, temperature range and number of
temperatures. Neither reading has rows the other lacks. The readings differ in the `kind` of one row (point 1) and in
the order of two PDB entries. Both readers left out the same values: the wild-type columns of S039 Table 4 (ref. 39)
and of S040 Tables 3 and 4 (refs. 20 and 26), the semi-classical limits of S039 Table 4, the per-temperature KIEs of
SI Tables S2 and S4 and of the figures, and the Eyring parameters of kcat. Decisions:

1. **Kind of Dkcat with Mg2+ (M0188):** the second reading entered `intrinsic`, since S040 says "The observed KIE on
   kcat (Dkcat) is equal to the intrinsic KIE"; the first reading entered `observed`. `observed` is kept: the Table 3
   caption calls Dkcat the observed H/D KIE on kcat and gives the intrinsic H/D KIE on the hydride transfer
   separately as Dk (M0189); the equality is the source's conclusion that the hydride transfer limits kcat, and
   `notes` say so. The Dkcat of SLO-1 in S038 was handled the same way.
2. **PDB entries of TS Y209W:** both readings found 2G8X and 4GEV. The curator confirmed them: 4GEV (with dUMP and
   CB3717) cites S039 and replaced 2G8M, the entry the source names in its introduction, on 29 August 2012; 2G8X is
   the apoprotein, cited to ref. 41 of S039. RCSB lists no sequence difference from P0A884 other than Y209W; the
   carbamylated N-terminus that the mutation field of 2G8X names, found by the second reading, is added to `notes`.
3. **Wild-type entries named by S040 (existing row `TS_ECOLI_WT`, from S020):** both readings found that 2G8O, which
   S040 calls "now 4IW5", was replaced by 4IW5 in February 2013, 4IW5 by 4KNZ in May 2013 and 4KNZ in 2019 by 6NNR,
   whose primary citation is S040. RCSB holds 37 full-length wild-type entries, so `pdb` stays empty, and `notes` now
   name the entries S020 and S040 use.
4. **Kept from the first reading:** the wording of the two new hydride-transfer steps, as for `TS_ECOLI_Y94F_C6H`
   (S020). Both readings describe the same transfer, from C6 of H4folate to the exocyclic methylene (C7) of the
   dUMP-derived intermediate; the C7 that S039 names is in the notes of the Y209W step.
5. **Judgement calls made the same way by both readers:**
   - S039 and S040: ΔEa = EaL − EaT, from the S039 text and from Eq. 2 (S039) and Eq. 9 (S040), both
     KIE = (AL/AT) exp(−ΔEa/RT) in the XML; hence dEa 0.5 for Y209W and 0.06 for the wild type with Mg2+. With these
     signs the Y209W KIE is about 8.4 at 25 °C and falls as the temperature rises, as the text says, and the
     wild-type KIE with Mg2+ is about 7.3 at 25 °C, close to the 7.1 that Dk 3.9 implies.
   - S039: 5–35 °C from the Results and the Experimental Section; the number of temperatures and the pH are not stated
     for the KIE experiments; `kind` intrinsic, since the source fits the intrinsic KIEs (equal to the observed ones
     at 5–25 °C, from the Northrop method at 35 °C).
   - S040: four temperatures ("at the four experimental temperatures"), their range not stated; pH 7.5 for the
     noncompetitive Dkcat, none for the competitive experiments; Dk as the intrinsic H/D KIE with `quantity`
     kcat/KM; Mg2+ as a condition of the wild type, not as a variant.
   - The ΔH‡ of kcat (S039 Table 3, S040 Table 1) is not entered as Ea_light.

## Inconsistencies inside the papers

None of them changes an entered value. All were checked by the curator in the HTML or the XML.

- **S039:** the Experimental Section places the new water molecule in "Figure 4.B", while the water displacement is
  shown in Fig. 3B; the Y209W ternary complex is 2G8M in the introduction and 4GEV later (RCSB replaced 2G8M by 4GEV).
- **S040:** the text says that Mg2+ "reduces the activation free energy and entropy of activation", while in Table 1
  −TΔS‡ falls from 13.9 to 12.8 kcal/mol, so ΔS‡ rises; 2G8O is "now 4IW5", which RCSB has since replaced twice (now
  6NNR); the Table 2 headers write CH4H4fol for CH2H4fol (XML).
- **Between the two papers:** the wild-type ΔEa(H-T) of ref. 39 of S039 and ref. 26 of S040, the same paper (S011,
  10.1021/bi036124g, not in hand), is printed as −0.02 ± 0.25 in S039 and as 0.02 ± 0.25 in S040, with the same
  equation; it is not entered. The wild-type Eyring row of S039 Table 3, which names no source, equals the row with
  50 mM MgCl2 of S040 Table 1, not the row without Mg2+ (ref. 26); S039 states MgCl2 only for its thiol-trapping
  assays, and the notes of T0080 now say so.

## SCHEMA.md

No change.

Both isotope effects, both temperature series, the enzyme variant and the two steps of S039–S040 are now `verified`;
`TS_ECOLI_WT` names the PDB entries of S040 in `notes`.
