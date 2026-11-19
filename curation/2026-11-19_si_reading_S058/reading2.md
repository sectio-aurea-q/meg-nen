# Reader 2 — SI of S058 (Hu 2016, Angew. Chem., 10.1002/anie.201603592)

Source read in full: /home/claude/hu/sources/S058_Hu2016_AngewChem_SI.txt. Answers only from what the file prints.
Arithmetic cross-checks are marked as "reader's check" and are not statements of the source.

## a) Heavy substrate

- **Perdeuterated (uniformly deuterated) linoleic acid, "D-LA".** Not a site-specific label (no 11,11-d2 or
  similar is printed anywhere).
  - Location: 1.1 General Information. Quote: "Perdeutero linoleic acid (D-LA) was isolated from a mixture of algal fatty acid"
- **Source:** Cambridge Isotope Laboratories, algal fatty acid methyl esters, catalogue DLM2497-0, isolated by
  Ag-silica column chromatography (ref. [1], Mogul/Johansen/Holman 2000).
  - Quote: "Cambridge Isotope Laboratories (Methyl esters U-D 97%-98%, DLM2497-0)"
- **Isotopic enrichment:** "U-D 97%-98%" is printed for the purchased methyl-ester mixture; the enrichment of the
  isolated D-LA itself is not stated. How the methyl esters were converted to the free acid: not stated.
- **Light substrate:** linoleic acid >99 % purity ("H-LA"), Sigma-Aldrich (1.1).
- **Deuterated positions as an explicit list:** not stated (only "Perdeutero" / "U-D").

## b) Buffer and pH; pressure dependence

- **Buffer:** 0.1 M borate, pH 9.0.
  - Location: 2.1. Quote: "the pH value of 0.1 M borate buffer (pH=9.0)"
  - Also 1.2 (enzyme storage): "buffer exchanged in 100 mM borate (pH 9.0)"
  - Caveat: Section 1.4 (the kinetics procedure itself) does not name the assay buffer or pH. The assignment rests
    on 1.3(2), 1.3(3) ("in borate buffer") and 2.1, which discuss the buffer as a factor "of steady-state kinetic assays".
- **Pressure dependence of pH:** measured with phenolphthalein as indicator (absorbance at 553 nm), ref. [5]; pH falls
  by about 0.3 up to about 1 kbar; shown in Figure S1.
  - Location: 1.3(2). Quote: "the pH value only decreases by ~0.3 when the pressure is up to 1 kbar"
  - Location: 2.1. Quote: "decreased ca. 0.3 for every 1,034 bar increase (Figure S1)"
- **Treatment:** neglected, no correction applied; justification is pH-independence of kcat and kcat/Km between pH 8
  and 10 (ref. [9]).
  - Location: 2.1. Quote: "the observed changes in pH could be neglected"
- pH values at the intermediate pressures 344 and 688 bar: not stated in the text (only in Figure S1, which the text
  file does not reproduce). Temperature dependence of the buffer pH: not stated.

## c) Temperatures at each pressure

- **15, 20, 25, 30 and 35 °C** at each of 1, 344, 688 and 1034 bar (one common set; no pressure-specific set printed).
  - Location: 1.4. Quote: "water bath circulator at 15°C, 20°C, 25°C, 30°C and 35°C"
  - Location: 1.4. Quote: "under pressure at 1, 344, 688 and 1034 bar"
- Tables S3–S6 print the same grid as 288, 293, 298, 303, 308 K × 1, 344, 688, 1034 bar, with a value in every cell
  for WT, I553V and L546A (kcat-H, kcat-D, Dkcat).
- Temperature accuracy/stability: not stated. Pre-incubation: 2 min of the substrate stock at the intended temperature (1.4).

## d) How kcat, Dkcat, Ea and ΔEa were obtained

- **kcat:** product 13-(S)-HPOD followed at 248 nm (not 234 nm); initial rates at a range of substrate and enzyme
  concentrations fitted to the Michaelis–Menten equation.
  - Location: 1.4. Quote: "initial rates fitted to the Michaelis-Menten equation to extract first order rate constants (kcat)"
  - Extinction coefficients at 248 nm (1.3(1)): 10,700 (1 bar), 10,800 (344), 10,900 (688), 11,100 (1034 bar) M-1 cm-1.
  - Concentrations corrected for compression with a compressibility factor σ = Va.p/Vh.p (Eq. S1–S3, values in Table S2,
    1.0147–1.0435). Quote: "the compressibility factor was introduced to obtain the initial rate and substrate concentration"
  - Dead time: 10–30 s to raise pressure plus 30 s stabilisation (1.4).
  - Substrate concentration range used in the kinetic fits: not stated ("a range"). Linear vs non-linear fit, software: not stated.
- **Ea:** kcat at the five temperatures fitted to the Arrhenius equation, weighted by the errors of the individual kcat values.
  - Location: 1.4. Quote: "The errors associated with individual kcat values were used to weight the Arrhenius fits."
  - Quote: "fitted to the Arrhenius equation to determine the enthalpy of activation (Ea) and prefactor (A)"
- **ΔEa:** difference Ea(D) − Ea(H) (the Δ symbol is lost in the text file; the sentence prints as "Ea is calculated …").
  - Location: 1.4. Quote: "calculated based on the difference between Ea(D) and Ea(H)"
  - Error propagation for ΔEa: not stated.
- **Dkcat:** the SI text does not say how Dkcat was formed. Reader's check: the tabulated Dkcat equals kcat-H / kcat-D of
  the same cell (e.g. WT, 1 bar, 288 K: 267 / 4.03 = 66.3) in 58 of 60 cells; two L546A cells deviate (see f).
- **Temperature at which the Dkcat of main-text Table 2 stands:** not stated in the SI. The SI gives Dkcat at all five
  temperatures (Tables S3–S5); which one was carried into Table 2 cannot be taken from this file.
- **Iron correction** (normalisation of kcat to iron content): not stated. The word iron does not occur in the SI.
  Enzyme concentration determination: not stated. Only printed concentrations: stock "80 M" (unit prefix lost),
  and Figure S2 caption "0.42 nm" (H-LA panels) and "6.5 nm" (D-LA panels) for WT.
- Meaning of the bracketed numbers in Tables S1, S3–S6 (SD, SE, fit error; number of replicates): not stated.

## e) Tables with kcat(H), kcat(D), Dkcat at single temperatures and pressures

Yes. Full grids, 5 temperatures (288, 293, 298, 303, 308 K) × 4 pressures (1, 344, 688, 1034 bar), each value with an
uncertainty in brackets:

| Table | Enzyme | Content | Units as printed |
|---|---|---|---|
| S3 | WT | kcat-H, kcat-D, Dkcat (20 cells each) | none printed |
| S4 | I553V | kcat-H, kcat-D, Dkcat (20 cells each) | kcat-H none; kcat-D "(s-1)" |
| S5 | L546A | kcat-H, kcat-D, Dkcat (20 cells each) | kcat-H "(s-1)"; kcat-D "(10-2 s-1)" |
| S6 | L754A | kcat-H only (20 cells) | "(10-1 s-1)" |

Quotes: "Table S3 Kinetic parameters for WT under different temperatures and pressures"; likewise S4 (I553V), S5 (L546A), S6 (L754A).

Corner values for orientation (1 bar / 1034 bar, at 288 K and 308 K):

| Enzyme | Quantity | 1 bar, 288 K | 1 bar, 308 K | 1034 bar, 288 K | 1034 bar, 308 K |
|---|---|---|---|---|---|
| WT | kcat-H | 267 (6) | 359 (8) | 260 (23) | 635 (26) |
| WT | kcat-D | 4.03 (0.07) | 6.02 (0.23) | 4.90 (0.09) | 12.10 (0.50) |
| WT | Dkcat | 66.3 (1.9) | 59.6 (2.6) | 53.1 (4.9) | 52.5 (3.0) |
| I553V | kcat-H | 167 (9) | 241 (3) | 169 (30) | 401 (4) |
| I553V | kcat-D | 1.55 (0.01) | 3.05 (0.05) | 1.94 (0.03) | 5.53 (0.09) |
| I553V | Dkcat | 108 (6) | 79.0 (1.6) | 87.1 (15.5) | 72.3 (1.4) |
| L546A | kcat-H | 6.10 (0.09) | 9.83 (0.02) | 7.83 (0.16) | 16.53 (0.53) |
| L546A | kcat-D (10-2 s-1) | 4.47 (0.07) | 10.07 (0.10) | 6.97 (0.10) | 19.60 (0.17) |
| L546A | Dkcat | 137 (3) | 97 (1) | 112 (3) | 84.3 (2.8) |

Other tables:
- **Table S1:** not absolute values but ratios S = value at 344 / 688 / 1034 bar divided by the 1-bar value, for kcat-H,
  kcat-D and Dkcat, only at 288 and 308 K, for WT, I553V, L546A and L754A (L754A: kcat-D and Dkcat "N.D.").
  Quote: "S is the ratio of kinetic parameters at the pressure listed relative to ambient pressure"
- **Table S2:** compressibility factors only, no kinetics.
- **Figure S3:** plots of kcat-H and Dkcat versus pressure, 15–35 °C (enzyme not named in the caption; no numbers in the text).
- **Ea, ΔEa, Arrhenius prefactors:** not tabulated in the SI. Km values: not tabulated.

## f) Contradictory or unclear

1. **Table S1, WT, 308 K, 1034 bar, S(kcat-D) printed 2.10.** Reader's check from Table S3: 12.10 / 6.02 = 2.01. The other
   entries of that row fit (S(kcat-H) 635/359 = 1.77; S(Dkcat) 52.5/59.6 = 0.88), and 1.77 / 2.10 would give 0.84, not 0.88.
   The 2.10 is inconsistent with Table S3.
2. **Table S1, L754A, 288 K, 1034 bar, S(kcat-H) printed 4.24.** Reader's check from Table S6: 9.94 / 2.20 = 4.52.
   (L754A is outside the three enzymes of Table 2, noted for completeness.)
3. **Table S5 (L546A), 293 K, two cells where Dkcat does not equal kcat-H / kcat-D** (reader's check, tolerance 1.5 %):
   - 1 bar: 7.17 / 0.0557 = 128.7, printed Dkcat 124 (3).
   - 344 bar: 7.07 / 0.0660 = 107.1, printed Dkcat 116 (2). In the same cell kcat-H falls from 7.17 (1 bar) to 7.07
     (344 bar), the only place in Table S5 where kcat-H decreases with pressure. Which of the three numbers is wrong
     cannot be decided from the file.
   All 20 WT cells, all 20 I553V cells and the other 18 L546A cells agree within rounding.
4. **Wrong table reference.** 1.4 says the compressibility factor is in Table S1 ("Table S1 summarizes the value");
   it is in Table S2, as 2.1 says ("compressibility factors (Table S2)").
5. **Temperature range.** Kinetics at 15–35 °C (1.4, Tables S3–S6), but the stability test names "the extreme of
   temperature (5 and 35°C)" (1.5). 5 °C is not a kinetics temperature anywhere else in the SI.
6. **Assay buffer not named in 1.4**; taken from 1.2, 1.3 and 2.1 (see b).
7. **pH shift wording.** 1.3: "~0.3 when the pressure is up to 1 kbar"; 2.1: "ca. 0.3 for every 1,034 bar increase".
   Same magnitude, but the second reads as a slope, the first as a total over the range.
8. **Units missing.** Table S3 prints no units for WT kcat; Table S4 none for kcat-H. By analogy with the other tables
   s-1 is likely, but it is not printed.
9. **Terminology.** kcat is called "first order rate constants"; Ea is called "enthalpy of activation" although it comes
   from an Arrhenius fit.
10. **Dkcat temperature for Table 2 and any iron correction: not stated** (see d). Table 2 of the main text cannot be
    reconstructed from the SI text alone without knowing these two points.
11. **Error type and replicate number** of the bracketed values: not stated.
12. **Table S6, 1034 bar, 308 K: 15.85 (0.11)** — the uncertainty is roughly 4–8 times smaller than its neighbours
    (0.42, 0.55, 0.75, 0.90). Unclear, possibly a misprint; not decidable from the file.
13. **Section heading 1.5** prints as "1.5 Steady-state kinetics under high pressure Protein Stability under high
    pressure" (heading of 1.4 repeated); table of contents gives "1.5 Protein stability under high pressure".
14. **Extraction losses in the text file** (not necessarily in the original): Greek letters and micro prefixes are
    missing ("80 M", "220 M", "200M", "0.5-5 L", "248,1 bar", "Ea is calculated" for ΔEa); Eq. S2/S3 are truncated
    ("[SLO] = [SLO]obs×S2)"); Eq. S4 is empty; enzyme concentration in Figure S2 printed as "nm". Section 2.2 refers
    once to "eq (4)" instead of (S4).
15. **Figure S2 caption** gives enzyme concentrations only for WT; values for I553V and L546A assays: not stated.
