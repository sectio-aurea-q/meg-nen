# Comparison of both readings of S039–S040, before the decisions in resolution.md

Numbers and categories (`kie_compare2.py`; reading 1 left, reading 2 right):

## measurements: numbers and categories agree in 1 of 2 rows; as_printed worded differently in 2; 0 rows only in reading 1, 0 only in reading 2

- M0188 (S040, TS_ECOLI_WT_C6H, Table 3, row w/ Mg2+, column Dkcat): kind: 'observed' vs 'intrinsic'; as_printed: 'Dkcat 3.8 ± 0.3' vs 'Dkcat 3.8 ± 0.3 (w/ Mg2+, 25 °C)'
- M0189 (S040, TS_ECOLI_WT_C6H, Table 3, row w/ Mg2+, column Dk, footnote a): as_printed: 'Dk 3.9 ± 0.2' vs 'Dk 3.9 ± 0.2 a (w/ Mg2+, 25 °C)'

## temperature: numbers and categories agree in 2 of 2 rows; as_printed worded differently in 2; 0 rows only in reading 1, 0 only in reading 2

- T0080 (S039, TS_ECOLI_Y209W_C6H, Table 4, column Y209W): as_printed: 'AH/AT 3.6 ± 0.9; ΔEa H-T −0.5 ± 0.1 (kcal/mol)' vs 'A_H/A_T 3.6 ± 0.9; ΔE_a H-T (kcal/mol) −0.5 ± 0.1'
- T0081 (S040, TS_ECOLI_WT_C6H, Table 4, column w/ Mg2+): as_printed: 'AH/AT 6.6 ± 1.3; ΔEa H-T -0.06 ± 0.12 (kcal/mol)' vs 'A_H/A_T 6.6 ± 1.3; ΔE_a H-T (kcal/mol) -0.06 ± 0.12'


Enzymes and steps (`kie_compare_meta2.py`):

## enzymes and steps

- TS_ECOLI_Y209W: pdb: '2G8X;4GEV' vs '4GEV;2G8X'
- TS_ECOLI_WT: ec, organism, uniprot, variant and pdb agree
  - TS_ECOLI_WT: reading 2 ('CH2H4fol (N5,N10-methylene-5,6,7,8-tetrahydrofolate)', 'C6 of the folate cofactor (6R-H of CH2H4fol)', 'exocyclic methylene carbon (C7) of the dUMP-derived intermediate', 'hydride') | reading 1 [('TS_ECOLI_WT_C5H', 'dUMP', 'dUMP C5 (covalent ternary intermediate)', 'active-site water oxygen (initial acceptor; the H-bond network acts as the general base)', 'proton'), ('TS_ECOLI_WT_C6H', '5,10-methylene-tetrahydrofolate', 'H4folate C6 (R-[6-3H]CH2H4folate labelling)', 'exocyclic methylene of the enzyme-bound dUMP intermediate', 'hydride')]
  - TS_ECOLI_Y209W: reading 2 ('CH2H4folate ((6R)-N5,N10-methylene-5,6,7,8-tetrahydrofolate)', 'C6 of H4folate (cofactor after methylene transfer; 6R-H of CH2H4folate)', 'C7 (exocyclic methylene) of the dUMP-derived intermediate (Complex D)', 'hydride') | reading 1 [('TS_ECOLI_Y209W_C6H', '5,10-methylene-tetrahydrofolate', 'H4folate C6 (R-[6-3H]CH2H4folate labelling)', 'exocyclic methylene of the enzyme-bound dUMP intermediate', 'hydride')]
