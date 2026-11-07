# MEG-NEN second reading (ai-2): S029–S033

I wrote three files in `out/`:

| file | rows | S029 | S030 | S031 | S032 | S033 |
|---|---|---|---|---|---|---|
| measurements.csv | 28 | 2 | 0 | 21 | 0 | 5 |
| temperature.csv | 9 | 2 | 1 | 2 | 2 | 2 |
| enzymes.csv | 13 | 1 | 1 | 5 | 2 | 4 |

**How I read the papers**
- I parsed the HTML with BeautifulSoup. The scripts are `work/extract.py` and `work/dumptables.py`, and the extracted texts are `work/*.txt`.
- Every text node containing a digit was checked to be present in the extraction. Footnote markers were checked against the raw HTML.
- `work/verify.py` re-opened all three CSVs and compared each number with the table cell or text string it came from: 69 checks, 0 failures.
- Enzyme metadata came from UniProt REST and RCSB search/data (`work/lk.py`, cache in `work/lookups/`). RCSB was searched by accession and by sequence at ≥90 % identity (≥95 % for P08170 and A0A0A1EQY0).
- Nothing outside `reading2_s029-s033/` was opened.

**Conventions I applied to every paper**
- **Eyring results:** ΔΔH‡ goes into dEa_kcal and A′H:A′D into AH_AX. ΔH‡ is never put into Ea_light_kcal, because it differs from Ea by RT. This affects S029, S030 and S031.
- **n_temperatures:** filled only where the paper lists or defines the temperature grid (S029, S031, S033). Otherwise empty.
- **Units:** kJ/mol ÷ 4.184 to four significant figures, errors included. °C + 273.15.

---

## S029 – Hay 2007 PNAS (morphinone reductase, MR)

**Entered**
- **M1:** KIE 4.0 ± 0.3, 298.15 K, 1 bar, pH 8.0 (Table 1, row k0 (25 °C), column KIE).
- **M2:** KIE 5.2, no error, 298.15 K, 2 kbar (Discussion "Pressure Dependence of the KIE", and Abstract).
- **T1 (1 bar):** A′H:A′D 0.09 ± 0.15; ΔΔH‡ 9.3 ± 3.8 kJ/mol = 2.223 ± 0.9082 kcal/mol.
- **T2 (2 kbar):** A′H:A′D 0.02 ± 0.03; ΔΔH‡ 13.6 ± 3.7 kJ/mol = 3.250 ± 0.8843 kcal/mol.
- Both series: 278.15–313.15 K, n = 8.
- Fields: H/D, primary, single_turnover (stopped-flow reductive half-reaction at saturating NADH), noncompetitive, observed, hydride from NADH C4 (pro-R H) to FMN N5.

**Left out**
- *Isotope effects on activation volume and pressure derivatives* (no schema field):
  - ΔΔV‡ −4.0 ± 1.3 cm³/mol
  - dΔΔV‡/dT −0.05 ± 0.06
  - dΔΔH‡/dp 0.6 ± 1.1
  - dΔΔS‡/dT 0.5 ± 4.1
  - d ln A′/dp 0.1 ± 0.5
- *ΔΔS‡* 20 ± 13 and 32 ± 13 J/mol/K: put in notes only.
- *Model outputs:* ΔΔH‡ fixed at 5.2 kJ/mol; maximum ΔΔH‡ ≈5.7 kJ/mol; minimum A′H:A′D ≈0.4; ω_X < 120 cm⁻¹; k_HO 5.3 J m⁻².
- *Figures and SI only:* KIEs at the other pressures and temperatures (Fig. 2C, Fig. 4B; SI Figs. 5–9).
- *Earlier work:* the paper cites it (refs 13, 41, 42) without numbers.

**Judgement calls**
- *Which version of 4.0:* Table 1's 4.0 ± 0.3 is the ratio of k0, which is extrapolated to 0 bar by the Eq. 1 fit. The text says "At 298 K and 1 bar, we have measured here that the KIE = 4.0", citing Table 1. I entered it once, as the Table 1 version (it carries the error), with the condition "1 bar" as the text states.
- *kind = observed:* the Introduction says "the observed KIE is essentially the intrinsic KIE (13, 41, 42)". I kept observed because the statement is hedged, cites earlier work, and the paper calls its own values "observed/measured".
- *Sign of ΔΔH‡:* the text defines ΔΔH‡ = ΔH‡D − ΔH‡H, which is heavy − light, so no sign change. It checks: 41.3 − 32.0 = 9.3.
- *Other fields:*
  - n = 8 comes from "every 5°C between 5°C and 40°C (278–313 K)".
  - pH 8.0 is from Materials and Methods.
  - The NAD²H contains ≈6 % R-C4 ¹H, and the paper did not correct for it.

**Inconsistencies in the paper**
- In the Table 1 HTML, the NADH ln A′ value 11.4 ± 0.6 sits in the "ln A′" heading row instead of the "1 bar" row. exp(11.4 − 13.8) = 0.09 confirms it belongs to 1 bar.
- The text says "dΔΔV‡/dp is not significantly less than zero", but the Table 1 row is dΔΔV‡/dT.
- The Table 1 row "dΔΔS‡/dT" carries the units J·mol⁻¹·K⁻¹·kbar⁻¹.
- The KIE column mixes directions: ΔΔV‡ is H − D, while ΔΔH‡ and ΔΔS‡ are D − H.

## S030 – Anandarajah 2013 JPOC (glucose dehydrogenase of *Bacillus megaterium*, BmGDH)

**Entered**
- **T1, monophasic treatment:** A_H/A_D 20 (printed "ca. 20") and dEa −1.195 kcal/mol (−5 kJ/mol), no errors printed.
- 288.15–313.15 K, pH 8.0 (Table 1 footnote a), kcat/KMβ, noncompetitive, observed.

**Left out**
- *TaGDH values (ref 16):* the lower block of Table 1, and the Introduction values (KIE ~1.6, A_H/A_D 2.0 ± 1.6 and 0.12 ± 0.15, 6–7 kJ/mol, KIEs 10–12 vs 2–3).
- *Biphasic BmGDH regimes:* the paper prints only the separate isotopic values, no difference or ratio:
  - high-T: ΔH‡ 2.1 ± 5.4 (H) and 0.42 ± 8.0 (D) kJ/mol
  - low-T: ΔH‡ 42 ± 10 (H) and 44 ± 12 (D) kJ/mol
  - ΔS‡ values for both regimes

  Making a row would mean recomputing a difference, so there is none.
- *"Observed isotope effects around 2":* approximate and at no stated temperature.
- *Hypothetical values:* "7 to 8-fold" and "reciprocal of 8–9".
- *Figure only:* the individual rate constants (Fig. 2).

**Judgement calls**
- *Sign of dEa:* the paper prints only the magnitude "5 kJ/mol" and says "it is the H-substrate that exhibits the larger enthalpy" (26 vs 21 kJ/mol). So heavy − light = −5 kJ/mol.
- *Temperature range:* I used 15–40 °C (Results and Fig. 2 legend). The Abstract says 25–55 °C.
- *n left empty:* the fit also includes steady-state data at three temperatures the paper does not state.
- *kind = observed:* the Concluding Remarks say the authors do not know whether the effects are intrinsic.

**Inconsistencies in the paper**
- Temperature range: Abstract 25–55 °C vs Results 15–40 °C.
- Optimal growth temperature: Abstract "around 35 °C" vs Introduction "~30 °C".
- The Introduction calls the organism "Bacterium megaterium".
- The Discussion and Concluding Remarks cite "Figure 1" for the Eyring plots, which are in Figure 2.
- Enzyme concentration: Table 1 footnote [BmGDH] 1.32–3.68 µM vs Experimental "50–60 nM".
- The same 5 kJ/mol difference is said to give "7 to 8-fold" in one place and "8–9" in another.
- The claim "βo < KMβ/15,000" does not fit 10 µM glucose with KMβ = 15 mM; it looks like 1,500 was meant.

## S031 – Nagel 2013 JBC (ht-ADH and ps-ADH)

**Entered: 21 measurements**, all kcat, H/D, primary (α,α-d2 benzyl alcohol, both α-H deuterated), noncompetitive, observed, pH empty.
- *Table 1, 30 °C:*
  - W87F 3.4 (±0.6)
  - W87L 3.0 (±0.3)
  - W87A 3.2 (±0.6)
  - Y25A 2.9 (±0.2)
- *Table 3, ht-W87A* (Dkcat ± Error):
  - 12.5 °C: 3.2 ± 0.2
  - 15 °C: 3.1 ± 0.4
  - 20 °C: 2.9 ± 0.4
  - 28.5 °C: 3.6 ± 0.5
  - 38 °C: 3.2 ± 0.6
  - 45 °C: 2.9 ± 0.2
  - 52 °C: 3.0 ± 0.3
- *Table 3, ps-A25Y:*
  - 5 °C: 2.4 ± 0.1
  - 16 °C: 2.8 ± 0.1
  - 29 °C: 3.7 ± 0.6
  - 46 °C: 3.5 ± 0.6
  - 52 °C: 3.6 ± 0.6
- *Table 3, ht-Y25A:*
  - 10 °C: 2.8 ± 0.2
  - 20 °C: 3.4 ± 0.6
  - 30 °C: 2.7 ± 0.1
  - 40 °C: 2.4 ± 0.2
  - 50 °C: 2.9 ± 0.3

**Entered: 2 temperature rows** (Table 2, Ea(D) − Ea(H), heavy − light as labelled, so no sign change):
- W87A: 0.2 ± 0.01 kcal/mol, 285.15–325.15 K, n = 7.
- Y25A: 0.5 ± 0.1 kcal/mol, 283.15–323.15 K, n = 5.
- Ea_light is empty because Table 2 gives only ΔH‡ and TΔS‡.

**Left out**
- *Wild-type ht-ADH (ref 5):* KIE 3.2 (±0.2); ΔEa 0.9 (±0.05) for 5–30 °C and 0.1 (±0.01) for 30–65 °C.
- *Wild-type ps-ADH (ref 22):* KIE 3.2; ΔEa 4.5 (±1.5).
- *ps-A25Y ΔEa:* not determined (ND).
- *Not isotope effects:* the A_OBS values.
- *Figures only:* Figs. 1 and 6.

**Judgement calls**
- *pH left empty:* the kinetic assays cite ref 5. Only the inactivation-study "standard assay" is given (50 mM potassium phosphate, pH 7.0).
- *ps-A25Y at 29/30 °C:* Table 1 ("30 °C") and Table 3 (29 °C) give the same KIE, 3.7 (0.6), and the same kcat 3.8. Table 3 footnote b says KIEs were measured only at the listed temperatures, so I entered it once, at 29 °C.
- *Y25A at 30 °C:* Table 1 gives 2.9 ± 0.2 and Table 3 gives 2.7 ± 0.1. The values differ, so both are entered and flagged.
- *W87A:* the Table 1 value at 30 °C and the Table 3 value at 28.5 °C are different measurements, so both are entered.
- *n_temperatures:* taken from the Table 3 lists. T_min and T_max are taken from the Table 2 column headings.
- *Acceptor:* NAD⁺ C4 is not named in the paper.

**Inconsistencies in the paper**
- Y25A at 30 °C: kcat 14.0 vs 13.0 s⁻¹ and KIE 2.9 ± 0.2 vs 2.7 ± 0.1 between Tables 1 and 3.
- ps-A25Y: "30 °C" vs 29 °C, and kcat error ±0.2 vs 0.3, between Tables 1 and 3.
- W87A temperature range: Table 2 12–52 °C, Table 3 starts at 12.5 °C, Fig. 1 legend says 10–52 °C.
- ps-A25Y upper range: "20–52 °C" in Results vs "between 20 and 50 °C" in Discussion.
- W87A preincubation: 100 µM enzyme (Methods) vs 200 µM (Results).
- The paper speaks of an "x-ray structure" of ps-ADH but also says it was "homology modeled". The only ps-ADH entry, 4Z6K, was released in 2016.

## S032 – Ranasinghe 2017 JACS (Candida boidinii formate dehydrogenase, FDH)

**Entered**
- ΔEa(T−H) 1.65 ± 0.11 kcal/mol for half-heavy FDH ([¹³C;¹⁵N]).
- ΔEa(T−H) 2.50 ± 0.07 kcal/mol for heavy FDH ([¹³C;¹⁵N;²H]).
- Both: intrinsic H/T, kcat/KM (Northrop method), competitive, 278.15–318.15 K, pH 7.5.
- ΔEa = Ea(T) − Ea(H) is heavy − light, so no sign change.

**Left out**
- *Light FDH:* ΔEa 0.05 ± 0.10 kcal/mol (ref 41).
- *SI only:* observed and intrinsic KIEs and Cf values (Tables S1–S3).
- *Figures only:* A_L/A_H (Fig. 1A) and ΔEa of Cf (Fig. 2B).
- *Single-turnover KIE:* only described as "essentially equal to one". The rate pairs in Table 2 were not divided.

**Judgement calls**
- *variant:* named "half-heavy [13C;15N]" and "heavy [13C;15N;2H]"; the sequence is wild type.
- *uniprot = A0A0A1EQY0:* the paper says the enzyme was prepared as in ref 41. Ref 41's structures, 5DN9 and 5DNA, are 100 % identical to A0A0A1EQY0. Swiss-Prot O13437 differs from it at 11 positions.
- *pdb empty:* there is no structure of labelled FDH.
- *EC:* kept the paper's 1.2.1.2; UniProt lists 1.17.1.9.

**Inconsistencies in the paper**
- Wrong table references: the k_obs values are cited as "Table 1" (they are in Table 2), and the steady-state parameters as "Table 2" (they are in Table 3).
- The Km values for NAD⁺ and formate are swapped between the Methods and Table 3.
- The Fig. 1 legend has "1/27π"; 1/2π is meant.
- The text cites "Scheme 1" for eq. 7 (Scheme 2 is meant) and "Fig 3B" (Fig. 1B is meant).

## S033 – Kockler 2026 Protein Sci (plant lipoxygenases)

**Entered: 5 measurements**, all at 298.15 K, D = 11,11-D2-LA (Table 2 footnote b), s.e.m. (footnote d):
- GmLOX1: Dkcat 72 ± 3, pH 9.0.
- OsLOX1: Dkcat 37 ± 2, pH 7.0.
- SlLOXA: Dkcat 62 ± 7, pH 7.0.
- AtLOX1: Dkcat 50 ± 1, pH 7.0.
- GmLOX1: Dkcat/Km "ca. 24", kcat/KM, pH 9.0.

**Entered: 2 temperature rows** (283.15–313.15 K, n = 7):
- GmLOX1: ΔEa 0.9 ± 0.5 kcal/mol, Ea(H) 2.2 ± 0.4 kcal/mol.
- AtLOX1: ΔEa −0.3 ± 0.6 kcal/mol, Ea(H) 7.2 ± 0.6 kcal/mol.

**Left out**
- *Cited literature values:* Dkcat 60–80 and 20–100, Ea ca. 2 kcal/mol, I553G ΔEa 5 kcal/mol, Ea 8–13 kcal/mol.
- *No isotope effect:* OsLOX1 and SlLOXA have Ea(H) only (1.2 and 6.0 kcal/mol; ΔEa not measured), and the ALA data in Table 3 have none.
- *SI only:* the D31-LA data (Fig. S2c).
- *Rounded text versions:* ~70, ~40–60, ~1 kcal/mol, 6–7 kcal/mol.

**Judgement calls**
- *Dkcat/Km entered:* the authors derived it themselves from Table 2. Its inline definition is written D/H, but 24 is H/D.
- *Labelled position of the ΔEa rows:* set to D31-LA, because the Fig. 3 legend names it and the text cites Fig. 3 for ΔEa. Table 2 footnote b instead assigns the D rows to 11,11-D2-LA. This conflict is flagged in the notes.
- *transfer = H_atom:* the paper describes hydrogen abstraction giving a carbon radical; PCET appears only in cited titles.
- *pH:* taken from Table 2 footnote d.

**Inconsistencies in the paper**
- The deuterated substrate for Ea(D): D31-LA (Fig. 3) vs D2-LA (Table 2).
- Two cells use "+" instead of "±": "10.5 + 0.4" and "35 + 2".
- Enzyme concentration for D-LA: "10–20-fold" higher (Methods) vs 90–120 nM against 2–4 nM (Discussion).
- Borate buffer: 50 mM (Methods) vs 100 mM (Table 2, Fig. 2).
- AtLOX1 switch residue "V557" in the text vs V577 in Table 1; Q06327 has Asn at 557.
- GmLOX1 "L266" is Val in P08170. "I252" is Lys in P08170; I552 is probably meant.

## Output 3 (enzymes.csv) in brief

| source | enzyme | UniProt | pdb |
|---|---|---|---|
| S029 | MR, WT | Q51990 | 1GWJ;2R14 |
| S030 | BmGDH, WT | empty | empty |
| S031 | ht-ADH W87F, W87L, W87A, Y25A | P42328 | empty |
| S031 | ps-ADH A25Y | Q8GIX7 | empty |
| S032 | half-heavy and heavy FDH | A0A0A1EQY0 | empty |
| S033 | GmLOX1 | P08170 | empty |
| S033 | AtLOX1 | Q06327 | 8I6Y |
| S033 | SlLOXA | P38415 | empty |
| S033 | OsLOX1 | Q76I22 | empty |

- **MR:** 1GWJ has G at position 160 where Q51990 has E, and RCSB does not list it as a mutation. 3GX9 (N189A) is excluded.
- **BmGDH:** this is a commercial enzyme (Sigma G7653) with no isozyme or strain given, so no UniProt entry can be assigned. Seven reviewed candidates are listed in the notes.
- **ht-ADH and ps-ADH:** the residue numbering matches UniProt at Y25, W49, W87, F272 (ht-ADH) and A25 (ps-ADH). RCSB has only wild-type and other mutants for these enzymes.
- **GmLOX1:** it has many wild-type entries. The paper itself names 1YGE, 3PZW and 1F8N.
- **AtLOX1:** 8I6Y is the wild-type full-length sequence, identical to Q06327.
- **DOIs:** no PDB entry cites any of the five papers' DOIs.
- **EC numbers:** taken from UniProt for S031 and S033, which give none; S029 has no EC in either the paper or UniProt.
