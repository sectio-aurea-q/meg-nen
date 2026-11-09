# Changelog

What changed in MEG-NEN, newest first. Times are Central European Time. Every second reading, comparison and
decision is kept in `curation/`.

## 2026-11-09 13:06

- Four further corrections from the last review of the draft data note, none of them in an entered value:
  `CURATION.md` rule 4 said a value read off a plot "is marked as such in `notes`", implying such values are
  entered; no row is so marked and none was entered, so the rule now says a value that can only be read off a plot
  is not entered, while a number printed in a figure legend is. Rule 5's `observed` carve-out said "only sets the
  value beside an intrinsic value", which did not cover M0188, whose source states the identity *and* prints the
  intrinsic value separately (held here as M0189); the carve-out now turns on the source printing that value for
  the same step. M0131's notes carried two overlapping sentences from different passes, and now carry one. The
  entry of 12:25 was written with a time later than the archive cut from it; the time is corrected.

## 2026-11-09 12:25

- A third reading settled a rule the database had been applying inconsistently. Rows were marked `intrinsic` on
  the strength of a source saying that the measured value *is* or *is realized as* the intrinsic effect, while
  other rows resting on similar wording were marked `observed`. The eighteen rows concerned were re-read against
  their sources. Seventeen stand as they were; **T0011** (trimethylamine dehydrogenase H172Q, S007) changes from
  `observed` to `intrinsic`, because the source states that "Only at pH values of 9.5 and above ... is the
  intrinsic isotope effect realized" and that series was run at pH 9.5 for the same enzyme and step. The earlier
  settlement had taken a figure legend's "the observed KIE" as decisive; that legend covers the whole pH 6-11
  histogram, most of which the same text calls inflated.
- `CURATION.md` rule 5 now states the distinction that separates these cases: an assertion that the measurement
  *is* the intrinsic effect counts, and carries to a temperature series fitted from the same measurements; a
  comparison with an intrinsic value obtained by another route does not, nor does a hedged or second-hand
  identification. Under that rule M0188 stays `observed`, because its source prints the intrinsic value beside it
  and the database holds it separately as M0189; T0062, T0063, M0104 and M0105 stay `observed` on the hedge
  "essentially the intrinsic KIE". T0012's notes now record why pH 11 does not carry the same warrant.
- `SCHEMA.md` carried the superseded one-limb wording for `kind` and now refers to the rule. `data/LICENSE.md`
  misdirected the grant of rights after the licence was narrowed, and now names the curation. `README.md` states
  that `seed/` is working material and not part of the release. T0153's notes carried T0152's arithmetic and now
  carry their own.
- Counts after these changes: 283 isotope effects, 280 `verified`; 153 temperature series, 151 `verified`;
  88 observed and 65 intrinsic among the series; 113 rows `intrinsic` in all, of which 22 do not yet quote the
  source's statement.

## 2026-11-09 11:40

- Four corrections found by an independent review of the draft data note, none of them in an entered value:
- `sources/first_sources.csv`: the `access` field of S013 said `open` while `pdf_in_hand` recorded an author
  manuscript, and the rows read from it say so themselves. Corrected to `open (PMC author manuscript)`. Counted
  over `pdf_in_hand`, 53 of the 57 papers read were read through PMC and 28 of those as author manuscripts,
  supplying 84 isotope effects and 64 temperature series.
- M0131, M0282, M0283, T0152 and T0153 stood at `verified` although each was found by one reading only, the other
  having missed it; the curator checked them against the source, which is not a second independent reading. All
  five are now `single`, and their notes say so. The counts are now 280 of 283 isotope effects and 151 of 153
  temperature series `verified`.
- `CURATION.md` rule 5 stated only the first limb of the rule actually in use. It now states both: a value is
  `intrinsic` where the source says so of that value, or where it comes from a competitive measurement the source
  reports as yielding intrinsic effects; and it records that 22 rows entered under the second limb do not yet
  quote the source's statement.
- `data/LICENSE.md` and `README.md` licensed `data/` and `sources/` wholesale under CC BY 4.0, which cannot be
  granted over the wording quoted from the primary sources in `as_printed`, `notes` and `conditions`. The licence
  now covers the curation, including `curation/` and the documentation, and excludes the quoted wording, which
  stays with its publishers and is used as short quotation.

## 2026-11-09 10:25

- Correction to the entry of 08:05, which said that all 65 papers of MEG-NEN had been read twice. The reading list
  holds 65 papers, but eight of them are behind paywalls, carry `pdf_in_hand = no` in `sources/first_sources.csv`
  and contribute no row to the data: S001, S003, S004, S005, S008, S010, S011 and S012. **57 papers have been
  read.** Earlier entries counted correctly (47 papers after S051–S055, 52 after S056–S060); the entry of 08:05
  counted the rows of the reading list instead of the papers read.
- The papers read were published between 2001 and 2026, not between 1989 and 2026: the only paper of 1989, Cha,
  Murray and Klinman, *Hydrogen Tunneling in Enzyme Reactions*, is one of the eight that are missing, as are
  Knapp, Rickert and Klinman (2002) on soybean lipoxygenase-1 and Kohen et al. (1999) on the thermophilic alcohol
  dehydrogenase. The earliest primary literature of the field is therefore not yet represented.
- No entered value, enzyme row, step or reading is affected. The error was in the count, not in the data; the
  validator and the double readings are unchanged. The project website carried the wrong figure for about an
  hour on 9 November and was corrected the same morning.

## 2026-11-09 08:05
- S061–S065 entered and read twice (block 5, the last block of the second reading list): the hydride transfer from
  NADH to the FAD of human NQO1 in the two non-equivalent sites of the dimer, the aromatic, tautomerization and
  benzylic isotope effects of the phenylalanine hydroxylase of *Chromobacterium violaceum* and of its I234D variant,
  the protonation of geranylgeranyl diphosphate by the class II terpene cyclase PtmT2 measured in mixed H₂O/D₂O
  buffers, the proton abstraction of the designed Kemp eliminase KE07 in six rounds of a directed-evolution
  trajectory, and the transient oxidation of CDP-glucose by the C2 epimerase of *Thermodesulfatator atlanticus* from
  20 to 80 °C: 35 isotope effects and 17 temperature series, all `verified`, with 11 new enzyme rows and 14 steps.
  Both readings agree in every value, error, temperature, pH, quantity and method. The second reading found two
  values and two temperature series the first had missed, all four now entered: the KIE of four that S063 reports
  for its mixed buffers (M0282), the D(kcat) of 6.1 at 40 °C of S065 (M0283) and the two forced Arrhenius fits of
  footnote b of S063 Table 1 (T0152, T0153, sign changed, because the printed Δ_H–D E_a is Ea(light) − Ea(heavy)).
  It also found one error: the UniProt accession A0ABS1GJY6, which RCSB cross-references from entry 9RL0 of the
  epimerase, is a *Persephonella atlantica* homolog at 85.6 % identity and not this protein, so the field is now
  empty. The four D(kcat) values of S062 Table 2 change from `primary` to `other`, because the paper states they
  combine the isotope effect on the attack of the Fe(IV)O intermediate on the ring, where no bond to a labelled
  hydrogen breaks, with the effect on the tautomerization, where a ring hydrogen is lost. The six values of S063
  stay `observed`: the word intrinsic appears only in the hypothesis sentence of its introduction, about the method
  and not about a number. The ten temperatures of S063 are listed in its Experimental Section, so those rows now
  carry `n_temperatures` 10. SCHEMA.md unchanged; the PDB fields of S062 and S064 follow its clause on sequence
  differences a study did not engineer, with both readings' findings in the notes.
  See `curation/2026-11-09_second_reading_S061-S065/`.
- The second reading list is finished: every paper that has been obtained has now been read twice. The reading
  list holds 65 papers, of which 57 have been read; 283 isotope effects and 153 temperature series come from
  those 57. 113 of 115 enzyme rows are `verified`; `MR_PSEPU_WT` and `PETNR_ENTCL_WT` wait for a person.

## 2026-11-09 07:09
- S056–S060 entered and read twice (block 4 of the second reading list): the C–H activation of soybean
  lipoxygenase-1 in three double mutants of its substrate pocket, in mutants of the surface residue Y317 and of
  S749, under hydrostatic pressure up to 1034 bar, and in the network residues I552 and V750, and of the
  lipoxygenase of Magnaporthe oryzae with and without its sugar chains: 29 isotope effects and 23 temperature
  series, all `verified`, with 8 new enzyme rows and 8 steps. Both readings agree in every number and sign. Every
  paper of this block defines ΔEa as Ea(D) − Ea(H), the direction of this database. The second reading also entered
  the recollected wild type of S059, whose four values are identical to S057; it is left out, so the measurement is
  counted once. The wild-type row of S060 is entered but flagged, because the paper's text credits its values to an
  earlier paper. See `curation/2026-11-09_second_reading_S056-S060/`.

## 2026-11-09 06:27
- S051–S055 entered and read twice (block 3 of the second reading list): the hydride transfer of DHFR from the
  deep-sea bacterium Moritella profunda and from Geobacillus stearothermophilus with six variants (L20M, A104Q,
  L20M/A104Q, P122E, P129D, P122E/P129D), of E. coli and human DHFR at five temperatures from 5 to 45 °C, and of
  recombinant Candida boidinii FDH and its variants V123A and V123G: 19 isotope effects and 12 temperature series,
  all `verified`, with 11 new enzyme rows and 11 steps. Both readings agree in every number and sign. The
  recombinant FDH has its own row (`FDH_CANBO_REC`), apart from the commercial enzyme. The second reading also
  entered two α-secondary KIEs of S051 that are averages over temperature; they are left out. S055 credits its
  wild-type values to the wrong reference; see `curation/2026-11-09_second_reading_S051-S055/`.

## 2026-11-08 20:10
- S046–S050 entered and read twice (block 2 of the second reading list): the hydride transfer of E. coli TS N177S
  and N177D, of E. coli DHFR I14A and the heavy (13C, 15N, 2H) E. coli DHFR, and of human DHFR M53W, S145V, their
  double mutant, F32M, F32L, F32L/PP26N/PEKN62G, Δ62-PEKN and Δ26-PPLR/Δ62-PEKN: 11 isotope effects and 13
  temperature series, all `verified`, with 12 new enzyme rows and 12 steps. Both readings agree in every number and
  sign. The wild-type values the papers print come from earlier work and are not entered; the human ones equal
  T0078 (S037). S050 prints F32L parameters that cannot both be right, and S048 and S050 print their Arrhenius
  equations with the opposite sign; see `curation/2026-11-08_second_reading_S046-S050/`.

## 2026-11-08 18:06
- `README.md` links *tunnelling informatics* to its definition page,
  https://sectio-aurea-q.github.io/tunnelling-informatics.html. No data changed.

## 2026-11-08 17:13
- S041–S045 entered and read twice (block 1 of the second reading list, thymidylate synthase): the proton
  abstraction of E. coli TS (wild type H/T and D/T, Y94F, Y209W, R166K) and the hydride transfer and proton
  abstraction of human TS: 7 temperature series, all `verified`, with 2 new enzyme rows and 4 steps. Both readings
  agree in every number and sign. The second reading also entered the single KIEs of S045 Table 2 and one value
  from its text; they are left out, since the paper states no temperature for them. See
  `curation/2026-11-08_second_reading_S041-S045/`.

## 2026-11-08 15:02
- S039–S040 entered and read twice: E. coli thymidylate synthase Y209W (intrinsic H/T Arrhenius parameters of the
  hydride transfer, 5–35 °C) and the wild type with 50 mM MgCl2 (Dkcat and intrinsic Dk at 25 °C, intrinsic H/T
  Arrhenius parameters): 2 isotope effects and 2 temperature series, all `verified`, with 1 new enzyme variant and
  2 steps. Both readings agree in every number; they differ only in whether the Dkcat with Mg2+, which the source
  finds equal to the intrinsic KIE, is `observed` or `intrinsic` (kept `observed`). The wild-type row now names the
  PDB entries of S040. See `curation/2026-11-08_second_reading_S039-S040/`.

## 2026-11-08 02:54
- S034–S038 entered and read twice: E. coli DHFR distal and double mutants (W133F, F125M, G121V/F125M, M42W/F125M,
  I14A/G121V; intrinsic H/T Arrhenius parameters), E. coli DHFR at pH 7.0 and the humanized mutants N23PP and
  N23PP/G51PEKN, native and heavy human DHFR, and soybean LOX-1 with ten variants (Dkcat and Dkcat/Km at 10 and
  40 °C, solvent isotope effects): 56 isotope effects and 9 temperature series, all `verified`, with 19 new enzyme
  variants and 19 steps. Both readings agree in every number and category. The second reading added the PDB entry
  4GH8 of N23PP/G51PEKN and seven wild-type entries of soybean LOX-1. SCHEMA.md: heavy-enzyme effects are not
  entered. See `curation/2026-11-07_second_reading_S034-S038/`.

## 2026-11-07 21:54
- S029–S033 entered and read twice: morphinone reductase at 1 bar and 2 kbar (Eyring series under pressure), the
  glucose dehydrogenase of Bacillus megaterium (commercial enzyme, no accession), ht-ADH W87F, W87L, W87A and Y25A
  and ps-ADH A25Y (Dkcat from 5 to 52 °C), half-heavy and heavy formate dehydrogenase (intrinsic H/T ΔEa) and four
  plant lipoxygenases, among them a wild-type row for soybean LOX-1: 28 isotope effects and 9 temperature series,
  all `verified`, with 12 new enzyme variants and 12 steps. The second reading added the D(kcat/KM) of soybean LOX-1,
  removed a pH the source does not state for S031 and set the range of the BmGDH series. `MR_PSEPU_WT` gains the PDB
  entries 1GWJ and 2R14, and the acceptor of its reductive half-reaction becomes FMN N5, as S029 names it.
  SCHEMA.md: conventions for EC numbers and isotope-labelled proteins written down.
  See `curation/2026-11-07_second_reading_S029-S033/`.

## 2026-11-07 21:01
- S024–S028 entered and read twice: nitroalkane oxidase (Fusarium oxysporum; proton abstraction from nitroethane),
  the aromatic amino acid hydroxylases (rat PheH and Δ117PheH, rat TyrH, rabbit TrpH102–416; benzylic H-atom
  abstraction, intrinsic primary and α-secondary effects), formate dehydrogenase (Candida boidinii; intrinsic H/T,
  H/D and D/T temperature dependence), the cyanobacterial lipoxygenase NspLOX (wild type, I219A) and soybean
  lipoxygenase-1 L546A/L754A at six temperatures: 25 isotope effects and 11 temperature series, all `verified`, with
  8 new enzyme variants and 8 steps. After the second reading the CD3 isotope effects of S025 count as
  `noncompetitive`, and rat PheH and TyrH list only PDB entries of the same construct; a later paper of the same group
  shows that S026 used a commercial FDH of unknown sequence, so no PDB entry is assigned. SCHEMA.md: conventions for
  truncated constructs written down. See `curation/2026-11-07_second_reading_S024-S028/`.

## 2026-11-07 20:02
- S019–S023 entered and read twice: E. coli DHFR (wild type, G121V; pre-steady state and pH 9.5), E. coli
  thymidylate synthase (wild type, Y94F; proton abstraction and hydride transfer), glutamate mutase (GlmES fusion;
  H-atom transfer), four protochlorophyllide oxidoreductases (hydride transfer and solvent isotope effects) and
  phosphite dehydrogenase (17X, T104S, T104A, T104G): 45 isotope effects and 24 temperature series, all
  `verified`, with 12 new enzyme variants and 17 steps. The second reading corrected the organism of the glutamate
  mutase (Clostridium tetanomorphum) and added PDB entries of the PORs and of 17X-PTDH. SCHEMA.md: conventions for
  `quantity` of intrinsic values, intramolecular competition and wild-type PDB entries written down.
  See `curation/2026-11-07_second_reading_S019-S023/`.

## 2026-11-07 18:43
- S014–S018 entered and read twice: five open-access papers on E. coli DHFR (M42W; I14V, I14G), soybean
  lipoxygenase-1 (L546A/I553A; L546A/L754A) and ht-ADH (L176V, L176A, L176G, L176Δ, V260A): 8 isotope effects and
  11 temperature series, all `verified`, with 10 new enzyme variants and their steps. The second reading found the
  PDB entries 4QLG and 4QLF of I14V and I14G, which the first reading had missed.
  See `curation/2026-11-07_second_reading_S014-S018/`.

## 2026-11-07 13:41
- Second check of 7 enzyme rows (`ai-2`): UniProt, EC, organism and variant agree in all 7; `SLO1_SOYBN_I553G` gains
  PDB 5TQP; notes on the TMADH residue numbering and the E. coli strain. `MR_PSEPU_WT` and `PETNR_ENTCL_WT` stay
  `single` until a person checks them. SCHEMA.md: rules for `variant` and `pdb` made precise.
  See `curation/2026-11-07_second_check_enzymes/`.

## 2026-11-07 12:45
- S013 (Wang et al. 2006, E. coli DHFR G121V) entered and read twice: 5 isotope effects and 3 temperature series,
  all `verified`. See `curation/2026-11-07_second_reading_S013/`.

## 2026-11-06
- Database set up: schema, curation rules, validator, licences, reading list.
- S002, S006, S007 and S009 entered and read twice: 20 isotope effects and 12 temperature series, all `verified`.
  See `curation/2026-11-06_second_reading/`.
