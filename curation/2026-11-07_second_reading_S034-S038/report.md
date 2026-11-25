# MEG-NEN second reading (reader ai-2): S034–S038

## Overview

| file | rows | content |
|---|---|---|
| `measurements.csv` | 56 | S036: 8, S038: 48 |
| `temperature.csv` | 9 | S034: 4, S035: 1, S036: 2, S037: 2 |
| `enzymes.csv` | 21 | one row per variant that has at least one value |

Limits that apply to all five papers:
- **Equations are not readable.** In S035, S037 and S038 they are empty MathJax placeholders in the saved pages. In S034 and S036 they are images. So every sign convention below rests on the printed text, the column subscripts and a consistency check.
- **Not used:** supporting information (not available) and values shown only in figures.
- **Units:** all energies were already printed in kcal/mol, so none needed converting. Temperatures are °C + 273.15.
- **Error type:** no table in any of the five papers states it.

## S034 – Singh 2014 JACS (E. coli DHFR, distal mutants)

**Entered** in temperature.csv (Table 1): Arrhenius fit of intrinsic H/T KIEs. All four rows are primary H/T, intrinsic, kcat/KM, competitive, 278.15–318.15 K, pH 9.0.

| variant | A_H/A_T | ΔEa(T-H), kcal/mol |
|---|---|---|
| W133F | 5.8 ± 0.8 | –0.01 ± 0.08 |
| F125M | 1.9 ± 0.3 | 0.96 ± 0.09 |
| G121V/F125M | 0.03 ± 0.004 | 3.4 ± 0.1 |
| M42W/F125M | 0.01 ± 0.003 | 4.0 ± 0.2 |

**Nothing in measurements.csv:** the main text prints no KIE at a single temperature. All observed and intrinsic KIEs are in SI Tables S1–S4.

**Left out**
- Cited rows of Table 1:
  - WT (footnote d, ref 30): 7.0 ± 1.5 / –0.1 ± 0.2
  - G121V (e, ref 29): 7.4 ± 1.6 / 0.23 ± 0.03
  - M42W (f, ref 28): 2.8 ± 0.2 / 0.58 ± 0.04
  - M42W-G121V (g, ref 25): 0.1 ± 0.1 / 3.6 ± 0.3
- Not isotope effects: k_hyd (single-turnover rates, 25 °C, pH 7, footnote a) and k_wt/k_mut.
- Derived values: ΔΔEa (footnote c) of 2.2 ± 0.1, 2.8 ± 0.3 and 2.5 ± 0.4.
- Model fits: Table 2 (Marcus-like DAD0, f, DAD_L, ΔG). Its WT, G121V, M42W and M42W-G121V rows are also cited (ref 55).
- Footnote b: H/D and D/T trends, "data not shown".
- Figure-only: Figs. 2–4, including the I14 mutants (ref 40) and the semiclassical range 0.3–1.7 (ref 32). Commitments are in SI Fig. S5.

**Judgement calls**
- ΔEa(T-H) read as Ea(T) − Ea(H), so no sign change. Check: with A_H/A_T 0.03 and ΔEa +3.4, the KIE at 25 °C is about 9; the reverse sign would give a KIE far below 1.
- Range "5 to 45 °C" from Results and Methods. pH 9.0 from Methods (Competitive KIE Experiments), not from Table 1. Number of temperatures not stated.
- Variant names "G121V-F125M" and "M42W-F125M" written as G121V/F125M and M42W/F125M.

**Inconsistencies (non-KIE)**
- k_wt/k_mut for W133F is printed as "3 ± 0.1", but 228/88 = 2.6.
- M42W-F125M: 512 ± 31 printed, 228/0.45 = 507 (within error).
- The ΔΔEa column reproduces correctly from footnote c.

## S035 – Singh 2015 ACS Catal (I14A-G121V)

**Entered:** one temperature.csv row for I14A/G121V: A_H/A_T 0.01 ± 0.002, ΔEa 4.25 ± 0.12 kcal/mol. Intrinsic H/T, kcat/KM, competitive, 278.15–318.15 K, pH 9.0.

**Left out**
- Table 1 rows cited through markers on the row labels:
  - WT (ref 55): 7.0 ± 1.5 / −0.1 ± 0.2
  - G121V (ref 42): 7.4 ± 1.6 / 0.23 ± 0.03
  - I14A (ref 51): 4.7 ± 0.5 / 0.39 ± 0.06
- Not isotope effects or derived: k_hyd 0.04 ± 0.001 s⁻¹, k_wt/k_mut 5700 ± 295, ΔΔG‡ 5.11 ± 0.32.
- Model fit: Table 2, DAD_L 3.34 Å and ΔG° 4.75 kcal/mol for the double mutant.
- SI-only: the observed and intrinsic KIE values.
- Footnote a: H/D and D/T trends not shown.
- Figures 2–5 not read.

**Judgement calls**
- Sign direction from the Fig. 4 legend ("ΔEa between Ea for tritium and Ea for hydrogen"). Check: KIE at 25 °C is about 13.
- pH 9.0 from Methods. The buffer for the KIE runs is not stated.

**Inconsistencies:** none affecting values. The double mutant is called G121V-I14A in Fig. 2.

## S036 – Francis 2013 JBC (N23PP, N23PP/G51PEKN)

**Entered**

measurements.csv, Table 1, WT at pH 7.0:

| temperature | H/T observed | D/T observed | H/T intrinsic |
|---|---|---|---|
| 45 °C | 2.68 ± 0.01 | 1.43 ± 0.01 | 5.1 ± 0.3 |
| 5 °C | 1.64 ± 0.02 | 1.23 ± 0.06 | 5.1 ± 0.4 |

measurements.csv, Table 2, k_H/k_T (intrinsic H/T at 25 °C, 298.15 K, pH 9.0):
- N23PP: 9.57 ± 0.88
- N23PP/G51PEKN: 6.47 ± 0.45

temperature.csv (278.15–318.15 K, pH 9.0):
- N23PP: A_H/A_T 2.31 ± 0.16, ΔEa 0.78 ± 0.04 kcal/mol
- N23PP/G51PEKN: A_H/A_T 7.1 ± 1.1, ΔEa −0.06 ± 0.09 kcal/mol

**Left out**
- Table 1 pH 9.0 rows (footnote c, "From Ref. 12"):
  - 45 °C: 4.8 ± 0.1, 1.65 ± 0.02, 6.1 ± 0.5
  - 5 °C: 3.0 ± 0.1, 1.51 ± 0.02, 6.1 ± 0.6
- Table 2 WT column (footnote a, ref 12): k_cat 12 ± 1, k_H 950 ± 50, k_H/k_T 6.18 ± 0.39, A_H/A_T 7.0 ± 1.5, ΔEa −0.1 ± 0.2.
- k_cat and k_H rows: rates, cited (refs 3, 19, 24).
- Figure-only: the Arrhenius data in Fig. 3 and the commitments in Fig. 4.

**Judgement calls**
- **pH 9.0 rows of Table 1 (most important one).** Marker c stands only on the "9.0" cell of the 45 °C row. I applied it to both pH 9.0 rows, because it sits on the shared pH value, ref 12 is the WT pH 9 series over 5–45 °C, and Table 2's WT column also comes from ref 12. If you read the marker as covering the 45 °C row only, the three 5 °C / pH 9.0 values would be primary and should be added.
- The pH 7.0 runs were read as competitive kcat/KM measurements. The buffer at pH 7.0 is not stated.
- The H/T_int column is primary; footnote b cites references only for the calculation method.
- k_H/k_T: 25 °C comes from footnote d and pH 9.0 from Methods. These values agree with the Table 2 Arrhenius parameters (8.6 vs 9.57 ± 0.88; 6.4 vs 6.47 ± 0.45).
- Methods define ΔEa as heavy minus light, so no sign change.

**Inconsistencies**
- The text says "we measured the intrinsic KIEs at pH 9.0 and 7.0", while footnote c attributes the pH 9.0 data to Ref. 12.
- The text discusses pH 8.0 twice, but Table 1 has no pH 8.0 data.
- Figure cross-references are shifted by one: the text cites Fig. 4 for the Arrhenius plot (it is Fig. 3) and Fig. 5 for the commitments (Fig. 4), and further shifted references appear in the Discussion and Conclusions.
- The Fig. 3 legend lists "WT (red)" and "ecDHFR (red)" as two separate series.

## S037 – Francis 2016 Biochemistry (native and heavy human DHFR)

**Entered** in temperature.csv (Table 1, pH 9.0):
- native (variant WT): A_H/A_T 6.6 ± 0.8, ΔEa −0.1 ± 0.1 kcal/mol
- heavy (13C, 15N, 2H): A_H/A_T 6.6 ± 1.1, ΔEa −0.1 ± 0.1 kcal/mol

**Left out**
- Model fit: DAD_avg 3.048 ± 0.002 and 3.056 ± 0.007 Å, and the ΔDAD of 0.010 ± 0.005 Å in the text.
- SI-only: the observed and intrinsic KIEs. Fig. 2 not read; its E. coli panels come from ref 27.
- Table 2 heavy-enzyme effects (h-KIE = light-enzyme parameter / heavy-enzyme parameter, pH 7.65, 25 °C):
  - k_cat(DHF) 1.44 ± 0.02, Km(DHF) 1.07 ± 0.40, (k_cat/Km)DHF 1.34 ± 0.50
  - k_on(THF) 1.01 ± 0.05, k_off(THF) 1.38 ± 0.13
  - k_cat(NADPH) 1.45 ± 0.02, Km(NADPH) 1.06 ± 0.26, (k_cat/Km)NADPH 1.37 ± 0.34
  - k_on(NADP) 0.94 ± 0.06, k_off(NADP) 1.00 ± 0.01

  The isotopes in these effects sit in the protein, not on the transferred hydrogen, a neighbouring hydrogen or the solvent. The isotopes field (H/D, H/T, D/T) cannot represent them, and several are Km or binding-constant ratios. Whether the database wants such protein-mass isotope effects is your decision.

**Judgement calls**
- ΔEa direction read from the (T-H) subscript; Methods only say "difference … between the two isotopologues". This is supported by the text: human DHFR KIEs are "slightly lower" than E. coli's, which fits 5.6 at 25 °C rather than 7.8 with the reverse sign.
- The 5–45 °C range comes from the Abstract, where it is stated for human DHFR. I applied it to the heavy enzyme too, although the paper does not state it separately for that form.

**Inconsistency:** Table 2 footnote c (the h-KIE definition) has no marker anywhere in the table.

## S038 – Hu 2019 JBC (soybean lipoxygenase-1 variants)

**Entered** in measurements.csv (48 rows):
- Table 1, D-kcat (noncompetitive, kcat; 283.15 and 313.15 K; pH 9.0): E256A, R707A, I553A, L546A, I538A, V750A, I552A, I839A, W500F. 18 rows.
- Table 1, D-kcat/Km (competitive, kcat/KM): all 11 variants, including WT and L754A. 22 rows.
- Table 2, solvent isotope effects at 293.15 K on kcat and kcat/Km: WT, I552A, L546A, V750A. 8 rows.

**Left out**
- Cited D-kcat (the footnote text limits the citation to kcat and D-kcat):
  - WT (ref 25): 66 (5) at 10 °C, 52 (1) at 40 °C
  - L754A (ref 17): 106 (8), 82 (6)
- Rates: the kcat column.
- Derived: Table 3 commitments and k_off.
- Figure-only: Figs. 1–2. SI Tables S1–S11 not available.
- Cited text values: D-kcat ∼80 (refs 16, 17), D-kcat/Km ∼30–40 for the double mutant (refs 30, 41).

**Judgement calls**
- **kind = observed for D-kcat.** The Scheme 1 legend says D-kcat and D-kchem "can be used interchangeably", but the paper never calls any value intrinsic. You may want to reclassify these.
- **kie_type = primary with perdeutero-LA.** D-LA is perdeuterated, so the transferred hydrogen and all other C–H positions are heavy; secondary contributions are included in the value.
- **Donor = linoleic acid C11.** The paper never numbers the carbon; I inferred C11 from the product, 13(S)-HPOD.
- **Transfer = PCET.** The paper describes "a proton and electron … removed … by a nonheme iron center Fe(III)–OH"; the term PCET appears only in cited titles.
- L546A and I553A D-kcat carry no footnote, so I entered them as this study's values, although both variants appear in earlier work.
- Solvent isotope effects read as H2O/D2O (the direction is not stated). pH 9.0 is the H2O buffer; the D2O buffer had a meter reading of 8.6.

**Inconsistencies**
- The Methods list competitive KIEs only for "WT, I552V, V750A, I538A, I839A, W500F". I552V should be I552A, and five variants of Table 1 are missing from the list.
- The Results list of variants names I553A twice and omits R707A.
- The Results give the measuring range as 10–45 °C; the competitive assays ran 10–40 °C.
- The Methods list solvent isotope effects for WT, I552A and L546A only; Table 2 also has V750A.
- The Methods heading speaks of "double mutants", but all variants are single mutants.
- The text's "180- and 2000-fold" reductions for L546A and L754A do not match the Table 1 kcat ratios (119 and 1400 at 10 °C).
- Table 3 for L754A (k_off 0.16) does not follow from Table 1 (0.162/0.69 = 0.23). For I839A the commitment from Eq 1 is 0.39, against 0.45 printed.
- The "2–4-fold" kcat decrease stated for Trend III is only about 1.3-fold for V750A and W500F.

## Enzymes

**UniProt accessions.** E. coli DHFR P0ABQ4 (strain K-12, EC 1.5.1.3), human DHFR P00374 (EC 1.5.1.3), soybean LOX-1 P08170 (EC 1.13.11.12). No paper prints an EC number, so all three come from UniProt.

**Numbering.** Every mutated or named position matches UniProt. For human DHFR the paper's positions (I17, 24-PWPP-27, 62-PEKN-65) match UniProt numbering that counts Met1.

**How RCSB was searched.** By accession and by ≥90 % sequence identity (182, 95 and 26 entities), each entity aligned to the UniProt sequence, and cross-checked by organism plus name and by full-text search. No entry cites any of the five DOIs.

**PDB entries assigned**

| variant | PDB | note |
|---|---|---|
| ecDHFR N23PP/G51PEKN | 4GH8 | cites ref 24; sequence lacks C-terminal R159 |
| SLO-1 I553A | 3BNE | E160 instead of S160 (see below) |
| SLO-1 L546A | 5TQN | E160 |
| SLO-1 L754A | 5TR0 | E160 |
| SLO-1 V750A | 7SOJ | E160 |
| SLO-1 I552A | 7SOI | E160 |
| SLO-1 WT | 1F8N; 1YGE; 2SBL; 3PZW; 5T5V; 9O4S; 9O4T | 1F8N is named in the paper; 4WFO left out (Mn-substituted) |

- All other variants have no PDB entry. N23PP exists only as N23PP/S148A (3QL0, 4KJL), so I did not list it. The heavy human DHFR has no entry.
- **Wild types with very many entries** (E. coli and human DHFR) are left empty. The papers name 1RX2 and 4M6K.
- **Sequence differences RCSB lists that the studies did not engineer:** 1RX2 has D37 where UniProt has N37. The Klinman-lab SLO-1 entries have E160 where UniProt has S160.
