# Second reading of S034–S038 (7 November 2026)

First reading `ai-1`, second reading `ai-2`. Both readers worked from the PMC pages of the five papers, saved on
7 November 2026 (S034, S036 and S038 as publisher versions, S035 and S037 as author manuscripts); the published PDFs
and the supporting information were not read. The second reader worked from those pages alone, did not see the first
reading, and looked up UniProt and RCSB PDB again for every enzyme. Its instructions repeated the rules of
CURATION.md and SCHEMA.md and allowed the web only for these lookups. Files in this folder:

- `reading2_measurements.csv`, `reading2_temperature.csv`, `reading2_enzymes.csv`, `report.md`: the second reading as
  delivered (`report.md` saved by the curator from the second reader's answer; the list of its output files was
  removed)
- `comparison.md`: row-by-row comparison of both readings, before the decisions below

## Result

All 65 rows of the first reading (56 isotope effects, 9 temperature series) have a partner in the second reading,
and all of them agree in value, error, temperature, pH, Arrhenius parameters, temperature range and every category.
Neither reading has rows the other lacks. The readings differ only in two sets of PDB entries (points 1 and 2) and in
the way organisms are named (point 3). Both readers left out the same values: the rows the papers take from earlier
work (the WT, G121V, M42W, I14A and M42W-G121V rows of S034 and S035, the pH 9.0 rows of Table 1 and the WT column of
Table 2 in S036, the Dkcat of WT and L754A in S038), the per-temperature KIEs of the SI, the single-turnover rates,
the Marcus-like model fits, the derived epistasis terms ΔΔEa and the commitments. Decisions:

1. **PDB entry of ecDHFR N23PP/G51PEKN:** the second reading found 4GH8, which the first reading's full-text search
   had missed. The curator confirmed it: the entity carries N23PP and G51PEKN (RCSB mutation field), is the expected
   sequence without the C-terminal Arg159, and cites 10.1073/pnas.1307130110, ref. 24 of S036. It is entered. 3QL0
   and 4KJL carry N23PP with S148A and stay unassigned, so N23PP alone has no entry.
2. **PDB entries of wild-type SLO-1 (existing row `SLO1_SOYBN_WT`, from S033):** the first reading of S033 had
   assumed very many wild-type entries and left `pdb` empty; the second reading here counted seven. The curator
   confirmed by sequence: 1F8N, 1YGE and 2SBL are identical to P08170; 3PZW, 5T5V, 9O4S and 9O4T differ only by S160E,
   which most SLO-1 entries share; 4WFO is the manganese-substituted enzyme and is not assigned. Since RCSB holds only
   a few, they are listed. The second reader's remark that S038 names 1F8N could not be confirmed in the HTML and is
   not repeated in `notes`.
3. **Kept from the first reading:** organism names without the common names in parentheses (the second reading wrote
   "human (Homo sapiens)" and "soybean (Glycine max)").
4. **Scope:** S037 reports heavy-enzyme effects (light over heavy hsDHFR) on kcat, Km and the rate constants of product
   release. Both readers left them out, since the isotopes sit in the protein, not on the transferred hydrogen. They
   are not entered, and SCHEMA.md now says so. The hydrogen isotope effects of the heavy enzyme itself are entered,
   with `variant` heavy (13C, 15N, 2H).
5. **Judgement calls made the same way by both readers:**
   - S034 and S035: ΔEa(T-H) as Ea(T) − Ea(H) (positive ΔEa with A_H/A_T well below 1 gives KIEs of about 9 to 13 at
     25 °C); 5–45 °C and pH 9.0 from the Methods; the double mutants written G121V/F125M, M42W/F125M and I14A/G121V.
   - S036: footnote c of Table 1 ("From Ref. 12") read as covering both pH 9.0 rows, though it stands on the first
     only; the pH 7.0 rows of the wild type as this paper's measurements, observed H/T and D/T and intrinsic H/T; the
     intrinsic kH/kT of N23PP and N23PP/G51PEKN at 25 °C and pH 9.0 (Table 2 footnote d), which agree with the
     Arrhenius parameters of Table 2.
   - S037: 5–45 °C from the Abstract for both forms of hsDHFR.
   - S038: D-LA as perdeuterated linoleic acid (Abstract and Methods), so the Dkcat and Dkcat/Km rows carry secondary
     contributions; `kind` observed for Dkcat, although the Scheme 1 legend says Dkcat and Dkchem can be used
     interchangeably; the solvent isotope effects as H2O over D2O at pH 9.0 (the D2O buffer read 8.6 on the pH meter);
     C11 and PCET as for SLO-1 elsewhere; the Dkcat of L546A and I553A, which carry no footnote, as this paper's own.

## Inconsistencies inside the papers

None of them changes an entered value. All were checked by the curator in the HTML.

- **S034:** kwt/kmut of W133F is printed as 3 ± 0.1, while 228/88 is 2.6.
- **S035:** the double mutant is called I14A-G121V in the text and tables and G121V-I14A in the Fig. 2 legend.
- **S036:** the text says "we measured the intrinsic KIEs at pH 9.0 and 7.0", while footnote c gives the pH 9.0 data
  to ref. 12; the text discusses pH 8.0, for which Table 1 has no row; the text cites Fig. 4 for the Arrhenius plot
  of Fig. 3 and Fig. 5 for the commitments of Fig. 4.
- **S038:** the Methods list the competitive KIEs for "WT SLO, I552V, V750A, I538A, I839A, and W500F" (I552V for
  I552A, and five variants of Table 1 missing); the Results list I553A twice and omit R707A; the Results give 10–45 °C,
  the competitive assays ran from 10 to 40 °C; the Methods list solvent isotope effects for WT, I552A and L546A, Table
  2 also has V750A; the Methods heading speaks of double mutants, all variants are single mutants; the "180- and
  2000-fold" reductions of kcat for L546A and L754A do not match Table 1 (about 119 and 1400 at 10 °C).

## SCHEMA.md

One convention written down: effects of labelling the protein itself (heavy-enzyme effects) are not entered.

All 56 isotope effects, 9 temperature series, 19 enzyme variants and 19 steps of S034–S038 are now `verified`;
`DHFR_ECOLI_N23PP_G51PEKN` gains 4GH8 and `SLO1_SOYBN_WT` seven wild-type entries.
