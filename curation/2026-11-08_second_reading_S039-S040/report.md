# Reading ai-2: S039 and S040

Outputs: `out/measurements.csv` (2 rows, both S040), `out/temperature.csv` (2 rows: S039, S040), `out/enzymes.csv` (2 rows); scripts in `work/`.

I used the XML only for things the HTML lacks: Eq 2 in S039; Eqs 5, 8, 9 and 11 in S040; and the KM/KI/Kd symbols in the headers of S039 Table 2 and S040 Tables 2–3. No numbers were taken from the XML.

---

## S039 — Wang et al. 2012, JACS 134:17722 (10.1021/ja307859m), ecTSase Y209W

### Entered
- **temperature.csv, Table 4, column Y209W**
  - A_H/A_T = 3.6 ± 0.9.
  - ΔEa,H-T is printed as −0.5 ± 0.1 kcal/mol. I entered **dEa_kcal = +0.5**, error 0.1 (sign changed).
  - H/T, primary, kcat/KM, competitive, intrinsic.
  - 278.15–308.15 K.
  - n_temperatures, pH and Ea_light are empty.
- **measurements.csv:** nothing. The paper prints no KIE at a single temperature; those values are only in Table S4 (SI) and Fig. 2.
- **enzymes.csv:** Y209W, P0A884, EC 2.1.1.45, pdb `4GEV;2G8X`.

### Left out
- **Cited values:** Table 4, column WT (footnote a, "Data from Ref 39"): A_H/A_T 6.8 ± 2.8 and ΔEa,H-T −0.02 ± 0.25. Fig. 2 WT data (ref 39). The text's statement that W80M has no effect on the KIE (ref 39; no number).
- **Theoretical values:** Table 4, column "S.C. A_L/A_T", 0.3–1.7 (footnote b, semi-classical limits, refs 54–58).
- **SI or figure only:** Y209W observed and intrinsic KIEs at each temperature (Table S4, Fig. 2), including the Swain–Schaad test at 5 and 25 °C and the Northrop extraction at 35 °C.
- **Not isotope effects:** Table 3, Eyring parameters of kcat:
  - WT, 5–35 °C: ΔH‡ 3.4 ± 0.2, TΔS‡ −12.8 ± 0.2, ΔG‡ 16.2 ± 0.4 kcal/mol.
  - Y209W, 5–25 °C: 7.0 ± 0.3, −12.8 ± 0.4, 19.8 ± 0.7 kcal/mol.
  - Y209W, 25–35 °C: lower limits ca. 30 and ca. 11.
  
  I did not use these as Ea_light: they are Eyring ΔH‡ values of kcat, not the Ea of the KIE series.
- Tables 1–2 (thiol trapping, steady-state parameters; the β-ME rows come from ref 41) contain no isotope effects.

### Judgement calls
1. **Sign of ΔEa.** The text defines ΔEa = EaL − EaT, and Eq 2 (from the XML) reads KIE = kL/kT = (AL/AT)·exp(−ΔEa/RT); the two agree. So dEa_kcal = −ΔEa = +0.5.
   - Check: this gives an H/T KIE of about 8.4 at 25 °C that falls as temperature rises, matching the text ("more temperature-dependent with slightly larger magnitude" than WT).
   - The opposite sign would give about 1.5, which is implausible.
2. **kind = intrinsic.** The text says "The intrinsic KIEs were fit to the Arrhenius equation" (also the Fig. 2 legend). Intrinsic equals observed at 5–25 °C (Swain–Schaad); at 35 °C the intrinsic value was extracted by the Northrop method.
3. **quantity and method.** "competitive H/T and D/T method … KIEs on … kcat/KM". A Northrop-derived value keeps kcat/KM, as SCHEMA.md says.
4. **Temperature range.** 5–35 °C is stated in Results and in the Experimental section. The fit covers all intrinsic KIEs, so the whole range.
5. **n_temperatures left empty.** It is not stated for the KIEs. The steady-state kcat was measured at 5, 15, 25 and 35 °C, but the KIE text names only 5, 25 and 35 °C.
6. **pH left empty.** No pH is stated for the KIE experiments; pH 7.5 is given only for the thiol-trapping mixture.
7. **H/T only.** The paper prints only H/T parameters, saying D/T and H/D "follow the same trend".
8. **Error type** is not stated.
9. **Donor and acceptor** come from the text: H4folate is the "hydride source" and "C7 of the exocyclic intermediate" the "hydride acceptor"; the labelled compound is [6R-xH]CH2H4folate.

### Inconsistencies
- The Experimental section places the new water in "Figure 4.B", but the water displacement (wat-1 → wat-2) is shown in Fig. 3B.
- The Y209W structure is named 2G8M in the introduction and 4GEV later. This is consistent with RCSB, where 2G8M is obsolete and was replaced by 4GEV on 2012-08-29.

---

## S040 — Wang et al. 2013, JACS 135:7583 (10.1021/ja400761x), WT ecTSase ± 50 mM MgCl2

### Entered
- **measurements.csv, Table 3, row w/ Mg2+, column Dkcat:** 3.8 ± 0.3; H/D, kcat, noncompetitive, kind intrinsic (see call 1); 298.15 K; pH 7.5.
- **measurements.csv, Table 3, row w/ Mg2+, column Dk (footnote a):** 3.9 ± 0.2; H/D, kcat/KM, competitive, intrinsic; 298.15 K; pH empty.
- **temperature.csv, Table 4, column w/ Mg2+:**
  - A_H/A_T = 6.6 ± 1.3.
  - ΔEa,H-T is printed as −0.06 ± 0.12. I entered **dEa_kcal = +0.06**, error 0.12.
  - H/T, kcat/KM, competitive, intrinsic; n_temperatures 4; T range and pH empty.
- **enzymes.csv:** WT, P0A884, EC 2.1.1.45 (taken from UniProt; the paper gives none), pdb empty.

### Left out
- **Cited values:**
  - Table 3, row w/o Mg2+: Dkcat 3.7 ± 0.1 (footnote b, Ref 20) and Dk 3.8 ± 0.3 (footnote c, Ref 26).
  - Table 4, column w/o Mg2+ (footnote b, Ref 26): A_H/A_T 6.8 ± 2.8 and ΔEa,H-T 0.02 ± 0.25.
  - Fig. 4A, adopted from ref 26.
- **SI or figure only:** Table S2 (observed H/T and D/T KIEs on kcat/KM, intrinsic KIEs and the commitment Cf at the four temperatures, and D(kcat/KM) at 25 °C from Eq 11). Fig. 4B.
- **Not isotope effects:**
  - Table 1, Eyring parameters of kcat with Mg2+: ΔH‡ 3.4 ± 0.2, −TΔS‡ 12.8 ± 0.2, ΔG‡ 16.2 ± 0.4 kcal/mol. Not used as Ea_light.
  - Table 3 rate and binding constants: for H, kcat 8.7 ± 0.2 s⁻¹, KM 15 ± 1 μM, KI 0.76 ± 0.07 mM; for D, 2.3 ± 0.2 s⁻¹, 19 ± 5 μM, 3 ± 1 mM. No KIE on KM or kcat/KM is printed, and I computed none.
  - Table 2 and the Mg2+ Kd values (27 ± 7 mM, 0.5 ± 0.2 M, 3.7 ± 1.2 mM).
  - The exponent 3.34 in Eq 8 (a Swain–Schaad constant).

### Judgement calls
1. **Dkcat kind = intrinsic.** This rests on rule 5. The text says "The observed KIE on kcat (Dkcat) is equal to the intrinsic KIE (Table 3)", while the table caption calls it "observed". If rule 5 is read strictly, it would be observed. **The curator should look at this one.**
2. **Dkcat method and conditions.** Noncompetitive comes from the Experimental section "Noncompetitive KIE Experiments" and the sentence after Eq 5. 25 °C is from the Table 3 caption; pH 7.5 is from the noncompetitive-experiments paragraph.
3. **Dk.** It is extracted by the Northrop method (Eq 8, from the XML) from competitive H/T and D/T KIEs on kcat/KM, so quantity is kcat/KM. Footnote a gives 25 °C. No pH is stated for the competitive experiments.
4. **Sign of ΔEa in Table 4.** The words give no direction ("between the light and heavy isotopes"). Eq 9 (from the XML) reads kL/kT = (AL/AT)·exp(−ΔEa/RT), so ΔEa = EaL − EaT and dEa_kcal = +0.06.
   - Check, not entered: this gives an H/T KIE of about 7.3 at 25 °C, close to the value implied by Dk 3.9 (3.9^1.44 ≈ 7.1). The opposite sign would give about 6.0.
5. **Temperatures of the Table 4 series.** n_temperatures = 4 is taken from "at the four experimental temperatures in the presence of Mg2+". The actual temperatures are not stated. They are probably 5, 15, 25 and 35 °C (the steady-state temperatures), and 25 °C is one of them, but I left T_min/T_max empty.
6. **Mg2+** is treated as a condition; the variant is WT.
7. **Acceptor atom.** S040 says only "its acceptor in dUMP". I entered C7 (the exocyclic methylene) from the mechanism as S039 names it. The donor C6 follows from the 6R-xH label.

### Inconsistencies
- **Same cited value, two signs:** the WT ΔEa,H-T from Agrawal 2004 is printed as −0.02 ± 0.25 in S039 (ref 39) but 0.02 ± 0.25 in S040 (ref 26). It is not entered in either reading; check it when that paper is read.
- S039 Table 3's WT row (no source given) is identical to S040 Table 1's "w/ Mg2+" row. S040's w/o Mg2+ row (Ref 26) differs: 3.4 ± 0.1, 13.9 ± 0.1, 17.3 ± 0.2. These are not KIEs.
- S040 says Mg2+ "reduces the entropy of activation", but in Table 1 −TΔS‡ falls from 13.9 to 12.8, so ΔS‡ actually increases.
- In the XML, the Table 2 headers read "CH4H4fol" (a typo for CH2H4fol).
- S040 says 2G8O is "now 4IW5", but 4IW5 is itself obsolete at RCSB (4IW5 → 4KNZ → 6NNR).

---

## Enzyme metadata
- **UniProt:** P0A884 (TYSY_ECOLI, strain K-12, 264 aa, EC 2.1.1.45). The sequence is identical in most E. coli strains. Neither paper names a strain.
- **Numbering:** all residues the papers name match P0A884 with Met1 = 1 (Y209, C146, W80, W83, L143, R21, R127, I264, E58, N76, T78, E82, and the residues listed in S040 Fig. 6). Both constructs are full length.
- **RCSB searches:** 67 entities by accession and 68 by sequence identity of at least 90 % (the extra one is 4LRR, WT).
- **Y209W:** 4GEV (its primary citation is S039's DOI) and 2G8X (apoprotein; its mutation field also lists "N-terminus is carbamylated", a modification, not a sequence change). 3BFI is Y209M, not this variant.
- **WT:** 37 full-length entries, so pdb is empty. The paper names 2G8O/4IW5 (now 6NNR, whose primary citation is S040's DOI), 4ISK and 1TSN.
