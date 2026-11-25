# Reading 2B (reader ai-2, blind), Group B: S067–S070 (cytochrome P450)

Read only the photos listed for Group B in papers.txt, SCHEMA.md, CURATION.md, enzymes.csv and steps.csv. No other reading folder opened. All numbers read from the photos, digit by digit, with zoomed crops for every table.

Summary of what was entered: 45 isotope effects (S067: 42, S069: 3, S068: 0, S070: 0), 0 temperature series, 0 rate constants. 6 new enzymes, 29 new steps. No existing enzyme_id or step_id fits: enzymes.csv/steps.csv contain no P450 entry.

## Proposed rows for sources/first_sources.csv

```
source_id,enzyme,doi,year,journal,volume,pages,title,first_authors
S067,"cytochrome P450 (CYP1A2, 2B1, 2C9, 2E1, P450cam)",10.1021/bi9729864,1998,Biochemistry,37,7039-7046,Evaluation of Cytochrome P450 Mechanism and Kinetics Using Kinetic Deuterium Isotope Effects,"Higgins, L.; Bennett, G. A.; Shimoji, M.; Jones, J. P."
S068,cytochrome P-450 (phenobarbital-induced rat liver microsomes),,1990,J. Org. Chem.,55,3992-3997,Active Site Dynamics of Toluene Hydroxylation by Cytochrome P-450,"Hanzlik, R. P.; Ling, K.-H. J."
S069,cytochrome P-450 (phenobarbital-induced rat liver microsomes),,1989,Biochem. Biophys. Res. Commun.,160,844-849,Deuterium Isotope Effects on Toluene Metabolism. Product Release as a Rate-Limiting Step in Cytochrome P-450 Catalysis,"Ling, K.-H. J.; Hanzlik, R. P."
S070,cytochrome P450cam (Pseudomonas putida),,1982,Biochemistry,21,370-377,Stereochemistry and Deuterium Isotope Effects in Camphor Hydroxylation by the Cytochrome P450cam Monooxygenase System,"Gelb, M. H.; Heimbrook, D. C.; Mälkönen, P.; Sligar, S. G."
```

DOI notes. None of the four copies prints a DOI.
- S067: the page prints the code `S0006-2960(97)02986-3`, the closing code `BI9729864` (p. 7046) and a download line `pubs.acs.org/bichaw/article-pdf/37/19/7039/1082329/bi9729864.pdf`. `10.1021/bi9729864` follows from these, but the page does not print it as a DOI. It goes into the rows with a note and needs a check.
- S068: a download path with `jo00300a010` is printed (from my earlier notes). The DOI was left empty because it is not printed.
- S069: only `0006-291X/89 $1.50` is printed. DOI left empty.
- S070: only `0006-2960/82/0421-0370$01.25/0` is printed. DOI left empty.
- S068 issue 13 and S069 issue 2 come from papers.txt and the page headers ("Vol. 160, No. 2, 1989"). S067 is "Vol. 37, No. 19, 1998" and S070 is "Vol. 21, No. 2, 1982".
- The S067 photo set also contains an hbz order slip (Aufsatzbestellung), which was ignored.

## S067 Higgins et al., Biochemistry 1998, 37, 7039–7046

Pages read: 7039, 7040, 7041, 7042, 7043, 7044 (twice), 7045 (twice), 7046. The set is complete, and everything was legible after zooming.

Decisive sentences:
- Temperature and pH (p. 7040, Incubation Conditions): "All incubations using HepG2-expressed CYP were run for 20 min in a shaking water bath at 37 °C … in a total volume of 5 mL of 50 mM KPi buffer, pH 7.4, 2 mM MgCl2. For P450cam, the assays were carried out at 37 °C for 20 min in a 1-mL reaction mixture in 50 mM KPi buffer, pH 7.4, 200 mM KCl, 1.5 µM P450cam, 3 µM Pd, 1.5 µM PdR, and 0.3 mM NADH." This covers all experiments, including the competitive ones. 37 °C becomes 310.15 K.
- Table 1 footnote a: "Each result is the average of three determinations, and the numbers in parentheses indicate the standard deviation in the last significant digit of the mean isotope effect value." It continues: "…the standard deviations reflect the precision of the method only and do not take into account systematic and day-to-day errors." This gives error_type sd and n = 3. I read the error from the parenthesis by placing the digit (4.24(1) becomes 0.01; 7(1) becomes 1). That is a reading of the notation, not a calculation, but please check it.
- Table 3 footnote a: "The numbers after the ± sign are propagated errors." This covers the intramolecular and the noncompetitive columns. Six Table 1 values are reprinted in that intramolecular column: 2E1 Br, CH3 (xylene), OCH3 and Cl; 2B1 Cl; 1A2 Cl. Those six rows therefore have `conflicting` (SD in Table 1, propagated error in Table 3). I entered Table 1 and did not enter the Table 3 intramolecular column a second time.
- Table 3 footnote b: "Intermolecular competitive values are expressed as the mean ± standard deviation of three samples." This gives sd and n = 3.
- Observed or intrinsic. Table 3 footnote: "The intermolecular isotope effects are masked, as compared to the unmasked intramolecular isotope effects, which closely approximate intrinsic values (see Table 1)." On p. 7043: "…bonded to the same carbon atom permit close measurement of the intrinsic isotope effects". Both are hedged ("closely approximate", "close measurement"), so all rows are observed.
- Transfer type: "rates of hydrogen atom abstraction" (abstract), so H_atom.

Coding choices to check:
- Intramolecular CH2D experiments: quantity `other`, method `competitive` (competition within one molecule), kie_type `primary`. The note says the value includes the geminal secondary effect.
- Intermolecular experiments: DV is `kcat`, D(V/K) is `kcat/KM`, d3 (or d6 for p-xylene) against d0.
- Table 1 row "CH2D" is p-xylene-α-²H1-α′-²H1 (footnote b). Row "H" is toluene-α-²H1. In Table 3, the 2E1 row "CH3" is p-xylene, d0 vs d6 (footnote d).
- The Table 1 rows run on a slant in the photo. Each Table 1 value whose row is printed again in Table 3 agrees with it, which confirms that the cells were assigned correctly.
- Enzyme species: the pages read do not name a species for 2E1/2B1/1A2/2C9. They say "four mammalian CYP isoforms" from the HepG2/vaccinia system (ref. 9, Gonzalez et al. 1991). I left organism, UniProt and EC empty, and the ids use `NS`. P450cam is given P. putida P00183, EC 1.14.15.1, by name. This is my assignment and needs checking.

Considered and not entered:
- Table 2 Vmax (nM min⁻¹) and V/K (min⁻¹) for d0/d3/d6 CYP2E1 substrates: single temperature, so rule 4b is not met.
- Table 2 SE, r², and n points: not isotope effects.
- Table 3 intramolecular column, reprints of Table 1: 6.75 ± 0.03, 5.45 ± 0.05, 4.24 ± 0.01, 6.75 ± 0.02, 8.06 ± 0.12, 7.06 ± 0.02. These are duplicates. Only the difference in meaning (and 8.06 vs 8.1) is recorded in the notes.
- p. 7046 text: p-bromotoluene "1.5 and 2.1", p-chlorotoluene "1.6 and 3.2", 2B1 "3.1", 1A2 "2.5", intramolecular "8.1 and 7.1". These are rounded restatements of table values. The text gives 3.1 for 2B1 where Table 3 prints 3.21; this is noted in the row.
- p. 7045 text: ranges "from 1 to 3", "from 4 to 8", "1.2–2.7", and "values of 1.2–3.2" (p. 7046). These are ranges.
- Figure 1 log Vmax = 0.11σ⁺p + 1.73, r² = 0.588: a regression, not an isotope effect.
- Figure 2, ln kH/kD against σ⁺: plot only.
- σ⁺ values (−0.78, 0.31 as printed for CH3, 0, 0.11, 0.15, 0.66): taken from ref. 33.
- 70 % (toluene benzylic share) and ~95 % (p-xylene): from refs 42, 43.
- 2C9/H and P450cam/H: "nd" (low product formation).
- CYP3A4: product too low, no value.

## S068 Hanzlik & Ling, J. Org. Chem. 1990, 55, 3992–3997

Pages read: all article pages in the set. Neighbouring-article pages were ignored.

Nothing was entered because no temperature is stated (rule 11). On the pages read, the Experimental section gives no incubation temperature; for the incubation procedure it refers to earlier papers (refs 2, 8, 15). Whether the referenced S069 conditions (37 °C) may be carried over is for adjudication. Under rule 11 as written ("its source states"), I did not carry them over.

Isotope effects that would otherwise be eligible, all without a temperature:
- Table II: P1 4.59 ± 0.54, P2 5.72 ± 0.60, P3 7.30 ± 0.72; S1 0.953 ± 0.094, S2 0.995 ± 0.097, S3 1.187 ± 0.146, S4 1.270 ± 0.134.
- Relative rate constants: kHHH 1.000 ± 0.056, kHHD 1.048 ± 0.084, kHDD 1.052 ± 0.057, kDHH 0.217 ± 0.022, kDHD 0.183 ± 0.012, kDDD 0.144 ± 0.012.
- Text: CH3/CD3 6.93 and 8.67; abstract intrinsic 7.4; P/B D0/D5 0.966 ± 0.062, D3/D8 0.936 ± 0.030; r1 9.639 ± 0.993, r2 2.874 ± 0.210, r1/r2 4.437 ± 0.639, S2/S3 1.109 ± 0.159.
- Eq. 5 analysis: kH/kD 6.29 and 7.38 (Σ-ratio 0.675, kH/k4 2.33, kD/k4 0.316).
- DV 1.92, D(V/K) 3.6, and alcohol/cresol D(V/K) 6.3. 1.92/3.6 restate S069, which is cited.
- Not entered on other grounds: LM2 Vmax 2.68 and D(V/K) 1.24 ± 0.28 (other work, ref. 32); octane P 7.6 and S 1.11 (other work); Table III mole fractions (not KIEs); commitment and partition ratios (Z 0.56, kH/kr 1.86, k−1/kH 0.682, k−1/kD 4.28, commitments 2.25, 1.01, Q1–Q4); "intrinsic presumably ≥ 6" (a bound).
- Error meaning: Table I is SD, n = 3, as noted from the source. Table II errors: my notes do not record their stated meaning, so recheck if a temperature is ever accepted.
- These S068 notes were written from my first pass over the pages and were not re-opened at the end.

## S069 Ling & Hanzlik, BBRC 1989, 160, 844–849

Pages read: 844 (twice), 845, 846 (twice), 847, 848, 849 (Acknowledgments/References). All legible.

Decisive sentences:
- Temperature (p. 845): "Incubation mixtures were combined at 0-4°C in a final volume of 6.0 mL … sealed under air, vortexed briefly, and incubated at 37°C in a shaking water bath for 60 min." This gives 310.15 K.
- pH: the incubation contains "0.45 mL buffer", with no composition or pH on the pages read, so pH is empty.
- Table 1 footnote: "Saturating concentrations (10.4 mM) of toluene (D0) and deuterated toluenes (D1-D3) were incubated separately in triplicate … Results are means ± S.D. for triplicate incubations."
- p. 847: "the apparent DV for benzyl alcohol formation is 1.92 (i.e. (69 x 836)/(24.3 x 1237); see Tables 1 and 2)". Also: "a mixture of D0 (34.9%) and D3 (65.1%) was incubated (in triplicate) … ca. 1% conversion … D(V/K) = (65.4/34.6)/(34.9/65.1) = 3.53".
- p. 847: "we deduce that the combined primary and secondary deuterium isotope effect on toluene hydroxylation is 7.06. … the intrinsic isotope effect for benzylic abstraction during toluene hydroxylation (which is ≥ 7.06) is being strongly suppressed". 7.06 is entered as calculated by the source (rule 4), kind observed (a bound, not an identification), quantity `other`.
- Table 2 does not say what its ± is, so DV 1.92 ± 0.27 and D(V/K) 3.53 ± 0.08 are `not_stated`.

Considered and not entered:
- Table 2 cytochrome P-450-LM2 values 2.68 ± 0.29 and 1.24 ± 0.28: footnote a, "Calculated from data of White and McCarthy (ref. 12)", which is other work.
- DV = 0.67 for total metabolism (1237/836): an effect on total oxidation (benzylic plus ring), not on one hydrogen-transfer step. For adjudication.
- kH/k4 = 69/31 = 2.23 and kD/k4 = 24/76 = 0.316: partition ratios, not isotope effects.
- Table 1 mol-% and total nmol (D0–D3): product yields at one temperature, not rate constants of a step (rule 4b not met).
- Product composition 65.4 mol-% d0 / 34.6 mol-% d3: an input.
- Ratio 69:31 and 24:76: summary approximations.
- Constraint ranges 2.5 ≤ k5/k3 ≤ 250 and 0.0017 ≤ k3/kH ≤ 0.17: model bounds.
- D1 and D2 (toluene-7-d1, -7,7-d2): only product percentages; the intramolecular KIE is from earlier work (ref. 2).
- P450cam/norcamphor statement: other work (refs 9, 10).

## S070 Gelb, Heimbrook, Mälkönen, Sligar, Biochemistry 1982, 21, 370–377

Pages read: 370 (twice), 371, 372, 373, 374 (twice), 376, 377 (twice). Page 375 is missing from the copy, as papers.txt says. Table II on p. 373 is blurry but readable after zooming.

Nothing was entered.

Decisive sentences:
- p. 372 Methods: "NADH-driven enzymatic turnovers were conducted under saturating conditions in 1 mL of 100 mM potassium phosphate buffer, pH 7.0, containing 1.5 µM substrate-free cytochrome P450, 3.3 µM putidaredoxin, 2.5 µM putidaredoxin reductase, and 300 µM substrate." No temperature is given for these or for the exogenous-oxidant reactions (pH 7.0), on any page read.
- Single-turnover (oxyferrous decay) experiments: "equilibrated in a 10 °C water bath for 5 min".
- Table I footnote a: "The normalized NADH oxidation rate refers to the observed reaction velocity with nondeuterated substrate divided by the velocity with deuterated substrate under identical conditions."

Considered and not entered:
- Table I, Vmax H/Vmax D: camphor-5-exo-d1 1.23 ± 0.05; 5,6-dideuterated camphor (drawn with D at C5 and C6) 1.13 ± 0.05; camphor-5-endo-d1 1.16 ± 0.05; 5-exo-bromocamphor-5-endo-d1 1.15 ± 0.05. Not entered because no temperature is stated (rule 11). The ± meaning is not stated. Page 375 might hold a temperature but is missing.
- Text p. 373: "(kH/kD = 1.1–1.2)": a range, no temperature.
- Oxyferrous P450 decay with 5-endo-d1 bromocamphor and nondeuterated bromocamphor: "0.18 and 0.19 µM/s, respectively" at 10 °C. These are rate constants (initial velocities) at one temperature only, so rule 4b is not met. Their ratio is not printed.
- Competitive V/K: "no change in the substrate deuterium content was observed (data not shown)". No number.
- Table II, alcohol-d1/alcohol-d0 product ratios. Each cell has two independent experiments plus an average, for NADH/O2, iodosobenzene, m-CPBA and H2O2:
  - 5-exo-d1: 1.15, 1.20 (av 1.18); 1.47, 1.50 (1.48); 1.58, 1.69 (1.64); 1.19, 1.21 (1.20).
  - 5,6-d2: 4.40, 4.62 (4.51); 3.77, 3.75 (3.76); 4.03, 3.88 (3.96); 3.85, 3.70 (3.78).
  - 5-endo-d1: 4.25, 4.52 (4.39); 4.72, 4.65 (4.69); 4.22, 3.99 (4.11); 3.97, 3.90 (3.94).
  - These are the experimental parameters A and B (A = kH endo/kD exo, B = kH exo/kD endo). They include the geometric partition and are not isotope effects of one step. The intramolecular effects I_exo and I_endo appear only as curves against G in Figure 2 (plot), so they are not entered. No temperature either.
- Label fractions a = 0.84, b = 0.04, c = 0.10, d = 0.05, e = 0.02, f = 0.93: inputs to a correction.
- Synthesis isotopic purities (98 % d1 and similar) and NMR couplings: not isotope effects.

## Illegible or uncertain spots
- S067 Figure 2 caption: σ⁺ for CH3 is printed "0.31" without a minus sign as far as I can see. It was not entered.
- S070 Table II is soft-focus. The digits were confirmed by zoom, and each average agrees with its pair. The Table I second-row structure is drawn with D at two adjacent ring carbons (5,6). My identification of it is uncertain, and it was not entered.
- The /tmp/crops folder used early in this reading was later found to contain a crop from another paper (Group A, MR/PETNR Table 1), apparently written by a parallel process. I did not use that image. All S067 values were re-read from fresh crops in a private folder, /tmp/ai2B.
