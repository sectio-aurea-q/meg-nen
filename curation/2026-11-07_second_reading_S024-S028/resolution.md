# Second reading of S024–S028 (7 November 2026)

First reading `ai-1`, second reading `ai-2`. Both readers worked from the PMC pages of the five papers, saved on
7 November 2026 (S024, S025 and S026 as author manuscripts, S027 and S028 as publisher versions); the published PDFs
and the supporting information were not read. The second reader worked from those pages alone, did not see the first
reading, and looked up UniProt and RCSB PDB again for every enzyme. Its instructions repeated the rules of
CURATION.md and SCHEMA.md and allowed the web only for these lookups. Files in this folder:

- `reading2_measurements.csv`, `reading2_temperature.csv`, `reading2_enzymes.csv`, `report.md`: the second reading as
  delivered (`report.md` saved by the curator from the second reader's answer; the list of the reader's working files
  was removed)
- `comparison.md`: row-by-row comparison of both readings, before the decisions below

## Result

All 36 rows of the first reading (25 isotope effects, 11 temperature series) have a partner in the second reading,
and all of them agree in value, error, temperature, pH, Arrhenius parameters, temperature range and number of
temperatures. Neither reading has rows the other lacks. They differ in one category (point 1), in the PDB entries of
three enzymes (points 2 and 3), in one organism name (point 4) and in the transfer class of the NspLOX steps
(point 5). Both readers left out the same values: the non-enzymatic acetate and phosphate columns of S024, the values
S025 marks ND, the extrapolated 30 °C values of S027 (footnote b), the SLO-1 rows that S027 takes from its ref. 16, the
average 661 ± 27 in the Abstract of S028 and all values cited from other papers. Decisions:

1. **`method` of Dk1 with 4-C2H3-phenylalanine in S025 (M0080–M0083, T0052–T0055):** the first reading used `other`,
   because the effect comes from the change in product partitioning (eq 1) rather than from rates; the second reading
   used `noncompetitive`, because the protio and the CD3 substrate were run in separate reactions. The second reading
   is taken: SCHEMA.md defines `noncompetitive` as light and heavy measured separately, whatever is observed. The
   values from the partially deuterated substrates stay `competitive` in both readings (H versus D loss within one
   methyl group).
2. **PDB entries of rat PheH and TyrH:** the first reading listed all wild-type entries, the second reading only
   entries of the same construct. The second reading is taken, and SCHEMA.md now says that entries of a shorter
   construct (a truncation or a single domain) are named in `notes`, not listed. `PHEH_RAT_WT` keeps 5DEN and 5FGJ
   (residues 1–453); 1PHZ and 2PHM (residues 1–429) move to `notes`. `TYRH_RAT_WT` keeps `pdb` empty: 1TOH and 2TOH
   (residues 156–498, catalytic and tetramerization domains) and 2MDA (regulatory domain) are named in `notes`. A
   missing initiator Met (3D9G of NAO), tags or a removed transit peptide (the POR B entries of S022) do not count as
   another construct.
3. **PDB entries of FDH:** both readings keep the reviewed entry O13437, from which all wild-type crystal structures
   of C. boidinii FDH differ at 11 positions (they match A0A0A1EQY0, strain 2.1645). The second reading listed 5DN9,
   5DNA, 8HTY and 8IQ7, assuming that the enzyme of S026 was the one the same group crystallized in 2016. The curator
   checked that paper (10.1021/acs.biochem.6b00181, PMC4917879): it states that earlier H-transfer studies, citing
   S026, used a commercially available CbFDH, while its own structures are of recombinant CbFDH from a gene given by
   N. Labrou. The sequence of the enzyme of S026 is therefore not known, and `pdb` stays empty; `notes` names the
   entries and the reason.
4. **Organism of NspLOX:** the second reading wrote `Nostoc sp.`, as the source does. The first reading's
   `Nostoc sp. PCC 7120` is kept, since both readers identified the protein as Q8YK97 of strain PCC 7120 through
   refs. 8, 10 and 11 of the source, and other rows name the strain as well (Synechocystis sp. PCC 6803,
   Pseudomonas stutzeri WM88); `notes` says that the source writes Nostoc sp.
5. **`transfer` of the NspLOX steps:** the second reading chose `H_atom` from the source's "net H-atom abstraction by
   a metal hydroxide"; the same paragraph says that this step is modelled as a nonadiabatic proton-coupled electron
   transfer. The first reading's `PCET` is kept, as for all SLO-1 steps (S002, S016, S017), so that the lipoxygenases
   share one class; `notes` gives the source's wording.
6. **Organisms the sources do not name (S024, S025):** both readings assigned Fusarium oxysporum (NAO), rat (PheH,
   TyrH) and rabbit (TrpH102–416); the second reader marked rat and rabbit as unverified. The curator checked the cited
   references: ref. 3 of S025 (10.1021/bi9711137) is indexed with MeSH Rats, and the lengths of its Δ117PAH and
   Δ155TYH (the C-terminal 336 and 343 residues) fit rat PheH (453) and TyrH (498); the abstract of ref. 4
   (10.1074/jbc.273.20.12259) names wild type rabbit tryptophan hydroxylase and TRH102-416; refs. 11 and 24 of S024
   name Fusarium oxysporum in their titles.
7. **Judgement calls made the same way by both readers:**
   - S024: 27 °C for the NAO KIE (footnote b of the cell, not footnote a of the row label); `kcat/KM` and
     `noncompetitive` (the note to ref. 25: protio and deuterated nitroethane assayed separately below Km/10); ΔEa as
     Ea(D) − Ea(H), against the sign in the Fig. 2 legend; `Ea_light` empty, since ΔH‡ comes from an Eyring fit; the
     NAO data as this paper's own (refs. 24 and 25 in the Fig. 1 legend give methods).
   - S025: 30 °C and pH 7.0 from the Fig. 1 legend, to which Table 1 refers; `quantity` other (k1, from product
     partitioning); `kind` intrinsic for all rows, as the Table 1 title says; Dk1 entered as primary although it
     equals Dk(αDk)²; the temperature series of all four enzymes from the 4-C2H3 substrate; ΔEact as Ea(D) − Ea(H);
     the TyrH values as this paper's own (Table 1 carries no citation; ref. 6 had measured TyrH before).
   - S026: no per-temperature values (SI and Fig. 4 only); 5–45 °C; pH 7.5; ΔEa read as heavy − light; H/D derived
     from the H/T and D/T measurements.
   - S027: the 20 °C KIEs as measurements; ΔEa as Ea(D) − Ea(H) (the text: Ea(D) is lower); Ea(H) as `Ea_light`;
     A_H (in s−1) and Ea(D) 11.6 only in `notes`; donor C11 and acceptor Fe(III)–OH from "between two double bonds"
     and "metal hydroxide".
   - S028: six Dkcat rows; ΔEa = EaD − EaH, as note 29 defines it; no A_H/A_D and no Ea(H) of this series in the
     main text.

## Inconsistencies inside the papers

None of them changes an entered value. All were checked by the curator in the HTML.

- **S024:** the Fig. 2 legend prints ln(KIE) = ln(AH/AD) − ΔEa/RT, which with the positive ΔEa of Table 1 would give
  a KIE of 0.09 instead of about 9; the text gives the rate enhancements of NAO "at 25 °C" but uses kH 4800 M−1 s−1,
  which footnote b places at 27 °C; note 31 is cited twice, the second time probably for note 32, which is otherwise
  not cited.
- **S025:** the Table 2 parameters of PheH and Δ117PheH predict Dk1 of about 9.7 at 30 °C against 12.4 and 12.1
  measured (within the errors of A_H/A_D); a note added after ASAP publication records corrections to paragraphs 4
  and 5 and to Fig. 1, and the PMC page does not show whether it holds the corrected version.
- **S026:** the organism is spelled Candida bodinii and Candida biodinii; the manuscript keeps the sentence "(I am
  sending you SI as a separate word document)".
- **S027:** from the text, Ea(D) − Ea(H) = 11.6 − 12.4 = −0.8, Table 1 prints −0.7; for I219A the positive ΔEa means
  a KIE that falls with temperature, yet the extrapolated 30 °C KIE (164 ± 26) lies above the 20 °C value (155 ± 7),
  within its error; footnote b speaks of an Eyring fit, the table gives Arrhenius parameters; ref. 8 is listed as
  (2007) J. Biol. Chem. 283, a 2008 volume.
- **S028:** the text names the other double mutant L546A/L553A, the Fig. 4 legend L546A/I553A; the Fig. 4 legend
  cites ref. 1, an alcohol dehydrogenase paper, for the WT data; Dkcat recomputed from the printed kcat values gives
  631 and 758 at 5 and 15 °C against the printed 630 and 760 (rounding).

## SCHEMA.md

Two conventions written down: a truncated construct is entered in `variant` as the source names it (e.g. `Δ117`,
`102–416`); PDB entries of a shorter construct (a truncation or a single domain) are named in `notes`, not listed,
while a missing initiator Met, tags or a removed transit peptide do not count.

All 25 isotope effects, 11 temperature series, 8 enzyme variants and 8 steps of S024–S028 are now `verified`.
