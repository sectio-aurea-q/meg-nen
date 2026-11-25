# Second reading (reader `ai-2`) — MEG-NEN sources S001, S008, S010, S011, S012

Saved by the curator from the second reader's answer of 10 November 2026; the list of its output files and the
table of enzyme look-ups were shortened. The second reader worked from the five PDFs, from page images made from
them and from SCHEMA.md and CURATION.md; it did not see the first reading or the tables of the collection. UniProt
and RCSB were queried on 10 November 2026 for `reading2_enzymes.csv` only.

Rows written: measurements 30 (S001 4, S008 6, S010 0, S011 2, S012 18), temperature 16 (S001 4, S008 3, S010 6,
S011 2, S012 1), enzymes 8.

## S001 — Knapp, Rickert, Klinman 2002 (SLO-1)

**Entered.** Table 1, KIE on kcat at 303.15 K, pH 9.0, noncompetitive, observed: WT 81 (5), L546A 93 (9), L754A
112 (11), I553A 93 (4). Table 1, Arrhenius series 5–50 °C, as AH/AD; ΔEact; Eact(H): WT 18 (5); 0.9 (0.2);
2.1 (0.2) — L546A 4 (4); 1.9 (0.6); 4.1 (0.4) — L754A 3 (3); 2.0 (0.5); 4.1 (0.3) — I553A 0.12 (0.06); 4.0 (0.3);
1.9 (0.2).

**Not entered.** Table 2 and all simulation numbers (calculated); Table 3 (qualitative); "AH/AD ≈ 3" in the text;
Introduction values attributed to refs 17 and 18; AH, kcat, kcat/KM, ΔΔG‡ (not isotope effects).

**Judgement calls.**
1. *Footnote e (rule 1).* The row labels WT-SLO and Leu546→Ala carry footnote e, citing Rickert & Klinman,
   Biochemistry 1999. For L546A the Methods say the data "appeared in an earlier publication … but were not analyzed
   in detail". Both entered, with the attribution in `notes`. For WT the paper presents the data as its own: Fig. 1,
   an O2 correction described in Methods, and Eact 2.1 in Table 1 against 2.2 quoted for ref 18. This needs settling
   against Rickert & Klinman 1999, which was not in the batch.
2. *Temperature of the KIE column.* Footnote b ("reported for 30 °C") sits only on kcat and kcat/KM. 303.15 K
   assigned because the KIE is the ratio of those kcat values and the text, the Abstract and the Table 2 header all
   say "KIE at 30 °C".
3. *Sign.* Footnote d defines ΔEact = EactD − EactH, heavy − light; no change.
4. *Kind.* All observed: the statements that kcat reflects only the chemical step cite prior work and are hedged.
5. *L754A substrate.* Perdeuterated 2H31-LA, not 11,11-2H2-LA; `kie_type` stays primary.

**Recomputation at 303.15 K.** WT 80.2 against 81; L546A 93.7 against 93; I553A 91.8 against 93: reproduced.
L754A 83.0 against 112: not reproduced. The digits were re-read on the 300 dpi image and are as printed. AH/AD is
printed with one digit, "3 (3)"; AH/AD = 4 would give 110.6.

## S008 — Sikorski et al. 2004 (ecDHFR)

**Entered.** At 25 °C, pH 9.0, competitive V/K: intrinsic primary H/D 3.5 ± 0.2; secondary observed H/T
1.149 ± 0.005 and D/T 1.058 ± 0.003; secondary corrected kH/kT 1.194 ± 0.007 and kD/kT 1.052 ± 0.007; secondary
intrinsic H/D 1.13, no error. Intrinsic primary series, 5–45 °C: H/T AH/AT 7.4 ± 4, ΔEa −0.1 ± 0.3; H/D AH/AD
4.0 ± 1.5, ΔEa −0.07 ± 0.2; D/T AD/AT 1.8 ± 0.3, ΔEa −0.03 ± 0.09.

**Not entered.** Observed primary V/K H/T 4.81 ± 0.06 and D/T 1.65 ± 0.01 "over 45 to 15 °C": a mean over a range
with no single temperature (rule 11) and no Arrhenius parameters. 3.0 ± 0.1 at 25 °C (refs 3, 33) and the
calculated 3.4: other work. T. maritima values, semiclassical limits, commitments, the exponent 3.5 ± 0.5, and Ea
3.7 ± 0.3 (ref 25, unpublished, not an isotope effect). Supporting information and anything only plotted.

**Judgement calls.**
1. *Sign.* No equation in the paper; established by recomputation: 4.0·exp(−0.07/RT) at 298.15 K is 3.55, against
   the printed intrinsic H/D of 3.5 ± 0.2; the opposite sign gives 4.50. The printed signs are heavy − light.
2. *Range.* 5–45 °C assembled from the text ("45 to 15 °C", commitments at 10 and 5 °C, "throughout the temperature
   range"). `n_temperatures` empty.
3. *Corrected secondary values marked intrinsic.* The sentence says "corrected for the commitment" and uses the
   kH/kT notation the paper defines as intrinsic; the next sentence derives "an intrinsic 2° H/D KIE" from them. The
   word "intrinsic" is not used of these two numbers themselves, so `observed` is the alternative.
4. *Secondary intrinsic H/D 1.13.* A Swain–Schaad calculation with no error; entered because the primary intrinsic
   3.5 is calculated in the same way, but it could be dropped as derived.
5. *Buffer.* Only in the supporting information; `conditions` says so.

## S010 — Kohen et al. 1999 (ADH-hT)

**Entered (temperature only).** Table 1, competitive primary, `dEa_kcal` empty because only the prefactor ratios are
printed: AH/AT 0.26 (±0.23) for 5–30 °C and 4.3 (±0.6) for 30–65 °C; AD/AT 0.23 (±0.14) and 1.73 (±0.26). Table 2,
noncompetitive kcat H/D: 5–30 °C AH/AD 1 × 10⁻⁵ (±1 × 10⁻⁵), ΔH‡(D) − ΔH‡(H) 7.8 (±1.8); 30–65 °C AH/AD 2.2 (±1.1),
0.5 (±0.6).

**Not entered.** No KIE is printed as a number (Figs 2 and 4 are plots); secondary KIEs and exponents (plotted
only); the "Semi-classical" row of Table 1 (theory).

**Judgement calls.** The two fitted regimes are separate rows. The row label ΔH‡(D) − ΔH‡(H) is heavy − light.
`Ea_light` left empty: ΔH‡ at 30 °C for H (23.6 ± 0.6 and 14.6 ± 0.3) is an enthalpy of activation, quoted in
`notes`. `kcat/KM` for the competitive rows is the reader's assignment. Kind observed ("close to fully
rate-determining" is hedged). AH/AD for 5–30 °C written as 0.00001 with error 0.00001.

## S011 — Agrawal et al. 2004 (ecTS)

**Entered.** Observed primary at 20 °C, pH 7.5: T(V/K)H 6.91 ± 0.05 and T(V/K)D 1.78 ± 0.02. Intrinsic series: H/T
AH/AT 6.77 ± 2.78, ΔEa 0.02 ± 0.25; D/T AD/AT 1.90 ± 0.27, ΔEa −0.04 ± 0.08.

**Not entered.** Dk = 3.72 on kcat (Spencer 1997, rule 1); exponents, the commitment, semiclassical limits; Ea
4.0 ± 0.1, ΔH‡ and KS (not isotope effects); KIEs at 5, 30 and 40 °C (plotted only).

**Judgement calls.** Sign: eq 4 with "ΔEa the difference in energy of activation between T and L", heavy − light.
Range and n: 5–40 °C with n = 4 (the Results name 20, 30, 5 and 40 °C, and the Fig. 2 axis labels are 40, 30, 20,
5); the Abstract says "5–45 °C", which conflicts. The Abstract has AD/AT = 1.9 ± 0.25 and AH/AT = 6.8 ± 2.8, the
Results 1.90 ± 0.27 and 6.77 ± 2.78; the Results values were entered. The 20 °C values are observed although the
paper reports no commitment there (hedged statements, and intrinsic values are obtained by another route).

**Recomputation at 293.15 K.** H/T 7.01 against the observed 6.91 ± 0.05; D/T 1.77 against 1.78 ± 0.02.

## S012 — Cha, Murray, Klinman 1989 (yeast ADH, scanned pages)

**Entered** (25 °C, pH 8.5, competitive V/Km, observed). Table 2 primary (kD/kT)obs: 1.72 ± 0.03, 1.70 ± 0.03,
1.76 ± 0.03, 1.72 ± 0.05, average 1.73 ± 0.02*; (kH/kT)obs: 7.15 ± 0.17, 7.00 ± 0.07, 7.23 ± 0.10, average
7.13 ± 0.07*. Table 3 secondary (kD/kT)obs: 1.03 ± 0.01, 1.03 ± 0.01, 1.03 ± 0.004, 1.04 ± 0.02, average
1.03 ± 0.006*; (kH/kT)obs: 1.37 ± 0.02, 1.33 ± 0.01, 1.35 ± 0.04, average 1.35 ± 0.015*. One temperature row,
primary H/D, 0–40 °C: AH/AD = 1.1 ± 0.1 and ED − EH = 3.3 ± 1.3 kJ/mol, converted to 0.7887 ± 0.3107 kcal/mol.

**Not entered.** The (kH/kT)calc columns, "kH/kT = 1.11 ± 0.02", the exponents 3.58 ± 0.09 and 10.2 ± 2.4
(derived); the equilibrium isotope effect 1.33 ± 0.05 and the earlier secondary H/T (ref 22); note 31 values; note
28, "primary H/D isotope effect (3.9 at 25 °C)" and "secondary H/D (1.2 at 25 °C)", inputs to a contamination
correction with no origin, conditions or rate constant stated.

**Judgement calls.** Individual experiments and averages both entered; the starred averages say in `notes` that
they summarise the rows above (the alternative is to keep only the four averages). The text gives the secondary
H/T average as 1.35 ± 0.02, the table as 1.35 ± 0.015; the table value was entered. The H/D series is indirect: the
difference and ratio of the H/T and D/T fits (Fig. 3 legend), whose own parameters are not printed. Sign printed as
ED − EH, heavy − light. The paper says only "YADH (Boehringer Mannheim)"; the assignment to S. cerevisiae ADH1
(P00330) is the reader's.

**Uncertain reading in the scan.** The Fig. 3 legend prints "ED − EH = 3/3 kJ/mol": a slash-like character between
the 3s, and no ±. The entered value and error come from the clear text sentence on p. 1329, "3.3 ± 1.3 kJ/mol". All
table digits were clear at 3× enlargement, including the 0.03/0.05 pairs, 0.004, 0.006 and 0.015. No digit was
guessed. For orientation, 1.1·exp(0.7887/RT) at 298.15 K is 4.16, and the ratio of the printed averages 7.13/1.73
is 4.12.

## Final pass

Every value and error was re-found on page images after the files were written: S001 Table 1 at 300 dpi; S008
p. 4778 at 300 dpi and p. 4779 at 170 dpi; S010 Tables 1 and 2 at 500 dpi; S011 pp. 2001–2002 at 300 dpi; S012
Tables 2 and 3, the Fig. 3 legend and the p. 1329 sentence at 3× enlargement.
