# Sample check of 10 and 11 November 2026: a third machine reading and a comparison by a person

Rule 3 of `CURATION.md` asks that a person check a random sample of at least 10 % of the verified rows
against the sources before a release, and that the error rate found be published. This is a first check
of that kind. It was made on the state of the archive `MEG-NEN_2026-11-10_18-08.zip`
(SHA-256 `c0d84be55f002b63a79ef0453f2bae2ba40ae3557ad8fd3f65f48446c82c5b5e`). The rows are listed in
`sample.csv`; the author's own words are in `author_statements.md`. This account was written by the model
from the readings and from the author's messages.

It does not discharge rule 3 for a numbered release: only 11 of the 47 rows have a row-by-row record
(see below). Before a numbered release the sample check will be repeated with every row recorded.

## The sample

47 value rows, stratified by table: 30 of the 297 isotope effects and then 17 of the 167 temperature
series, drawn with one seeded generator from the identifiers of each table in sorted order:

    import random
    rng = random.Random(int("c0d84be55f002b63", 16))   # first 16 hex digits of the archive digest
    sample = rng.sample(sorted(meas_ids), 30) + rng.sample(sorted(temp_ids), 17)

Nobody chose the rows. The status of a row played no part, so one `single` row (M0131) is in the sample;
the other 46 are `verified`, 10.0 % of the 459 verified value rows. The 47 rows come from 31 of the 62
papers read. Enzyme and step rows were not sampled.

## Third machine reading (10 November 2026)

A fresh instance of the same model read the 47 values from the saved copies of the sources. It was given
the identifier, the source, the step, the labelled position, the type fields, the place in the source
and, for a single-temperature value, the temperature. It was not given the value, the error, the pH,
`as_printed` or `notes`. Because it was given the place, this reading tests the transcription at that
place and not whether the place is the right one.

Result: all 47 readings agree with the entered value and its error, for a series with the entered
Arrhenius or Eyring parameters and their errors, including the two rows the database converts from
kJ/mol to kcal/mol (T0042, T0103).

One reading was marked ambiguous by the reader: for M0017 the recorded place was "Table I" without a
row, the table has one value for each pH, and the reader, who did not have the pH, took the row from a
sentence of the running text. It is the entered one (pH 9.5). The `location` of M0017 now names the row.

For 26 of the rows (column `looked_up_on_pmc_page` in `sample.csv`) the reader had only text extracted
from the source, not the page itself. For these the model then looked up the table row or the sentence on
the article's PubMed Central page. That look was not blind. All 26 agree.

The reading pointed again to places where a row rests on a decision that `notes` already record:

- M0260, M0262 (S064): the table attaches 303 K to the kinetic parameters, not to the kH/kD column; the
  temperature of the ratio is inferred.
- M0110, M0116 (S031): the pH is stated for the standard assay only, so `pH` is empty.
- M0277 (S065): the table prints the value under pL 7.0, the running text quotes it with pL 7.5; the row
  follows the table.
- M0055 (S021): the column is headed "KH/KD (0 °C)"; the table does not say whether the value was measured
  at 0 °C or taken from the fit.
- T0115 (S057): the number of temperatures is printed as "7 to 8", so `n_temperatures` is empty.

## Comparison by a person (11 November 2026)

The person is the author, Sabrina Hackfort.

**Ten rows, recorded.** Ten rows were drawn at random from a pool of 28: the sample rows from the 17
sources whose PubMed Central page the model had already located (the 26 rows above and the two rows of
S013; column `pool_of_28`):

    rng2 = random.Random(int("c0d84be55f002b63"[::-1], 16))
    ten = rng2.sample(sorted(pool_ids), 10)

The pool was a matter of convenience and is not a random part of the sample: it leaves out the four
sample rows whose source is not on PubMed Central and 15 rows from PubMed Central sources the model had
not opened. On 11 November 2026, between about 08:10 and 09:15 CET, the author opened each of the ten
articles on PubMed Central, went to the place the model had named (table, row, column, search word) and
compared the printed number and its error with the entered value, which she could see. The comparison was
therefore not blind, and it was made on the copy from which the value had been read: for five of the ten
rows (M0023, T0020, T0053, T0055, T0067) that copy is an author manuscript, not the version of record.
All ten agree: T0020, T0053, T0055, T0059, T0067, M0023, M0057, M0116, M0142, M0150.

The record of these ten is the author's written confirmation after the comparison. She first entered her
answers in a local browser form, which did not keep them.

For M0150 she first reported "148 (4)". That is the first entry of the neighbouring row I538A (a rate
constant, kcat-H), not of the row I553A; the model's description of the place ("the third number") had
been ambiguous. She then copied both rows from the article. Row I553A reads "I553A 115 (3) 153 (3)
148 (5) 77 (2) 12 (1) 57 (2)". The entered value, 148 (5), agrees.

**One further row, recorded by the copied table row.** The copied row I553A contains the value of M0151,
12 (1), which agrees.

**36 rows, not recorded.** For the other 36 rows the author states that she looked the values up and
compared them as well, without noting "yes" or "no" for each row, and she reported no discrepancy. There
is no record of when she did so or from which copies. These rows should be counted as unrecorded.

## What was compared, and what was not

The printed value and its error; for a temperature series the printed Arrhenius or Eyring parameters and
their errors. Not compared: temperature, pH, the type fields (`kie_type`, `quantity`, `method`, `kind`),
the labelled position, and the enzyme and step rows. Because the place was supplied by the model, the
comparison tests the transcription at that place, not the choice of the place.

## Error rate

No discrepancy was found. If all 47 comparisons are taken at face value, none wrong in 47 excludes, at the
95 % level, a rate above about 6 % of rows whose entered value or error differs from what is printed at
the recorded place. The 11 recorded rows alone exclude only a rate above about 24 %. Neither figure covers
a value taken from the wrong place, any other field, or a misreading shared by the model and a reader who
was shown the model's value; and the 47 rows come from 31 papers, within which errors need not be
independent.

## Changes made

No value, error or parameter was changed. Two text fields were: the `location` of M0017 names the row of
the table, and the `notes` of M0131 no longer say that no person has checked the row but that it was in
this sample, among the rows without a record.
