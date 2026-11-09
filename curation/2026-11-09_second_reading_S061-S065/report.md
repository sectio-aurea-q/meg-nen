# Second reading (reader `ai-2`) — MEG-NEN sources S061–S065

Saved by the curator from the second reader's answer of 9 November 2026; the list of its output files was shortened.

Files written: `out/measurements.csv` (35 rows: S061 3, S062 6, S063 2, S064 6, S065 18), `out/temperature.csv`
(17 rows: S061 2, S062 1, S063 6, S064 6, S065 2), `out/enzymes.csv` (11 rows: S061 1, S062 2, S063 1, S064 6,
S065 1).

Method: numbers were read from the saved HTML with BeautifulSoup (`work/dump_tables.py` keeps `<sup>`/`<sub>` markers
so footnote markers stay attached to the right header or cell). The PMC XML was used **only** for equations and
symbols the HTML lost — this is flagged in the relevant `notes`. Every entered value+error pair was re-matched
verbatim against the normalised HTML text in a final pass; the only non-verbatim pairs are the unit conversions
(S065 kJ/mol → kcal/mol) and the `(± x)` parenthesised forms, which were checked individually.

---

## S061 — Anoz-Carbonell et al. 2020, *Antioxidants* 9, 772 (human NQO1)

**Entered — measurements (3).** Table 2 KIE column: `1.8 ± 0.1` (row A→B) and `1.8 ± 0.3` (row B→C); text
(Sect. 3.3) `2.3 ± 0.5` at 6 °C under saturating coenzyme. All: NADH → FAD N5, hydride, `primary`, `H/D`,
`single_turnover`, `noncompetitive`, `observed`, pH 7.4, 279.15 K.

**Entered — temperature (2).** Table 2 rows A→B and B→C: `A_H/A_D` 1.3 ± 0.6 and 13 ± 6; `dEa_kcal` 0.2 ± 0.4 and
−1.1 ± 0.7; `Ea_light_kcal` 6.1 ± 0.2 and 10.9 ± 0.5. T 278.45–293.15 K.

**Judgement calls.**
- *Equation direction.* Eq. (2) is lost in the HTML; the XML gives `KIE = kHT/kDT = HTkobs/DTkobs`, i.e. light/heavy
  as required. Noted in the rows.
- *Sign.* The Table 2 header defines ΔEa = E_aDT − E_aHT = Ea(heavy) − Ea(light), identical to the schema — no sign
  change.
- *Temperature of the Table 2 KIE column.* Footnote `a` ("Values at 6 °C") is attached only to the `HTkobs` and
  `DTkobs` headers, not to the KIE, ΔEa or A_H/A_D headers. 279.15 K was assigned because Eq. (2) is literally the
  ratio of those two footnoted numbers and 78/44 = 1.77 reproduces the printed 1.8 ± 0.1. The alternative reading
  (the text calls the KIEs "apparent" and temperature-independent over 5.3–20 °C, so the column could be a series
  mean) is recorded in `notes`. Supporting the ambiguity: 8.9/5.3 = 1.68 does not reproduce the printed 1.8 ± 0.3
  exactly, and the ±0.3 is larger than the propagated ratio error.
- *2.3 ± 0.5 entered despite being extrapolated.* It is the ratio of the limiting (saturating) constants
  k_HT1 = 284 ± 17 s⁻¹ and k_DT1 = 122 ± 5 s⁻¹ from hyperbolic fits to Eq. (1) — a fitted saturating value, not one
  measured at a stated coenzyme concentration. Entered because the paper prints it as a KIE with an error and an
  explicit temperature (6 °C), and because `single_turnover` in SCHEMA covers a saturating pre-steady-state rate
  constant; it sits in its own row because the condition (saturating) differs from Table 2's (equimolar). Flagged in
  `notes`.
- *quantity / method / kind.* `single_turnover`: stopped-flow pre-steady-state constants from spectral deconvolution
  of the reductive half-reaction. `noncompetitive`: NADH and NADD in separate mixings. `observed`: the paper calls
  them "apparent" and says intrinsic values are not yet obtainable.
- *pH* 7.4 from Methods 2.4; *T range* 5.3–20 °C from Methods 2.5. `n_temperatures` not stated.

**Left out.** Table 1 rate constants (rate constants, not isotope effects; the paper prints no KIE from them and the
reader computed none); the hedged "a KIE_B→C may also be close to a value of 2"; Table 3 (Eyring ΔH‡ and ΔS‡ per
isotope: HT A→B 5.3 ± 0.3, B→C 11 ± 1; DT A→B 5.7 ± 0.6, B→C 9.8 ± 0.8 kcal/mol; ΔS‡ −31 ± 1, −16 ± 2, −30 ± 2,
−20 ± 3 cal·mol⁻¹·K⁻¹), because the paper prints no isotope difference and no A′_H:A′_D, so no Eyring row could be
filled without recomputing; Appendix A viscosity slopes (0.55 ± 0.05, 1.6 ± 0.1); cited values (K_M^NADH
160–240 µM, k_cat 180–200 s⁻¹, K_d^Dic 1–20 nM, the theoretical KIE maximum of 8 of ref 78).

**Internal inconsistencies.**
1. **DT k_obsB→C differs between tables**: Table 1 (4R-NADD row) gives `6.3 ± 0.2 s⁻¹`, Table 2 (row B→C) gives
   `5.3 ± 0.2 s⁻¹`. The printed KIE 1.8 is closer to 8.9/5.3 = 1.68 than to 8.9/6.3 = 1.41.
2. Text rounds the table values: A_H/A_D "close to the unity" (table 1.3 ± 0.6) and "about 10" (table 13 ± 6); ΔEa
   "nearly 0" (0.2 ± 0.4 and −1.1 ± 0.7); KIEs "~1.8". Table values entered, text versions in `notes`.

---

## S062 — Panay & Fitzpatrick 2008, *Biochemistry* 47, 11118 (CvPheH)

**Entered — measurements (6).** Table 2 `Dkcat` with [ring-²H₅]-Phe: WT/6-MePH₄ `1.24 ± 0.04`; WT/DMPH₄
`1.43 ± 0.07`; I234D/6-MePH₄ `1.00 ± 0.01`; I234D/DMPH₄ `0.90 ± 0.03` (all 298.15 K, pH 7.2, `kcat`,
`noncompetitive`, `observed`). Text: tautomerization KIE `5.1 ± 1.0` (298.15 K, pH 7.0, `other`, `competitive`,
`observed`, `primary`); benzylic `10 ± 1` (298.15 K, pH 7.0, `other`, `competitive`, **`intrinsic`**, `primary`,
`H_atom`).

**Entered — temperature (1).** Benzylic series: `A_H/A_D = 0.29 ± 0.03`, `dEa_kcal = 2.1 ± 0.4`.

**Judgement calls.**
- *Sign and unit of ΔEa.* Eq. 7 is lost in the HTML; the XML gives
  `ln(kH/kD) = ln(AH/AD) + [Ea(D) − Ea(H)]/RT`, so the printed ΔEa is Ea(heavy) − Ea(light) — no sign change. The
  text prints no unit for 2.1 ± 0.4; kcal/mol is implied by eq 7 and confirmed numerically
  (0.29 × exp(2.1/RT) = 10 at 298 K, the printed KIE).
- *`kie_type = other` for the four Table 2 rows.* [ring-²H₅]-Phe labels all five ring hydrogens, and the Discussion
  says the observed effects "are combinations of the isotope effect on this step [Fe(IV)O attack on the ring, where
  the C4-D is not transferred] and the isotope effect on the subsequent tautomerization" (where a ring hydrogen *is*
  lost). It is therefore neither purely primary nor purely secondary; `transfer` left `unknown` and `acceptor` marked
  unassigned, with the composite spelled out in `notes`.
- *`kind = observed` for I234D/DMPH₄ (0.90 ± 0.03).* The paper says it "is thus **likely** to be the intrinsic
  isotope effect for that step with CvPheH also". Per CURATION rule 5 the hedge was read as short of an assertion and
  `observed` entered, with the paper's wording quoted in `notes`. **This is the single most likely point of
  disagreement with the first reading.**
- *`kind = intrinsic` for the benzylic 10 ± 1.* Here the paper is unhedged: it names the quantity "the intrinsic
  isotope effect on benzylic hydroxylation, D k_Benz".
- *`method = competitive` for 5.1 and 10.* Both are intramolecular competitions within one molecule (Ha vs Hb on one
  carbon; benzylic vs aromatic hydroxylation of one substrate), which SCHEMA puts under `competitive`.
- *`method = noncompetitive` for Table 2.* Eq. 3 (XML: `v/e = kcat·S/[KM + S(1 + Fi(Ev−1))]`) fits initial rates with
  `Fi` the fraction of deuterium in the substrate, i.e. rates of light and heavy substrate compared directly, not
  product fractionation.
- *`transfer = proton` for 5.1 and `H_atom` for 10.* The paper assigns no transfer type to the tautomerization;
  proton loss from the sp³ carbon is the best-supported reading (stated in `notes`). For the benzylic reaction it
  does: "hydrogen atom abstraction from the methyl group".
- *Temperature and pH from other sections.* 25 °C from "Enzyme assays" for Table 2, whose footnote `a` only says
  "Conditions as in Table 1"; pH 7.2 from the Table 1 footnote; pH 7.0 and 25 °C for the Table 3 and
  4-methylphenylalanine experiments from the Table 3 footnote and Experimental Procedures. The DMPH₄ concentration
  (250 µM) comes from Experimental Procedures — the Table 1 footnote lists only 150 µM 6-MePH₄.

**Left out.** Table 3 (`6.3 ± 0.5`, `4.1 ± 0.2`, `5.7 ± 0.3`, `4.4 ± 0.3`), which are product isotope ratios, not
isotope effects — the XML eqs 4 and 5 define them as `PD/PH = R1 = Dka(kb/ka)` and `PD2/PD = R2 = Dkb(ka/kb)`, a KIE
multiplied by an intramolecular branching ratio; only their geometric mean, the printed 5.1 ± 1.0, is an isotope
effect. Table 1 (storage effects), Table 4 (DMPH₄ oxidation rates), k_cat(trp)/k_cat(phe), DTT K_A 0.6 ± 0.2 mM.
Cited values: the rat PheH catalytic-domain benzylic KIE `12 ± 1` (ref 23); "For the three eukaryotic enzymes, the
isotope effects on the initial hydroxylation are all `0.90 ± 0.03`" (refs 7, 29, 34) — numerically identical to this
paper's own I234D/DMPH₄ value, a real trap, flagged in that row's `notes`; the rat tautomerization KIE of 5.1
(ref 29); the rat 34 % Hb preference (ref 29); 55 % benzylic hydroxylation by the rat enzyme (ref 23); the computed
isotope-insensitivity of the 1,2-hydride shift (footnote 2, ref 33). No temperature range for the benzylic series:
the text and the Fig. 2 legend state none, and the plot was not read, so `T_min_K`/`T_max_K` are empty; "each point
is the average of three experiments" are replicates, so `n_temperatures` is empty too; `Ea_light` not reported.

**Inconsistency.** The Abstract rounds Table 2 to 1.2, 1.4 and 0.9; table values entered.

---

## S063 — Eriksson, Kürten & Syrén 2017, *ChemBioChem* 18, 2301 (PtmT2)

**Entered — measurements (2).** `KIE = 7` (94 % D₂O, pD 6, 28 °C; printed as the word "seven", no error) and
`KIE = 4` (24/48/72 % D₂O mixed buffers, 28 °C, no error). Both: `solvent`, `H/D`, `other`, `competitive`,
**`intrinsic`**, pH 6, 301.15 K.

**Entered — temperature (6).** Table 1 `A_H/A_D` per D₂O concentration: 24 % `4.4 ± 0.5`, 48 % `3.9 ± 0.3`, 72 %
`4.2 ± 0.4`, 94 % `6 ± 2` (`dEa_kcal` left empty — see below). Plus the two forced-fit pairs from footnote [b]: 24 %
`A_H/A_D = 5`, `dEa_kcal = −0.060`; 48 % `A_H/A_D = 4`, `dEa_kcal = −0.020`. All T 280.15–303.15 K,
`n_temperatures = 10`.

**Judgement calls.**
- **Sign change applied.** Footnote [b] prints "Δ_{H–D}E_a of 60 and 20 cal mol⁻¹". Eq. (7) is lost in the HTML; the
  XML gives `ln KIE = −[(EaH − EaD)/R](1/T) + ln(AH/AD)`, so the printed quantity is Ea(H) − Ea(D) =
  Ea(light) − Ea(heavy), the opposite of the schema. Entered as `−0.060` and `−0.020` kcal/mol. Checked numerically:
  5 × exp(−0.060/RT) ≈ 4.5 at ~292 K, close to the measured mean KIE 4.4 (the reverse sign would give 5.6,
  inconsistent).
- *`dEa_kcal` empty for the four Table 1 columns.* Footnote [b]: the values come from "Arrhenius analysis … by using
  the average values of the isotope effect to determine A_H/A_D", i.e. the fit assumes a temperature-independent KIE
  (ΔEa = 0). By construction those A_H/A_D numbers equal the mean KIE over 7–30 °C; they were kept in
  `temperature.csv` (they are printed as Arrhenius prefactor ratios) and not also entered as measurements.
- *Forced fits kept as separate rows* because they are a different fit of the same data with a different A_H/A_D and
  a non-zero slope.
- *`kind = intrinsic`* because the paper states its design "would allow for determination of intrinsic … kinetic
  isotope effects (KIEs)" and Eq. (1) assigns the MS-accessed rate constant to `k_prot`. No individual value is
  labelled intrinsic, so this is explicitly flagged as a judgement call in `notes`. **Second likely disagreement
  point.**
- *`kie_type = solvent`* (the label is D₂O, which SCHEMA reserves for `solvent`), with a note that the effect is also
  primary on the transferred proton, delivered by the catalytic acid D313 in exchange with solvent. `substrate` holds
  the hydrogen acceptor molecule (GGPP) here, which is noted.
- *`quantity = other`*: by Eq. (1) the MS measurement reports on `k_prot`, not on k_cat or k_cat/K_M.
- *Errors* are "estimated error range based on 2 % uncertainty in pipetting" (footnote [c]), not fit errors.
- *`n_temperatures = 10`* counted from the explicit list in the Experimental Section (7.0, 12.0, 14.0, 16.0, 19.0,
  22.0, 24.0, 26.0, 28.0, 30.0 °C), consistent with footnote [a]'s "7 to 30 °C".

**Left out.** Table S1 (per-concentration KIEs at each temperature) and Table S2 (k_cat and k_cat/K_M in ¹H₂O and
²H₂O), both Supporting Information. The main text's prose solvent effects on macroscopic constants — "the
**approximatively twofold** reduction of k_cat in heavy water" and "an experimentally determined **twofold increase**
in k_cat/K_M in heavy water relative to that in light water (Table S2)" — were not entered: no number is printed,
only "approximately twofold", and the actual values live in Table S2. This is a judgement call — a curator who
accepts prose approximations would add two rows. Figure 1 (KIE vs T, and the Arrhenius plot) was not read off the
plot. Molecular-modelling distances (2.3 Å protonation distance, 2.9 Å vdW, 3.2 Å from ref 13, 1.7 Å MD from ref 19,
RMSD 2.1 Å) are computational or cited.

**Inconsistency.** None found inside the paper beyond the two coexisting fits of the same data (Table 1 body vs
footnote [b]), which the footnote itself explains.

---

## S064 — Hong et al. 2018, *Nat. Commun.* 9, 3900 (Kemp eliminase KE07)

**Entered — measurements (6).** Table 1 `kH/kD`, one row per enzyme variant: R1 `4.9 (0.2)`, R4 `5.6 (0.2)`, R5
`8.6 (0.2)`, R6 `6.5 (0.1)`, R7 `7.0 (0.2)`, R7-2 `7.3 (0.1)`. `primary`, `H/D`, `kcat`, `noncompetitive`,
`observed`, pH 7.25, 303.15 K.

**Entered — temperature (6).** Table 1, one row per variant: `A_H/A_D` 0.004 (0.0006), 0.005 (0.0009), 0.875
(0.1211), 0.181 (0.0126), 0.009 (0.0011), 0.005 (0.0003); `dEa_kcal` 4.3 (1.5), 4.2 (1.2), 1.4 (1.1), 2.2 (0.7),
4.0 (1.1), 4.4 (0.6); `Ea_light_kcal` 10.8 (1.1), 5.6 (0.8), 7.7 (0.8), 9.5 (0.5), 7.1 (0.7), 6.9 (0.4).
T 283.15–323.15 K, `n_temperatures = 8`.

**Judgement calls.**
- *Sign.* The column header is literally `Ea(D) − Ea(H)`, which is the schema's Ea(heavy) − Ea(light) — no change.
  Units kcal/mol per footnote `b`.
- *Temperature of the `kH/kD` column = 303.15 K.* No temperature is printed for that column: footnote `a` ("Values,
  at 303 K, …") marks only `kH`, `KM(H)` and `kcat/KM(H)`, while footnote `b` covers `Ea`, `ln A` and `kH/kD` as
  "calculated from the Arrhenius equation from rate constants measured at a range of temperatures (283–323 K)".
  303 K was entered because it is the only temperature the table states, and because back-solving the printed
  `A_H/A_D` and `Ea(D)−Ea(H)` against the printed `kH/kD` gives 301.0, 304.3, 302.4, 303.9 K for R4, R1, R7, R7-2 and
  308.3/309.1 K for R5/R6 (mean ≈ 305 K; the scatter is dominated by A_H/A_D being printed to 1–3 significant
  figures). Leaving `temperature_K` empty is recorded in `notes` as the alternative. **Third likely disagreement
  point.**
- *T range.* Footnote `b` states "283–323 K"; the Methods list 10, 20, 25, 30, 35, 40, 45, 50 °C. 283.15–323.15 K was
  entered with `n_temperatures = 8` counted from that explicit list, and both forms noted.
- *`quantity = kcat`*: `kH` is the Michaelis-Menten turnover number (footnote `a`); the Arrhenius plots are of `ln k`
  for that constant. *`method = noncompetitive`*: hydrogenated and 3-deutero substrate assayed separately.
  *`transfer = proton`*: Fig. 1 legend has the base's nucleophilic oxygen taking "the electrophilic 3′-H".
- *Errors* are propagated standard errors in the fitted parameters (footnote `b`).

**Left out.** Row B of Table 1 (`kH/kD = 4.6 (0.1)`, `Ea(D)−Ea(H) = 2.3 (1.1)`, `A_H/A_D = 0.107 (0.01)`,
`Ea(H) = 14.5 (0.8)`, `kH = 3.25E-05`): non-enzymatic — footnote `c` says "B stands for the nonenzymatic reaction
rate in buffer". The text's "a value of 4.9 at 298 K", in the paragraph that introduces Ea and A "in aqueous
solution", i.e. the non-enzymatic reaction (see the inconsistency below). The computed tunneling-corrected KIE of 5.8
at 298 K (⁻OH·(H₂O)₄ cluster, QM/MM with Polyrate) and the barriers 17.4 vs 19.8 kcal/mol. Supplementary Fig. 11,
Supplementary Tables 1, 3, 4, 8, 9 and Fig. 5 (which plots the same ΔEa and A_H/A_D already in Table 1). The
Trp50Ala mutants of R1 and R7-2 (">95 % reductions in kcat", a sevenfold K_M increase; no isotope effect reported, so
no rows). EVB barriers (16.8, 16.4, 19.0 kcal/mol) and the MD/fluorescence results. Cited: KE07 R1 k_cat 0.018 s⁻¹
and the 10³-fold rate acceleration (ref 1).

**Inconsistency.** The text says the solution reaction gives "a value of 4.9 at 298 K", but Table 1's row B (the
nonenzymatic buffer reaction) is `4.6 (0.1)`, while `4.9 (0.2)` is exactly R1's tabulated `kH/kD`. Either the text
mis-quotes row B, or it refers to R1 — in which case the `kH/kD` column would be at 298 K, not 303 K. Both readings
are recorded in the R1–R7-2 `notes`. A second, smaller mismatch: Table 1 footnote `a` gives the substrate range as
0.1–1.2 mM, the Methods as "9−11 different concentrations (0.01−1.1 mM)".

---

## S065 — Rapp & Nidetzky 2022, *ACS Catal.* 12, 6816 (TaCPa2E)

**Entered — measurements (18).**
- Table 1 primary KIEs, pH 7.5: `Dkcat` 2.20 ± 0.75 (20 °C), 4.30 ± 0.30 (60 °C), 3.34 ± 0.09 (80 °C); `Dkcat/KM`
  2.06 ± 0.67, 3.80 ± 0.40, 3.19 ± 0.24 at the same three temperatures.
- Text: `Dkcat = 6.1` at 40 °C (no error); `Dkcat = 2.34 ± 0.27` at 60 °C in ²H₂O (pL 7.5).
- Table 3 solvent KIEs on k_cat (`solvent`, `noncompetitive`, `observed`): with CDP-Glc 0.97 ± 0.12 (pL 7.0, 60 °C),
  1.03 ± 0.13 (pL 7.5, 60 °C), 0.99 ± 0.11 (pL 8.0, 60 °C), 0.49 ± 0.07 (pL 7.5, 20 °C); with CDP-[2-²H]Glc
  0.84 ± 0.03 (pL 7.5, 80 °C), 0.57 ± 0.11, 0.57 ± 0.10, 0.59 ± 0.10 (pL 7.0/7.5/8.0, 60 °C), 0.51 ± 0.10
  (pL 7.5, 20 °C).
- Table 3 footnote b: `ᴰ²ᴼ(kcat/KM) = 0.65 ± 0.31` (CDP-Glc, pL 7.5, 20 °C).

**Entered — temperature (2).** Table 2, both sub-ranges, units converted: 20–40 °C (293.15–313.15 K) `A_H/A_D`
7.0E6 ± 1.1E6, `dEa_kcal` −8.772 ± 1.816, `Ea_light_kcal` 15.94 ± 2.247; 45–70 °C (318.15–343.15 K) `A_H/A_D`
0.05 ± 0.007, `dEa_kcal` 3.035 ± 0.6214, `Ea_light_kcal` 14.39 ± 0.7887.

**Judgement calls.**
- *Sign.* Table 2 footnote `a` defines ΔE_A = E_A,D − E_A,H, identical to the schema — no change.
- *Unit conversion* (kJ/mol ÷ 4.184, four significant figures): −36.7 → −8.772; 7.6 → 1.816; +66.7 → 15.94;
  9.4 → 2.247; +12.7 → 3.035; 2.6 → 0.6214; +60.2 → 14.39; 3.3 → 0.7887. Originals kept in `as_printed`.
- *Partial fit ranges.* Both Table 2 fits cover only part of the measured 20–80 °C range (k_cat has a break between
  40 and 45 °C); Figure 3b also omits the 25 and 80 °C points for a low coefficient of determination, and the paper
  notes a possible non-linearity for the deuterated substrate at ≤40 °C. All recorded; `n_temperatures` left empty
  because the paper states none for the sub-ranges.
- *`6.1` entered.* Printed in the text ("The Dkcat peaked at 40 °C, with its value of 6.1") and the Abstract; nothing
  was read off Figure 4. It comes from the single-saturating-concentration series (Table S1), not from the Table 1
  global fit — recorded, together with the Methods' statement that the two determinations agree within 5 %.
- *`kind = observed` throughout*, including 6.1 and the 60–80 °C values. The paper only assumes "that the
  substantially inflated Dkcat of 6.1 at 40 °C implies the intrinsic KIE to have largely been revealed" and
  "considered" 40–80 °C to show the chemical-step KIE intrinsically; it never says a measured value *is* the
  intrinsic KIE (`Dk_H` in eq 2 is the intrinsic KIE, and no number is given for it). **Fourth likely disagreement
  point** — a reader taking that sentence as an assertion would mark 4.30, 3.34 and 6.1 as `intrinsic`.
- *`pH` column for Table 3* holds the printed `pL` value (L = ¹H or ²H; pD set with NaOD per the Methods), noted in
  every such row.
- *Direction of the solvent KIE.* The Methods confirm "SKIEs (Table 3) were obtained as the ratio of the k_cat for
  the enzymatic reaction in ¹H₂O and ²H₂O", i.e. light/heavy as required. Cross-check:
  4.30 × 0.57/1.03 = 2.38 ≈ the printed 2.34.
- *Double-label rows.* The CDP-[2-²H]Glc rows of Table 3 are solvent KIEs measured with the C2-deuterated substrate;
  `labelled_position` and `conditions` say so.
- *Mechanism fields.* Primary rows: CDP-Glc C2 → C4 of the tightly bound NAD⁺, `hydride`. Solvent rows: CDP-Glc 2-OH
  oxygen → Tyr164, `proton` (from the paper's own description of concerted hydride/proton abstraction and of Tyr164
  as the general base), with a note that the solvent label covers all exchangeable positions and that the paper
  interprets the effect through ground- and transition-state fractionation factors (ᴰ²ᴼk_cat = Φ_GS/Φ_TS).

**Left out.** The `n.d.` cell (CDP-Glc, pL 7.5, 80 °C), footnote `a`. Table S1 (the full per-temperature KIE series
behind Figure 4), Figure S3 full MM data, Figures S7/S9 model fits — Supporting Information. Model-fitted parameters,
not isotope effects: the Marcus-like two-population DAD fit (long-distance population 3.31 ± 0.02 Å, ΔG
17.24 ± 2.1 kJ/mol) and the two-state equilibrium model (K ≈ 1, E_A → 0 at low T). Non-isotopic: k_cat/K_M values,
the enzyme-NADH fractions (2.22 ± 0.5 %, 4.15 ± 1.0 %, ~3 %, 1.90 ± 0.60 %, 2.33 ± 0.88 %), K_M 0.32 ± 0.02 mM, the
Y164F variant (inactive, ≥10⁴-fold lower rate — no isotope effect), the viscosity control (±3 %). Cited values: DHFR
variants' ΔE_A larger for ³H by +13.8 kJ/mol (I14G, ref 9), +15.5 kJ/mol (M42W-G121V, ref 30), +16.7 kJ/mol
(M42W-F125W, ref 115); methylamine dehydrogenase with ethanolamine ΔE_A = +8.4 kJ/mol, A_H/A_D = 0.57 (ref 116);
malate synthase inverse SKIE 0.6 ± 0.1 on k_cat/K_M (ref 103); ᴰK_eq 1.1–1.2 for NAD⁺ alcohol oxidation
(refs 98–100); Zn²⁺-ADH fractionation factors Φ_GS 0.37 / Φ_TS 0.73 / Φ_PS 1 (refs 105, 106); the semiclassical KIE
limit ~6.9 (refs 33, 85) and A_H/A_D limit 0.5; DHFR M42W-G121V ΔG 18.42 kJ/mol and DAD_L 3.34 Å (refs 13, 30).

**Inconsistencies.**
1. The Abstract gives "2.1 at low (20 °C) and 3.3 at high temperature (80 °C)", against Table 1's `2.20 ± 0.75` and
   `3.34 ± 0.09`. 2.1 vs 2.20 is more than rounding; the two numbers come from different determinations
   (single-concentration series vs eq-6 global fit). Table 1 values entered; the Abstract values are in `notes`.
2. The Discussion rounds Table 2 to "−37 kJ mol⁻¹", "+13 kJ mol⁻¹" and "A_H/A_D ratio is 0.05"; table values
   entered.
3. The Methods list SKIEs only "at pL 7.0, 7.5 and 8.0 at 60 °C and pL 7.5 at 20 °C", but Table 3 and the text also
   report the 80 °C SKIE (0.84 ± 0.03).
4. The Methods cross-reference the k_cat/K_M isotope-effect data to "Table 2" where Table 1 is meant.

---

## `enzymes.csv` — metadata, lookups and checks (UniProt REST + RCSB, 9 November 2026)

| source | name | ec | organism | uniprot | variant | pdb |
|---|---|---|---|---|---|---|
| S061 | NQO1 | 1.6.5.2 | *Homo sapiens* | P15559 | WT | *(empty)* |
| S062 | CvPheH | 1.14.16.1 | *Chromobacterium violaceum* | P30967 | WT | 1LTU;1LTV;1LTZ;3TCY;3TK2;3TK4;4JPY |
| S062 | CvPheH | 1.14.16.1 | *C. violaceum* | P30967 | I234D | *(none exists)* |
| S063 | PtmT2 | *(none)* | *Streptomyces platensis* | A0A023VSF1 | WT | 5BP8 |
| S064 | Kemp eliminase KE07 | *(none)* | designed; HisF scaffold, *Thermotoga maritima* | Q9X0C6 *(scaffold)* | R1 | 4Z08;5D2T;5D2V;5D2W |
| S064 | " | | | | R4 | *(none)* |
| S064 | " | | | | R5 | 5D2X;5D2Y;5D30;6C7M;6C7T;6C7V;6DKV;6DNJ |
| S064 | " | | | | R6 | 5D32;6C8B |
| S064 | " | | | | R7 | 5D33;5D37;6CAI;6DC1 |
| S064 | " | | | | R7-2 | 5D38;6CT3 |
| S065 | TaCPa2E | *(none)* | *Thermodesulfatator atlanticus* | *(none found)* | WT | 9RL0 |

**Numbering checks (all passed).** P15559 has Y127, Y129, R139, Y156, H162, P187, S82 exactly where S061 names them.
P30967 position 234 is Ile, so S062's `I234D` matches UniProt. A0A023VSF1 position 313 is Asp, so S063's catalytic
D313 matches. S064's numbering matches **Q9X0C6** at every named position (I7, V12, W50, F77, E101, I102, Y128, K146,
G202, K222, N224, F229); the PDB entries of that series number one higher because the deposited construct has an
extra Ala after the initiator Met. 9RL0 position 164 is Tyr, matching S065's catalytic Tyr164.

**EC.** Only S061 prints an EC (1.6.5.2, which matches UniProt). For S062 the EC comes from UniProt. For S063, S064
and S065 neither the paper nor UniProt gives one, so the field is empty (S064's scaffold EC 4.3.2.10 belongs to a
different reaction; S065's homolog P14169 carries EC 5.1.3.10 — both noted, not entered).

**PDB notes worth flagging.**
- **S061**: left empty — 29 RCSB entries for P15559, and the paper names none.
- **S062**: 7 WT entries listed; 1LTU/1LTV/1LTZ/3TCY/4JPY differ from P30967 at M64L, Q85E, V276I, R288H (isolate
  variation this study did not engineer), 3TCY/3TK2/3TK4 carry a GPLGS/GLPGS remnant. All `pdbx_mutation` fields in
  RCSB are empty even for entries titled as mutants, so every entity sequence was compared with P30967 by hand; the
  engineered-mutant entries (4ESM Y155A, 4ETL F258A, 4JPX S203P, 4Q3W–4Q3Z D139E/N/A/K) were excluded. No I234D
  entry exists.
- **S064**: the ten entries citing DOI 10.1038/s41467-018-06305-y are 6C7H, 6C7M, 6C7T, 6C7V, 6C8B, 6CAI, 6CT3,
  6DC1, 6DKV, 6DNJ; the 4Z08/5Dxx entries of the same titled series carry no primary citation in RCSB but are
  sequence-identical, so they are listed with that caveat. **6C7H is R1 + W50A (Trp50Ala)** and is deliberately not
  listed, because no isotope effect was entered for a Trp50Ala variant. Sequence-derived mutation sets (paper
  numbering) differ from the main text in several places — R5 and R6 lack K146E, R6 shows an unmentioned K19E, R7
  shows V12L/H84Y/M207T and no I102F — all recorded in `notes`; the full lists are in Supplementary Table 1, which
  was not available. L227F, present in every evolved variant, is a reversion to the HisF residue and is not named in
  the main text. Relative to Q9X0C6 the design itself carries M1A (insertion), C9A, D11I, T21S, V48S, L50W, S101E,
  A128Y, D130A, L169V, T171G, D176L, S201H, L222K, A224N, F227L plus a C-terminal GSLEHHHHHH. R4's mutation set
  occurs only in 3IIO, whose citation is Khersonsky et al. 2010, so R4's `pdb` is empty.
- **S065**: the paper names no accession and no structure, but PDB **9RL0** ("CDP-tyvelose 2-epimerase from
  *Thermodesulfatator atlanticus*", released 2026-06-10) is identifiably this wild type: 340 residues, Tyr164
  present, average mass **39362.4 Da** against the paper's stated 39362 g/mol for TaCPa2E_WT, depositors including
  Rapp C. and Nidetzky B. Its citation is 10.1016/j.jbc.2026.111384, not S065. `uniprot` is empty: UniProtKB holds
  only two *T. atlanticus* proteins (C0MPG6, C0MPG7, sulfite reductase subunits), and RCSB's cross-reference of 9RL0
  to **A0ABS1GJY6** is a best-match only — UniProt assigns that accession to *Persephonella atlantica* and its
  sequence differs from 9RL0's at 49 of 340 positions (~86 % identity), so it is not this protein.

---

## Summary of the four most likely disputes with reading 1

1. **S062 I234D/DMPH₄ 0.90 ± 0.03** — `observed` (mine) vs `intrinsic`; the paper says "likely to be the intrinsic
   isotope effect".
2. **S063 all values** — `intrinsic` (mine) vs `observed`; the paper claims intrinsic KIEs for its method, not for
   individual numbers.
3. **S064 `temperature_K` of the kH/kD column** — 303.15 K (mine, from footnote `a` plus a back-check) vs empty vs
   298.15 K (if the text's "4.9 at 298 K" means R1).
4. **S061 `temperature_K` of the Table 2 KIE column** — 279.15 K (mine) vs empty/series mean; and whether the
   saturating-condition 2.3 ± 0.5 belongs in `measurements.csv` at all.

Also worth a curator's eye: S065 `kind` for the 40–80 °C values; whether S063's prose "approximately twofold" solvent
effects on k_cat and k_cat/K_M should be entered; and whether S062's Table 3 product ratios count as isotope effects
(the second reader says no, per eqs 4–5).
