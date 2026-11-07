# Second reading of S019–S023 (7 November 2026)

First reading `ai-1`, second reading `ai-2`. Both readers worked from the PMC pages of the five papers, saved on
7 November 2026 (S019 and S022 as publisher versions, S020, S021 and S023 as author manuscripts); the published PDFs
and the supporting information were not read. The second reader worked from those pages alone, did not see the first
reading, and looked up UniProt and RCSB PDB again for every enzyme. Its instructions repeated the rules of
CURATION.md and SCHEMA.md and added four clarifications that apply to any paper: a value the paper calls equal to the
intrinsic KIE counts as intrinsic; a series printed twice is entered once; D2O effects are `solvent`; a wild type
with many PDB entries keeps `pdb` empty. Files in this folder:

- `reading2_measurements.csv`, `reading2_temperature.csv`, `reading2_enzymes.csv`, `report.md`: the second reading as
  delivered (`report.md` saved by the curator from the second reader's answer; the list of the reader's working files
  was removed)
- `comparison.md`: row-by-row comparison of both readings, before the decisions below

## Result

All 69 rows of the first reading (45 isotope effects, 24 temperature series) have a partner in the second reading,
and all of them agree in value, error, temperature, pH, Arrhenius parameters and temperature range, with one
exception decided in point 3. They differ in two categories (points 1 and 2). The second reading has three
additional rows (point 4). Both readers left out the same cited values: the values of other papers in S019 (e.g.
2.9 ± 0.2, 2.92 ± 0.076, A_H/A_D 4.0 ± 1.5), the wild-type hydride-transfer columns of S020 (ref. 10), the three
literature rows of Table 1 in S021, and the semi-classical limits. Decisions:

1. **`quantity` of the intrinsic KIEs of S020 (11 rows):** the second reading used `other`, since an intrinsic KIE is
   the isotope effect on the chemical step and not on kcat/KM. The first reading's `kcat/KM` is kept, because all
   intrinsic values calculated from competitive kcat/KM KIEs (S009, S013, S014, S015) are entered that way; together
   with `kind` = intrinsic this says how the value was obtained. SCHEMA.md now states this convention.
2. **`method` of the intramolecular competition in S021 (M0055, T0034):** the second reading's `competitive` is taken
   instead of `other`, since H and D compete in one mixture, here within one molecule. SCHEMA.md now says so.
   `quantity` stays `other` in both readings.
3. **A_H/A_D of 17X-PTDH (T0047):** the second reading's 1.60 ± 0.09 from the Results is taken instead of the
   1.6 (0.1) of Table 3, which rounds the same fit (CURATION.md, rule 4: nothing is rounded); `location` and
   `as_printed` follow.
4. **Three rows only in the second reading (S020):** the Y94F value 1.10 ± 0.02, which the paper calls an asymptote,
   and the KIEs at zero CH2H4folate, 1.86 ± 0.10 and 1.96 ± 0.15, come from fits to the paper's Eq. 6, not from
   measurements at a stated concentration. They are not entered; the notes of M0044 name them.
5. **Glutamate mutase (correction):** the paper names no organism. The first reading assigned the Clostridium
   cochlearium enzyme; the second reading assigned Clostridium tetanomorphum and asked for a check against ref. 25.
   The curator confirmed C. tetanomorphum: the same group cloned and overexpressed that enzyme (UniProt Q05488, GlmS,
   and Q05509, GlmE, whose entries cite Marsh and Holloway) before building the GlmES fusion. `organism`, `uniprot`
   and `notes` are corrected, and the identifiers become `GLM_CLOTT_GLMES` and `GLM_CLOTT_GLMES_MASP` (the rows were
   not yet published under the old ones). `variant` stays `GlmES fusion` rather than WT, since the fusion is an
   engineered construct.
6. **PDB entries:**
   - **The four PORs:** the second reading listed the few wild-type entries, the first reading had left wild types
     empty. Since RCSB holds only a few, they are listed, after the curator compared their sequences:
     T. elongatus 6L1H, 6RNV, 6RNW (6R46 is Y193F); Synechocystis 6L1G, 6R48; Arabidopsis POR B 7JK9 and nine
     cryo-EM entries; G. violaceus none. DHFR and TS wild types, with dozens of entries, stay empty. SCHEMA.md now
     states this rule.
   - **17X-PTDH:** the paper does not list the mutations of 17X, but its Fig. 4 shows the co-crystal structure of its
     ref. 25 (10.1021/bi2016926), which is 4E5K; 4E5N from the same paper has the same substitutions. Both are entered.
     9PR0 and 9PR2 (released 2026, not yet published), which the second reading added by sequence, share the 14
     substitutions of 4E5K and add E332N and C336D beyond the end of its sequence. They are not entered, because the
     paper cannot tell whether those belong to 17X.
   - TS Y94F 2FTN and 2FTO, and no entry for the other variants, in both readings.
7. **Steps and notes taken over from the second reading:** the acceptor of the TS proton abstraction is the
   active-site water oxygen, as the paper names it; the POR proton donor is the Tyr OH, and its numbering per enzyme
   (Y193 in T. elongatus and Synechocystis, Y189 in G. violaceus, Y276 in Arabidopsis, YKDSK motif) goes into the
   notes. Otherwise both readings describe the same steps.
8. **Judgement calls made the same way by both readers:**
   - S019: the fits of the KIEs in the Fig. 4 legend, not the separate Arrhenius fits of kH and kD in the text;
     ΔEA H/D read as Ea(D) − Ea(H); pH 9.5 against the Fig. 4B legend's "pH 9.0 and 5.0"; the range of the pH 9.5
     fit, 15–35 °C.
   - S020: Table 1 rather than the text for the intrinsic H/T KIEs; ΔEa as E_T − E_L; Ea of k_hydride as Ea of the
     light isotope; the Table 3 KIEs as H/D, as column head and text say.
   - S021: 6.0 at 0 °C without error; the fitted range −2.5 to 5.0 °C; `kind` intrinsic.
   - S022: ΔΔH‡ as dEa_kcal, read as heavy − light, since the paper does not define its direction; the ranges above
     and below the break at −27 °C; no pH for the hydride rows.
   - S023: `kind` intrinsic for Dkcat, which the paper declares equal to the intrinsic KIE, `observed` for
     D(kcat/KM) and Dkobs; the 17X values at 25 °C entered once.

## Inconsistencies inside the papers

None of them changes an entered value. All were checked by the curator in the HTML.

- **S019:** the Fig. 4B legend says pH 9.0 and 5.0, the Methods and the text pH 9.5; Ea(D) of the wild type is
  37.7 ± 0.7 kJ/mol in the text and ± 0.6 in the Fig. 3 legend; A_H/A_D is 0.108 ± 0.04 in the text and 0.109 ± 0.043
  in Fig. 4 (wild type), 0.0025 ± 0.0007 and 0.0024 ± 0.0004 (G121V); the text defines ΔEA for G121V as
  EA(H) − EA(D) = −15.7 kJ/mol, the Fig. 4 legend prints 15.83 ± 0.44.
- **S020:** the text gives the intrinsic H/T KIEs as 3.25 ± 0.31 (wild type) and 3.17 ± 0.22 (Y94F), Table 1 as
  3.2 ± 0.2 and 3.2 ± 0.3, so the errors are swapped; above 20 °C the text prints E_T − E_H = −0.03 ± 0.30 kcal/mol,
  Table 2 0.03 ±0.40; the caption of Table 3 says T kcat, the column head and the text Dkcat; a footnote gives the
  KIE at zero CH2H4folate as 1.8 (Figure 2), the text 1.86 ± 0.10 (Figure 3).
- **S021:** the Arrhenius plot spans −2.5 to 10.5 °C in the text and −2.5 to 10.0 °C in the Fig. 5 caption; the
  quench times are 12–160 ms in Methods and 10–120 ms in Results.
- **S022:** none among the printed numbers; the Tyr-193 of Fig. 1 is not assigned to one of the four enzymes.
- **S023:** A_H/A_D of 17X is 1.60 ± 0.09 in the Results and rounded to 1.6 in Table 3 and the Abstract; the text
  refers to Figure 5 for the mutants' temperature dependence, which Figure 6 shows.

## SCHEMA.md

Three conventions written down: an intrinsic value calculated from competitive kcat/KM KIEs keeps `quantity`
kcat/KM; intramolecular competition counts as `competitive`; a wild type with very many PDB entries keeps `pdb`
empty, and `notes` names the entries the source uses.

All 45 isotope effects, 24 temperature series, 12 enzyme variants and 17 steps of S019–S023 are now `verified`.
