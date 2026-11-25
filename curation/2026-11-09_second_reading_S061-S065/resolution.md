# Second reading of S061–S065 (9 November 2026)

First reading `ai-1`, second reading `ai-2`. These five papers are block 5, the last block of the second reading
list: the hydride transfer from NADH to the FAD of human NQO1 in the two non-equivalent sites of the dimer (S061),
the aromatic, tautomerization and benzylic isotope effects of the phenylalanine hydroxylase of *Chromobacterium
violaceum* and of its I234D variant (S062), the protonation of geranylgeranyl diphosphate by the class II terpene
cyclase PtmT2, measured in mixed H₂O/D₂O buffers by mass spectrometry (S063), the proton abstraction of the
computationally designed Kemp eliminase KE07 in six rounds of a directed-evolution trajectory (S064), and the
transient oxidation of CDP-glucose by the thermophilic C2 epimerase of *Thermodesulfatator atlanticus* from 20 to
80 °C (S065). Both readers worked from the PMC pages of the papers, saved on 9 November 2026; the published PDFs and
the supporting information were not read. Both readers also had the PMC XML of the same five manuscripts, which for
these papers holds the equations the HTML loses — S061 Eq. (2), S062 eqs 3, 4, 5 and 7, S063 eqs (4) and (7) — and
both used it for the definitions of the printed quantities, never for a value. The second reader worked from these
files alone, did not see the first reading, and looked up UniProt and RCSB PDB again for every enzyme. Its
instructions repeated the rules of CURATION.md and SCHEMA.md and allowed the web only for these lookups. Files in
this folder:

- `reading2_measurements.csv`, `reading2_temperature.csv`, `reading2_enzymes.csv`, `report.md`: the second reading as
  delivered (`report.md` saved by the curator from the second reader's answer; the list of its output files was
  shortened)
- `comparison.md`: row-by-row comparison of both readings, before the decisions below

## Result

All 33 isotope effects and all 15 temperature series of the first reading have a partner in the second reading, and
all of them agree in value, error, temperature, temperature range, number of temperatures, pH, quantity, method and
isotope type. The second reading found two values and two temperature series the first reading had missed, and one
metadata error; the first reading was right on two classification questions. Both readers left out the same values:
everything the papers take from other work (the rat PheH benzylic KIE of 12 ± 1 and the tautomerization KIE of 5.1 of
S062, the eukaryotic 0.90 ± 0.03 that S062 quotes with the same value as its own I234D result, the DHFR and
methylamine dehydrogenase activation energies of S065), the non-enzymatic row B of S064 Table 1 and the solution
value of 4.9 the text gives for it, the computed KIEs of S064 (5.8) and the model-fitted parameters of S065, the
Eyring rows of S061 Table 3 (which print no isotope difference), the product isotope ratios of S062 Table 3 (a KIE
multiplied by a branching ratio, by its own eqs 4 and 5), the rate constants, Michaelis constants and viscosity
controls of all five papers, and everything that stands only in a figure or in the supporting information.
Decisions:

1. **S062 Table 2, the four D(kcat) values (reading 2 adopted, `kie_type` changed):** the first reading entered
   1.24 ± 0.04, 1.43 ± 0.07, 1.00 ± 0.01 and 0.90 ± 0.03 as `primary`, the second as `other`. The second reading is
   right. The substrate is [ring-²H₅]-phenylalanine, and the paper states plainly: "Neither value is the intrinsic
   isotope effect for the reaction of the Fe(IV)O intermediate with the aromatic ring of the substrate. Rather, the
   observed isotope effects are combinations of the isotope effect on this step and the isotope effect on the
   subsequent tautomerization to form phenylalanine." In the first of those two steps no bond to a labelled hydrogen
   is broken, so that contribution is secondary — which is what the inverse 0.90 ± 0.03 of the three eukaryotic
   enzymes shows — while in the tautomerization a ring hydrogen is lost, a primary effect. A number that mixes a
   secondary and a primary effect over two steps is neither, so `other` is entered for M0252–M0255 and the notes say
   what it combines. The perdeutero precedent of S033, S038 and S056, entered as `primary`, does not apply: there the
   label sits on the one position whose C–H is cleaved in the single step measured, and the paper reports a primary
   KIE. The step rows keep `transfer = hydride` for the 1,2-hydride shift, which is a defined hydrogen transfer of
   this enzyme; the uncertainty is about which steps the measurement reports on, and that belongs in the measurement
   rows, not in the step.
2. **S063, the KIE of seven and the four A_H/A_D values (reading 1 kept, `kind` stays `observed`):** the second
   reading entered all six rows as `intrinsic`. The paper's only use of the word is the hypothesis sentence of its
   introduction — "We reasoned that kinetic analyses in mixed H₂O/D₂O buffers coupled with mass spectrometry would
   allow for determination of intrinsic kinetic isotope effects (KIEs)" — which is a claim about the method, not
   about a measured number; no individual value is called intrinsic anywhere, the text calls the seven "a large KIE",
   and no commitment analysis is reported. CURATION.md rule 5 asks for the source to say so of the value, so
   `observed` stands for M0258, M0282 and T0140–T0143. The notes of those rows now carry both readings.
3. **S063, the KIE of four in mixed buffers (reading 2 adopted, row added as M0282):** the first reading missed it.
   The text prints "The KIE at 28 °C converged to 4 under these experimental conditions (Table S1)" — a value with a
   temperature and a pD, printed in the main text, so the rule against supporting-information values does not reach
   it; only the per-concentration series behind it stands in Table S1, which neither reader read. It is entered
   without an error, as the second value of this source, with a note that it is the value the three lower D₂O
   concentrations converge to and that by footnote [b] it is the average used for the Arrhenius fits of T0140–T0142.
4. **S065, D(kcat) of 6.1 at 40 °C (reading 2 adopted, row added as M0283):** the first reading missed it. It is
   printed twice in the main text ("The Dkcat peaked at 40 °C, with its value of 6.1") and in the Abstract, so it is
   not a figure-only value, and the database already holds one errorless prose value of this kind (M0258). It is
   entered as `observed`, as both readers judge every S065 value: the paper writes "We **assume** in the discussion
   to follow that the substantially inflated Dkcat of 6.1 at 40 °C **implies** the intrinsic KIE to have largely been
   revealed", which is an assumption about what the number approaches, not a statement that it is the intrinsic KIE.
   The notes say that the underlying series stands in Table S1 and Figure 4, neither of which was read, and that the
   Methods report the two determinations agreeing within 5 %.
5. **S063 footnote [b], the two forced fits (reading 2 adopted, rows added as T0152 and T0153):** the first reading
   missed them. The footnote prints "For 24 and 48 % D₂O, forced fitting of the data as a linear function of 1/T
   resulted in A_H/A_D of 5 and 4, respectively (with slopes corresponding to Δ_{H–D}E_a of 60 and 20 cal mol⁻¹,
   respectively)" — a second, different Arrhenius fit of the same data, with its own prefactor ratio and a non-zero
   slope, so it belongs in its own rows beside T0140 and T0141. **The sign is changed:** the printed quantity is
   Δ_{H–D}E_a = Ea(H) − Ea(D) = Ea(light) − Ea(heavy), the opposite of this database, so −0.060 and −0.020 kcal/mol
   are entered. Three things agree on that direction: the subscript H–D itself, Eq. (7) of the paper, which the PMC
   XML gives as ln KIE = −[(Ea_H − Ea_D)/R](1/T) + ln(A_H/A_D), and the arithmetic — 5 × exp(−0.060/RT) = 4.5 at
   292 K, close to the measured mean KIE of 4.4, where the other sign would give 5.6.
6. **S065, the UniProt accession of TaCPa2E (reading 2 adopted, field emptied):** the first reading entered
   A0ABS1GJY6, the accession RCSB cross-references from entry 9RL0, and noted that UniProt files it under a different
   organism. The second reading left the field empty and gave the reason: the sequences differ. The curator checked
   this directly on 9 November 2026 — 9RL0 entity 1 (340 residues) against the A0ABS1GJY6 FASTA (342 residues)
   differs at 49 of 340 aligned positions, 85.6 % identity, and UniProt names the organism *Persephonella atlantica*
   (Aquificae), not *Thermodesulfatator atlanticus*. A0ABS1GJY6 is therefore a homolog and not this protein, so
   `uniprot` is empty for CPA2E_THEAT_WT and the notes record the cross-reference, the identity and that UniProtKB
   holds only two *T. atlanticus* proteins (C0MPG6 and C0MPG7, sulfite reductase subunits). The catalytic Tyr164 the
   source names is present in 9RL0 itself, so that check does not depend on the accession. This is the one factual
   error the second reading caught.
7. **S062, the PDB entries of the wild type (reading 1 kept):** the first reading lists `3TK2;3TK4`, the second
   `1LTU;1LTV;1LTZ;3TCY;3TK2;3TK4;4JPY`. SCHEMA.md decides it: the field holds "PDB entries of exactly this variant …
   sequence differences that RCSB lists but the study did not engineer go into `notes`". Both readers find that
   1LTU, 1LTV, 1LTZ, 3TCY and 4JPY carry M64L, Q85E, V276I and R288H, which this study did not engineer, so those
   five belong in the notes, where the first reading already has them, and only the two entities RCSB reports without
   differences from P30967 stay in the field. The notes now also carry the second reading's finding that every
   `pdbx_mutation` field of this group is empty in RCSB, so the entity sequences have to be compared by hand, and
   that 3TCY, 3TK2 and 3TK4 carry a GPLGS/GLPGS tag remnant.
8. **S064, the PDB entries of the six rounds (reading 1 kept, notes extended):** the first reading lists only the
   entries the source itself names for each round (R1 5D2W, R5 6DKV;6C7M;6DNJ, R7 6CAI;6DC1, R7-2 5D38;6CT3, R4 and
   R6 empty), the second adds every sequence-matching entry of the titled series (R1 +4Z08;5D2T;5D2V, R5
   +5D2X;5D2Y;5D30;6C7T;6C7V, R6 5D32;6C8B, R7 +5D33;5D37). The same SCHEMA clause keeps the narrower field: the
   second reading's own sequence analysis finds that the mutation sets of those entries do not match the rounds the
   main text describes — 5D2X/5D2Y/5D30 lack K146E for R5, the R6 group lacks K146E and carries an unmentioned K19E,
   the R7 group carries V12L, H84Y and M207T and not the I102F the text names — so they are not demonstrably "exactly
   this variant", and their assignment rests on RCSB titles while the full mutation lists stand in a supplementary
   table neither reader could read. All of it is now in the notes, together with the ten entries that cite this
   paper's DOI (6C7H, 6C7M, 6C7T, 6C7V, 6C8B, 6CAI, 6CT3, 6DC1, 6DKV, 6DNJ), the fact that 6C7H is R1 with the
   Trp50Ala mutation and belongs to no entered row, the reversion L227F present in every evolved variant, and the
   sixteen differences of the design itself from the HisF scaffold Q9X0C6.
9. **S065, a second step for the proton transfer to Tyr164 (not created, documented):** the second reading splits the
   chemistry into two steps and hangs the ten solvent isotope effects on a proton transfer from the substrate 2-OH to
   Tyr164. The enzyme does transfer that proton, and the paper describes it, but the ten values are not entered as a
   primary effect on it: they are inverse (0.49 to 0.59 with the deuterated substrate) and the paper reads them
   through ground- and transition-state fractionation factors of all exchangeable positions,
   ᴰ²ᴼk_cat = Φ_GS/Φ_TS, not as an effect on one transferred proton. They therefore stay on the chemical step
   `CPA2E_THEAT_WT_CDPGLC`, as the solvent rows of S056 stay on theirs, and the step notes now record the proton
   transfer to Tyr164 and the second reading's proposal. If the schema ever gains a field for the position a solvent
   effect reports on, this is the row to revisit.
10. **Cross-reference corrected in M0258 (first-reading error):** its note pointed at T0150 for the 94 % D₂O average
    of 6 ± 2, which is T0143; T0150 is a series of S065. Corrected.
11. **Judgement calls made the same way by both readers:** 279.15 K (6 °C) for the KIE column of S061 Table 2,
    whose footnote a marks only the two rate-constant columns, because Eq. (2) is the ratio of those two numbers and
    78/44 reproduces the printed 1.8; the saturating 2.3 ± 0.5 of S061 entered in its own row, because the paper
    prints it with an error and a temperature, with a note that the condition differs from Table 2's; `observed` for
    the I234D value of 0.90 ± 0.03 of S062, whose "likely to be the intrinsic isotope effect" is a hedge; `intrinsic`
    for the benzylic 10 ± 1 of S062, which the paper names an intrinsic isotope effect outright; 303.15 K for the
    kH/kD column of S064, the only temperature its table states, at which the printed Arrhenius parameters reproduce
    the printed ratios; 283.15–323.15 K and eight temperatures for S064 from the list in the Methods;
    280.15–303.15 K and ten temperatures for S063 from the list in its Experimental Section; no number of
    temperatures for S061, S062 and the two S065 sub-ranges, which state none; `single_turnover` for S061 and
    `competitive` for the two intramolecular competitions of S062; and the conversion of the S065 energies from
    kJ/mol to kcal/mol to four significant figures, with the printed values kept in `as_printed`.

## Inconsistencies inside the papers

None of them changes an entered value. All were checked by the curator in the HTML or the XML.

- **S061:** the deuterated rate constant k_obs(B→C) is 6.3 ± 0.2 s⁻¹ in Table 1 and 5.3 ± 0.2 s⁻¹ in Table 2, and
  the printed KIE of 1.8 follows the Table 2 value; the text rounds the table throughout ("close to the unity" for
  1.3 ± 0.6, "about 10" for 13 ± 6, "nearly 0" for ΔEa, "~1.8" for the KIEs).
- **S062:** the Abstract rounds the four D(kcat) values to 1.2, 1.4 and 0.9; the quoted eukaryotic intrinsic effect
  of 0.90 ± 0.03 is numerically identical to this paper's own I234D value measured with DMPH₄, which is the trap this
  block most needed two readers for, and both readers kept the two apart.
- **S063:** the paper gives two different Arrhenius fits of the same data, the KIE-independent fit in Table 1 and the
  forced linear fit in footnote [b] (decision 5), which the footnote itself explains; the prose solvent effects on
  k_cat and k_cat/K_M are given only as "approximatively twofold" with the numbers in Table S2, and neither reader
  entered them.
- **S064:** the text gives the solution KIE as "a value of 4.9 at 298 K" while row B of Table 1, the non-enzymatic
  reaction, is 4.6 ± 0.1 and 4.9 ± 0.2 is exactly the tabulated value of R1; either the text mis-quotes row B or the
  kH/kD column is at 298 K and not 303 K, and both readings stand in the notes of the six rows. Table 1 footnote a
  gives the substrate range as 0.1–1.2 mM, the Methods as 0.01–1.1 mM.
- **S065:** the Abstract gives 2.1 and 3.3 where Table 1 gives 2.20 ± 0.75 and 3.34 ± 0.09, which are different
  determinations (the single-concentration series against the global fit of eq 6); the Discussion rounds Table 2 to
  −37 and +13 kJ/mol; the Methods list the solvent isotope effects only at 60 and 20 °C although Table 3 also
  reports the 80 °C value of 0.84 ± 0.03; the Methods cross-reference the k_cat/K_M isotope effects to Table 2 where
  Table 1 is meant.

## SCHEMA.md

No change. Decisions 7 and 8 apply the `pdb` clause as it stands; decision 9 names the one case that would need a
new field.

All 35 isotope effects, all 17 temperature series, the 11 new enzyme rows and the 14 new steps of S061–S065 are now
`verified`.
