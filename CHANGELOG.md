# Changelog

What changed in MEG-NEN, newest first. Times are Central European Time. Every second reading, comparison and
decision is kept in `curation/`.

## 2026-11-12 07:22

- First rows under rule 4a: 50 isotope effects from tables of supporting information, M0298–M0347, all read twice
  and `verified` (both readings agree on all 50; no person has checked them).
  - S026 (formate dehydrogenase, doi:10.1021/ja902120t), SI Tables S2 and S3: observed H/T and D/T and intrinsic
    H/T, H/D and D/T at 5, 15, 25, 35 and 45 °C (25 rows).
  - S014 (DHFR M42W, doi:10.1098/rstb.2006.1871), SI Tables 1 and 2: the same quantities at the same temperatures (25 rows).
  - Counts: 347 isotope effects, of which 297 are printed in the articles themselves and 50 in supporting information.
  - Series T0016–T0018 and T0056–T0058: `notes` now say that the per-temperature values were read and where they are;
    `n_temperatures` set to 5 from the supporting tables. No value, error or Arrhenius parameter changes.
  - One printed value is entered with a remark: S026, Table S3, 5 °C, intrinsic H/D 3.14 (see
    `curation/2026-11-12_si_reading_S014_S026/resolution.md`, point 5).
  - Record of both readings, their comparison and the decisions: `curation/2026-11-12_si_reading_S014_S026/`.

## 2026-11-12 07:05

- Rule change, no value added or changed. `CURATION.md` rule 4a: a value printed in a table of a source's
  supporting information may now be entered, read twice like any other value, with `location` beginning
  `SI:` and `notes` beginning `supporting information`; such rows are counted separately. Values that can
  only be read off a plot stay out, in the supporting information as in the article. `SCHEMA.md`: the
  `location` field names the `SI:` prefix. Versions 1 and 2 of the data note describe the collection
  before this rule; no row has been entered under it yet.

## 2026-11-11 10:45

- Corrections after two referee readings of version 2 of the data note and of the record of the sample check.
  No value, error or parameter changes.
  - `curation/2026-11-11_person_check/report.md` rewritten where it was inexact: the sample is stratified by
    table (30 isotope effects, then 17 series, one generator), and the code of the draw is given; the ten recorded
    rows were drawn from a pool of 28 rows whose PubMed Central page the model had already located, not from all
    rows free to read; the person's comparison was made on the copies from which the values had been read, which
    for 17 of the 47 rows are author manuscripts, so "against the published articles" was too strong; the 36 rows
    without a row-by-row record are counted as unrecorded, and the check does not discharge rule 3 for a numbered
    release; the statement on the error rate names its limits; one third reading (M0017) had been marked ambiguous
    by the reader. `sample.csv` gains columns for the table, the kind of source copy, the pool and the kind of
    record. `author_statements.md` holds the author's own words.
  - Two text fields: the `location` of M0017 names the row of Table I (pH 9.5), which the third reading showed
    was needed to find the value; the `notes` of M0131 no longer say that no person has checked the row.
  - `README.md`, `CURATION.md` (rule 3) and `CITATION.cff`: the wording on the sample check follows the report;
    the DOI given for the data note is the one for all versions (10.5281/zenodo.24116484).
  - The 09:50 entry below said the sample was "checked against the published articles by the author"; read it
    with these corrections.

## 2026-11-11 09:50

- **First sample check under rule 3.** A random sample of 47 rows (30 isotope effects, 17 temperature series;
  46 of them `verified`, 10.0 % of the verified rows) was read a third time by the model, blind to the entered
  values, on 10 November, and checked against the published articles by the author on 11 November. No discrepancy
  was found and no row was changed. The record, with what the check covered, what it did not, and for which rows
  a row-by-row record exists, is `curation/2026-11-11_person_check/` (`report.md`, `sample.csv`). `CURATION.md`,
  rule 3, and `README.md` point to it.
- `README.md`: the status line names the data note (doi:10.5281/zenodo.24116485); a section on how to cite;
  the paragraph on `seed/` no longer says that the table is withheld, because it lies in this repository: it says
  that the table is kept only to show where the reading list came from and is not part of the data.
- `CITATION.cff` added.
- `TIMESTAMPS.md` lists the 18:08 archive of 10 November.

## 2026-11-10 18:08

- Corrections from a third referee reading, of the revised note and the 10:59 archive. None changes an entered
  value or a count of rows.
  - `SCHEMA.md` gives the three cases of
    `kind` as rule 5 does; rule 5 counted 22 rows of its last case without the source's statement, and counts 20,
    because M0024 and M0025 (S013) record a correction for the commitment and so belong to the case added today;
    the five read-once rows say "not a blind second reading" where they said "independent"; `as_printed` of the
    S008 and S011 series quotes the print with ellipses and no longer reorders it; T0167 says that its conditions
    are those stated for 25 °C; the note of `YADH_YEAST_WT` says which fields are empty; the comment in
    `tools/validate.py` names the 1 K margin the code has always used.
  - `TIMESTAMPS.md` lists the 10:59 archive.

## 2026-11-10 10:59

- Corrections from two referee readings of the note and of the 10:44 archive, made the same day. They change which
  of the rows read this morning are entered; they change no number that was read.
  - **Four rows of S001 are not entered.** The 10:45 entry below had entered the WT-SLO and Leu546→Ala rows of
    Table 1 of Knapp, Rickert and Klinman and held them at `single`. Footnote e of that table cites Rickert &
    Klinman, Biochemistry 1999, 38, 12218 for exactly these two rows, the Introduction gives the wild-type KIE of
    81 with the same citation, and the Methods say the Leu546→Ala data appeared in that paper. Rule 1 leaves such
    rows out, and the collection had applied it to the same kind of citation mark before (S027, S041–S045). Holding
    the rows was the exception, and rule 1 has none. The rows are removed; the earlier paper is added to
    `sources/first_sources.csv` as S066, not yet obtained. The reading list now holds 66 papers.
  - **Rows renumbered.** With those four gone, the rows of this morning are M0284–M0297 and T0154–T0167. The
    numbers M0284–M0299 and T0154–T0169 of the 10:44 archive were never released and are not those of the
    collection.
  - **Yeast alcohol dehydrogenase.** `YADH_YEAST_WT` no longer carries a species, an accession or an EC number: S012
    names none. The second reader's presumption (S. cerevisiae ADH1, P00330) is in `notes`. The row is `verified`,
    since both readings agree on what the source says.
  - **T0167** (S012, the H/D series): `pH` is empty; the source states pH 8.5 for the 25 °C tables only.
  - **`as_printed`** of twelve of the new rows now follows the print where the first reading had abbreviated or
    reordered it (S001 series, S008 series, S010 Table 2, S011 values).
  - **Calculated values are marked.** M0286 and M0291 (S008) are effects the source calculates from its H/T and D/T
    measurements; `notes` now begin "calculated by the source, not measured".
  - **S010 Table 2** is an Arrhenius fit reported as enthalpies of activation, not an Eyring analysis; the notes of
    T0163 and T0164 say so.
  - **`CURATION.md`.** Rule 2 is headed "Two readings, the second blind" and says that blind is not independent.
    Rule 4 says what is done with individual experiments printed beside their average, with calculated predictions
    and with calculated effects. Rule 5 names a third case of `intrinsic`: a value the source reports as corrected
    for the commitment (M0289, M0290). Rules 10 and 11 give their counts out of 167 series. The closing paragraph
    says that the convention check admits a temperature within 1 K of the fitted range and does not match on
    `kind`.
  - **`README.md`, `SCHEMA.md`.** Both said that whether a step counts as tunnelling is computed from the data by
    code. No such code exists and rule 7 says none is computed; both now say that. "Independent" readings are now
    called blind in both files. `README.md`: "under construction".
  - **`TIMESTAMPS.md`** speaks of working archives, not release archives, and lists the 10:44 archive.
  - **`sources/first_sources.csv`**: the five papers read today say how they were obtained.
  - Record: `curation/2026-11-10_second_reading_S001_S008_S010-S012/resolution.md`, rewritten with these decisions.
- Counts after these changes: the reading list holds 66 papers, of which 62 have been read; S003, S004, S005 and
  S066 are closed. 297 isotope effects, 294 `verified` and 3 `single`; 167 temperature series, 165 `verified` and
  2 `single`; 97 observed and 70 intrinsic among the series; 122 rows `intrinsic` in all, 99 of them competitive.
  115 of 117 enzyme rows are `verified`. `tools/validate.py` compares 64 series/value pairs; all agree within a
  factor of 3.

## 2026-11-10 10:45

- (Row numbers, counts and the four held rows in this entry were superseded the same day; see the entry above.)
- S001, S008, S010, S011 and S012 entered and read twice: five of the eight papers that the reading list marked as
  closed. Copies of the published articles reached the author on 10 November 2026 from the offices of two of the
  corresponding authors; `pdf_in_hand` is now `yes` for these five. They are the temperature study of soybean
  lipoxygenase-1 and three mutants by Knapp, Rickert and Klinman (S001), the intrinsic primary and the secondary
  effects of E. coli dihydrofolate reductase (S008), the thermophilic alcohol dehydrogenase above and below its
  30 °C transition (S010), the hydride transfer of E. coli thymidylate synthase (S011), and Cha, Murray and
  Klinman, *Hydrogen Tunneling in Enzyme Reactions*, on yeast alcohol dehydrogenase (S012), which is a scan
  without a text layer and was read from page images by both readers. 16 isotope effects (M0284–M0299) and 16
  temperature series (T0154–T0169).
- Both readings agree in every value, error, prefactor ratio, ΔEa, temperature, pH, effect type, isotope pair,
  quantity, method and kind. Three differences were settled against the sources: the fourteen individual
  experiments of S012 Tables 2 and 3, which the second reading had entered beside their printed averages, are
  left out and listed in `notes`; the intrinsic series of S011 cover 5–40 °C at four temperatures, as the Results
  and the axis of Fig. 2 say, not 5–45 °C as the Abstract does; and the activation enthalpies of S010 Table 2 are
  not put into `Ea_light_kcal`. Record: `curation/2026-11-10_second_reading_S001_S008_S010-S012/`.
- Four of the new rows are held at `single` on purpose although both readings agree: M0284, M0285, T0154 and
  T0155, the WT-SLO and Leu546→Ala rows of S001 Table 1. A footnote credits them to Rickert & Klinman,
  Biochemistry 1999, 38, 12218, which is not among the sources and has not been read; under rule 1 a person is
  to decide whether they stay.
- Two enzymes are new: `HTADH_GEOSE_WT` (`verified`) and `YADH_YEAST_WT`, held at `single` because S012 names
  neither species nor isozyme and the assignment to P00330 is not a statement of the source. Two steps are new.
- Counts after these changes: the reading list holds 65 papers, of which 62 have been read; S003, S004 and S005
  are still closed. 299 isotope effects, 294 `verified`; 169 temperature series, 165 `verified`; 99 observed and
  70 intrinsic among the series; 122 rows `intrinsic` in all, 99 of them competitive. 114 of 117 enzyme rows are
  `verified`. `tools/validate.py` now compares 66 series/value pairs for the sign and unit convention; all agree
  within a factor of 3. `CURATION.md` rules 10 and 11 give their counts out of 169 series; the counts themselves,
  15 and 46, are unchanged.
- `TIMESTAMPS.md`: the proofs of the 17:36, 17:38 and 21:27 archives of 9 November are confirmed and listed
  (Bitcoin blocks 975200, 975200 and 975221).

## 2026-11-09 21:27

- Corrections from a third referee reading, of the note together with the archive. None changes an entered value.
  - `data/enzymes.csv`, `CPA2E_THEAT_WT`: the row said "the curator confirmed why" of a sequence comparison.
    That is the pattern rule 3 was written for, in a file rule 3 does not reach, and the same pattern was
    already removed from `MR_PSEPU_WT` in the 17:36 pass and missed here. The row no longer names an actor.
  - `CURATION.md` rule 8: the papers stay with **the author**, not "the curator". The word was doing two
    jobs in the same file - the model in rule 3, the person in rule 8. Rule 8 now says which is which.
  - `README.md`: the same correction for the seed table.
  - `data/temperature.csv`, T0084: `as_printed` carried U+27C2 PERPENDICULAR where the source prints a
    multiplication sign. One wrong character in 436 verbatim fields, in the one field whose whole purpose
    is to reproduce what the source printed.
- Checked and not changed: the claim in `CHANGELOG.md` of 14:06 that the sign check was tested by reversing
  the sign of T0011. It does catch it, but T0011/M0010 is the pair whose predicted and printed values
  already differ most of all 59, so that is the easiest case for the check and not evidence that it catches
  a small error. The note says as much; this entry records it here too.

## 2026-11-09 17:38

- `TIMESTAMPS.md`: the proofs of the 13:30 and 14:06 archives are confirmed, both in Bitcoin block 975184,
  and the 17:36 archive is listed. The note on pending proofs now says that a cell reading `pending` was
  pending when the file was written and that `ots upgrade` fetches the block, so the table does not go
  stale as proofs confirm. The archive that carries this file cannot list its own digest, which the file
  states; the digest is in the data note that cites the archive.

## 2026-11-09 17:36

- Changes from a third referee reading, of the note together with the archive. None changes an entered value.
  - `CURATION.md` rule 3 now says what *the curator* means in the records under `curation/`. Those records
    attribute some checks to the curator - a sequence compared, an equation or a scheme read from an image,
    a PDB entry looked up again. That work was the model's, done outside the two blind readings. It is a
    third machine look, not a check by a person, and it does not make a row `verified` on its own. Where a
    person is meant, these files now say so. Nothing in the records was rewritten; the term is defined.
  - `CURATION.md` rule 4 now states the collection's scope, which until now stood only in the resolution
    record of one block: isotope effects on rate constants and on Arrhenius or Eyring parameters and nothing
    else. An isotope effect on another quantity, such as an activation volume or a pressure derivative, has
    no field here and is not entered.
  - `CURATION.md` rule 10: the clause about a conversion from kJ/mol asked `notes` to give the printed value
    and the conversion. Only 3 of the 35 rows concerned do that, so the rule was wrong. `as_printed` keeps
    the printed number with the source's own unit, so every conversion can be recomputed from the row; the
    rule now says that instead. All 35 conversions were checked against `as_printed` and are correct.
  - `CURATION.md` rule 10 also said `notes` record that a direction was *assumed*. The 15 rows concerned
    write "read as heavy - light"; the rule now uses the wording the rows use.
  - `CURATION.md` rule 11 asked `notes` to record a missing fitted temperature range. Only 5 of the 46 rows
    concerned do, and 3 say nothing about it, so the rule was wrong. It now says what is true and is worth
    saying: `T_min_K` and `T_max_K` are left empty rather than guessed.
  - `data/enzymes.csv`, `MR_PSEPU_WT`: the row said the first reading confirmed the two PDB entries by
    sequence, while the resolution record of block S029-S033 attributes that to the curator. The row no
    longer names an actor, since the two statements cannot both be right and the record is the older one.
  - `data/LICENSE.md`: `TIMESTAMPS.md` added to the list of documentation the licence covers.
## 2026-11-09 14:06

- Changes from two independent referee readings of the draft data note. None of them changes an entered value.
  - `CURATION.md` rule 2: `single` now covers both cases that occur — a row only one reading produced, and a
    row held at `single` on purpose until a person has checked it — and the rule states that every reading
    so far, and every settlement of a difference between two readings, is the work of the model.
  - `CURATION.md` rule 7 rewritten. It said that whether a step counts as tunnelling "is computed from the
    data by documented rules". No such label exists in the database and none is computed; the rule now says
    so, and says that deciding what the measurements can determine is the work this collection serves rather
    than an input to it.
  - `CURATION.md` rule 10, new: the sign and unit convention, and how each paper's own convention is
    established before a value is entered. This was practice from the start and stood only in the draft note.
  - `CURATION.md` rule 11, new: a single-temperature value is not entered without its temperature.
    `tools/validate.py` has enforced this from the start; the rule was not written down.
  - `tools/validate.py` now checks the sign and unit convention against the data: where a series and a
    single-temperature value cover the same step, isotope pair, effect type, quantity and method in the same
    paper, and the value's temperature lies inside the series' fitted range, the series must reproduce the
    value through KIE = (A_light/A_heavy) exp(dEa/RT). There are 59 such pairs; all 59 agree within a factor
    of three and the median ratio is 1.00. The check was tested by reversing the sign of T0011 on purpose,
    which it caught.
  - `TIMESTAMPS.md`, new: the SHA-256 digest and Bitcoin block of every stamped archive, with a note that
    stamping began on 9 November 2026 and that the eleven archives of 6 to 8 November carry no proof.
  - The five `single` values M0131, M0282, M0283, T0152 and T0153 now carry `checked_by` ai-1, which the
    resolution record of their block already stated, and their notes name the first reading as the checker.
    Four of them said "the curator", which can be read as a person; no person has checked any row.
  - The two `single` enzyme rows now say why each is single: morphinone reductase was read a second time and
    its difference settled, but its PDB entries were identified from sequence rather than read from the
    paper; pentaerythritol tetranitrate reductase was never read a second time.
  - `README.md`: the quoted wording stays with its rightsholders, not "its publishers" --- the same
    correction already made in `data/LICENSE.md`; `TIMESTAMPS.md` added to the contents table.
  - `SCHEMA.md`: the Arrhenius pre-factor ratios are named as apparent, since a tunnelling correction, if
    any, is absorbed in them; `location` is described as it is used, including a page or a figure legend.
- The OpenTimestamps proofs of the 12:26 and 13:06 archives are now confirmed, in Bitcoin blocks 975172 and
  975173. The proof of the 13:30 archive is still pending.
## 2026-11-09 13:30

- Seven corrections from the further reviews of the draft data note, none of them in an entered value:
  - `CURATION.md` rule 1 now states what until now stood only in the draft note: a value a paper attributes to
    other work is not entered, and where a paper reprints such a value in its own table without attribution, or
    forms an isotope effect from a rate constant published elsewhere, the credit is recorded in `notes`.
  - `CURATION.md` rule 2: the three statuses restated. `verified` covers a row both readings produced where a
    difference between them was settled against the source, which is the case for 57 of the 431 rows read twice;
    the earlier wording said `verified` only where both readings agree, which the data contradicted. `single`
    now also names the case of a check made by the curator rather than by a second independent reading.
  - `CURATION.md` rule 4 now also states that a value appearing only in supporting information is not entered.
  - M0131: the note said the same thing twice in two wordings; merged into one clause.
  - T0011: the settlement of the second reading, reversed by the re-read of 9 November, is marked as superseded,
    so that it can no longer be read as the decision in force.
  - `data/LICENSE.md`: the quoted wording remains with its rightsholders, not with "their publishers", and no
    legal doctrine is asserted over it.
  - `README.md`: `seed/` marked in the contents table as not part of a release, as the text already said.
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
