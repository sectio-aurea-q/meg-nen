# Second reading of S029–S033 (7 November 2026)

First reading `ai-1`, second reading `ai-2`. Both readers worked from the PMC pages of the five papers, saved on
7 November 2026 (S029, S031 and S033 as publisher versions, S030 and S032 as author manuscripts); the published PDFs
and the supporting information were not read. The second reader worked from those pages alone, did not see the first
reading, and looked up UniProt and RCSB PDB again for every enzyme. Its instructions repeated the rules of
CURATION.md and SCHEMA.md, named pressure among the conditions that get a row of their own, and allowed the web only
for these lookups. Files in this folder:

- `reading2_measurements.csv`, `reading2_temperature.csv`, `reading2_enzymes.csv`, `report.md`: the second reading as
  delivered (`report.md` saved by the curator from the second reader's answer; the path of its output folder was
  shortened)
- `comparison.md`: row-by-row comparison of both readings, before the decisions below

## Result

All 36 rows of the first reading (27 isotope effects, 9 temperature series) have a partner in the second reading,
and all of them agree in value, error, temperature, Arrhenius and Eyring parameters and number of temperatures. They
differ in the pH of the 23 rows of S031 (point 1) and in the temperature range of the S030 series (point 2); the
second reading has one row more (point 3). Both readers left out the same values: the wild-type columns of S031
(refs. 5 and 22), the light FDH of S032 (ref. 41), the TaGDH rows of S030 (ref. 16), the biphasic BmGDH fits (no
printed isotope difference), the isotope effects on activation volume and the pressure derivatives of S029 (no field),
the single-turnover kobs of S032 (no printed ratio), values in the SI or in figures only, and all values cited from
other papers. Decisions:

1. **pH of S031 (M0106–M0126, T0065, T0066):** the first reading took pH 7.0 from the standard activity assay in
   Experimental Procedures; the second left it empty, since the kinetic assays follow ref. 5 and the paper states no
   pH for them. The second reading is taken (pH only when the source states it for the measurement); `notes` give the
   pH of the standard assay. S018, from the same lab, had stated pH 7.0 for its own characterizations.
2. **Temperature range of the BmGDH series (T0064):** the first reading left it empty, because the Abstract
   (25–55 °C) and the Results and Fig. 2 legend (15–40 °C) disagree; the second used 15–40 °C. The second reading is
   taken, since the Results and the legend describe the measurements; `notes` give the Abstract's range and say that
   the monophasic fit includes steady-state data from three temperatures the source does not name.
3. **D(kcat/KM) of GmLOX1 (M0131, only in the second reading):** the Discussion prints "at 25°C, the Dkcat/Km for
   GmLOX1 is ca. 24 (from data in Table 2)". The first reader had missed it; checked in the HTML, it is entered as
   printed, 24 without error, with `extracted_by` ai-2 and `checked_by` ai-1. The source computed it from its own kcat
   and Km values; its inline definition writes the ratio as D over H, while 24 is H over D.
4. **EC of the labelled FDHs (S032):** the second reading took the source's EC 1.2.1.2, the first UniProt's 1.17.1.9.
   1.17.1.9 is kept, as for `FDH_CANBO_WT`, and SCHEMA.md now says that `ec` holds the number UniProt gives, while a
   different number printed by the source goes into `notes`.
5. **PDB entries of MR (existing row `MR_PSEPU_WT`, from S006):** the second reading listed 1GWJ and 2R14. The curator
   confirmed them by sequence (1GWJ has G160 where Q51990 has E160, not marked as a mutation; 2R14 is identical;
   3GX9 is N189A and not assigned). They are entered under the rule for wild types with few entries. The row stays
   `single` until a person checks it, as decided in the second check of the enzymes on 7 November.
6. **Acceptor of the MR reductive half-reaction (existing step `MR_PSEPU_WT_RED`):** S029 names the N5 atom of FMN,
   which the second reading also used. The acceptor becomes FMN N5, and `notes` say which source names what.
7. **Kept from the first reading:** the organism Geobacillus stearothermophilus for the ht-ADH variants (the second
   reading wrote Bacillus stearothermophilus, as the source does; `notes` say so, as for S018); `PCET` for the four
   plant LOX steps (second reading: `H_atom`), as for all lipoxygenases (S024–S028, point 5); the notation
   half-heavy (13C, 15N) and heavy (13C, 15N, 2H) for the labelled FDHs (second reading: brackets), now written into
   SCHEMA.md; organism names without the common names in parentheses.
8. **Judgement calls made the same way by both readers:**
   - S029: the KIE 4.0 ± 0.3 of Table 1 (k0, extrapolated to 0 bar) as the 1-bar value, as the text calls it; 5.2 at
     2 kbar without error; `kind` observed, although the source calls the observed KIE "essentially the intrinsic
     KIE" with reference to earlier work; ΔΔH‡ = ΔH‡D − ΔH‡H; n = 8 from "every 5°C between 5°C and 40°C"; pH 8.0.
   - S030: only the monophasic Eyring series, with ΔΔH‡ = −5 kJ/mol (the H-substrate has the larger enthalpy) and
     A′H/A′D ca. 20; no rows for the biphasic fits; `kind` observed; no accession, since the commercial enzyme could
     be any of seven isozymes.
   - S031: Table 1 (30 °C) and Table 3 as separate measurements, except ps-A25Y, where Table 1 repeats the 29 °C
     value of Table 3 and is entered once; ht-Y25A at 30 °C with both 2.9 ± 0.2 (Table 1) and 2.7 ± 0.1 (Table 3);
     ranges from the Table 2 headings; `Ea_light` empty (Table 2 gives ΔH‡).
   - S032: accession A0A0A1EQY0, since the enzyme follows ref. 41, whose recombinant FDH is the protein of 5DN9 and
     5DNA; no PDB entry for the labelled proteins; only ΔEa(T−H) is printed.
   - S033: 11,11-D2-LA (Table 2 footnote) for the Dkcat rows and D31-LA (Fig. 3) for the ΔEa rows, with the conflict
     in `notes`; pH from the Table 2 footnote; 8I6Y for AtLOX1.

## Inconsistencies inside the papers

None of them changes an entered value. All were checked by the curator in the HTML.

- **S029:** in Table 1 the NADH value of ln A′ at 1 bar (11.4 ± 0.6) stands in the heading row; the text speaks of
  dΔΔV‡/dp where Table 1 has dΔΔV‡/dT, and the row dΔΔS‡/dT carries the units J·mol−1·K−1·kbar−1; the KIE column
  gives ΔΔV‡ as H − D but ΔΔH‡ and ΔΔS‡ as D − H.
- **S030:** the temperature range is 25–55 °C in the Abstract and 15–40 °C in the Results and the Fig. 2 legend;
  optimal growth "around 35 °C" (Abstract) and "in the neighborhood of 30 °C" (Introduction); the Introduction writes
  Bacterium megaterium; the Discussion refers to Figure 1 for the Eyring plots of Figure 2; enzyme 50–60 nM (Kinetic
  measurements) against 1.32–3.68 µM (Table 1 footnote a); the same 5 kJ/mol difference gives "7 to 8-fold" and "the
  reciprocal of 8–9"; "βo is less than KMβ/15,000" does not hold for 10 µM glucose and KMβ = 15 mM.
- **S031:** ht-Y25A at 30 °C has kcat 14.0 (±1.0) and KIE 2.9 (±0.2) in Table 1, 13.0 ± 1.0 and 2.7 ± 0.1 in Table 3;
  ps-A25Y appears at "30 °C" in Table 1 and at 29 °C in Table 3, with kcat errors ±0.2 and 0.3; the range of
  ht-W87A is 12–52 °C (Table 2), 12.5–52 °C (Table 3) and 10–52 °C (Fig. 1 caption); ps-A25Y above its break is
  measured "between 20 and 52 °C" (Results) and "between 20 and 50 °C" (Discussion); W87A is preincubated at 100 µM
  (Experimental Procedures) and 200 µM (Results); the Results speak of x-ray structures of ps-ADH, the Discussion of
  homology modelling (the only ps-ADH entry, 4Z6K, was released in 2016).
- **S032:** the text cites Table 1 for the kobs values of Table 2 and Table 2 for the steady-state parameters of
  Table 3, Scheme 1 for the ordered mechanism of Scheme 2, and Fig. 3B where Fig. 1B is meant (Fig. 3 has no panel
  B); the Fig. 1 legend writes ν = (1/27π)(k/μ)^1/2.
- **S033:** Ea(D) comes from D31-LA in Fig. 3, while Table 2 labels its D rows 11,11-D2-LA; two cells print "+" for
  "±" (10.5 + 0.4, 35 + 2); the enzyme concentration with D-LA is 10- to 20-fold higher in Methods, 90–120 nM against
  2–4 nM in the Discussion; borate is 50 mM in Methods and 100 mM in Table 2 and the Fig. 2 legend; the text names
  V557 of AtLOX1, Table 1 and Q06327 give V577; L266 and I252 of GmLOX1 are V266 and K252 in P08170 (I552 is probably
  meant).

## SCHEMA.md

Two conventions written down: `ec` holds the number UniProt gives, and a different number printed by the source goes
into `notes`; an isotope-labelled protein is entered in `variant` by its labels, e.g. `heavy (13C, 15N, 2H)`.

All 28 isotope effects, 9 temperature series, 12 enzyme variants and 12 steps of S029–S033 are now `verified`;
`MR_PSEPU_WT` gains two PDB entries and stays `single`.
