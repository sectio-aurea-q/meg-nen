I read all five papers and wrote the three CSV files. A check script re-opened the files and matched every number I entered to its cell in the saved HTML: 37 numbers, no mismatches. No ΔE_a value needed a sign change. All rows use the paper's own fitted parameters or Northrop-derived intrinsic KIEs (kcat/KM, competitive, intrinsic), except the S048 ^Dk_cat and ^Dk_burst values, which are observed KIEs. The main point the curator needs to settle is the human wild-type DHFR values in S049 and S050: I left them out as probably cited.

# Second reading ai-2, sources S046–S050

**Files**
- out/measurements.csv (11 rows)
- out/temperature.csv (13 rows)
- out/enzymes.csv (13 rows)
- Scripts, including the check script verify.py: work/

**Rules applied to all five papers**
- **Intrinsic KIEs:** every intrinsic KIE comes from competitive H/T and D/T kcat/KM KIEs via the Northrop method. So all are quantity = kcat/KM, method = competitive, kind = intrinsic.
- **Error type:** no table states it, so every error field is "type not stated".
- **Temperature range:** S047, S049 and S050 give none in the main text, so those fields are empty.
- **XML use:**
  - S046: equations and inline ΔE_a values were readable only in the XML MathML.
  - S048 and S050: the equations are images in both the HTML and the XML. For these I inferred the ΔE_a direction from the numbers and say so in the notes.

## S046 Gurevic 2018 (E. coli thymidylate synthase, N177S and N177D)

**Entered**
- **measurements.csv (4 rows):** N177D intrinsic H/T KIE from Table 4, column KIE^exp, all at pH 7.5:
  - 23.33 ± 2.90 at 278.15 K
  - 21.23 ± 3.00 at 288.15 K
  - 18.40 ± 2.96 at 298.15 K
  - 14.86 ± 2.50 at 308.15 K
- **temperature.csv (2 rows), Table 2:** 278.15–308.15 K, n = 4, pH 7.5:
  - N177S: A_H/A_T 1.4 ± 0.3, ΔE_a 1.5 ± 0.1 kcal/mol
  - N177D: A_H/A_T 0.3 ± 0.1, ΔE_a 2.4 ± 0.2 kcal/mol

**Left out**
- **Cited WT values:**
  - WT columns of Tables 1 and 2 (ref 49; A_H/A_T 5.3 ± 1.0, ΔE_a 0.2 ± 0.1).
  - WT KIE^exp in Table 4: 7.54 at 278 K, 7.58 at 293 K, 7.22 at 303 K, 7.39 at 313 K. WT was not measured in this study: the caption says the WT data are from ref 12, and those temperatures are not this study's 5/15/25/35 °C.
- **Other cited values:**
  - R166K ΔE_a,T−H 3.6 ± 0.1 (ref 9; readable only in the XML).
  - WT proton-abstraction curve in Fig. 2 (ref 30).
- **Computational values:** Table 4 KIE^QC, KIE^κ, KIE^γ, KIE^total, and all of Table 5.
- **SI or figures only:**
  - Observed and intrinsic KIEs and commitment factors (Tables S1–S3). The N177S intrinsic KIEs exist only there and in Fig. 3a.
  - Proton-abstraction KIE_obs versus [MTHF] (Fig. 2).
- **Model fits:** average donor–acceptor distances in Table 3, and the model's ΔE_a thresholds of 1 kcal/mol.

**Judgement calls**
- **Temperature:** Table 4 prints 278/288/298/308 K; the Methods give 5/15/25/35 °C. I entered 278.15–308.15 K.
- **pH and n:** pH 7.5 and the four temperatures (n = 4) come from the Methods section on hydride-transfer KIEs.
- **Sign:** eq 2 in the XML defines ΔE_a,T−H = E_a,T − E_a,H, which is heavy minus light, so I entered the values as printed.
- **Transfer:** hydride, from MTHF C6 to the exocyclic methylene C7 of intermediate E, as the paper assigns it.

**Inconsistencies**
- The Table 2 row label reads "ΔE_a,H-T" (and "A_h/A_t"), but eq 2 and the text use ΔE_a,T−H for the same numbers. The text also has the typo "ΔAE_a,T-H". The Table 5 header says "ΔG^OC", the caption "ΔG^QC".
- Tables 2 and 4 agree: 0.3·exp(2.4/RT) gives 23.1 at 278.15 K and 15.1 at 308.15 K, against 23.33 and 14.86 printed.

## S047 Stojković 2010 (E. coli DHFR, I14A)

**Entered**
- **temperature.csv (1 row), Table 1:** A_H/A_T 4.7 ± 0.5, "ΔE_aT-H" 0.39 ± 0.06 kcal/mol. The main text gives no temperature range, n or pH.
- **enzymes.csv:** PDB 4QLE.

**Left out**
- wtDHFR column (Ref 10: 7.0 ± 1.5, −0.1 ± 0.2).
- Hydride-transfer rates of 450 s⁻¹ and 33 ± 3 s⁻¹ (refs 30 and 31; rates, not KIEs).
- H/D and D/T parameters: footnote b says "data not shown".
- KIEs in the supplementary information (Table 1S, Fig. 1S) and in Fig. 1.
- Molecular-dynamics distances and the semiclassical range 0.3–1.7.

**Judgement calls**
- **Sign:** the paper does not define the direction of ΔE_a. I read "T-H" as E_a(T) − E_a(H), which fits the text: the heavier isotope gains more at higher temperature, so the KIE falls with temperature. No sign change.
- **Inconsistency:** the "*" after the ΔE_a label has no footnote.

## S048 Wang 2014 (E. coli DHFR, light l-DHFR and heavy h-DHFR)

**Entered**
- **measurements.csv (7 rows):**
  - ^Dk_cat (Table 1; 298.15 K; kcat; noncompetitive; observed):

    | | l-DHFR | h-DHFR |
    |---|---|---|
    | pH 9 | 2.5 ± 0.4 | 2.5 ± 0.2 |
    | pH 7 | 1.18 ± 0.07 | 1.11 ± 0.08 |

  - ^Dk_burst (Table 2; 298.15 K; pH 7; single_turnover; noncompetitive): l-DHFR 3.2 ± 0.1, h-DHFR 3.15 ± 0.08.
  - ^Dk_hyd for h-DHFR: 3.88 ± 0.05, intrinsic H/D, 298.15 K, pH 9.
- **temperature.csv (2 rows), Table 3, h-DHFR, pH 9:**
  - 25–45 °C: A_H/A_T 5.6 ± 1.9, ΔE_a 0.1 ± 0.2 kcal/mol
  - 5–25 °C: A_H/A_T 0.01 ± 0.003, ΔE_a 4.1 ± 0.3 kcal/mol

  Both fits cover only part of the measured 5–45 °C range.
- **Heavy enzyme:** h-DHFR is entered as its own construct, variant "heavy (13C, 15N, 2H)".

**Left out**
- **Cited (ref 31):** l-DHFR ^Dk_hyd 3.6 ± 0.2 (the text cites ref 31), the l-DHFR column of Table 3, and the l-DHFR data in Fig. 4.
- **Heavy-enzyme effects:** the Table 1 "h-KIE" column and the Table 4 ratios.
- **SI or figures only:** Table S1, Fig. 4, and pre-steady-state data at other pH values.
- **Model fits:** donor–acceptor distances.

**Judgement calls**
- **^Dk_hyd conditions:** 25 °C comes from the Table 2 title. I used pH 9 because the Methods run the competitive experiments at pH 9, although the Table 2 title says pH 7.
- **Sign:** eq 2 is an image. I read ΔE_a,H-T as E_a(T) − E_a(H) because A_H/A_T = 0.01 needs a positive exponent to give a KIE above 1, and the text says the h-DHFR KIE rises below 25 °C. No sign change.

**Inconsistencies**
- The Table 2 title "pH 7" also covers the ^Dk_hyd column, whose values come from pH 9 experiments.
- The Table 3 distance error "± 0.0008" looks misprinted (not entered).

## S049 Li 2019 (human DHFR)

**Entered**
- **temperature.csv (3 rows), Table 1, pH 9.0:**
  - M53W: A_H/A_T 1.5 ± 0.2, ΔE_a 1.03 ± 0.06 kcal/mol
  - S145V: A_H/A_T 1.4 ± 0.2, ΔE_a 0.7 ± 0.1 kcal/mol
  - M53W/S145V: A_H/A_T 0.030 ± 0.008, ΔE_a 3.7 ± 0.1 kcal/mol
- The text defines ΔE_a(T-H) = Ea_T − Ea_H, so no sign change.

**Left out**
- **E. coli columns (refs 43 and 50):** WT 7.0/−0.1; M42W 2.8/0.58; G121V 7.4/0.23; M42W-G121V 0.011/3.6, ΔΔE_a 2.8.
- **ΔΔE_a 2.0 ± 0.2** for the double mutant (a derived quantity).
- **Human WT 6.6 ± 0.8 / −0.1 ± 0.1 (needs the curator's check):**
  - Against leaving it out: the text says the WT was measured here, and its Table 1 column carries no reference.
  - For leaving it out:
    - The Fig. 2 legend cites ref 44 (Francis et al. 2016, Biochemistry 55, 1100) for the wild-type data.
    - SI Table S1 covers only the mutants.
    - S050 prints the same values and attributes WT to the same paper.

**Inconsistencies**
- Left and right panels are swapped between the text and the Fig. 2 legend.
- Typo "S14V"; the definition is printed with unbalanced brackets.
- The ΔΔE_a arithmetic is consistent.

## S050 Li 2021 (human DHFR, evolution-site variants)

**Entered**
- **temperature.csv (5 rows), Table 2, pH 9.0:**

  | Variant | A_H/A_T | ΔE_a (kcal/mol) |
  |---|---|---|
  | F32M | 0.2 ± 0.1 | 2.8 ± 0.2 |
  | F32L | 0.1 ± 0.1 | 6.5 ± 0.3 |
  | F32L/PP26N/PEKN62G | 19.3 ± 6.7 | −0.01 ± 0.2 |
  | Δ62-PEKN | 3.1 ± 0.3 | 0.5 ± 0.1 |
  | Δ26-PPLR/Δ62-PEKN | 5.2 ± 0.5 | 0.1 ± 0.1 |

- Variant names are joined with "/" where the paper uses "-".

**Left out**
- WT hsDHFR row: the Fig. 2 and Fig. 3 legends cite ref 2 for it, and Table 3 marks WT "From ref (2)".
- Donor–acceptor distance column (model fit), steady-state Table 3, and the KIEs, which are only in the supplementary information.

**Judgement calls**
- **Sign:** eq 2 is an image and the text does not give a direction. I read "(T-H)" as E_a(T) − E_a(H); F32M has A_H/A_T 0.2 yet KIEs above WT, which needs that sign.
- **Triple mutant:** I entered the Table 2 error (± 0.2) rather than the text's ± 0.05, because ± 0.2 matches the A_H/A_T uncertainty.

**Inconsistencies**
- **F32L:** the printed pair gives 0.1·exp(6.5/RT) ≈ 5.8×10³ at 25 °C, so either A_H/A_T or ΔE_a is misprinted.
- **Abstract numbering:** the abstract says "F28M/F28L", but residue 28 in UniProt P00374 is Leu; the text's F32 is correct.
- **Triple-mutant text vs table:** the text gives ΔE_a −0.01 ± 0.05 (table ± 0.2) and a distance of 3.09 Å (table 3.10).
- **Wrong table reference:** the text cites "Table 1" for values that are in Table 2.
- **Typos and dates:** Fig. 2 legend "F3M". The text dates the F32M form to ~797 million years ago, Table 1 to ~499.
- **Deleted span:** the Introduction speaks of deleting "26PP" while the variant is named "Δ26-PPLR", so the exact deleted span is unclear.

## Enzyme metadata
- **UniProt:**
  - P0A884, EC 2.1.1.45 (thymidylate synthase)
  - P0ABQ4, EC 1.5.1.3 (E. coli DHFR)
  - P00374, EC 1.5.1.3 (human DHFR)
- **Numbering:** every named or mutated residue matches UniProt with Met1 counted as 1. Only S047 prints an EC number; the others come from UniProt.
- **PDB:**
  - I searched RCSB by UniProt accession and by sequence identity of at least 0.9, then aligned each entity's sequence to UniProt.
  - The only exact match for an entered variant is 4QLE (I14A), which cites a different paper (10.1021/jp5059963).
  - No entry cites any of the five DOIs.
  - For the many E. coli DHFR wild-type entries the field stays empty. The notes name the papers' own entries 1RX2 and 1RX4, which carry D37 where UniProt has N37.
  - RCSB writes human DHFR mutations without Met1 (e.g. "F31G" = F32G).
