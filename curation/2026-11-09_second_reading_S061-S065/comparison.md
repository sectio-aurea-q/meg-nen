# Comparison of the two readings of S061–S065 (9 November 2026)

Reading 1 `ai-1` (in the MEG-NEN folder), reading 2 `ai-2` (in `out/`). Rows are matched by source, enzyme variant,
quantity, method, kind, value, error, temperature and pH; `as_printed` is expected to differ, because both readers
wrote it themselves. Produced by `kie_compare2.py` and `kie_compare_meta2.py`. The decisions taken on these
differences are in `resolution.md`.

## measurements: numbers and categories agree in 28 of 33 rows; as_printed worded differently in 29; 4 rows only in reading 1, 6 only in reading 2

- M0249 (S061, NQO1_HUMAN_WT_NADH_AB, Table 2, row A→B, column KIE): as_printed: 'KIE 1.8 ± 0.1 (kobs at 6 °C)' vs 'KIE 1.8 +/- 0.1 (row A->B)'
- M0250 (S061, NQO1_HUMAN_WT_NADH_BC, Table 2, row B→C, column KIE): as_printed: 'KIE 1.8 ± 0.3 (kobs at 6 °C)' vs 'KIE 1.8 +/- 0.3 (row B->C)'
- M0251 (S061, NQO1_HUMAN_WT_NADH_AB, Results, section 3.3, paragraph on the KIEs (Figure 4E)): as_printed: 'KIE A→B at 6 °C of 2.3 ± 0.5 (kHT1 284 ± 17 s−1)' vs '2.3 +/- 0.5 for the KIE A->B at 6 degC'
- M0252 (S062, PHEH_CHRVO_WT_PHE, Table 2, row Wild type, 6-MePH4): no match in reading 2
- M0253 (S062, PHEH_CHRVO_WT_PHE, Table 2, row Wild type, DMPH4): no match in reading 2
- M0254 (S062, PHEH_CHRVO_I234D_PHE, Table 2, row I234D, 6-MePH4): no match in reading 2
- M0255 (S062, PHEH_CHRVO_I234D_PHE, Table 2, row I234D, DMPH4): no match in reading 2
- M0256 (S062, PHEH_CHRVO_WT_PHE_TAUT, Results, section Isotope effects on aromatic hydroxylation, last paragraph): as_printed: 'This value is 5.1 ± 1.0 for the reactions with both 6-MePH4 and DMPH4' vs 'This value is 5.1 +/- 1.0 for the reactions with both 6-MePH4 and DMPH4'
- M0257 (S062, PHEH_CHRVO_WT_4MEPHE, Results, section Isotope effects on benzylic hydroxylation): as_printed: 'an intrinsic isotope effect on benzylic hydroxylation of 10 ± 1 at 25 °C' vs 'an intrinsic isotope effect on benzylic hydroxylation of 10 +/- 1 at 25 degC'
- M0258 (S063, PTMT2_STRPL_WT_GGPP, Results, paragraph on the 94 % D2O experiment): kind: 'observed' vs 'intrinsic'; as_printed: 'resulted in a large KIE of seven (94 % D2O buffer, pD 6, 28 °C)' vs 'resulted in a large KIE of seven (94 % D2O buffer, pD 6, 28 degC)'
- M0259 (S064, KE07_R1_NBI, Table 1, row R1, column kH/kD): as_printed: 'k H /k D 4.9 (0.2)' vs 'kH/kD 4.9 (0.2) (row R1)'
- M0260 (S064, KE07_R4_NBI, Table 1, row R4, column kH/kD): as_printed: 'k H /k D 5.6 (0.2)' vs 'kH/kD 5.6 (0.2) (row R4)'
- M0261 (S064, KE07_R5_NBI, Table 1, row R5, column kH/kD): as_printed: 'k H /k D 8.6 (0.2)' vs 'kH/kD 8.6 (0.2) (row R5)'
- M0262 (S064, KE07_R6_NBI, Table 1, row R6, column kH/kD): as_printed: 'k H /k D 6.5 (0.1)' vs 'kH/kD 6.5 (0.1) (row R6)'
- M0263 (S064, KE07_R7_NBI, Table 1, row R7, column kH/kD): as_printed: 'k H /k D 7.0 (0.2)' vs 'kH/kD 7.0 (0.2) (row R7)'
- M0264 (S064, KE07_R7_2_NBI, Table 1, row R7-2, column kH/kD): as_printed: 'k H /k D 7.3 (0.1)' vs 'kH/kD 7.3 (0.1) (row R7-2)'
- M0265 (S065, CPA2E_THEAT_WT_CDPGLC, Table 1, row 20 °C, column Dkcat): as_printed: 'Dkcat 2.20 ± 0.75' vs 'Dkcat 2.20 +/- 0.75 (20 degC)'
- M0266 (S065, CPA2E_THEAT_WT_CDPGLC, Table 1, row 20 °C, column Dkcat/KM): as_printed: 'Dkcat/KM 2.06 ± 0.67' vs 'Dkcat/KM 2.06 +/- 0.67 (20 degC)'
- M0267 (S065, CPA2E_THEAT_WT_CDPGLC, Table 1, row 60 °C, column Dkcat): as_printed: 'Dkcat 4.30 ± 0.30' vs 'Dkcat 4.30 +/- 0.30 (60 degC)'
- M0268 (S065, CPA2E_THEAT_WT_CDPGLC, Table 1, row 60 °C, column Dkcat/KM): as_printed: 'Dkcat/KM 3.80 ± 0.40' vs 'Dkcat/KM 3.80 +/- 0.40 (60 degC)'
- M0269 (S065, CPA2E_THEAT_WT_CDPGLC, Table 1, row 80 °C, column Dkcat): as_printed: 'Dkcat 3.34 ± 0.09' vs 'Dkcat 3.34 +/- 0.09 (80 degC)'
- M0270 (S065, CPA2E_THEAT_WT_CDPGLC, Table 1, row 80 °C, column Dkcat/KM): as_printed: 'Dkcat/KM 3.19 ± 0.24' vs 'Dkcat/KM 3.19 +/- 0.24 (80 degC)'
- M0271 (S065, CPA2E_THEAT_WT_CDPGLC, Results, section Solvent Isotope Effects): as_printed: 'it was 2.34 (± 0.27) in 2H2O (KIE from deuteration of CDP-Glc)' vs 'it was 2.34 (+/- 0.27) in 2H2O'
- M0272 (S065, CPA2E_THEAT_WT_CDPGLC, Table 3, row CDP-Glc, column D2Okcat (pL 7.0) 60 °C): as_printed: 'D2O k cat (pL 7.0) 60 °C: 0.97 ± 0.12' vs 'D2Okcat 0.97 +/- 0.12 (pL 7.0, 60 degC)'
- M0273 (S065, CPA2E_THEAT_WT_CDPGLC, Table 3, row CDP-Glc, column D2Okcat (pL 7.5) 60 °C): as_printed: 'D2O k cat (pL 7.5) 60 °C: 1.03 ± 0.13' vs 'D2Okcat 1.03 +/- 0.13 (pL 7.5, 60 degC)'
- M0274 (S065, CPA2E_THEAT_WT_CDPGLC, Table 3, row CDP-Glc, column D2Okcat (pL 8.0) 60 °C): as_printed: 'D2O k cat (pL 8.0) 60 °C: 0.99 ± 0.11' vs 'D2Okcat 0.99 +/- 0.11 (pL 8.0, 60 degC)'
- M0275 (S065, CPA2E_THEAT_WT_CDPGLC, Table 3, row CDP-Glc, column D2Okcat (pL 7.5) 20 °C): as_printed: 'D2O k cat (pL 7.5) 20 °C: 0.49 ± 0.07' vs 'D2Okcat 0.49 +/- 0.07 (pL 7.5, 20 degC)'
- M0276 (S065, CPA2E_THEAT_WT_CDPGLC, Table 3, row CDP-[2-2H]Glc, column D2Okcat (pL 7.5) 80 °C): as_printed: 'D2O k cat (pL 7.5) 80 °C: 0.84 ± 0.03' vs 'D2Okcat 0.84 +/- 0.03 (pL 7.5, 80 degC)'
- M0277 (S065, CPA2E_THEAT_WT_CDPGLC, Table 3, row CDP-[2-2H]Glc, column D2Okcat (pL 7.0) 60 °C): as_printed: 'D2O k cat (pL 7.0) 60 °C: 0.57 ± 0.11' vs 'D2Okcat 0.57 +/- 0.11 (pL 7.0, 60 degC)'
- M0278 (S065, CPA2E_THEAT_WT_CDPGLC, Table 3, row CDP-[2-2H]Glc, column D2Okcat (pL 7.5) 60 °C): as_printed: 'D2O k cat (pL 7.5) 60 °C: 0.57 ± 0.10' vs 'D2Okcat 0.57 +/- 0.10 (pL 7.5, 60 degC)'
- M0279 (S065, CPA2E_THEAT_WT_CDPGLC, Table 3, row CDP-[2-2H]Glc, column D2Okcat (pL 8.0) 60 °C): as_printed: 'D2O k cat (pL 8.0) 60 °C: 0.59 ± 0.10' vs 'D2Okcat 0.59 +/- 0.10 (pL 8.0, 60 degC)'
- M0280 (S065, CPA2E_THEAT_WT_CDPGLC, Table 3, row CDP-[2-2H]Glc, column D2Okcat (pL 7.5) 20 °C): as_printed: 'D2O k cat (pL 7.5) 20 °C: 0.51 ± 0.10' vs 'D2Okcat 0.51 +/- 0.10 (pL 7.5, 20 degC)'
- M0281 (S065, CPA2E_THEAT_WT_CDPGLC, Table 3, footnote b): as_printed: 'the D2O k cat /K M was determined as 0.65 (± 0.31)' vs 'the D2Okcat/KM was determined as 0.65 (+/- 0.31)'
- only in reading 2: S062 Table 2, row Wild type, column 6-MePH4 | CvPheH WT H/D other | 1.24 +/- 0.04 (wild type, 6-MePH4) | Dkcat with [ring-2H5]-phenylalanine, from fits to eq 3 (v/e = kcat*S/[KM + S(1 + Fi(Ev-1))], read from the PMC XML), which assumes an isotope effect on kcat onl
- only in reading 2: S062 Table 2, row Wild type, column DMPH4 | CvPheH WT H/D other | 1.43 +/- 0.07 (wild type, DMPH4) | Dkcat with [ring-2H5]-phenylalanine, from fits to eq 3 (v/e = kcat*S/[KM + S(1 + Fi(Ev-1))], read from the PMC XML), which assumes an isotope effect on kcat onl
- only in reading 2: S062 Table 2, row I234D, column 6-MePH4 | CvPheH I234D H/D other | 1.00 +/- 0.01 (I234D, 6-MePH4) | Dkcat with [ring-2H5]-phenylalanine, from fits to eq 3 (v/e = kcat*S/[KM + S(1 + Fi(Ev-1))], read from the PMC XML), which assumes an isotope effect on kcat onl
- only in reading 2: S062 Table 2, row I234D, column DMPH4 | CvPheH I234D H/D other | 0.90 +/- 0.03 (I234D, DMPH4) | Dkcat with [ring-2H5]-phenylalanine, from fits to eq 3 (v/e = kcat*S/[KM + S(1 + Fi(Ev-1))], read from the PMC XML), which assumes an isotope effect on kcat onl
- only in reading 2: S063 Results, paragraph on mixed H2O/D2O buffers | PtmT2 WT H/D solvent | The KIE at 28 degC converged to 4 under these experimental conditions | KIE from the ratio of protonated to deuterated product fragment (m/z 273 vs 274) by MS, Eq. (4) (read from the PMC XML; the HTML lost all equations): KIE = kH/k
- only in reading 2: S065 Results, 'Temperature Dependence of kcat', text (also Abstract) | TaCPa2E WT H/D primary | The Dkcat peaked at 40 degC, with its value of 6.1 | Noncompetitive primary KIE (the paper's own wording: 'We determined noncompetitive primary kinetic isotope effects (KIE) due to 2H at the glucose C2'); light an

## temperature: numbers and categories agree in 11 of 15 rows; as_printed worded differently in 15; 0 rows only in reading 1, 2 only in reading 2

- T0137 (S061, NQO1_HUMAN_WT_NADH_AB, Table 2, row A→B): as_printed: 'EaHT 6.1 ± 0.2; ΔEa 0.2 ± 0.4; AH/AD 1.3 ± 0.6' vs 'AH/AD 1.3 +/- 0.6; dEa 0.2 +/- 0.4 kcal/mol; EaHT 6.1 +/- 0.2 kcal/mol'
- T0138 (S061, NQO1_HUMAN_WT_NADH_BC, Table 2, row B→C): as_printed: 'EaHT 10.9 ± 0.5; ΔEa −1.1 ± 0.7; AH/AD 13 ± 6' vs 'AH/AD 13 +/- 6; dEa -1.1 +/- 0.7 kcal/mol; EaHT 10.9 +/- 0.5 kcal/mol'
- T0139 (S062, PHEH_CHRVO_WT_4MEPHE, Results, section Isotope effects on benzylic hydroxylation): as_printed: 'A H /A D of 0.29 ± 0.03 and ΔE a of 2.1 ± 0.4' vs 'AH/AD of 0.29 +/- 0.03 and the difference in activation energy (dEa) ... of 2.1 +/- 0.4'
- T0140 (S063, PTMT2_STRPL_WT_GGPP, Table 1, column 24 % D2O): kind: 'observed' vs 'intrinsic'; as_printed: 'A H /A D 4.4±0.5 (24 % D2O)' vs 'AH/AD 4.4 +/- 0.5 (24 % D2O)'
- T0141 (S063, PTMT2_STRPL_WT_GGPP, Table 1, column 48 % D2O): kind: 'observed' vs 'intrinsic'; as_printed: 'A H /A D 3.9±0.3 (48 % D2O)' vs 'AH/AD 3.9 +/- 0.3 (48 % D2O)'
- T0142 (S063, PTMT2_STRPL_WT_GGPP, Table 1, column 72 % D2O): kind: 'observed' vs 'intrinsic'; as_printed: 'A H /A D 4.2±0.4 (72 % D2O)' vs 'AH/AD 4.2 +/- 0.4 (72 % D2O)'
- T0143 (S063, PTMT2_STRPL_WT_GGPP, Table 1, column 94 % D2O): kind: 'observed' vs 'intrinsic'; as_printed: 'A H /A D 6±2 (94 % D2O)' vs 'AH/AD 6 +/- 2 (94 % D2O)'
- T0144 (S064, KE07_R1_NBI, Table 1, row R1): as_printed: 'Ea(H) 10.8 (1.1); Ea(D)−Ea(H) 4.3 (1.5); AH/AD 0.004 (0.0006)' vs 'AH/AD 0.004 (0.0006); Ea(D)-Ea(H) 4.3 (1.5); Ea(H) 10.8 (1.1) kcal/mol'
- T0145 (S064, KE07_R4_NBI, Table 1, row R4): as_printed: 'Ea(H) 5.6 (0.8); Ea(D)−Ea(H) 4.2 (1.2); AH/AD 0.005 (0.0009)' vs 'AH/AD 0.005 (0.0009); Ea(D)-Ea(H) 4.2 (1.2); Ea(H) 5.6 (0.8) kcal/mol'
- T0146 (S064, KE07_R5_NBI, Table 1, row R5): as_printed: 'Ea(H) 7.7 (0.8); Ea(D)−Ea(H) 1.4 (1.1); AH/AD 0.875 (0.1211)' vs 'AH/AD 0.875 (0.1211); Ea(D)-Ea(H) 1.4 (1.1); Ea(H) 7.7 (0.8) kcal/mol'
- T0147 (S064, KE07_R6_NBI, Table 1, row R6): as_printed: 'Ea(H) 9.5 (0.5); Ea(D)−Ea(H) 2.2 (0.7); AH/AD 0.181 (0.0126)' vs 'AH/AD 0.181 (0.0126); Ea(D)-Ea(H) 2.2 (0.7); Ea(H) 9.5 (0.5) kcal/mol'
- T0148 (S064, KE07_R7_NBI, Table 1, row R7): as_printed: 'Ea(H) 7.1 (0.7); Ea(D)−Ea(H) 4.0 (1.1); AH/AD 0.009 (0.0011)' vs 'AH/AD 0.009 (0.0011); Ea(D)-Ea(H) 4.0 (1.1); Ea(H) 7.1 (0.7) kcal/mol'
- T0149 (S064, KE07_R7_2_NBI, Table 1, row R7-2): as_printed: 'Ea(H) 6.9 (0.4); Ea(D)−Ea(H) 4.4 (0.6); AH/AD 0.005 (0.0003)' vs 'AH/AD 0.005 (0.0003); Ea(D)-Ea(H) 4.4 (0.6); Ea(H) 6.9 (0.4) kcal/mol'
- T0150 (S065, CPA2E_THEAT_WT_CDPGLC, Table 2, columns 20-40 °C): as_printed: 'EA +66.7 ± 9.4; ΔEA –36.7 ± 7.6 kJ/mol; AH/AD (7.0 ± 1.1)×10^6' vs 'dEA -36.7 +/- 7.6 kJ/mol; AH/AD (7.0 +/- 1.1) x 10^6; EA(CDP-Glc) +66.7 +/- 9.4 kJ/mol'
- T0151 (S065, CPA2E_THEAT_WT_CDPGLC, Table 2, columns 45-70 °C): as_printed: 'EA +60.2 ± 3.3; ΔEA +12.7 ± 2.6 kJ/mol; AH/AD 0.05 ± 0.007' vs 'dEA +12.7 +/- 2.6 kJ/mol; AH/AD 0.05 +/- 0.007; EA(CDP-Glc) +60.2 +/- 3.3 kJ/mol'
- only in reading 2: S063 Table 1, footnote [b] | PtmT2 WT H/D solvent | AH/AD of 5 ... with slopes corresponding to dH-D Ea of 60 cal mol-1 (24 % D2O) | Second, alternative fit given in footnote [b]: 'forced fitting of the data as a linear function of 1/T'. SIGN CHANGED: the printed quantity is dH-D Ea, and Eq. 
- only in reading 2: S063 Table 1, footnote [b] | PtmT2 WT H/D solvent | AH/AD of 4 ... with slopes corresponding to dH-D Ea of 20 cal mol-1 (48 % D2O) | Second, alternative fit given in footnote [b]: 'forced fitting of the data as a linear function of 1/T'. SIGN CHANGED: the printed quantity is dH-D Ea, and Eq. 


## enzymes and steps

- NQO1_HUMAN_WT: organism: 'Homo sapiens' vs 'Homo sapiens (human)'
- PHEH_CHRVO_WT: pdb: '3TK2;3TK4' vs '1LTU;1LTV;1LTZ;3TCY;3TK2;3TK4;4JPY'
- PHEH_CHRVO_I234D: ec, organism, uniprot, variant and pdb agree
- PTMT2_STRPL_WT: ec, organism, uniprot, variant and pdb agree
- KE07_R1: organism: 'designed enzyme on the HisF scaffold of Thermotoga maritima' vs 'none - computationally designed enzyme; scaffold imidazole glycerol phosphate synthase (HisF) from Thermotoga maritima; expressed in Escherichia coli BL21(DE3)'; pdb: '5D2W' vs '4Z08;5D2T;5D2V;5D2W'
- KE07_R4: organism: 'designed enzyme on the HisF scaffold of Thermotoga maritima' vs 'none - computationally designed enzyme; scaffold imidazole glycerol phosphate synthase (HisF) from Thermotoga maritima; expressed in Escherichia coli BL21(DE3)'
- KE07_R5: organism: 'designed enzyme on the HisF scaffold of Thermotoga maritima' vs 'none - computationally designed enzyme; scaffold imidazole glycerol phosphate synthase (HisF) from Thermotoga maritima; expressed in Escherichia coli BL21(DE3)'; pdb: '6DKV;6C7M;6DNJ' vs '5D2X;5D2Y;5D30;6C7M;6C7T;6C7V;6DKV;6DNJ'
- KE07_R6: organism: 'designed enzyme on the HisF scaffold of Thermotoga maritima' vs 'none - computationally designed enzyme; scaffold imidazole glycerol phosphate synthase (HisF) from Thermotoga maritima; expressed in Escherichia coli BL21(DE3)'; pdb: '' vs '5D32;6C8B'
- KE07_R7: organism: 'designed enzyme on the HisF scaffold of Thermotoga maritima' vs 'none - computationally designed enzyme; scaffold imidazole glycerol phosphate synthase (HisF) from Thermotoga maritima; expressed in Escherichia coli BL21(DE3)'; pdb: '6CAI;6DC1' vs '5D33;5D37;6CAI;6DC1'
- KE07_R7_2: organism: 'designed enzyme on the HisF scaffold of Thermotoga maritima' vs 'none - computationally designed enzyme; scaffold imidazole glycerol phosphate synthase (HisF) from Thermotoga maritima; expressed in Escherichia coli BL21(DE3)'
- CPA2E_THEAT_WT: uniprot: 'A0ABS1GJY6' vs ''
  - NQO1_HUMAN_WT: reading 2 ('NADH', 'NADH nicotinamide C4 (4R hydrogen)', 'FAD N5', 'hydride') | reading 1 [('NQO1_HUMAN_WT_NADH_AB', 'NADH', 'NADH C4 (nicotinamide)', 'FAD N5', 'hydride'), ('NQO1_HUMAN_WT_NADH_BC', 'NADH', 'NADH C4 (nicotinamide)', 'FAD N5', 'hydride')]
  - PHEH_CHRVO_WT: reading 2 ('phenylalanine', 'phenylalanine ring carbons (C4 hydroxylation site; C3 in the tautomerization)', 'not assigned (composite: ring C-O bond formation, then loss of a C3 hydrogen)', 'unknown') | reading 1 [('PHEH_CHRVO_WT_PHE', 'phenylalanine', 'phenylalanine ring C4 (site of hydroxylation)', 'the neighbouring ring carbon (1,2-hydride shift)', 'hydride'), ('PHEH_CHRVO_WT_PHE_TAUT', 'phenylalanine', 'the ring carbon next to the hydroxylation site, carrying both hydrogens after the 1,2-shift', 'solvent (loss of H or D to form tyrosine)', 'proton'), ('PHEH_CHRVO_WT_4MEPHE', '4-CH3-phenylalanine', '4-CH3-phenylalanine methyl carbon (benzylic)', 'oxygen of the hydroxylating intermediate (proposed Fe(IV)=O)', 'H_atom')]
  - PHEH_CHRVO_I234D: reading 2 ('phenylalanine', 'phenylalanine ring carbons (C4 hydroxylation site; C3 in the tautomerization)', 'not assigned (composite: ring C-O bond formation, then loss of a C3 hydrogen)', 'unknown') | reading 1 [('PHEH_CHRVO_I234D_PHE', 'phenylalanine', 'phenylalanine ring C4 (site of hydroxylation)', 'the neighbouring ring carbon (1,2-hydride shift)', 'hydride')]
  - PHEH_CHRVO_WT: reading 2 ('phenylalanine', 'dienone C3 (carbon adjacent to the hydroxylation site, bearing Ha and Hb)', 'solvent/base (proton lost on tautomerization)', 'proton') | reading 1 [('PHEH_CHRVO_WT_PHE', 'phenylalanine', 'phenylalanine ring C4 (site of hydroxylation)', 'the neighbouring ring carbon (1,2-hydride shift)', 'hydride'), ('PHEH_CHRVO_WT_PHE_TAUT', 'phenylalanine', 'the ring carbon next to the hydroxylation site, carrying both hydrogens after the 1,2-shift', 'solvent (loss of H or D to form tyrosine)', 'proton'), ('PHEH_CHRVO_WT_4MEPHE', '4-CH3-phenylalanine', '4-CH3-phenylalanine methyl carbon (benzylic)', 'oxygen of the hydroxylating intermediate (proposed Fe(IV)=O)', 'H_atom')]
  - PHEH_CHRVO_WT: reading 2 ('4-methylphenylalanine (4-CH3-phenylalanine)', '4-methyl carbon of 4-methylphenylalanine', 'Fe(IV)O oxygen', 'H_atom') | reading 1 [('PHEH_CHRVO_WT_PHE', 'phenylalanine', 'phenylalanine ring C4 (site of hydroxylation)', 'the neighbouring ring carbon (1,2-hydride shift)', 'hydride'), ('PHEH_CHRVO_WT_PHE_TAUT', 'phenylalanine', 'the ring carbon next to the hydroxylation site, carrying both hydrogens after the 1,2-shift', 'solvent (loss of H or D to form tyrosine)', 'proton'), ('PHEH_CHRVO_WT_4MEPHE', '4-CH3-phenylalanine', '4-CH3-phenylalanine methyl carbon (benzylic)', 'oxygen of the hydroxylating intermediate (proposed Fe(IV)=O)', 'H_atom')]
  - PTMT2_STRPL_WT: reading 2 ('geranylgeranyl diphosphate (1)', 'catalytic acid D313 carboxyl oxygen (solvent-exchangeable)', 'C=C isoprene carbon of geranylgeranyl diphosphate (protonation site)', 'proton') | reading 1 [('PTMT2_STRPL_WT_GGPP', 'geranylgeranyl diphosphate', 'the carboxyl of the catalytic acid D313 (exchangeable with solvent)', 'a C=C isoprene carbon of the prefolded substrate', 'proton')]
  - KE07_R1: reading 2 ('5-nitrobenzisoxazole', "5-nitrobenzisoxazole C3'", 'Glu101 carboxylate oxygen', 'proton') | reading 1 [('KE07_R1_NBI', '5-nitrobenzisoxazole', '5-nitrobenzisoxazole C3', 'carboxylate oxygen of the catalytic base Glu101', 'proton')]
  - KE07_R4: reading 2 ('5-nitrobenzisoxazole', "5-nitrobenzisoxazole C3'", 'Glu101 carboxylate oxygen', 'proton') | reading 1 [('KE07_R4_NBI', '5-nitrobenzisoxazole', '5-nitrobenzisoxazole C3', 'carboxylate oxygen of the catalytic base Glu101', 'proton')]
  - KE07_R5: reading 2 ('5-nitrobenzisoxazole', "5-nitrobenzisoxazole C3'", 'Glu101 carboxylate oxygen', 'proton') | reading 1 [('KE07_R5_NBI', '5-nitrobenzisoxazole', '5-nitrobenzisoxazole C3', 'carboxylate oxygen of the catalytic base Glu101', 'proton')]
  - KE07_R6: reading 2 ('5-nitrobenzisoxazole', "5-nitrobenzisoxazole C3'", 'Glu101 carboxylate oxygen', 'proton') | reading 1 [('KE07_R6_NBI', '5-nitrobenzisoxazole', '5-nitrobenzisoxazole C3', 'carboxylate oxygen of the catalytic base Glu101', 'proton')]
  - KE07_R7: reading 2 ('5-nitrobenzisoxazole', "5-nitrobenzisoxazole C3'", 'Glu101 carboxylate oxygen', 'proton') | reading 1 [('KE07_R7_NBI', '5-nitrobenzisoxazole', '5-nitrobenzisoxazole C3', 'carboxylate oxygen of the catalytic base Glu101', 'proton')]
  - KE07_R7_2: reading 2 ('5-nitrobenzisoxazole', "5-nitrobenzisoxazole C3'", 'Glu101 carboxylate oxygen', 'proton') | reading 1 [('KE07_R7_2_NBI', '5-nitrobenzisoxazole', '5-nitrobenzisoxazole C3', 'carboxylate oxygen of the catalytic base Glu101', 'proton')]
  - CPA2E_THEAT_WT: reading 2 ('CDP-glucose (CDP-Glc)', 'CDP-glucose C2', 'C4 of the tightly bound NAD+', 'hydride') | reading 1 [('CPA2E_THEAT_WT_CDPGLC', 'CDP-glucose', 'CDP-glucose C2 (of the D-hexopyranosyl ring)', 'NAD+ nicotinamide C4', 'hydride')]
  - CPA2E_THEAT_WT: reading 2 ('CDP-glucose (CDP-Glc)', 'CDP-glucose 2-OH oxygen (solvent-exchangeable)', 'Tyr164 hydroxyl oxygen (active-site general base)', 'proton') | reading 1 [('CPA2E_THEAT_WT_CDPGLC', 'CDP-glucose', 'CDP-glucose C2 (of the D-hexopyranosyl ring)', 'NAD+ nicotinamide C4', 'hydride')]
  - CPA2E_THEAT_WT: reading 2 ('CDP-[2-2H]glucose (CDP-[2-2H]Glc)', 'CDP-glucose 2-OH oxygen (solvent-exchangeable)', 'Tyr164 hydroxyl oxygen (active-site general base)', 'proton') | reading 1 [('CPA2E_THEAT_WT_CDPGLC', 'CDP-glucose', 'CDP-glucose C2 (of the D-hexopyranosyl ring)', 'NAD+ nicotinamide C4', 'hydride')]
