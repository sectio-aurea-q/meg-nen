# Supporting information read for open point 3 — 19 November 2026 (second round)

## Why

The reading of the main texts earlier today (`curation/2026-11-19_source_reading_open_point_3/`) left five points
that only the supporting information or a cited paper could answer: the heavy substrate, buffer and pH of S057,
S058 and S059; the fitted range of S059 and S051; the cryo-solvent of the POR series (S022, its ref. 12).

## Sources

- S057, SI (oc7b00142_si_001.pdf, 57 pages); S059, SI Appendix (pnas.2211630120.sapp.pdf, 31 pages); S051, SI
  (ja208844j_si_001.pdf, 27 pages): from the supplementary-files service of Europe PMC; text by `pdftotext -layout`.
- Heyes, Sakuma, de Visser and Scrutton, J. Biol. Chem. 284, 3762–3767 (2009), doi:10.1074/jbc.M808548200, ref. 12
  of S022: the open-access article page was read in the browser; Experimental Procedures and Tables 1–3 were kept
  as text. Its supplemental tables were not obtained.
- Not obtained: the SI of S058 (Hu 2016). T0121–T0132 stay as they are.

Four questions (`questions.md`), two readers blind to each other (`reading1.md`, `reading2.md`); the readers are
runs of the model. They agree on every question.

## Result and what changes (`changes.csv`)

1. **S057 (T0115–T0120, M0239–M0244).** The heavy substrate is D31-LA (SI Table S7, footnote b); 0.1 M sodium
   borate, pH 9.0; 10–45 °C in steps of 5 °C, Y317L only 15–45 °C. `heavy_other` nd → 30, `pH` → 9.0,
   `labelled_position` filled; T0119 `T_min_K` 283.15 → 288.15. The SI does not print at which temperature the
   Dkcat of Table 1 stands (the main text does: 30 °C) and says its Table S7 rates are not corrected for iron.
2. **S059 (T0133, T0134, M0245, M0246).** Perdeuterated d31-LA; 100 mM borate, pH 9.0; Arrhenius analysis over
   10–40 °C, at least seven temperatures. `heavy_other` nd → 30, `pH` → 9.0, `labelled_position` filled;
   `T_min_K`, `T_max_K` → 283.15, 313.15. The SI prints no rate at any temperature but 30 °C for these variants, so
   slope and single value cannot be recomputed, and it does not say more on the origin of the data than Table S1
   ("This work").
3. **S051 (T0102, T0103).** SI Tables S1 (pH 7) and S2 (pH 9) list 5, 10, 15, 20, 25, 30 °C; KIE at 5 °C 2.25 ± 0.13
   (pH 7) and 2.61 ± 0.10 (pH 9). Which temperatures entered the fit is not stated for MpDHFR, so `T_min_K` and
   `T_max_K` stay empty (rule 11); the tabulated range is added to `notes`. The values of the tables are not
   entered here.
4. **POR (T0035, T0036, T0038, T0039, T0041, T0042, T0044, T0045).** Ref. 12 of S022 gives the medium of the
   temperature-dependence measurements: 44 % glycerol and 20 % sucrose with 50 mM Tris-HCl, pH 7.5, 0.1 % Genapol,
   0.1 % β-mercaptoethanol; controls without cryoprotectant showed no influence on KIE and SIE. S022 says its
   measurements were made "as described previously (12)". `cosolvent` → `glycerol 44 %; sucrose 20 %`, `pH` → 7.5,
   with the note that both come by this reference and are not printed in S022. The single values at 25 °C
   (M0056–M0063) and the solvent series are left as they are: neither paper says in which medium they were measured.

## Found on the way — open, not decided

- **Rule 1, T0035 and T0036.** The ΔΔH‡ of T. elongatus in S022 Table 1 (8.2 ± 0.6 above, 0.4 ± 1.0 below the
  break) are number for number those of Table 3 of the 2009 paper, while every other T. elongatus number of S022
  differs from 2009 (rate, KIE, proton-transfer ΔΔH‡). S022 does not say that it takes them from ref. 12. If they
  are the 2009 fit, the two rows belong to the 2009 paper. A note is added to both rows; nothing is moved.
- S051: Table S2 is captioned with kH/kD, the main text calls the pH 9 series steady state; two tables of the SI
  disagree on single rates (pH 9, 20 °C; pH 7, 5 °C).
- S057 and S059: iron correction of the rates is stated differently in main text and SI.
- S058: SI still to be read.

No value, error or status changes.
