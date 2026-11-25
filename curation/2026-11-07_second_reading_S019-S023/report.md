# Second reading (ai-2) of S019–S023: MEG-NEN KIE extraction

I've done the second reading of all five papers and written the three tables: 48 rows in `measurements.csv`, 24 temperature series in `temperature.csv` and 13 enzyme rows in `enzymes.csv`. After the last rebuild I re-opened each file and checked it by script against the HTML. Every value/error pair, °C value, pH and kJ→kcal conversion was found in the source text (0 problems), and all 67 numbers taken from tables match their exact cell, row label against column header (0 mismatches).

## Method
- **Reading:** I read `in/SCHEMA.md`, `in/CURATION.md` and `in/sources.csv`, then parsed the five saved pages with BeautifulSoup (`python3 -I`, scripts in `work/`). Tables were read cell by cell, following each footnote anchor to its cell, row or header.
- **Equations:** in all five pages the display equations are unrendered MathJax placeholders with no content. All sign conventions therefore rest on definitions in the text.
- **What I did not read:** values shown only in figures, and supporting information (not available).
- **Web use:** only for enzyme metadata, via UniProt REST and RCSB. For RCSB I searched by UniProt accession and by sequence identity, listed differences from RCSB's entity-to-UniProt alignments, and ran my own global alignment for entities RCSB had not mapped. Nothing outside `reading2_s019-s023/` was opened; no remote-device or browser tools were used.

## Conventions used for all papers (judgement calls)
- **Temperature range:** `T_min_K`/`T_max_K` are the range of the fitted series as the paper states it. Where the fit covers only part of the measured range, the full measured range is in `notes` (S019 pH 9.5, S020, S021, S022).
- **Northrop-derived intrinsic KIEs (S020):** quantity = `other`, because the number is the KIE on the chemical step, not on V/K. Method = `competitive`, kind = `intrinsic`.
  - Where a paper says an observed KIE equals the intrinsic one (S023 Dkcat), quantity = `kcat` and kind = `intrinsic`.
- **Intramolecular competition (S021):** quantity = `other`, method = `competitive`.
- **kcat KIEs:** always `noncompetitive`.
- **Error type:** no paper states whether its errors are SD or SE.
- **substrate:** the hydrogen-donor molecule, as SCHEMA defines it. The one exception is the POR proton step, where the donor is an enzyme Tyr; there the substrate field holds Pchlide and the notes say so.

## S019 – Swanwick 2006 (E. coli DHFR: WT, G121V)
**Entered (5 measurements, 3 series)**
- **Measurements:**
  - WT, pH 7.0, single turnover: 2.7±0.2 (25 °C), 3.0±0.2 (5 °C), 2.2±0.2 (40 °C).
  - WT, pH 9.5, kcat: 2.72±0.1 (25 °C).
  - G121V, pH 7.0, single turnover: 1.450±0.042 (25 °C).
- **Series:**
  - WT pH 7.0, 5–40 °C (Fig. 4 legend): AH/AD 0.109±0.043; ΔEa 7.83±0.98 kJ/mol (1.871±0.2342 kcal/mol); Ea_light 29.9±0.6 kJ/mol (7.146±0.1434).
  - G121V, 5–35 °C: AH/AD 0.0024±0.0004; ΔEa 15.83±0.44 kJ/mol (3.783±0.1052); Ea_light 23.3±0.3 kJ/mol (5.569±0.07170).
  - WT pH 9.5, fit 15–35 °C: AH/AD 1.81±0.19; ΔEa 1.11±0.79 kJ/mol (0.2653±0.1888).

**Left out**
- **Cited:** 2.8 [31]; 2.9±0.2 [41]; 220 s⁻¹ [26,37]; 222.8±1.3 s⁻¹ [8]; Ea 28.2±0.9 kJ/mol [8]; 2.92±0.076 at pH 9.0 [2]; AH/AD 4.0±1.5 [2]; 1.9 [52]; 13.4 and 2.9 kJ/mol [31]; the limits 0.71 and 1.41.
- **Supporting information only:** Supplementary Tables 1–3.
- **Figures only:** the individual points in Figs 3 and 4.
- **Not isotope effects:** the WT/G121V ΔH‡ difference (6.3±0.2 kJ/mol); TΔS‡ values; the "no KIE" phases at ~3.5 and ~6.5 s⁻¹ (no number given).

**Judgement calls**
- **Fit version:** each pH 7.0 series appears twice. I entered the KIE fit from the Fig. 4 legend because it prints both ΔEa and AH/AD, so nothing had to be recomputed. The separate kH/kD fits in the text are in `notes`.
- **Sign:** ΔEA^H/D in Fig. 4 is not defined. A positive value with EA^D > EA^H means Ea(D)−Ea(H). The text's G121V "ΔEA=EA^H−EA^D = −15.7" is defined the other way round and was not entered.
- **Quantity:** single_turnover with excess enzyme; for G121V the paper assigns the slow phase to hydride transfer. kcat at pH 9.5 (excess H2F; saturation by NADPH not stated). All values `observed`.

**Inconsistencies in the paper**
- The Fig. 4B legend says "pH 9.0 and 5.0"; text and Methods say pH 9.5. I entered 9.5.
- WT EA^D is 37.7±0.7 in the text but 37.7±0.6 in the Fig. 3 legend; A_D is 3.07±0.81 vs 3.07±0.80 ×10⁸ s⁻¹.
- AH/AD is 0.108±0.04 (text) vs 0.109±0.043 (Fig. 4) for WT, and 0.0025±0.0007 vs 0.0024±0.0004 for G121V.
- G121V ΔEA is −15.7 in the text (opposite sign) vs 15.83±0.44 in Fig. 4.

## S020 – Hong 2007 (E. coli thymidylate synthase: WT, Y94F)
**Entered (19 measurements, 4 series)**
- **Proton abstraction from dUMP C5, 25 °C, pH 7.5 (14 rows):**
  - Table 1 for WT and Y94F: T(V/K)H and T(V/K)D (observed, at 5 µM CH2H4folate), and intrinsic H/T, D/T, H/D.
  - Text: WT 1.02±0.02 at 1 mM CH2H4folate; Y94F asymptote 1.10±0.02; values extrapolated to zero CH2H4folate, 1.86±0.10 (WT) and 1.96±0.15 (Y94F).
- **Hydride transfer, Y94F (5 rows):**
  - At 20 °C: observed T(V/K) 2.62±0.01 and intrinsic 4.86±0.18.
  - Table 3, Dkcat: 2.24 (40 °C), 2.36 (20 °C), 4.20 (5 °C). No ± per value; the footnote says relative errors are under 2 %.
- **Series (Table 2, Y94F intrinsic KIEs, 5–20 / 20–40 °C, kcal/mol):**
  - H/T: AH/AT 0.0002±0.0001 / 4.5±0.5; ΔEa 6.0±0.5 / 0.03±0.40; Ea_light 6.2±0.3 / 3.1±0.1.
  - D/T: AD/AT 0.07±0.02 / 1.6±0.1; ΔEa 1.8±0.2 / 0.06±0.12.

**Left out**
- **Cited:** all wild-type hydride-transfer values (Table 2 and Table 3, footnote b "From ref. (10)"); the earlier "unity/slightly inverse" KIE [4]; the semi-classical column of Table 2.
- **Figures only:** Figs 2, 3 and 5.
- **Not enzymatic KIEs:** DKeq 0.99 (±0.02), an equilibrium IE on a non-enzymatic model.
- **Not isotope effects:** ΔH‡, TΔS‡, ΔΔH‡ 0.9, ΔEa(Y94F−wt) ≈ 2.8 kcal/mol, commitments, k_hydride.

**Judgement calls**
- **ΔEa sign:** the Eq. 9 text defines E_T − E_L, so the Table 2 rows ΔEaH-T and ΔEaD-T are heavy minus light and no sign change was needed. This reading is supported by AH/AT = 0.0002 and by the text's own "E_T − E_H".
- **Ea_light:** this is Ea of k_hydride (H), estimated via Eq. 10 from kcat at only 5, 20 and 40 °C. Entered for the H/T rows only.
- **Y94F 1.10±0.02:** the paper does not say whether this is the value measured at 1 mM or the fitted asymptote.
- **Table 3 label:** the title says "Tkcat" but the column header and Eq. 10 text define Dkcat. Entered as H/D.

**Inconsistencies in the paper**
- Intrinsic H/T: the text gives "3.25 ± 0.31 and 3.17 ± 0.22" (wt, Y94F) while Table 1 gives 3.2±0.2 (wt) and 3.2±0.3 (Y94F). The errors are swapped between the two places; I entered Table 1.
- 20–40 °C ΔEa(H/T): text "−0.03 ± 0.30" vs Table 2 "0.03 ±0.40".
- The footnote to Eq. 6 gives the zero-[B] KIE as "1.8, see Figure 2"; the text gives 1.86±0.10 from Figure 3.
- The Fig. 1 legend puts the water 1.7 Å from Y94; the text and Fig. 4 legend say 2.6 Å.

## S021 – Yoon 2010 (glutamate mutase, GlmES fusion)
**Entered:** KH/KD at 0 °C = 6.0 (no error). One series, fit −2.5 to 5.0 °C: AH/AD 0.17±0.04, ΔEa(D–H) 1.94±0.13 kcal/mol (defined heavy − light, no sign change).

**Left out**
- **Cited:** KIE ~4 at 10 °C (ref 24); the three literature rows of Table 1 (refs 21–23); "~20 to ~50".
- **Figures only:** Figs 3–5.

**Judgement calls**
- The paper calls these KIEs intrinsic throughout, so kind = `intrinsic`; quantity = `other`; method = `competitive` (intramolecular).
- It is not stated whether 6.0 was measured at 0 °C or read from the fit. Footnote a ("extrapolated to 0 °C") is attached only to the literature rows.
- Measurements span −2.5 to 30 °C; the fit uses −2.5 to 5.0 °C only.
- **The organism is not stated in the paper.** I filled in C. tetanomorphum (UniProt Q05488;Q05509) from knowledge of the Marsh-lab construct, outside the paper, and flagged it for checking against ref. 25.

**Inconsistencies in the paper**
- The Arrhenius plot spans −2.5 to 10.5 °C in the text but −2.5 to 10.0 °C in the Fig. 5 legend.
- Aging times are 12–160 ms in Methods but 10–120 ms in Results.

## S022 – Heyes 2011 (POR from four organisms)
**Entered (8 measurements at 25 °C, 12 series)**
- **Hydride KIE, NADPH vs pro-S-NADP²H:** T. elongatus 1.91±0.17; Synechocystis 1.90±0.16; G. violaceus 1.94±0.13; Arabidopsis POR B 1.91±0.23.
- **Solvent isotope effect on proton transfer:** 2.01±0.14, 1.80±0.08, 1.54±0.07, 1.50±0.07 (same order).
- **ΔΔH‡ series (kJ/mol, converted to kcal/mol):**
  - Hydride above the −27 °C breakpoint: 8.2±0.6, 7.0±0.3, 6.9±0.7, 7.6±0.9.
  - Hydride below the breakpoint: (0.4±1.0), (0.4±1.5), (0.5±1.2), (0.3±1.2).
  - Proton transfer: 15.6±3.1, 17.6±3.7, 2.6±2.4, 1.0±1.9.

**Left out**
- **Supporting information only:** A′H/A′D, ΔH‡ and ΔS‡ (Tables S1/S2).
- **Figures only:** Figs 3 and 4 with their insets.
- **Not isotope effects:** rate constants.

**Judgement calls**
- **Eyring ΔΔH‡ entered as dEa_kcal (per SCHEMA). Its direction is not defined in the paper**; I entered the printed sign and read it as heavy − light.
- **Ranges:** hydride −27 to +50 °C and −70 to −27 °C (measured range and breakpoint from the text, sub-ranges from footnotes a and b). The proton-transfer range is not stated, so left empty.
- **Parentheses:** the below-breakpoint values are printed in parentheses with no explanation; I entered the numbers inside them.
- **pH:** empty for hydride rows (not stated); 7.5 for the solvent-effect rows (deuterated buffer, Methods).
- **Quantity and kind:** single_turnover (laser-flash rate constants), noncompetitive, observed.
- **Tyr numbering:** the Fig. 1 legend names Tyr-193 without saying which organism. Y193 fits T. elongatus and Synechocystis; the same Tyr is Y189 in G. violaceus and Y276 in Arabidopsis PORB (precursor numbering).

**Inconsistencies:** none among the printed numbers.

## S023 – Howe 2019 (phosphite dehydrogenase: 17X-PTDH and T104S/A/G)
**Entered (15 measurements, 4 series)**
- **Measurements:**
  - Table 1, 17X at 5, 25 and 45 °C: Dkcat, D(kcat/Km,PT) and Dkobs.
  - Table 2, mutants at 25 °C: Dkcat and D(kcat/Km,PT).
  - The 25 °C values also printed in Table 2 and the text were entered once.
- **Series, 5–45 °C, pH 7.25:**
  - 17X: AH/AD 1.60±0.09, ΔEa 0.21±0.05 kcal/mol.
  - T104S: 0.66 (0.07) and 0.75 (0.06).
  - T104A: 0.45 (0.05) and 0.96 (0.06).
  - T104G: 0.60 (0.05) and 0.77 (0.05).

**Left out**
- **Supporting information only:** Tables S1–S4.
- **Figures only:** Figs 2, 3, 5, 6.
- **Cited limits:** refs 1 and 59.
- **Not isotope effects:** the other kinetic parameters in Table 2.

**Judgement calls**
- **Kind:** Dkcat = `intrinsic`, because the paper says the observed Dkcat is the intrinsic KIE from 5 to 45 °C for 17X and the mutants. D(kcat/Km) and Dkobs are not called intrinsic, so `observed`.
- **Dkobs quantity = single_turnover:** the paper calls these pre-steady-state KIEs, but the traces were fitted to a zeroth-order rate law. Flagged.
- **Variant notation:** "17X" for the parent (the paper does not list its mutations) and "17X/T104S" etc. for the mutants.
- **17X AH/AD:** I entered the unrounded text value 1.60±0.09 rather than 1.6 (0.1) from Table 3 and the Abstract (same fit).
- **pH for the 17X series:** not restated for Fig. 3; taken as 7.25 from Table 1 footnote a.
- **Sign:** the text defines ΔEa as D−H, so no sign change.

**Inconsistencies in the paper**
- AH/AD rounding only: 1.60±0.09 vs 1.6 (0.1).
- The text refers to "Figure 3 and Figure 5" for the mutant temperature dependence; the mutant Arrhenius plots are in Figure 6.

## Enzyme metadata (enzymes.csv)
- **Numbering:** matches UniProt at every named position: G121 (P0ABQ4), Y94 (P0A884), T104 (O69054), Tyr-193 (Q8DLC1, Q59987).
- **PDB entries by variant:**

| Enzyme / variant | PDB |
|---|---|
| DHFR WT | left empty (182 entities; the paper names 1RA2) |
| DHFR G121V | none |
| TS WT | left empty (68 entities; the paper names 2KCE, 2FTQ) |
| TS Y94F | 2FTN;2FTO (residue 1 is CXM, a modified residue the study did not engineer) |
| Glutamate mutase GlmES fusion | none (only isolated C. tetanomorphum S subunit; holoenzyme structures are C. cochlearium) |
| POR T. elongatus WT | 6L1H;6RNV;6RNW (6R46 is Y193F, excluded) |
| POR Synechocystis WT | 6L1G;6R48 |
| POR G. violaceus WT | none |
| Arabidopsis PORB WT | 10 entries, all listed |
| 17X-PTDH | 4E5K;4E5N (from ref. 25); 9PR0;9PR2 matched by sequence only |
| T104S/A/G | none |

- No PDB entry cites any of the five papers' DOIs.
- **Current organism names:** T. elongatus is now T. vestitus; Pseudomonas stutzeri is now Stutzerimonas stutzeri.

## Calls most likely to cause disputes
1. Fitted range rather than measured range in `T_min_K`/`T_max_K`.
2. quantity = `other` for the Northrop-derived intrinsic KIEs (S020).
3. Fig. 4 fit chosen over the text fits (S019).
4. Table 1 chosen over the text for intrinsic H/T (S020).
5. Undefined direction of ΔΔH‡ (S022).
6. Dkobs quantity and Dkcat kind = intrinsic (S023).
7. Organism of the glutamate mutase, which is not in the paper (S021).
8. Including 9PR0/9PR2 for 17X, and listing all 10 PORB entries.
