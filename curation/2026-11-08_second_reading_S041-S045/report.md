# Second reading (ai-2) of S041–S045

I wrote the second reading for S041–S045. **The five papers yield 7 single-condition values (all from S045) and 7 fitted Arrhenius series.** Every value was re-checked cell by cell against the HTML. The papers contain no non-enzymatic KIE values. Two points need curator attention: three ΔEa values had to be sign-flipped, and S043 and S045 each contain an internal numeric inconsistency (details below).

Files: `out/measurements.csv` (7 rows, all S045), `out/temperature.csv` (7 rows), `out/enzymes.csv` (5 rows); scripts in `work/`.

## Conventions that apply to all rows
- **kie_type:** primary in every row (the transferred hydrogen: dUMP C5-H, or MTHF C6-H for S045 hydride).
- **method:** competitive in every row. All experiments are ³H/¹⁴C mixtures of both isotopologues.
- **quantity:** kcat/KM in every row. Each paper says its competitive KIEs are on V/K or kcat/Km. Intrinsic values from the Northrop method keep kcat/KM, as SCHEMA requires.
- **kind:** intrinsic only where the paper calls the KIEs intrinsic.
- **Scientific notation:** AH_AX values and their errors are written with the printed mantissa (8.3×10⁻⁶ → `8.3e-6`; error 0.1×10⁻² → `0.1e-2`).
- **Temperatures:** 5, 15, 25, 35 °C → 278.15–308.15 K, n = 4, wherever the paper lists them.
- **Error type:** no paper states it for any entered value.
- **XML use:** only for the equations that define ΔEa (S041 Eq. 5, S042 Eq. 10, S043 Eq. 5, S044 Eq. 5, S045 Eq. 4) and for the S045 Methods inline formula showing the KIE is a ratio of kcat/Km. Table headers and footnote links in the XML are identical to the HTML.
- **Figures and SI:** no values were read off plots. Supporting information was not available.

### ΔEa sign decisions (dEa_kcal = Ea(heavy) − Ea(light))

| Paper | How the paper defines ΔEa | Printed | Entered |
|---|---|---|---|
| S041 | Eq. 5: k_L/k_H = (A_L/A_H)exp(−ΔEa/RT), so light − heavy | −8.0 (H/T), −2.44 (D/T) | **flipped:** +8.0, +2.44 |
| S042 | Eq. 10, light − heavy | −11.9 | **flipped:** +11.9 |
| S043 | Text: ∆Ea = E_aL − E_aT | −7.70 | **flipped:** +7.70 |
| S044 | Label ΔE_a(T−H), heavy − light | 9.0 | 9.0, no change |
| S045 | Label ΔE_a(T−H), heavy − light | 0.5, 6.0 | no change |

- **S044 and S045 equations contradict their labels.** Both print the equation with exp(−ΔE_a(T−H)/RT). Taken literally, that would make KIE ≈ 10⁻¹² given A_H/A_T ≪ 1. The positive values only make sense as heavy − light, so I followed the label.
- **Cross-check:** both papers cite the S041 E. coli proton-abstraction value as +8.0, where S041 printed −8.0 as light − heavy. This confirms the heavy − light reading.

## S041 (Wang 2010)
- **Entered (temperature.csv):** Table 1, Proton Transfer column, wild type, intrinsic.
  - H/T: A_H/A_T 8.3e-6 ± 1.0e-6, dEa 8.0 ± 0.1
  - D/T: A_D/A_T 2.8e-2 ± 0.1e-2, dEa 2.44 ± 0.03
  - 278.15–308.15 K, n = 4, pH 7.5 (Experimental Section: Tris/HCl, adjusted at each temperature), 3 μM CH₂H₄folate.
- **Left out:**
  - Hydride Transfer column, cited (ref 32): 6.8 ± 2.8; 1.9 ± 0.3; 0.02 ± 0.25; −0.04 ± 0.08.
  - Semi-classical limits column, cited (refs 11, 22, 45): 0.5–1.6 and 0.9–1.2.
  - "KIE of unity" in the text, cited (ref 41).
  - Per-temperature observed and intrinsic KIEs: SI only, plotted in Fig. 2A.
  - Commitments (Fig. 3) and KIE vs conversion (Fig. 4): plots only.
- **Judgement calls:** the acceptor is an oxygen (the abstract calls it a "C-H-O proton transfer"), but the base is not named. Error type for the fit is not stated.
- **Inconsistencies:** none inside the paper. Across papers, the cited hydride ΔEa (Agrawal 2004) has the opposite sign here (+0.02 as light − heavy) compared with S043 (−0.02 as light − heavy) and S044 (+0.02 as heavy − light).

## S042 (Ghosh 2015)
- **Entered:** Table 1, Y94F column, H/T intrinsic: A_H/A_T 1.46e-8 ± 1.2e-8, dEa 11.9 ± 0.45.
  - 278.15–308.15 K, n = 4, pH 7.5 (Methods: adjusted at each temperature), 10 μM CH₂H₄folate.
  - "⟂" (U+27C2) in both HTML and XML read as "×".
- **Left out:**
  - Wild-type column, cited (ref 19 = S041): 8.3 (±1.0)×10⁻⁶ and −8.0 (±0.1).
  - Table 2, fit parameters of a phenomenological model, not isotope effects: DAD_L 3.61±0.03 / 3.78±0.03 Å; ΔG° 9.44±0.5 / 12.80±0.6 kcal/mol.
  - Figs. 2 (reproduced from ref 18), 3 and 6: plots only.
  - The ref-18 intrinsic KIE for Y94F at 25 °C: cited, no number given.
  - D/T Arrhenius parameters: not reported.
- **Inconsistencies:**
  - The PDB IDs are swapped. The Introduction says "WT and mutant, PDB IDs 2FTO and 1TYS, respectively"; the Fig. 4 legend says WT = 1TYS, Y94F = 2FTO. RCSB confirms 2FTO is Y94F, so the legend is right.
  - The ΔEa label is inconsistent. The row header reads "ΔE_a,H/T" and the value is negative. The caption and text use "ΔE_a,T/H", and the text treats it as positive (">1 kcal/mol … see Table 1").

## S043 (Abeysinghe 2015)
- **Entered:** Table 1, Proton Abstraction column, Y209W, H/T intrinsic: A_H/A_T 1.4e-6 ± 0.1e-6, dEa 7.70 ± 0.40.
  - 278.15–308.15 K, n = 4, pH 7.5 and 200 μM CH₂H₄folate (Section 3.3).
- **Left out (cited, footnotes a, b, c):**
  - Proton-abstraction wild type, "Data from [16]": 8.3 (±1.0)×10⁻⁶, −8.0 (±0.1).
  - Hydride wild type, "Data from [25]": 6.8 (±2.8), −0.02 (±0.25).
  - Hydride Y209W, "Data from [15]": 3.6 (±0.9), −0.5 (±0.1).
- **Left out (other):** Km fold-changes (ref 15; not KIEs); Figs. 5–7 (plots only); Table S2 and Fig. S1 (SI only).
- **Judgement call:** the Y209W proton-abstraction column carries no footnote, and the Introduction says this step is studied here, so I treated it as primary. The Fig. 6 legend's "Y209W [15]" I read as referring to the hydride panel.
- **Inconsistencies:**
  - **The printed Y209W parameters imply an inverse KIE.** They give k_H/k_T of 1.57 at 5 °C, 0.62 at 25 °C and 0.40 at 35 °C. The text calls the KIEs "similar" to wild type, whose parameters give 16.0, 6.07 and 3.92. An A_H/A_T of 1.4×10⁻⁵ would give 15.7, 6.17 and 4.05, so the exponent is probably a typo. I entered the values as printed.
  - The text says Table 1 lists H/T and D/T parameters; the table shows only H/T.
  - The "2G80" the paper cites is a yeast UTR4 protein, not TSase; probably 2G8O was meant. "2G8M" is obsolete and was replaced by 4GEV.

## S044 (Islam 2015)
- **Entered:** Table 1, row "PA (R166K)", H/T intrinsic: dEa 9.0 ± 0.10, A_H/A_T 3.30e-6 ± 1.4e-6.
  - 278.15–308.15 K, n = 4, pH 7.5 (Methods: adjusted at each temperature).
- **Left out:**
  - PA (WT), cited (ref 16): 8.0 (±0.16), 8.3 (±1.0)×10⁻⁶.
  - HT (WT), cited (ref 15): 0.02 (±0.25), 6.8 (±2.80).
  - HT (R166K), cited (ref 42): 3.62 (±0.02), 0.023 (±0.003). The row is marked with ref 42 and the Methods say the hydride data were reported there, so I treated it as cited.
  - kcat and Km fold-changes (ref 42); the secondary KIE on C6 of dUMP (ref 42, no number).
  - Table S1 and Fig. S1 (SI only); Figs. 2 and 4 (plots only).
- **Inconsistencies:**
  - The Eq. 5 sign problem described above.
  - The Chemicals section lists "[6-³H] dUMP", but the experiments use [5-³H] dUMP.
  - The Synthesis section says C146 attacks "C5_U"; everywhere else it attacks C6.
  - "~25–30% excess to dUMP (1.35 mM)" does not make clear which compound is at 1.35 mM.
  - Across papers, the wild-type ΔEa error is ±0.16 here versus ±0.1 in S041.

## S045 (Islam 2018)
- **Entered (measurements.csv), human TSase, wild type:**
  - Table 2 (hydride transfer, both Mg²⁺ conditions):

    | Quantity | With Mg²⁺ | Without Mg²⁺ |
    |---|---|---|
    | Observed H/T | 3.05 ± 0.03 | 3.19 ± 0.03 |
    | Observed D/T | 1.61 ± 0.02 | 1.64 ± 0.01 |
    | Intrinsic H/T | 11.0 ± 0.9 | 11.6 ± 0.8 |

  - Text: observed H/T on proton abstraction at high MTHF, 1.10 ± 0.02.
- **Entered (temperature.csv):**
  - Table 3, hydride: dEa 0.5 ± 0.1, A_H/A_T 2.2 ± 0.2 (278.15–308.15 K, n = 4). The text repeats 0.5 ± 0.1; entered once, from the table.
  - Table 3, proton abstraction: dEa 6.0 ± 0.4, A_H/A_T 3.6e-4 ± 2.3e-4.
- **Left out:**
  - Table 1: steady-state parameters, not KIEs.
  - Table 2 E. coli rows, cited (refs 8, 18): 4.14±0.02 / 7.07±0.03; 1.65±0.01 / 1.81±0.04; 7.4±0.9 / 7.4±0.5.
  - Table 3 E. coli columns, cited: hydride (ref 8) 0.2±0.1, 5.6±1.8; proton abstraction (ref 22) 8.0±0.1, 8.3(±1.3)×10⁻⁶.
  - "Mg²⁺ … seven-fold" (refs 8, 9; not a KIE); Figs. 3–5 (plots only); S1/S2 Figs and XLSX files (SI only).
- **Judgement calls:**
  - Table 2 assigned to the hydride transfer from the text above it.
  - Table 2 states no temperature, so temperature_K is empty. The hydride KIEs were measured at 5–35 °C.
  - For the 1.10 value, 298.15 K is inferred from "The pH of each mixture was adjusted at 25°C"; the exact MTHF concentration is not stated, only "high".
  - The Mg²⁺ condition of the fitted hydride series is not stated.
  - The temperature range of the proton-abstraction series is not stated, so T_min/T_max are empty.
  - pH 7.5 from Methods in all rows.
- **Inconsistencies:**
  - The Eq. 4 sign problem described above.
  - **The Table 3 hydride parameters do not match Table 2.** They give intrinsic KIEs of 5.44 at 5 °C, 5.12 at 25 °C and 4.98 at 35 °C. Table 2 gives 11.0 and 11.6. The text also says human intrinsic KIEs are larger than E. coli's, whose ref-8 parameters give about 7.8.
  - Across papers, the cited E. coli A_H/A_T error is ±1.3×10⁻⁶ here versus ±1.0×10⁻⁶ in S041.

## Enzymes (enzymes.csv)
- **UniProt:** E. coli TSase is P0A884 (EC 2.1.1.45; the K-12 entry, as the papers do not state a strain). Human TSase is P04818 (EC 2.1.1.45). S044 and S045 give no EC number, so I took it from UniProt.
- **Numbering:** matches UniProt at every named position (E. coli Y94, R166, Y209, C146, E58, H147, N177, W80; human C195).
- **RCSB searches:** by UniProt accession, by ≥90% sequence identity to the wild type, and by 100% identity to each mutant sequence. No entry cites any of the five study DOIs.

| Paper | Variant | pdb | Notes |
|---|---|---|---|
| S041 | WT | empty | many E. coli entries (68); the paper names none |
| S042 | Y94F | 2FTN;2FTO | only Y94F; both cite Roberts 2006 (ref 47) |
| S043 | Y209W | 2G8X;4GEV | 2G8X's RCSB mutation field also lists "N-terminus is carbamylated" (not engineered); 4GEV cites ref 15 |
| S044 | R166K | empty | no R166K entry exists; only R166Q (1FFL, 1FWM) |
| S045 | WT (human) | empty | 61 entries; the paper names 1HVY. Tag removed by thrombin; no truncation stated |

- 1TYS, which S042 names as a wild-type structure, has no mutation listed in RCSB, but its sequence has Ser at position 146 by my alignment.

No facts from memory were used for this reading.
