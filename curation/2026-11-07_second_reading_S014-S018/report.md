# Second reading (ai-2) of S014–S018: MEG-NEN KIE extraction

I entered 8 rows in measurements.csv, 11 in temperature.csv and 10 in enzymes.csv. Every number comes from a table in the saved HTML. Before finishing I re-opened all three files and checked each number with a separate parser against its table cell, footnote or sentence (0 mismatches), then read every text field by hand.

I worked only inside `reading2_s014-s018/`. The only web access was rest.uniprot.org, search.rcsb.org and data.rcsb.org. The equations in all five saved pages are empty MathJax placeholders. In the running text they stand only for symbols, so no number was lost.


---

## S014 – Wang et al. 2006, Phil Trans B (ecDHFR M42W)

**Entered (temperature.csv, 3 rows), from Table 1, column M42W:**

| isotopes | AH_AX (A_l/A_h) | error |
|---|---|---|
| H/T | 2.9 | 1.6 |
| H/D | 2.1 | 0.6 |
| D/T | 1.35 | 0.16 |

All three rows have kind = intrinsic, quantity = kcat/KM, method = competitive, T 278.15–318.15 K, pH 8.0.

**Left out:**
- **WT column** (7.0±1.5, 3.5±0.5, 1.70±0.14): the text says these come from Sikorski et al. 2004.
- **G121V column** (6.7±0.8, 3.8±0.4, 1.76±0.07): the text says these come from Wang et al. 2006.
- **Semi-classical limits** (1.6, 1.4, 1.2): literature values (footnote a).
- **"rates" row** (228, 1.4, 5.6 s⁻¹): not KIEs, and cited from Rajagopalan et al. 2002 (footnote b).
- **KIEs at each temperature, observed and intrinsic:** only in SI Tables 1–2 and Figs. 2–3.
- **C_f:** Fig. 4 only.
- **ΔEa for M42W:** not printed. The text says the isotope effects on the slopes are not summarized.

**Judgement calls:**
- **kind = intrinsic:** the text says the Table 1 values come from fitting the intrinsic KIEs to eq. 2.4.
- **quantity = kcat/KM, method = competitive:** the intrinsic values were derived by the Northrop method from competitive H/T and D/T V/K KIEs ("observed KIEs (in … k_cat/K_M)").
- **Temperature range and pH:** 5–45 °C and pH 8.0 are from Methods (iv), the competitive KIE experiments. n_temperatures is not stated.
- **H/D row:** no H/D-labelled cofactor was used; this row is computed from the H/T and D/T data.
- **Acceptor:** "DHF C6" is my reading. The text only says the hydride reduces the C=N bond; Scheme 1 is an image.
- **Error type:** not stated for Table 1.

**Inconsistencies:**
- The text says Fig. 2 shows "KIEs with G121V-ecDHFR", but its caption says M42W.
- The text has "M42V" where M42W is meant.
- Endnote 1 says "equation (2.1)" where the numerically solved equation is (2.3).
- The Fig. 1 caption has "PDB 1r×2" for 1RX2.

## S015 – Stojković et al. 2012, JACS (ecDHFR I14 series)

**Entered (temperature.csv, 2 rows), from Table 1, footnote f "This work":**

| variant | A_H/A_T | ΔE_aT-H (kcal/mol) |
|---|---|---|
| I14V | 4.2 ±0.4 | 0.27 ±0.05 |
| I14G | 0.024 ±0.003 | 3.31 ±0.07 |

Both rows: H/T, intrinsic, kcat/KM, competitive.

**Left out:**
- **WT** (7.0 ±1.5; −0.1 ±0.2): footnote e cites Ref. 47.
- **I14A** (4.7 ±0.5; 0.39 ±0.06): footnote g cites Ref. 46.
- **k_H rates:** not isotope effects.
- **H/D and D/T parameters:** footnote c says "data not shown"; they are in the SI.
- **KIEs at each temperature:** Fig. 3 only.
- **Table 2:** MD simulation data, not KIEs.

**Judgement calls:**
- **Sign convention:** the text defines ΔE_ah-l = E_ah − E_al (heavy − light), so no sign change was needed.
- **quantity = kcat/KM:** rests on "KIEs were measured competitively"; the intrinsic values were obtained by the Northrop method (ref 49).
- **T range and pH left empty:** the main text gives neither for the KIE runs. The 25 °C and pH 7 it mentions belong to the stopped-flow rates.
- **Error type:** the Methods sentence "Each value is reported with standard deviation" may or may not cover the fitted parameters.

**Inconsistencies:**
- Footnote e attributes the WT parameters to Ref. 47 (a ¹⁴C-cofactor synthesis paper), while the Fig. 3 caption attributes the WT data to ref 38.
- The footnote marker "c" is typeset inside the subscript of "ΔE_aT-Hc" and is not linked.
- The text says the single-turnover rates were measured for wtDHFR, but Table 1 cites WT k_H to Ref. 58.

## S016 – Sharma & Klinman 2008, JACS (SLO-1 L546A/I553A)

**Entered:**
- **measurements.csv:** KIE 128 (3), H/D, kcat, noncompetitive, 303.15 K, pH 9.0.
- **temperature.csv:** A_H/A_D 1.05 (0.45), ΔEa 2.8 (0.4), Ea(H) 3.8 (0.4), 288.15–323.15 K, pH 9.0.
- Both come from Table 1, row 546A/553A (footnote g "This work").

**Left out:**
- **WT and 546A rows:** cited as Ref (10a).
- **553A row:** cited as Ref (4a).
- **Text values:** A_H/A_D = 0.027 for I553G (ref 12) and k_H/k_D = 81 for WT (ref 10).
- **k_cat, k_cat/K_M and A_H:** not isotope effects (A_H is mentioned in the row notes).
- **Data at each temperature:** Fig. 1 only.

**Judgement calls:**
- **30 °C for the KIE:** taken from footnote b ("rate constants are reported for 30 °C"), which is attached to the k_cat column. The KIE column carries only footnote c, which defines KIE = k_cat(H)/k_cat(D).
- **pH and temperature range:** pH 9.0 is from the table title; 15–50 °C is from footnote a.
- **Sign convention:** footnote d reads "ΔE_a = E_a(D) − ΔE_a(H)", a typo for E_a(D) − E_a(H). It is heavy − light, so no sign change.
- **transfer = PCET:** the text calls the step a proton-coupled electron transfer, with the proton going to the Fe³⁺–OH oxygen.
- **Donor and label:** "C11" is my assumption; the main text names only "dideutero linoleic acid".
- **Variant notation:** the paper writes Leu546Ala/Ile553Ala; I entered L546A/I553A.
- **Error type:** not stated.

**Inconsistencies:**
- **Footnote d** has the typo noted above.
- **Substrate name:** written as "9,12-(Z,Z)-octadecanoic acid" (should be octadecadienoic).
- **Single-mutant attribution:** the text attributes the single-mutant L546A data to ref 4, but Table 1 cites Ref (10a).
- **Fold decrease:** the text says k_cat drops "one hundred fifty-fold"; Table 1 gives about 127–134-fold.
- **Internal check:** the printed Arrhenius parameters predict about 110 at 30 °C against the printed 128 (3). That is within the error on A_H/A_D, so I do not count it as an inconsistency.

## S017 – Hu et al. 2014, JACS (SLO L546A/L754A, "DM SLO")

**Entered (measurements.csv, 2 rows):**

| value | quantity | T | pH | source in paper |
|---|---|---|---|---|
| 537 (55) | single_turnover | 308.15 K | empty | Table 1, footnote d; text |
| 729 ± 26 | kcat | 303.15 K | 9 | Table 1, footnote d; text |

Both are H/D, noncompetitive, labelled 11,11-²H₂-LA.

**Left out:**
- **WT row:** cited as Ref (13); the text value k_H/k_D = 80 is also from ref 13.
- **DM Ea(H) 9.9 (0.2) and A_H 3.3 × 10⁵:** these are not isotope effects on the Arrhenius parameters, so there is no temperature.csv row. The paper's own ref note 25 says the temperature dependence of the KIE is not yet available.
- **Rate constants** (0.021 s⁻¹; 0.0250 ± 0.0004 s⁻¹; (7.68 ± 0.67) × 10⁻⁵ s⁻¹): not isotope effects themselves.
- **Abstract range "540–730":** a summary of the two entered values.
- **Modelling parameters** (λ, W, Ω, R_eq): computed, not measured KIEs.

**Judgement calls:**
- **537 as single_turnover:** the table labels it ^Dk_cat, but footnote d and the text describe pre-steady-state, single-turnover reduction of Fe(III)–OH.
- **pH:** pH 9 for the 729 row is from the Fig. 2A legend. The pH of the single-turnover runs is not stated, so that field is empty.
- **transfer = PCET:** the paper does not name the transfer type. PCET is the best-supported choice because LA reduces Fe(III)–OH to Fe(II)–OH₂.
- **Error type:** not stated.

**Inconsistencies:**
- A single-turnover value at 35 °C sits in the "^Dk_cat" column next to 30 °C parameters; only footnote d flags this.
- The protio single-turnover rate at 35 °C, from which 537 is computed, is not printed.

## S018 – Nagel et al. 2012, Biochemistry (ht-ADH)

**Entered:**
- **measurements.csv (5 rows):** Table 1 ^Dk_cat at 303.15 K and pH 7.0.
- **temperature.csv (5 rows):** Table 2, E_a(D) − E_a(H) above the break.

| variant | ^Dk_cat | E_a(D) − E_a(H) (kcal/mol) |
|---|---|---|
| L176V | 4.1 (±0.4) | 1.3 (±1.1) |
| L176A | 4.1 (±0.6) | 1.4 (±0.9) |
| L176G | 4.0 (±1.1) | 1.2 (±1.0) |
| L176Δ | 4.4 (±1.4) | 1.7 (±0.4) |
| V260A | 4.1 (±0.4) | 1.9 (±1.0) |

All rows: H/D, kcat, noncompetitive. For V260A, footnote a puts the break at 40 °C.

**Left out:**
- **WT ^Dk_cat 3.1 (±0.2) and WT 0.2 (±0.2):** the WT 0.2 is in fact E_a(T) − E_a(H) per footnote b. This is a judgement call: the text says the WT H/D KIEs were calculated from the competitive H/T KIEs of ref 21, and the SI note says those KIEs are reproduced from ref 21. So they are not this paper's own measurements.
- **Log(A_obs) column:** footnote c, ref 40, protio substrate only.
- **Text values:** WT A_H/A_D = 2.6 (ref 21) and the HLADH EXP 3.3 (ref 20).
- **A_H/A_D of the mutants:** only described as "less than unity", no numbers.
- **KIEs at each temperature:** Fig. 3 and the SI only.
- **k_cat, K_m, pK_a:** not isotope effects.

**Judgement calls:**
- **pH 7.0 for the Table 2 rows:** neither Table 2 nor Fig. 3 states a pH. I took 7.0 from the Results sentence "extensive characterizations at pH 7.0".
- **T_min/T_max left empty:** only the lower bound ("above the 30 °C break") is stated.
- **Sign convention:** E_a(D) − E_a(H) is heavy − light, so no sign change.
- **Error type:** the Results call the errors "propagated errors".
- **kie_type = primary:** α,α-d₂ labels both α-H, but the paper calls these primary KIEs.
- **Acceptor:** "NAD⁺ nicotinamide C4" is my reading; the text names only the nicotinamide ring.

**Inconsistencies:**
- The text gives the WT E_a(D) − E_a(H) as "0.1 kcal/mol", while Table 2 gives 0.2 (±0.2) and footnote b says that value is E_a(T) − E_a(H).
- The text says the k_cat decrease is "between 5- and 50-fold"; Table 1 gives 3.2-fold (L176G) to 58-fold (L176Δ).
- The Discussion cites "(Table 1)" where Table 2 is meant.
- The SI tables are referred to as "Tables S2–S5" in one place and "Tables S1 and S2" in another.

## Enzymes (enzymes.csv)

In every paper the residue numbering at the mutated positions matches UniProt (Met1 = 1). None of the papers gives an EC number, so all EC numbers are from UniProt.

| enzyme | UniProt | EC | variants entered | PDB |
|---|---|---|---|---|
| E. coli DHFR | P0ABQ4 | 1.5.1.3 | M42W | none |
| E. coli DHFR | P0ABQ4 | 1.5.1.3 | I14V | 4QLG |
| E. coli DHFR | P0ABQ4 | 1.5.1.3 | I14G | 4QLF |
| SLO-1 (Glycine max) | P08170 | 1.13.11.12 | L546A/I553A | none |
| SLO-1 (Glycine max) | P08170 | 1.13.11.12 | L546A/L754A | 4WHA; 5TQO |
| ht-ADH (Geobacillus stearothermophilus) | P42328 | 1.1.1.1 | L176V, L176A, L176G, L176Δ, V260A | none |

- **DHFR:**
  - Searching RCSB by accession finds only 165 entities. A ≥90 % sequence-identity search finds 182, including 4QLF and 4QLG, which RCSB maps to the accession U6N356.
  - 4QLF and 4QLG differ from P0ABQ4 only at residue 14. They cite 10.1021/jp5059963, not S015.
  - No entity has W42.
- **SLO-1 L546A/L754A:**
  - 4WHA cites S017's DOI (10.1021/ja502726s). 5TQO cites 10.1021/jacs.8b10992.
  - Both also differ from P08170 by S160E. The study did not engineer it; it is also present in WT entries (3PZW, 5T5V).
  - No L546A/I553A entry exists.
- **ht-ADH:**
  - The paper says B. stearothermophilus; the current name is Geobacillus stearothermophilus. P42328 is strain NCIMB 12403 / LLD-R, the strain of the 1RJW structure the paper uses.
  - RCSB has only 1RJW (WT) and 3PII (L176F). The paper itself says no mutant X-ray structures are available.

No entry cites S014, S015, S016 or S018.
