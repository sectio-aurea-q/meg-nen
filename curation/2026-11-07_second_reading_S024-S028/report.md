# Second reading S024–S028 (ai-2): report

I did the second reading (ai-2) of all five papers and wrote the three CSV files. Every value and error was checked by script against its exact table cell or sentence in the HTML. All temperatures were converted from °C; all energies were already printed in kcal/mol. I opened nothing outside `reading2_s024-s028/` and used the web only for UniProt and RCSB lookups.

---

## S024 Valley & Fitzpatrick 2004 (nitroalkane oxidase, NAO)

**Entered**
- measurements: NAO WT, kH/kD on kcat/Km = 9.2 ± 0.4 at 300.15 K (Table 1).
- temperature: ΔEa 1.35 ± 0.17 kcal/mol and AH/AD 0.89 ± 0.25 (Table 1).
- Neither row has a temperature range, number of temperatures or pH, because the paper states none.

**Left out**
- Non-enzymatic values:
  - acetate: kH/kD 7.8 ± 0.1 (25 °C), ΔEa 1.38 ± 0.26, AH/AD 0.81 ± 0.35;
  - phosphate: kH/kD 8.8 ± 0.1 (25 °C), ΔEa 1.20 ± 0.32, AH/AD 1.22 ± 0.66.
- Cited values: semiclassical limits ΔEa = 1.4 and 0.7 < AH/AD < 1.7 (ref 28); phenylnitromethane AH/AD < 0.7 (ref 30, non-enzymatic).
- Not isotope effects: kH, ΔG‡, ΔH‡, −TΔS‡, the rate-enhancement factors, ΔΔG‡ 12.3 and 9.9.
- Figure only: the per-temperature KIEs (Fig. 2C).

**Judgement calls**
- **Temperature:** the kH/kD row label carries footnote a (25 °C), but the NAO cell carries footnote b (27 °C). I used 27 °C (300.15 K).
- **Quantity, method, kind:**
  - kcat/KM, from the text.
  - Noncompetitive: the ref 25 note says protiated and deuterated nitroethane were assayed separately below Km/10.
  - Observed: the paper never calls the value intrinsic.
- **Transfer and label:** proton, from "abstraction of a proton … by Asp402". Both C1 hydrogens are deuterated, so the primary value includes an α-secondary contribution.
- **Primary, not cited:** the NAO data count as this paper's own measurements. Refs 24 and 25 in the Fig. 1 legend cite enzyme preparation and assay methods. Note 31 describes this paper's three enzyme preparations; the table values are averages with propagated errors.
- **Sign of ΔEa:** the fitting equation, ln(KIE) = ln(AH/AD) − ΔEa/RT, taken literally makes ΔEa = Ea(H) − Ea(D). Only Ea(D) − Ea(H) is consistent with the numbers: 0.89·exp(1.35/RT) = 8.6 versus 9.2 measured, while the opposite sign gives 0.09. I kept the sign as printed and read it as Ea(heavy) − Ea(light).
- **Ea_light:** left empty. The printed ΔH‡ of 3.3 ± 0.4 comes from an Eyring fit and is not an Ea.

**Inconsistencies**
- The fitting equation's sign contradicts the reported positive ΔEa (see above).
- The text gives the NAO rate enhancements "at 25 °C" (1.2 × 10⁹ and 2.5 × 10⁷). These use 4800 M⁻¹ s⁻¹, which footnote b places at 27 °C.
- Citation "31" appears twice in the text. The second occurrence is probably meant to be ref 32, which is otherwise never cited.

## S025 Pavon & Fitzpatrick 2005 (PheH, Δ117PheH, TyrH, TrpH102–416)

**Entered**
- measurements, 16 rows, all at 303.15 K and pH 7.0:
  - Dk1 with 4-C²H₃-phe: 12.4 ± 1.1, 12.1 ± 1.1, 13.8 ± 1.2, 13.0 ± 1.7 (PheH, Δ117PheH, TyrH, TrpH).
  - 4-CH₂²H-phe, Dk and αDk, for Δ117PheH, TyrH and TrpH: 9.5 ± 0.4 and 1.12 ± 0.05; 9.5 ± 0.6 and 1.20 ± 0.08; 10.9 ± 0.4 and 1.09 ± 0.03.
  - 4-CH²H₂-phe, Dk and αDk, same order: 7.1 ± 0.2 and 1.31 ± 0.03; 7.6 ± 0.3 and 1.35 ± 0.05; 7.5 ± 0.1 and 1.31 ± 0.02.
- temperature, 4 rows (Table 2), AH/AD and ΔEact:
  - PheH: 0.18 ± 0.08 and 2.4 ± 0.3
  - Δ117PheH: 0.13 ± 0.06 and 2.6 ± 0.3
  - TyrH: 0.11 ± 0.05 and 2.9 ± 0.3
  - TrpH: 0.10 ± 0.05 and 2.9 ± 0.3

**Left out**
- Values marked ND for full-length PheH.
- Rounded text summaries: "about 10 / about 1.1", "less than 8 / 1.3 or greater", and the theoretical "upper limit of about 7".
- Cited semiclassical ranges (refs 16, 18–20).
- Figure or SI only: product distributions (Fig. 1) and the per-temperature KIEs (Fig. 2; the other enzymes' plots are in the SI).

**Judgement calls**
- **Temperature and pH:**
  - Table 1 footnote a points to the Fig. 1 legend, which gives 30 °C and pH 7.0.
  - Table 2 footnote a points to Figures 1 and 2, which gives pH 7.0.
  - The paper states no temperature range for the Arrhenius fits.
- **Quantity:** "other" for all rows. These are isotope effects on k1, the H-abstraction step, obtained from product partitioning.
- **Method:**
  - Dk1: noncompetitive, because the protio and CD₃ substrates were run in separate reactions.
  - Partially deuterated substrates: competitive, because the result comes from H versus D loss within one molecule (footnote c).
- **Kind:** intrinsic for every row, as the Table 1 title says. The text adds that the CHD₂ values are distorted by coupled motion; I put that in the notes.
- **kie_type:** Dk1 is entered as primary, although the text says it equals Dk(αDk)².
- **Sign of ΔEact:** the paper does not define the direction. I read it as Ea(D) − Ea(H). Check: TyrH 0.11·exp(2.9/RT) = 13.6 versus 13.8 measured.
- **Label of the temperature series:** CD₃ is stated only for Δ117PheH (Fig. 2 legend). For the other three enzymes I assumed it from "similar analyses".
- **PMC artefact:** the mass number "2" in ²H is hyperlinked to ref 2. These are not citations.
- **TyrH values:** entered as this paper's own. Ref 6 measured TyrH intrinsic KIEs earlier, but Table 1 carries no citation marker.
- **Organisms (the paper names none):**
  - Rat PheH and rat TyrH, inferred indirectly: the same lab's PDB entries are rat, and P04177 cites the lab's papers.
  - Rabbit TrpH (P17290) is unverified: none of the permitted sources links to ref 4.

**Inconsistencies**
- For PheH and Δ117PheH, the Table 2 parameters predict Dk1 = 9.7 at 30 °C, against 12.4 and 12.1 measured. This is within the large AH/AD errors.
- A "Note Added after ASAP Publication" records corrections to paragraphs 4–5 and to Fig. 1. I cannot tell whether the PMC copy is the corrected version.

## S026 Bandaria et al. 2009 (FDH, Candida boidinii)

**Entered**
- temperature, 3 rows (Results text), intrinsic kcat/KM, competitive, 278.15–318.15 K, pH 7.5:
  - H/T: ΔEa −0.02 ± 0.08, AH/AT 6.1 ± 0.8
  - H/D: ΔEa −0.02 ± 0.06, AH/AD 3.5 ± 0.3
  - D/T: ΔEa −0.007 ± 0.03, AD/AT 1.7 ± 0.1
- No measurement rows: the per-temperature KIEs are only in SI Tables S2/S3 and Fig. 4.

**Left out**
- Cited semiclassical limits 1.73, 1.41 and 1.22 (ref 30).
- Not isotope effects: the FFCF parameters (data from ref 23), azide Kd 57 nM, and the gating frequencies (cited).

**Judgement calls**
- **Sign of ΔEa:** not defined in the paper; I read it as Ea(heavy) − Ea(light). The value is zero within error.
- **Temperature range:** 5–45 °C, from the Results.
- **pH:** 7.5, from the Experimental section.
- **H/D:** not measured directly; it was computed from H/T and D/T through the Northrop equations.
- **Number of temperatures:** not stated.

**Inconsistencies**
- The species is spelled "bodinii" and "biodinii".
- A leftover sentence from the manuscript reads "(I am sending you SI as a separate word document)".
- The named residues (Arg-284, His-332, Ile-122, Asn-146) use Pseudomonas sp. 101 numbering from PDB 2NAD. I checked them against 2NAD's own numbering.

## S027 Carr & Klinman 2014 (NspLOX WT and I219A)

**Entered**
- measurements: KIE on kcat at 293.15 K, WT 118 ± 3 and I219A 155 ± 7 (Table 1; repeated identically in the text, entered once).
- temperature: WT 280.65–300.65 K, ΔEa −0.7 ± 0.3, Ea(H) 12.4 ± 0.3; I219A 278.15–298.15 K, ΔEa 1.1 ± 0.5, Ea(H) 2.7 ± 0.5. Ranges from footnote a.

**Left out**
- Extrapolated 30 °C values (footnote b): KIE 128 ± 3 and 164 ± 26; kcat 37.1 and 16.7.
- All WT and L546A SLO-1 rows, which come from ref 16 (footnote c).
- The KIE range 30–100 (refs 3, 4).
- Absolute AH values and Ea(D) 11.6: no schema field, so they are in the notes.

**Judgement calls**
- **20 °C values:** entered as measurements. The paper does not say whether 20 °C was a measured point for WT (range 7.5–27.5 °C); only the 30 °C values are marked as extrapolated.
- **Sign of ΔEa:** from the text, Ea(D) is lower than Ea(H), so ΔEa = Ea(D) − Ea(H).
- **Quantity and method:** kcat (saturating substrate); noncompetitive.
- **Substrate label:** uniformly deuterated LA, so secondary effects are included.
- **Transfer:** H_atom, because the paper says "net H-atom abstraction". It also says models treat the step as PCET.
- **Donor and acceptor:** C11 and Fe(III)–OH are inferred; the paper only says "between two double bonds" and "metal hydroxide".

**Inconsistencies**
- From the text values, 11.6 − 12.4 = −0.8, while the table gives −0.7 (rounding).
- For I219A, a positive ΔEa implies the KIE falls with temperature, yet the extrapolated 30 °C KIE (164) is above the 20 °C value (155).
- Footnote b mentions an "Eyring fit", but the table reports Arrhenius parameters.
- Ref 8 is listed as "(2007) J. Biol. Chem. 283"; the year and volume do not match.

## S028 Hu et al. 2017 (SLO-1 double mutant L546A/L754A)

**Entered**
- measurements, Dk_cat (6 rows, Table 1), noncompetitive, observed, no pH:
  - 5 °C, 278.15 K: 630 (68)
  - 10 °C, 283.15 K: 708 (60)
  - 15 °C, 288.15 K: 760 (67)
  - 20 °C, 293.15 K: 553 (43)
  - 25 °C, 298.15 K: 624 (46)
  - 30 °C, 303.15 K: 692 (43)
- The 30 °C values are repeated identically in the text; entered once.
- temperature: ΔEa 0.3 ± 0.7 kcal/mol over 278.15–303.15 K, 6 temperatures. Note 29 defines ΔEa = EaD − EaH, so no sign change was needed.

**Left out**
- The abstract's average of 661 ± 27. This is the mean of the six values; the ± equals the population SD divided by √6.
- The text range "550–760".
- Cited values: WT ca. 80 and 0.9 ± 0.2 (ref 19); DM-SLO 537 ± 55 (35 °C, single turnover) and 729 ± 26 (30 °C) (ref 45).
- Not isotope effects: the pressure ratios S (Table 2), "EaH ca. 8" (from the pressure study), and the model fit parameters R₀ and Ω.
- Figure only: Fig. 4A.

**Inconsistencies**
- The text names the other double mutant "L546A/L553A"; the Fig. 4 legend names it "L546A/I553A".
- The Fig. 4 legend cites ref 1 (an alcohol dehydrogenase paper) for the WT SLO data.
- Recomputing Dk_cat from the printed kcat values gives 631 and 758 instead of 630 and 760. This is just rounding.

## Enzyme metadata (enzymes.csv)

- **PDB rule I applied:** an entry is listed only if it has the same mutation state and the same construct as the studied enzyme. Near misses are named in the notes. No PDB entry cites any of the five DOIs.

| Source | Enzyme | UniProt | Organism | PDB |
|---|---|---|---|---|
| S024 | NAO WT | Q8X1D8 | Fusarium oxysporum | 2C0U;2C12;3D9G |
| S025 | PheH WT | P04176 | Rattus norvegicus | 5FGJ;5DEN |
| S025 | Δ117PheH | P04176 | Rattus norvegicus | none |
| S025 | TyrH WT | P04177 | Rattus norvegicus | none (only domain structures 1TOH, 2TOH, 2MDA) |
| S025 | TrpH102–416 | P17290 | Oryctolagus cuniculus (unverified) | none |
| S026 | FDH WT | O13437 | Candida boidinii | 5DN9;5DNA;8HTY;8IQ7 |
| S027 | NspLOX WT | Q8YK97 | Nostoc sp. | none |
| S027 | NspLOX I219A | Q8YK97 | Nostoc sp. | none |
| S028 | SLO-1 L546A/L754A | P08170 | Glycine max | 4WHA;5TQO |

- **NAO:** the organism was found through refs 11 and 24, both cited by Q8X1D8. Asp402 matches the sequence.
- **PheH WT:** 5DEN differs from the UniProt sequence at T87S, which the study did not engineer.
- **FDH:** the four listed structures differ from O13437 at 11 positions (strain variants) and match A0A0A1EQY0 exactly. They come from the same labs (Guo et al. 2016), so the paper's enzyme is probably the A0A0A1EQY0 sequence. I kept the reviewed entry O13437 in the field. The paper's Pseudomonas residues correspond to R258, H311, V93 and N119 in C. boidinii FDH.
- **NspLOX:** Q8YK97 is the only LOX-family protein of Nostoc sp. PCC 7120 in UniProt. It carries catalase/AOS signatures and is 773 residues long, matching the paper's "residues 344–773" of a fusion protein. I219 in the construct's numbering is I562 in Q8YK97 (offset 343). The conserved Ile seven residues further on is I569, as the paper says.
- **SLO-1 L546A/L754A:** both listed structures also show S160E. That difference is common to most SLO-1 entries and was not engineered.
- **Unverified items for the curator:**
  - TrpH species: no permitted source links to ref 4, so rabbit rests on my prior knowledge of that reference.
  - Rat for PheH and TyrH: inferred from the same lab's PDB entries and UniProt citations; the paper names no species.
  - FDH accession: O13437 versus A0A0A1EQY0, as described above.
