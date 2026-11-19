# S058 (Hu 2016, Angew. Chem. SI) - Reader 1 answers

Source read in full: `/home/claude/hu/sources/S058_Hu2016_AngewChem_SI.txt`. Answers are taken only from what the file prints. "Not stated" means the file does not print it. Arithmetic checks in (f) are my own recomputation from printed numbers and are marked as such.

## a) Heavy substrate

- **Name:** perdeutero linoleic acid, abbreviated D-LA. Section 1.1 General Information: "Perdeutero linoleic acid (D-LA) was isolated from a mixture of algal"
- **Positions:** no positions are named. The only labelling information is "perdeutero" and the supplier specification "U-D". Section 1.1: "(Methyl esters U-D 97%-98%, DLM2497-0)". A specific label such as 11,11-d2 is not stated anywhere in the file.
- **Source:** isolated from an algal fatty acid mixture bought from Cambridge Isotope Laboratories, by Ag-silica column chromatography, citing ref. [1] (Mogul, Johansen, Holman, Biochemistry 2000). Section 1.1: "purchased from Cambridge Isotope Laboratories ... following Ag-silica column chromatography.[1]"
- **Isotopic purity of the isolated D-LA itself:** not stated (the 97%-98% refers to the purchased methyl ester mixture).
- **Light substrate, for reference:** Section 1.1: "Linoleic acid (>99% purity) (H-LA) was purchased from Sigma-Aldrich."

## b) Buffer and pH; pressure dependence of pH

- **Assay buffer:** Section 1.4 (steady-state kinetics) does not name the assay buffer or its pH explicitly. The buffer is identified only indirectly:
  - Section 1.3 (2): "pressure dependence of the pH value of 0.1 M borate buffer"
  - Section 2.1: "the pH value of 0.1 M borate buffer (pH=9.0)"
  - Section 1.2 (enzyme storage): "buffer exchanged in 100 mM borate (pH 9.0)"
  - Section 1.3 (3) (CMC): "around 220 µM in borate buffer[6]"
  So: 0.1 M borate, pH 9.0 (at ambient pressure), with the caveat that the kinetics paragraph itself is silent.
- **Pressure dependence of pH:** measured with phenolphthalein as indicator (absorbance at 553 nm), Figure S1.
  - Section 1.3 (2): "the pH value only decreases by ~0.3 when the pressure is up"  (continues: "to 1 kbar, consistent with previous theoretical calculations")
  - Section 2.1: "decreased ca. 0.3 for every 1,034 bar increase (Figure S1)"
  - Treated as negligible. Section 2.1: "the observed changes in pH could be neglected" (justified by kcat and kcat/Km being unaltered between pH 8-10, ref. [9]).
  - Figure S1 caption: "Pressure effects on pH value of borate buffer (0.1 M)". The figure itself is not in the text file; no pH values at 344 or 688 bar are printed.
- **Temperature dependence of the buffer pH:** not stated.

## c) Temperatures at each pressure

- Section 1.4: "water bath circulator at 15°C, 20°C, 25°C, 30°C and 35°C"
- Pressures, Section 1.4: "under pressure at 1, 344, 688 and 1034 bar"
- Tables S3, S4, S5 list the same five temperatures as 288, 293, 298, 303, 308 K at every one of the four pressures (1, 344, 688, 1034 bar); every cell of the 4 x 5 grid is filled for kcat-H, kcat-D and Dkcat. So the same five temperatures apply at each pressure; no pressure has a reduced temperature set.
- Figure S3 caption agrees: "in the temperature range from 15-35°C"
- A different temperature (5 °C) appears only for the stability assay, see (f).

## d) How kcat, Dkcat, Ea and ΔEa were obtained

- **kcat:** initial rates, product (13-(S)-HPOD) formation followed at 248 nm, fitted to Michaelis-Menten. Section 1.4: "initial rates fitted to the Michaelis-Menten equation to extract first order"  (continues "rate constants (kcat)").
  - Extinction coefficients at 248 nm, Section 1.3 (1): 10,700 M-1 cm-1 at 1 bar; "344, 688, 1034 bar were measured as 10800, 10900, 11100"
  - Compressibility correction of rate and concentrations, Section 1.4: "the compressibility factor was introduced to obtain the initial rate"; Eq. (S1) σ = Va.p / Vh.p; Eqs. (S2), (S3) scale [SLO] and [LA] (the equations are garbled in the text file, see (f)).
  - Dead time, Section 1.4: "typically 10-30s to raise the pressure and another 30s"
  - Substrate and enzyme concentration ranges: only "a range of substrate and enzyme concentration"; numerical ranges not stated.
- **Ea:** Arrhenius fit of kcat versus temperature, weighted. Section 1.4: "kcat values at different temperatures were fitted to the Arrhenius equation" and "errors associated with individual kcat values were used to weight the". The fit also gives the prefactor A. Whether the fit is linear (ln k vs 1/T) or non-linear: not stated.
- **ΔEa:** Ea(D) minus Ea(H). Section 1.4: "calculated based on the difference between Ea(D) and Ea(H)" (the sentence prints "Ea", not "ΔEa", as its subject; see (f)).
- **Dkcat:** the SI gives no sentence defining how Dkcat was computed. The tabulated Dkcat values in Tables S3-S5 agree with the ratio kcat-H / kcat-D of the tabulated values (my recomputation; two cells deviate, see (f)). How the Dkcat errors were propagated: not stated.
- **Temperature at which the Dkcat (and kcat) of main-text Table 2 stands:** not stated in the SI. The SI tabulates Dkcat at all five temperatures and never refers to main-text Table 2.
- **Iron correction:** not stated. The file contains no mention of iron content, metal analysis (e.g. ICP) or normalisation of kcat to iron. Only purity is given, Section 1.2: "purity of the enzymes was greater than 90% as visualized by SDS-PAGE".
- **Ea, ΔEa, A values:** not tabulated anywhere in the SI.

## e) Does the SI tabulate kcat(H), kcat(D), Dkcat at single temperatures and pressures?

Yes. Every table gives values with an uncertainty in parentheses (the kind of uncertainty, e.g. s.d. or s.e., is not stated).

| Table | Title quote | Content |
|---|---|---|
| S3 | "Kinetic parameters for WT under different temperatures and pressures" | WT: kcat-H, kcat-D, Dkcat at 288, 293, 298, 303, 308 K x 1, 344, 688, 1034 bar (60 values). No unit printed for kcat. |
| S4 | "Kinetic parameters for I553V under different temperatures and pressures" | I553V: same grid. kcat-H without unit; "kcat-D (s-1)"; Dkcat. |
| S5 | "Kinetic parameters for L546A under different temperatures and pressures" | L546A: same grid. "kcat-H (s-1)"; "kcat-D (10-2 s-1)"; Dkcat. |
| S6 | "Kinetic parameters for L754A under different temperatures and pressures" | L754A: kcat-H only, "kcat-H (10-1 s-1)", same grid. No kcat-D, no Dkcat. (L754A is not one of the three variants asked about.) |
| S1 | "Impact of pressure on rate constants and KIEs at the extremes" | Not absolute values: ratios S(kcat-H), S(kcat-D), S(Dkcat) = value at 344/688/1034 bar divided by the 1 bar value, at 288 and 308 K only, for WT, I553V, L546A, L754A. Footnote [a]: "S is the ratio of kinetic parameters at the pressure listed relative". L754A kcat-D and Dkcat "N.D.", footnote [b]: "The kcat-D values were too slow to be accurately determined." |
| S2 | "Compressibility factors under different temperatures and pressures" | Factor σ at 288-308 K for 344, 688, 1034 bar (range 1.0147 to 1.0435). No kinetic data. |

Anchor values at 298 K, 1 bar (kcat-H / kcat-D / Dkcat): WT 332 (7) / 5.25 (0.13) / 63.2 (2.1); I553V 210 (4) / 2.19 (0.03) / 95.9 (2.3); L546A 8.10 (0.14) s-1 / 6.63 (0.20) x 10-2 s-1 / 122 (4).

## f) Contradictory or unclear points

Textual:

1. **Table number of the compressibility factors.** Section 1.4 says "Table S1 summarizes the value as a function of ranging temperature"; Section 2.1 says "leading to the use of compressibility factors (Table S2)". The printed table with that content is Table S2; Table S1 holds the pressure ratios.
2. **ΔEa sentence.** Section 1.4 prints "Ea is calculated based on the difference between Ea(D) and Ea(H)", directly after stating that Ea comes from the Arrhenius fit. Read literally it is circular; a "Δ" was probably lost in the text conversion, but the file does not print it. The sign convention Ea(D) - Ea(H) is therefore implied by word order only.
3. **Temperature range.** Kinetics at 15-35 °C (Section 1.4, Tables S3-S6), but Section 1.5 gives the stability test at "the extreme of temperature (5 and 35°C)". 5 °C is outside the kinetic range; possibly a misprint for 15 °C, not resolvable from the file.
4. **Size of the pH shift.** "~0.3 when the pressure is up to 1 kbar" (Section 1.3) versus "ca. 0.3 for every 1,034 bar increase" (Section 2.1). Compatible numerically, but the second wording implies a per-interval slope that was only measured up to about 1 kbar.
5. **Assay buffer not named in the kinetics section** (see b); borate pH 9.0 follows only from Sections 1.2, 1.3 and 2.1.
6. **Ea called an enthalpy.** Section 1.4: "to determine the enthalpy of activation (Ea) and prefactor (A)". An Arrhenius Ea is not ΔH‡; which quantity main-text Table 2 reports cannot be decided from the SI.
7. **kcat called "first order rate constants"**, and units are missing for all kcat blocks of Table S3 and for kcat-H in Table S4 (s-1 is printed only in S4 kcat-D, S5, S6).
8. **Garbled symbols in the text file** (conversion loss, not necessarily in the original): Eqs. (S2)/(S3) print as "[SLO] = [SLO]obs×S2)"; Eq. (S4) is empty; "µ" is missing ("80 M", "200 M LA", "220 M", "0.5-5 L"); "ε" missing in "(248,1 bar = 10,700 M-1 cm-1)".
9. **Section heading 1.5** prints as "1.5 Steady-state kinetics under high pressure Protein Stability under high pressure", repeating the 1.4 title; the table of contents has "1.5 Protein stability under high pressure".
10. **Figure S2 caption** gives enzyme concentration as "0.42 nm" and "6.5 nm" (presumably nM; not stated).
11. **Table S2:** factors are identical for 288/293 K and for 298/303 K (e.g. 1.0155, 1.0155, 1.0151, 1.0151, 1.0147 at 344 bar). Not explained.
12. **Main-text Table 2 link:** the SI never says which temperature the kcat/Dkcat of main-text Table 2 refer to, and gives no Ea/ΔEa values, no Arrhenius prefactors and no iron correction (see d).
13. **Stability window versus assay length:** activity retention was shown "following reaction at 1,034 bar for 2 min" (Section 2.1), with a dead time of up to about 1 min (Section 1.4). The length of the trace used for initial rates is not stated.

Numerical (my recomputation from printed values; tolerance 2%):

14. **Table S5, L546A, 293 K:** printed Dkcat 124 (3) at 1 bar, but kcat-H / kcat-D = 7.17 / 0.0557 = 128.7; printed Dkcat 116 (2) at 344 bar, but 7.07 / 0.0660 = 107.1. All other 58 Dkcat cells of Tables S3-S5 match the ratio within 2%.
15. **Table S1 versus Table S3, WT, 308 K, 1034 bar:** S(kcat-D) printed 2.10 (0.11), but 12.10 / 6.02 = 2.01.
16. **Table S1 versus Table S6, L754A, 288 K, 1034 bar:** S(kcat-H) printed 4.24 (0.24), but 9.94 / 2.20 = 4.52. (L754A is outside the three variants asked about.)
17. **Non-monotonic temperature dependence in single cells**, relevant for the weighted Arrhenius fits: WT kcat-H at 688 bar runs 421 (50), 475 (38), 476 (13) for 293-303 K, and WT Dkcat at 688 bar is 54.5 at 288 K but 71.1 at 293 K; WT Dkcat at 1034 bar 49.3 at 298 K then 59.8 at 303 K. Large errors are printed for these cells; no comment in the SI.
18. **Table S6, 1034 bar, 308 K:** error 15.85 (0.11) is much smaller than the neighbouring errors (0.42 to 0.90); possibly a misprint, not resolvable.
