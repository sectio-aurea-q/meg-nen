# Second reading (ai-2) of S051–S055: KIE extraction report

All three output files are written, and every entered number was re-checked against the HTML by a separate script, with no mismatches.

| | S051 | S052 | S053 | S054 | S055 | total |
|---|---|---|---|---|---|---|
| measurements.csv | 4 | 7 | 10 | 0 | 0 | 21 |
| temperature.csv | 2 | 7 | 0 | 1 | 2 | 12 |
| enzymes.csv | 2 | 7 | 2 | 1 | 2 | 14 |

Files (in this folder, as `reading2_*.csv`; the list of output files was shortened by the curator):
- `out/measurements.csv`
- `out/temperature.csv`
- `out/enzymes.csv`
- The scripts are in `work/`: `html2txt.py` (HTML dump), `xmlmath.py` (MathML), `rcsb.py` (RCSB search), `build.py` (CSV writer) and `verify.py` (re-check against the HTML).

**General method**
- **Parsing:** numbers were read from the HTML with BeautifulSoup. The XML was used only for the equations: S053 eq 1, S054 eq 1–7 and S055 eq 1–4. From the XML I took the Northrop exponents, 1/3.3 in S054 and 1/3.34 in S055. I also compared the S051/S052/S053/S055 tables between XML and HTML; they are identical.
- **Conversions:** kJ/mol was divided by 4.184 with exact decimals and rounded half-up to four significant figures; °C was converted with +273.15.
- **Enzyme lookups:** UniProt REST and RCSB search/data only.

## S051 – Loveridge 2011 JACS (MpDHFR)

**Entered**
- **Single-turnover primary KIE:** MpDHFR WT 1.83 ± 0.10 at 298.15 K, pH 7, from Table 1 (MpDHFR column, footnote a "At 25 °C").
- **Steady-state primary KIE:** 1.98 ± 0.13 at 274.15 K on kcat (from text).
- **α-secondary KIEs:** MpDHFR 1.044 ± 0.011 and EcDHFR 1.065 ± 0.022, single turnover, pH 7. These are averages over temperature, so temperature_K is empty.
- **Temperature series 1 (Table 1, single turnover, pH 7):**
  - AH/AD 0.13 ± 0.09
  - ΔEa 6.6 ± 3.4 kJ/mol → 1.577 ± 0.8126 kcal/mol
  - Ea^H 21.6 ± 2.2 kJ/mol → 5.163 ± 0.5258 kcal/mol
- **Temperature series 2 (text, steady state, pH 9, kcat):** ΔEa 1.5 ± 1.1 kJ/mol → 0.3585 ± 0.2629 kcal/mol.

**Not entered**
- **Cited columns of Table 1:**
  - EcDHFR column (header cites ref 36): KIE 2.71 ± 0.22, ΔEa 7.9 ± 0.9, AH/AD 0.11 ± 0.02, Ea^H 29.9, Ea^D 37.8.
  - TmDHFR column (header cites ref 22): KIE 4.02 ± 0.29, and with footnote b "Above 25 °C": ΔEa 2.5 ± 1.0 and AH/AD 1.54 ± 0.36.
- **Other cited values:** steady-state KIE at pH 7 "is unity" (ref 29), and the computational KIE changes of 60–100%, ~10% and ~40% (ref 17).
- **Eyring data:** ΔH‡H 19.2, ΔH‡D 25.7 and ΔS‡ are printed, but ΔΔH‡ and A′H/A′D are not, so I made no Eyring row and did not compute them.
- **ΔG‡ at 25 °C** (H 57.5 ± 2.2, D 59.0 ± 2.6 kJ/mol): not entered.
- **Not KIEs:** rates, extrapolated rates at physiological temperatures, pKa values and the D₂O pKa shift. The "apparent inverse solvent KIE" has no number.
- **SI or figures only:** KIEs in cosolvents (Figs. 3–4), the KIE(kcat) temperature series at pH 9 (Fig. 1) and individual α-secondary values.

**Judgement calls**
- **pH 9 and kcat for the 1.98 value:** pH 9 comes from the preceding sentences of the same paragraph (steady state at pH 9; "EcDHFR at elevated pH"). The kcat assignment rests on the Fig. 3 label "KIE on kcat at pH 9".
- **EcDHFR α-secondary value entered as primary data:** it has no citation, and the Discussion calls it one of "the values obtained here".
- **Labelled cofactors:** I inferred 4-(R)-NADPD for the primary KIE and 4-(S)-NADPD for the secondary KIE from Methods; the paper never links them explicitly.
- **Sign of ΔEa:** Table 1 ΔEa = Ea^D − Ea^H by its own numbers. The pH 9 ΔEa is undefined; I read it the same way.
- **Temperature ranges:** not stated for either series.

**Inconsistencies**
- Ea^D − Ea^H = 28.1 − 21.6 = 6.5, but 6.6 is printed (rounding).
- EcDHFR data are credited to ref 36 in Table 1 but to ref 37 in the Fig. 1 legend.

## S052 – Guo 2014 Biochemistry (BsDHFR and 6 variants)

**Entered**
- **KIEs:** Table 5 KIE (20 °C), at 293.15 K and pH 7, for WT, L20M, A104Q, L20M/A104Q, P122E, P129D and P122E/P129D.
- **Temperature series:** 7 rows with Ea^H, ΔEa and AH/AD (kJ converted).

**Not entered**
- **Not isotope effects:** Table 4 (steady-state Ea, AH, KM).
- **Figures or SI only:** temperature-resolved KIEs (Fig. 4C), salt and cosolvent effects on KIEs (Figs. 5–6), and KIE(kcat).

**Judgement calls**
- **Sign of ΔEa:** the paper does not define the direction and does not print Ea^D. I read it as Ea^D − Ea^H because (AH/AD)·exp(ΔEa/RT) at 293.15 K reproduces the 20 °C KIE in every row (calculated vs printed):

  | Variant | Calculated | Printed |
  |---|---|---|
  | WT | 3.37 | 3.44 |
  | L20M | 2.83 | 2.80 |
  | A104Q | 1.94 | 2.00 |
  | L20M/A104Q | 1.88 | 1.90 |
  | P122E | 2.01 | 2.02 |
  | P129D | 2.04 | 2.05 |
  | P122E/P129D | 1.94 | 1.89 |

  The reversed sign would give KIEs below 1.
- **Temperature range:** not stated, so T_min/T_max are empty.
- **NADPD stereochemistry:** not stated (made with T. brockii ADH and d8-2-propanol).

**Inconsistencies:** the text lists "Phe31, Lys31"; the second one is Lys32 in the sequence.

## S053 – Andrews 2022 JPCB (E. coli and human DHFR)

**Entered**
- **ecDHFR:** Table 3 KIEs at 5–45 °C: 3.02, 3.19, 2.96, 2.96, 2.82. No errors are printed. pH 9.0 comes from the Results text.
- **hsDHFR:** Table 5 KIEs: 2.9 ± 0.05, 2.9 ± 0.2, 1.6 ± 0.2, 1.5 ± 0.3, 1.4 ± 0.2. The error is ± 1 SD of 2 trials (footnote a).
- **Temperature series:** none, because no Arrhenius parameters are printed.

**Not entered**
- **Cited:** the KIE of 3 from Fierke 1987 (ref 13, "previously reported … approximately 3").
- **Heavy-enzyme work:** the intrinsic H/T KIE of refs 16/23 has no number.
- **SI only:** solvent KIEs and multiple KIEs for ecDHFR.
- **Not KIEs:** rates, pKa values and simulated rates (ref 33).
- **Duplicate:** "the expected value of 3" in the text is the rounded 5 °C hsDHFR value; the table value (2.9) is entered.

**Judgement calls**
- **hsDHFR pH left empty:** the paper only says "at high pH". The 25 °C kNADPH (25 ± 0.3 s⁻¹) equals the Table 4 rate at pH 9.00, which suggests pH 9.0, but it is not stated.

**Inconsistencies**
- **ecDHFR KIE vs rate ratio:** the ratios of printed rates are 3.01, 3.20 and 2.97 where 3.02, 3.19 and 2.96 are printed.
- **hsDHFR KIE vs rate ratio:** the rate ratios differ more (15 °C 2.79 vs 2.9; 45 °C 1.33 vs 1.4). These may be explained by averaging over trials.
- **ecDHFR rate at 25 °C, pH 9:** Table 3 gives 30.0 s⁻¹; Table 2 gives 25 ± 1 at pH 8.99.
- **ecDHFR rates are not monotonic:** 31.8 at 15 °C but 30.0 at 25 °C.
- **Markup artifact:** "isopropanol-d8" has its 8 tagged as citation ref 8 in both the HTML and XML (no effect on data).

## S054 – Guo 2016 Biochemistry (recombinant CbFDH)

**Entered**
- **Temperature series:** intrinsic H/T KIE (kcat/KM, competitive) for WT. AH/AT 6.8 ± 2.0 and ΔEaT-H 0.01 ± 0.2 kcal/mol; 278.15–318.15 K, n = 5, pH 7.5 (temperatures and pH from Methods).
- **Sign of ΔEa:** by its label, T − H, which matches the database direction.

**Not entered**
- **Cited:** commercial CbFDH AH/AT 6.1 ± 0.5 and ΔEaT-H −0.02 ± 0.05 kcal/mol (ref 2).
- **SI only:** single-temperature observed and intrinsic KIEs (Table S1).
- **Not KIEs:** the single-turnover rates 35 ± 2 and 25 ± 4 s⁻¹, and the QM/MM ΔG‡ values.

**Inconsistencies**
- References 2 and 6 are the same paper.
- The paper gives EC 1.2.1.2; UniProt gives 1.17.1.9.

## S055 – Pagano 2019 ACS Catal (CbFDH V123A and V123G)

**Entered (Table 1)**
- **V123A:** AH/AT 0.8 ± 0.2, ΔE_H-T 1.8 ± 0.2 kcal/mol.
- **V123G:** AH/AT 0.03 ± 0.02, ΔE_H-T 3.7 ± 0.4 kcal/mol.
- **Both:** intrinsic H/T, kcat/KM, competitive; 278.15–318.15 K, n = 5, pH 7.5.

**Not entered**
- **Cited WT row:** the Table 1 WT row is marked "* From Ref 29" (AH/AT 7 ± 2, ΔE 0.0 ± 0.2).
- **SI only:** the per-temperature KIEs.
- **Not KIEs:** ΔG‡ from kcat (16.4, 18.8 and 19.6 kcal/mol) and the Fig. 4 fit.

**Judgement calls**
- **Sign of ΔE_H-T:** the label suggests H − T but the order is not defined. The positive values, together with AH/AT < 1 and the "inflated" KIEs, only fit Ea(T) − Ea(H). For example, the implied 25 °C KIE is about 16.7 with that reading, versus 0.038 with the reverse sign. Entered as printed.
- **Error type:** not stated in Table 1; the Fig. 4 legend calls its error bars 95% confidence intervals.

**Inconsistencies**
- Ref 29 (Bandaria 2009, the commercial enzyme) does not fit the WT values. They match S054's recombinant values (6.8 ± 2.0 and 0.01 ± 0.2; that paper is ref 32 here).
- The text writes "DE_H-T" (typo).

## Enzyme metadata (enzymes.csv)

**DHFRs**
- **MpDHFR:** Q70YQ6; PDB 2ZZA, 3IA4, 3IA5. The paper names 2ZZA (RCSB lists M1V for it).
- **EcDHFR:** P0ABQ4. pdb left empty because there are 165 entries; S051 names 1RX2.
- **hsDHFR:** P00374. pdb left empty because there are 89 entries; S053 names 4M6J.
- **BsDHFR:** Q5KZ26, which UniProt files under G. kaustophilus HTA426 rather than G. stearothermophilus.
  - The paper's own structure, 1ZDR, maps to Q5KZ26, with one difference: R64G.
  - The exact 1ZDR sequence matches only deleted UniProtKB entries.
  - The numbering matches at L20, A104, P122 and P129.
  - pdb: 1ZDR for WT only; there are no mutant structures.

**CbFDH**
- **Accession:** A0A0A1EQY0, not O13437 (the accession S055 names).
  - The paper's own structures (5DN9, 5DNA, 6D4B, 6D4C) all map to A0A0A1EQY0.
  - A0A0A1EQY0 has the L128, I227 and I354 that S054 states for its isozyme.
  - O13437 differs at 11 positions, including V128, V227 and V354.
- **WT pdb:** 5DN9, 5DNA, 8HTY, 8IQ7. 5DN9 and 5DNA cite S054's DOI.
- **Variants:** V123A is 6D4B and V123G is 6D4C; both cite S055's DOI.
- **EC:** 1.17.1.9 (UniProt).
