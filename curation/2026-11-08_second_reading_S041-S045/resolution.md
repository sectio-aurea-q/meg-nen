# Second reading of S041–S045 (8 November 2026)

First reading `ai-1`, second reading `ai-2`. These five papers on thymidylate synthase are block 1 of the second
reading list. Both readers worked from the PMC pages of the papers, saved on 8 November 2026 (S041, S042 and S044 as
author manuscripts, S043 and S045 as publisher versions); the published PDFs and the supporting information were not
read. The saved pages lost the equations, which PMC renders with MathJax, so both readers also had the PMC XML of the
same five manuscripts and used it only for those; no number was taken from it. The second reader worked from these
files alone, did not see the first reading, and looked up UniProt and RCSB PDB again for every enzyme. Its
instructions repeated the rules of CURATION.md and SCHEMA.md and allowed the web only for these lookups. Files in this
folder:

- `reading2_measurements.csv`, `reading2_temperature.csv`, `reading2_enzymes.csv`, `report.md`: the second reading as
  delivered (`report.md` saved by the curator from the second reader's answer; the list of its output files was
  shortened)
- `comparison.md`: row-by-row comparison of both readings, before the decisions below

## Result

All 7 temperature series of the first reading have a partner in the second reading, and all of them agree in
A_L/A_heavy, ΔEa and its sign, errors, temperature range, number of temperatures, pH and every category. The papers
print no isotope effect at a single, stated temperature, so the first reading has no rows in `measurements.csv`; the
second reading has 7 there, all from S045 (point 1). Both readers left out the same values: everything the papers
mark as taken from other work (the wild-type columns of S041–S045, the hydride-transfer rows of S041, S043 and S044,
the E. coli rows of S045), the semi-classical limits, the DAD and ΔG° fits of S042, and the per-temperature KIEs and
commitments, which stand only in figures and the supporting information. Decisions:

1. **Single values of S045 (only in the second reading):** the six observed and intrinsic KIEs of the human enzyme
   in Table 2 (with and without Mg2+) and the observed H/T KIE of 1.10 ± 0.02 at high MTHF in the Results. They are
   not entered. Table 2 states no temperature, and the hydride-transfer KIEs of this paper were measured at 5, 15, 25
   and 35 °C, so none can be assigned; the second reading left the temperature empty, which `measurements.csv` does
   not allow. For 1.10 ± 0.02 the second reading took 25 °C from the Methods sentence that the pH was adjusted at
   25 °C; the paper gives neither the temperature nor the MTHF concentration, nor whether the value is a measured
   point or the plateau of the fit in Fig. 3. The notes of T0087 and T0088 record both.
2. **Signs of ΔEa:** S041, S042 and S043 define ΔEa as light minus heavy, by their equations (S041 Eq. 5, S042 Eq.
   10, S043 Eq. 5, read in the XML) and, for S043, in the text, so both readers changed the printed signs. S044 and
   S045 head their columns ΔEa,T/H and ΔEa,T-H and print positive values; both readers kept them, although the
   equations as printed (S044 Eq. 5, S045 Eq. 4, exp(−ΔEa(T−H)/RT)) would invert them. With A_H/A_T far below 1, only
   the heavy-minus-light reading gives a normal KIE, and S044 and S045 print the S041 value as +8.0.
3. **Steps:** four new steps (proton abstraction of Y209W, R166K and the human enzyme, hydride transfer of the human
   enzyme). Both readings name C5 of dUMP and C6 of the folate as donors, a water oxygen or the hydrogen-bonded
   network as the proton acceptor where the paper names one, and C7 of the exocyclic intermediate as the hydride
   acceptor. The wording of the existing TS steps (S020) is kept.
4. **Enzymes:** both readings give P0A884 and P04818, EC 2.1.1.45, no PDB entry for R166K (1FFL and 1FWM carry R166Q)
   and none listed for the human wild type (61 entries; the paper shows 1HVY). The notes of T0084 now also say that
   the row label and the caption of S042 Table 1 differ (found by the second reading).

## Inconsistencies inside the papers

None of them changes an entered value. All were checked by the curator in the HTML, the XML or at RCSB.

- **S042:** the Introduction calls 2FTO the wild type and 1TYS the mutant, Fig. 4 the reverse (RCSB: 2FTO is Y94F);
  RCSB's sequence of 1TYS, which Fig. 4 shows as the wild type, has Ser at 146 without a listed mutation; the Table 1
  row is labelled ΔEa,H/T and prints a negative value, the caption and the text say ΔEa,T/H.
- **S043:** the printed Y209W proton-abstraction parameters (A_H/A_T 1.4 × 10−6, ΔEa 7.70 kcal/mol) give a KIE of
  about 0.6 at 25 °C, while the text calls the KIEs of WT and Y209W similar and the WT parameters give about 6 (an
  A_H/A_T of 1.4 × 10−5 would fit); the text says Table 1 gives H/T and D/T parameters, it gives H/T only; the
  Introduction cites "2G80", a yeast protein, for the WT ternary complex (2G8O is meant).
- **S044:** Eq. 5 as noted in point 2; the Chemicals list [6-3H]dUMP, the experiments use [5-3H]dUMP; the synthesis
  paragraph has C146 attack C5 of dUMP, elsewhere C6; "~25–30 % excess to dUMP (1.35 mM)" leaves open which compound
  is at 1.35 mM.
- **S045:** Eq. 4 as noted in point 2; the Table 3 parameters of the human hydride transfer give a KIE of about 5 at
  25 °C, while Table 2 prints intrinsic H/T KIEs of 11.0 and 11.6 and the text calls the human KIEs larger than the
  E. coli ones (about 7.8 from the cited parameters).
- **Between the papers:** the wild-type hydride-transfer ΔEa of S011 (Agrawal et al. 2004, not in hand) is printed
  as −0.02 (S039, S043) and +0.02 (S040, S041, S044) under the papers' own definitions; it is zero within its error
  and is not entered. The wild-type proton-abstraction values that S044 and S045 cite from S041 carry other errors
  there (±0.16 kcal/mol; ±1.3 × 10−6).

## SCHEMA.md

No change.

All 7 temperature series, the 2 enzyme rows and the 4 steps of S041–S045 are now `verified`.
