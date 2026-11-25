# S013, second reading (ai-2)

(Saved by the curator from the second reader's final answer; the second reader could not write report files itself.)

Source: Wang, Tharp, Selzer, Benkovic, Kohen, "Effects of a distal mutation on active site chemistry", Biochemistry 45, 1383–1392 (2006), doi 10.1021/bi0518242. I read it only from the saved PMC page of the author manuscript (PMC2553318). Numbers come from the parsed HTML, and I checked each one on a rendering of the saved page (JavaScript off, all network requests blocked). The figure images, the equation images and the Supplementary Information are not part of the saved page.

All rows describe one step: E. coli DHFR (ecDHFR) G121V. A hydride moves from the pro-R hydrogen at C4 of the NADPH nicotinamide ring to C6 of the pterin of 7,8-dihydrofolate (si face). This is the paper's own statement (unheaded introduction, PMC P2), and P8 names "the donor carbon (4C of NADPH)".

## Included

**temperature.csv: 3 rows.** Source: Table 1, G121V column. These are the intrinsic 1° KIEs fitted to Eq. 4 over 5–45 °C (278.15–318.15 K) at pH 8.0, competitive method.

| isotopes | A_L/A_I | ΔEa (kcal/mol) |
|---|---|---|
| H/T | 6.6 ±1.3 | 0.22 ±0.12 |
| H/D | 3.7 ±0.5 | 0.16 ±0.08 |
| D/T | 1.8 ±0.1 | 0.07 ±0.03 |

**measurements.csv: 5 rows.** All are at 25 °C (298.15 K) and pH 8.0, competitive method.
- 1° H/D, intrinsic: 4.9 ±0.2. Results, "Competitive 1° KIEs", the paragraph after Eq. 5.
- 2° H/T, observed: 1.087 ±0.005 with H-transfer and 1.125 ±0.007 with D-transfer.
- 2° H/T, intrinsic: 1.15 ±0.01 with H-transfer and 1.14 ±0.02 with D-transfer.
- Both 2° pairs stand in the last paragraph of the Results section "“Marcus Like” models (Environmentally Coupled Tunneling)" (PMC P35).

## Left out
- **Table 1, Wild Type column (every row).** Footnote b: "From Ref. (31)".
- **Table 1, S.C. A_l/A_h column** (0.5–1.6, 0.6–1.4, 0.9–1.2). These are semiclassical limits cited from Refs 39, 41, 57, 64–67, not measurements.
- **Table 1, Rate** (228 ±8 and 1.4 ±0.2 s⁻¹) **and ΔG‡ at 25 °C** (14.3 ±0.5 and 17.3 ±0.5). Footnote c says these are pre-steady-state rates at pH 7 from Refs 11 and 30. They are rates and activation parameters, not isotope effects.
- **Table 1, ΔH‡** (3.1 ±0.2 and 2.6 ±0.3) **and TΔS‡ at 25 °C** (−11.2 ±0.5 and −14.7 ±0.6). These are activation parameters of the rate, not isotope effects.
- **Ea = 3.7 ±0.2 (WT) and 3.2 ±0.3 kcal/mol (G121V)** (P26). These are activation energies of kcat from initial velocities at 20–45 °C, pH 9, not isotope effects. See Judgement for why they are not in Ea_light_kcal.
- **Effects of the mutation on activation parameters:** ΔΔH‡ = 0.5 ±0.5 and TΔΔS‡ = 3.5 ±0.8 kcal/mol at 297 K (P26); TΔS‡ = 3 ±1 kcal/mole at 300 K and ΔH‡ = 0.5 ±1.7 kcal/mol (P32). Not isotope effects.
- **Noncompetitive KIE on kcat with R-[4-²H]-NADPH:** "all temperature independent and within the range of 2.8 ±0.6" (P27). This summarises a temperature range and gives no single temperature. No Arrhenius isotope effects are fitted for it, and its pH and temperature range are ambiguous (see Unclear).
- **Pre-steady-state KIE for G121V, 2.4 at 25 °C.** From Ref. 30.
- **WT intrinsic 2° H/T KIE, 1.19 ±0.2.** From Ref. 31.
- **Commitments:** Cf = 0.7 ±0.1 (H) and 0.15 ±0.05 (D) (P35), and "a commitment close to 1.8" on the pre-steady-state KIE. These are not isotope effects. The Cf values appear only in the notes of the intrinsic 2° rows.
- **1° H/T, D/T and H/D KIEs, observed and intrinsic, at each temperature from 5 to 45 °C.** They are only in Supplementary Tables 1–2, which are not in the input, and in the plots of Figs. 1–2, whose images are not in the saved page. No values were read off plots.
- **Swain–Schaad exponent 3.3** (Methods). This is an assumed semiclassical value, not a measurement.
- **Rates in the introduction and discussion** (220 → 1.3 s⁻¹; 3.5 s⁻¹; >2000 s⁻¹; 163-fold). These are rates, from Refs 11 and 30.

## Judgement
- **kind.** I set kind = intrinsic only where the paper uses that word:
  - Table 1 rows: Results says "fitting the intrinsic KIEs to Eq. 4 … summarized in Table 1", and Methods calls them "activation parameters for the intrinsic KIEs".
  - 4.9 ±0.2: "The intrinsic KIE that we report here".
  - 1.15 and 1.14: "These intrinsic 2° KIEs".
  - 1.087 and 1.125 are observed ("The observed 2° KIEs").
- **quantity.** I used kcat/KM for every row.
  - The competitive experiments give V/K KIEs: Results says "Primary H/T and D/T V/K KIE measurements", and Eq. 3 uses ᵀ(V/K).
  - The intrinsic values are derived from those V/K KIEs by Northrop's method. Setting kind = intrinsic marks that the commitments have been removed.
  - The possible alternative is "other", since an intrinsic KIE is on the chemical step itself ("kD/kT is the intrinsic D/T KIE").
  - For the 2° KIEs, "V/K" is my inference from the competitive method; the paper does not write V/K for them.
- **method.** I used competitive for every row: the 1° values stand under the heading "Competitive 1° KIEs", and all values come from ¹⁴C/³H mixtures. The H/D values (4.9, and the H/D row of Table 1) were computed from the competitive H/T and D/T data. H and D were never competed directly; the notes say so.
- **labelled_position.** This follows the compound names as printed, plus the paper's statement that the pro-R C4 hydrogen is the one transferred.
  - 1° H/T: R-[4-³H]-NADPH vs [Ad-¹⁴C]-NADPH.
  - 1° D/T: R-[4,4-²H,³H]-NADPH vs [Ad-¹⁴C,4-²H₂]-NADPH. Pro-S is D in both compounds, according to the synthesis.
  - 2° with H-transfer: S-[4-³H]-NADPH vs [Ad-¹⁴C]-NADPH.
  - 2° with D-transfer: S-[4,4-³H,²H]-NADPH vs R-[Ad-¹⁴C,4-²H]-NADPH.
- **Sign of dEa.**
  - The paper defines the fitted parameter as ΔEa I-L, with L = H or D and I = D or T. I read this as Ea(heavy) − Ea(light), which is the schema's convention.
  - Eq. 4 itself is only a placeholder in the saved page, so I could not read it.
  - Check: 3.7·exp(0.16/RT) at 298.15 K gives 4.85, which matches the printed intrinsic H/D KIE of 4.9 ±0.2. The opposite sign would give 2.82.
  - Values are entered unchanged. They are already in kcal/mol (Table 1 footnote a), so nothing was converted.
- **Ea_light_kcal is empty.** The only Ea given for G121V (3.2 ±0.3 kcal/mol) belongs to kcat at pH 9 over 20–45 °C, not to the intrinsic KIE series.
- **pH 8.0.** This comes from Methods, "Competitive kinetic isotope effects": "at pH 8.0 …" and "readjusted to 8.0 at the experimental temperature". Results does not restate the pH for these values.
- **Temperatures.**
  - 25 °C → 298.15 K.
  - 5–45 °C → 278.15–318.15 K. The range is printed twice: "5–45 °C" in Methods and "from 5°C to 45°C" in Results.
  - n_temperatures is empty: the paper does not state it.
- **transfer, substrate, acceptor.** transfer = hydride, as the paper states it. substrate = NADPH, because the schema defines substrate as the hydrogen donor molecule. DHF C6 goes in acceptor.
- **error.** Errors are entered as printed.
  - The ± on the 1° intrinsic KIEs are standard errors (Methods, "Intrinsic KIEs").
  - The error type is not stated for the Table 1 fit parameters or for the 2° values.
- **as_printed.** Each is a verbatim fragment of at most 15 words.
  - Table 1 rows give the row label and the G121V cell, plus "(footnote a: kcal/mol)" for the unit.
  - The two observed 2° rows share one fragment, and so do the two intrinsic 2° rows; the value field says which number belongs to the row.

## Unclear
1. **pH of the 4.9 ±0.2.** The sentence that introduces it mentions "the same temperature and pH 7 as reported in Ref. (11)". That refers to the pre-steady-state rate. The competitive experiments themselves ran at pH 8.0, which is what I recorded.
2. **Commitments said to be "reported above".** Cf 0.7 ±0.1 and 0.15 ±0.05 are described this way, but no such values appear earlier in the main text; they may be in the Supplementary Information. Putting them into Eq. 5 reproduces the intrinsic 2° values: 1.087·1.7 − 0.7 = 1.148 and 1.125·1.15 − 0.15 = 1.144.
3. **Conditions of the kcat KIE.** Methods ("Non-competitive KIEs") gives pH 8.0 and 5–45 °C. Results gives 20–45 °C at pH 9 for the initial-velocity Ea (P26), then says the kcat KIEs were measured "under the same conditions" and refers to pH 8 (P27). The value is left out anyway.
4. **Figure 1 caption.** It says the lines are the regression "to Equation 2", but Eq. 2 is the fractional-conversion formula. The text says the fit used Eq. 4.
5. **Synthesis of R-[Ad-¹⁴C,4-²H]-NADPH.**
   - P11 says it was made with [1-²H]-glucose and GluDH. Elsewhere the paper uses that route to label the pro-S position (S-[4-³H]-NADPH, 4S-[Ad-¹⁴C,4-²H]-NADPH).
   - P12 makes the same compound with [U-²H]-isopropanol and tbADH.
   - My labelled positions follow the R/S names as printed.
6. **Inconsistent numbers outside the isotope effects.** Neither affects any row.
   - Rates: 220 and 1.3 s⁻¹ in the introduction, but 228 ±8 and 1.4 ±0.2 s⁻¹ in Table 1, all cited from Refs 11 and 30.
   - Effect of the mutation on activation parameters, given twice with different numbers: ΔΔH‡ 0.5 ±0.5 and TΔΔS‡ 3.5 ±0.8 at 297 K (P26), against ΔH‡ 0.5 ±1.7 and TΔS‡ 3 ±1 at 300 K (P32).
7. **Labels of the Table 1 energy rows.** The rows read "ΔEa H-T", "ΔEa H-D" and "ΔEa D-T" with no direction given. The direction comes only from the Methods definition (ΔEa I-L); see Judgement.
