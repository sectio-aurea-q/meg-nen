# MEG-NEN second reading (ai-2): S056–S060

The three CSVs are written and every value and error in them matches the HTML (0 mismatches).

**Outputs**
- `out/measurements.csv`: 30 rows
- `out/temperature.csv`: 24 rows
- `out/enzymes.csv`: 18 rows

(The list of output files was shortened by the curator; the files are in this folder as `reading2_*.csv`.)

**How I read the papers**
- I parsed the HTML with BeautifulSoup (`work/extract.py`, run as `python3 -I`).
- I rendered the XML tables as a cross-check (`work/xml_tables.py`). Captions, cells and footnote markers were identical to the HTML.
- The XML added nothing numeric:
  - The display equations of S056 and S057 are images in the XML too.
  - S059 Eqs. 1–2 (k_obs = F(conf) × k(tun); F(conf) = E(active)/E(total)) are not in the HTML; I read them in the XML. They hold no values.
- `work/verify.py` re-reads every value and error from the row named in `location`. I checked the column positions by hand. Phrases taken from text and footnotes were matched in the raw HTML.

**Independence**
- I opened nothing outside `reading2_s056-s060/` and used no remote-device or browser tools.
- The web was used only for rest.uniprot.org, search.rcsb.org and data.rcsb.org.

**Conventions used for all five papers**
- **Variants:** one-letter code in the paper's own numbering. S056's table labels (e.g. "546A/553A") are kept in `location`.
- **Units:** temperatures are °C + 273.15. No paper uses kJ/mol.
- **Numbers:** numeric fields use ASCII minus; `as_printed` keeps the printed "−".
- **Errors:** parenthesised or ± values as printed. Only S060 states the error type (s.e.m., for kcat, kcat/KM and Dkcat).
- **Step:** substrate is linoleic acid and the donor is C11 in all papers. The acceptor is Fe(III)–OH oxygen for SLO-1 and the Mn-bound hydroxide oxygen for MoLOX.
- **Transfer:** PCET, as S056, S057, S059 and S060 assign it; S058 does not assign one (see below).
- **Kind:** no paper calls any value intrinsic, so every row is `observed`.

## S056 Sharma & Klinman 2015 (SLO-1 double mutants)

**Entered**
- **Table 1, row 553A/754A:** Dkcat 85 (7) at 303.15 K, pH 9.0. The row has no source footnote; the other rows (footnotes b–e) are cited.
  - kcat, noncompetitive: protio-LA and 11,11-²H₂-LA were assayed separately.
- **Table 2:** 12 competitive D(kcat/KM) values, for 4 enzymes × (pH 9.0, 30 °C; pH 9.0, 10 °C; pH 7.0, 30 °C).
  - Footnote a says all are new to this study.
  - Method: a 1:4 mixture of protio-LA and perdeutero-LA (²H₃₁-LA), analysed by HPLC.
  - pH 7.0 buffer: 0.1 M Tris-HCl.
- **Table 3:** 6 solvent isotope effects on kcat and kcat/KM (WT, I553A/L754A, L546A/L754A) at 303.15 K.
  - H₂O at pH 9.0; D₂O at pD 9.0 (meter reading 8.6), from footnote a.
- **temperature.csv, I553A/L754A:**
  - A_H/A_D "∼0.2" and Ea(D) – Ea(H) = 3.5 kcal/mol, from text (Results 3.2), no errors. The direction is as printed and matches the schema.
  - Ea(H) 6.9 (0.2), from Table 1.

**Left out**
- **Cited Table 1 rows:** WT (ref 19) 81 (5); 553A (ref 13) 93 (4); 546A (ref 19) 93 (9); 546A/553A (ref 20) 128 (3); 754A (ref 13) 112 (11); 546A/754A (ref 18) 729 (26). Their Ea(H) and A_H are also cited.
- **Cited text values:** KIE ∼80 (WT) and 500–700 (ref 18); "WT (81)" (ref 13); "(128)" (ref 20).
- **Not a measurement:** "intrinsic KIE for H transfer of ∼80" is an assumption based on WT.
- **Derived:** Table 2 footnote b column averages 32, 29, 46.
- **Figures and SI only:** Fig. 2 and Fig. 4 data; SI rate-constant tables; viscogen numbers.

**Judgement calls**
- **T range of the I553A/L754A series:** Fig. 2 gives 15–45 °C for the d₂ substrate and 5–50 °C for protio. I entered 288.15–318.15 K, the range where both isotopes were measured; the protio range is in notes.
- **Perdeutero-LA (Table 2):** I set kie_type `primary`, because the transferred C11 H is heavy. Every non-transferred C–H is also heavy, so the values include secondary effects; `other` could be argued.
- **11,11-d₂:** both C11 hydrogens are heavy.
- **Kind of Dkcat 85:** the Discussion sets kchem = kcat, but never calls this value intrinsic, so it is `observed`.
- **Ionic strength:** the Methods place "ionic strength of 0.2 M" after the Tris-HCl buffer; it may apply to both buffers.
- **Duplicate:** the text repeats "(85)" without error; I entered the table value.

**Inconsistencies inside the paper**
- The text credits WT Dkcat (81) to ref 13; the Table 1 footnote credits the WT row to ref 19.
- Results 3.3 says "mutations at positions 756, 564, and 553"; the paper's mutations are at 754, 546 and 553.
- Typos: "Ile553Ala/ILeu754Ala" and "Leu546Ala/Leu754/Ala".
- Not an inconsistency: A_H/A_D 0.2 with ΔEa 3.5 gives about 67 at 303 K, close to Dkcat 85 given the "∼".

## S057 Offenbacher 2017 (S749 and Y317 mutants)

**Entered**
- **Table 1:** Dkcat at 303.15 K for WT, S749A, S749G, Y317S, Y317L and Y317F. Footnote e says the WT values are new (modified purification).
- **temperature.csv:** 6 series with Ea(H) and ΔEa. Footnote d defines ΔEa = Ea(D) – Ea(H). T range 283.15–318.15 K, from footnote b.

**Left out**
- **Cited:** Dkcat ∼80 and ΔEa 0.9 kcal/mol (ref 12); Ea(H) of L546A 4.1 kcal/mol (ref 26).
- **Not isotope effects:**
  - Ea(H) 2.1 and 0.03 kcal/mol for WT and I553G (earlier data, Table S3).
  - HDX activation energies (5.0, 0.7, 11.6, 4.0, 14 kcal/mol).
- **Non-enzymatic (ref 18):** intrinsic amide-exchange barrier, ca. 17 kcal/mol.
- **Cited:** Ea of other lipoxygenases, 8–12 kcal/mol (refs 53–55).
- **Figure only:** Fig. 5 Ea labels; the I553L data there are reproduced from ref 27.
- **SI only:** Tables S3, S5–S7.

**Judgement calls**
- **pH and labelled substrate:** the main text states neither (methods are in the SI). pH is empty and labelled_position reads "not stated in main text".
- **Method:** noncompetitive, inferred. A KIE on kcat needs separate kcat(H) and kcat(D) measurements.
- **n_temperatures:** footnote b says "7 to 8 (depending on mutant)", so I left it empty.
- **T range:** stated only for the Ea(H) fits.
- **Donor:** C11 is not named in the text (Scheme 1 is an image).

**Inconsistencies:** none. The values repeated in the text match Table 1.

## S058 Hu 2016 (pressure)

**Entered**
- No measurements.
- **temperature.csv:** 12 series from Table 2, entries 1–12 (WT, I553V, L546A at 1, 344, 688 and 1034 bar).
  - Ea(H) and ΔEa; footnote b defines ΔEa = Ea(D) − Ea(H).
  - 288.15–308.15 K; n = 5 (text: "five temperatures between 15°C and 35°C").

**Left out**
- **Table 1 S values:** ratios of rate constants at pressure to 1 bar; not isotope effects.
- **Figures and SI only:** Dkcat at each T and P is only in Fig. 2B and Fig. S3.
- **No isotope effect:** entries 13–16 (L754A) give only Ea(H), with ΔEa "N.D."; so L754A has no rows and no enzyme row.
- **No isotope ratio:** the ln(A_H) column (kept in notes).
- **Summaries:** "ΔEa ~1.0" and "~3.0" in the text.
- **Model value:** the 0.02 Å compression.

**Judgement calls**
- **Transfer:** S058 does not assign it ("C-H activation", "H-transfer"). PCET is best supported: its ref 7a and the other three SLO papers treat the reaction as PCET.
- **Unstated:** pH and the labelled position ("D-LA") are not given.
- **Method:** kcat, noncompetitive.
- **1034 bar:** the 1034-bar entries, set apart in the table by a separator row, are entered like the others.

**Inconsistencies inside the paper**
- Table 1, L754A: lower temperature printed "208" K; it should be 288 K.
- Text: "at 1.034 bar" should read 1,034 bar.
- Table 1 cell "0.98 (0.03" is missing a parenthesis.

## S059 Zaragoza 2023 (I552A, V750A)

**Entered**
- Dkcat for I552A 60 (2) and V750A 69 (4), plus the recollected WT from footnote †, 57 (2).
- **temperature.csv:** 3 series with Ea(H) and ΔEa (ΔEa = Ea(D) − Ea(H), defined in the text).

**Left out**
- **Cited WT row (Ref. 20):** kcat 297 (10), Dkcat 81 (5), Ea 2.1 (0.2), ΔEa 0.9 (0.2).
- **Cited introduction values:** Ea ~2.0 kcal/mol, A_H < 10⁵ s⁻¹, Dkcat 81, and 500–700 for the double mutant.
- **Not isotope effects:** Stokes-shift and HDX activation energies; correlation slopes 1.0 (0.1) and 0.7 (0.1).
- **SI only:** Tables S1, S2 and S4.

**Judgement calls (flag for the curator)**
- **Possible duplicate of ref 35:** footnote * says the temperature-dependent data of I552A and V750A "had been reported (35) but were not previously analyzed for Ea and ΔEa". I entered them because the table marks the row "This work".
- **Possible duplicate of S057:** the footnote † WT is described as "recollected" in this study, but all four numbers are identical to S057's Table 1 WT (S059 ref 5).
- **Temperature:** footnote † says 303 K and the text says 30 °C; I entered 303.15 K.
- **Unstated:** pH for the kinetics (the pH 9.0 in Fig. 3 is for fluorescence), T range, and labelled position.

**Inconsistency (paper vs RCSB):** the paper calls 5T5V the 300 K WT structure; its RCSB title says 293 K.

## S060 Whittington 2024 (MoLOX glycan variants)

**Entered**
- Dkcat for WT 70±2 and GLN 57±5, at 293.15 K and pH 9.0 (footnote a; ± is s.e.m.).
- **temperature.csv:** 2 series, WT and GLN.
  - 283.15–303.15 K, n = 7, pH 9, all from Methods.
  - ΔEa −1±0.6 (WT) and −1.1±0.8 (GLN).

**Left out**
- **Cited rows:** PNG (ref 26): Dkcat 73±3, Ea 9.7±0.6, ΔEa 0.6±0.6. ENDO (ref 25): Dkcat 70±6, Ea 8.5±1.0, ΔEa −0.9±1.5.
- **Cited text values:** Dkcat ≈ 70 temperature-invariant (ref 26); Ea 9–10 kcal/mol (ref 26); F332A Ea ~10 → 7 kcal/mol (ref 25).
- **Not isotope effects:** kcat/KM values; N72Q and N215Q have no KIEs.

**Judgement calls**
- **ΔEa sign:** footnote c defines ΔEa = Ea(D) – Ea(H), but the Discussion writes "ΔEa = Ea(H) – Ea(D)". I entered the values as printed under footnote c.
- **Possible duplicate of ref 26:** the WT row has no footnote, but the text credits WT Dkcat ≈ 70 and Ea 9–10 to ref 26. I entered it and flagged it.
- **GLN:** entered as the eight mutations N18Q/N28Q/N48Q/N72Q/N150Q/N215Q/N501Q/N535Q.
- **Rounded duplicate:** the text gives "12 ± 0.7"; I entered the table's 12.1±0.7.
- **Error type for Ea and ΔEa:** not stated (footnote a does not cover those columns).

**Minor:** the kcat header carries footnote "a" twice, the ΔEa header has a stray ",c", and "NeNGlyc" should be NetNGlyc.

## Enzymes, UniProt and PDB

**UniProt and numbering**
- **SLO-1 = P08170** (Glycine max, EC 1.13.11.12, from UniProt; no paper gives an EC). The papers' numbering matches P08170 at L546, I553, L754, I552, V750, S749 and Y317.
- **MoLOX = G4NAP4** (stated in S060).
  - UniProt names the organism Pyricularia oryzae, strain 70-15; the paper names no strain.
  - EC from UniProt: 1.13.11.-; 1.13.11.45; 1.13.11.58.
  - S060's numbering is UniProt − 14 at all eight Asn sites and at L331/F332; it is the author numbering of 5FNO.

**RCSB searches**
- Each enzyme was searched two ways: by exact UniProt accession, and by sequence (identity ≥ 0.95).
- P08170 gave 26 entities either way.
- G4NAP4 gave only 5FNO. The full-length G4NAP4 sequence query timed out at RCSB, so I searched with the mature chain (residues 17–619).

**Entries per variant**

| Variant | PDB | Cites which DOI |
|---|---|---|
| L546A/L754A | 4WHA; 5TQO | 4WHA: S056 ref 18; 5TQO: Hu 2019 JACS |
| I553V | 3BND | Meyer 2008 PNAS |
| L546A | 5TQN | Hu 2019 JACS |
| I552A | 7SOI | S059 |
| V750A | 7SOJ | S059 |
| MoLOX WT | 5FNO | S060 ref 22 |

- **Not engineered:** RCSB shows S160E against P08170 in most SLO-1 entries, including all the variant entries above.
- **5FNO:** the Endo H-treated enzyme. Its N-terminal "EF" (V15E/A16F) is a cloning remnant inside the signal peptide.
- **SLO-1 WT:** pdb is left empty because there are 8 WT entries. The notes list them and the ones each paper names: 3PZW (S057, S059), 1F8N (S058), 5T5V (S059).
- **Entries citing one of these five DOIs:** 5T5V and 5TQP (S057), 7SOI and 7SOJ (S059). None cites S056, S058 or S060.
- **No PDB entry:** L546A/I553A, I553A/L754A, all five S749/Y317 mutants, and GLN MoLOX.
