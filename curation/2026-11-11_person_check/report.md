# Sample check of 11 November 2026: a third machine reading and a check by a person

Rule 3 of `CURATION.md` asks that a person check a random sample of at least 10 % of the verified rows
against the sources before a release, and that the error rate found be published. This is the first such
check. It was made on the state of the archive `MEG-NEN_2026-11-10_18-08.zip`
(SHA-256 `c0d84be55f002b63a79ef0453f2bae2ba40ae3557ad8fd3f65f48446c82c5b5e`). The rows are listed in
`sample.csv`.

## The sample

47 rows: 30 of the 297 isotope effects and 17 of the 167 temperature series. They were drawn with
Python's `random.Random`, seeded with the first 16 hexadecimal digits of the archive digest above read as
an integer, by `random.sample` over the rows sorted by identifier, the isotope effects first. Nobody
chose the rows, and the draw can be repeated. 46 of the 47 rows are `verified` (10.0 % of the 459 verified
rows); the other one, M0131, is `single`.

## Third machine reading (10 November 2026)

A fresh instance of the model read the 47 values from the saved copies of the sources. It was given the
identifier, the source, the step, the labelled position, the type fields, the place in the source and, for
a single-temperature value, the temperature. It was not given the value, the error, the pH, `as_printed`
or `notes`. Its readings were then compared with the entered rows.

Result: all 47 agree with the entered value and its error, including the two rows the database converts
from kJ/mol to kcal/mol (T0042, T0103).

For 26 of the rows the reader had only text extracted from the source, not the page itself. For these the
model then looked up the table row or the sentence on the article's PubMed Central page. That look was
not blind. All 26 agree.

The reading turned up no error. It pointed again to places where a row rests on a decision that `notes`
already record:

- M0260, M0262 (S064): the table attaches 303 K to the kinetic parameters, not to the kH/kD column; the
  temperature of the ratio is inferred.
- M0110, M0116 (S031): the pH is stated for the standard assay only, so `pH` is empty.
- M0277 (S065): the table prints the value under pL 7.0, the running text quotes it with pL 7.5; the row
  follows the table.
- M0055 (S021): the column is headed "KH/KD (0 °C)"; the table does not say whether the value was measured
  at 0 °C or taken from the fit.
- T0115 (S057): the number of temperatures is printed as "7 to 8", so `n_temperatures` is empty.

## Check by a person (11 November 2026)

The author, Sabrina Hackfort, checked the 47 rows against the published articles.

**With a row-by-row record (11 rows).** Ten rows were drawn at random from the 28 rows of the sample
whose source is free to read on PubMed Central (the same generator, seeded with the same 16 digits in
reverse order). On 11 November 2026, between about 08:10 and 09:15 CET, the author opened each article on
PubMed Central, went to the place and compared the printed number and its error with the entered value.
The places (table, row, column, search word) were given to her by the model, and she could see the entered
value, so this check was not blind. All ten agree: T0020, T0053, T0055, T0059, T0067, M0023, M0057, M0116,
M0142, M0150.

For M0150 the author first reported "148 (4)". That is the first entry of the neighbouring row I538A
(a rate constant, kcat-H), not of the row I553A; the model's description of the place ("the third number")
had been ambiguous. She then copied the row I553A from the article: "I553A 115 (3) 153 (3) 148 (5) 77 (2)
12 (1) 57 (2)". The entered value, 148 (5), agrees. The same copied row contains the value of M0151,
12 (1), which therefore has a record as well.

The answers for the ten rows were first entered in a local browser form that did not keep them; the
author then confirmed the results in writing, row M0150 with the copied table rows.

**Without a row-by-row record (36 rows).** For the other 36 rows the author states that she looked the
values up and checked them as well, without noting "yes" or "no" for each row. She reported no
discrepancy. For these rows the only record is this statement.

## What was compared, and what was not

The printed value and its error, for a temperature series the printed Arrhenius or Eyring parameters and
their errors. Temperature, pH, the type fields (`kie_type`, `quantity`, `method`, `kind`), the labelled
position and the enzyme and step rows were not part of the person's check.

## Error rate

No discrepancy in 47 rows. With 47 rows and none wrong, the sample excludes an error rate above about
6 % at the 95 % level (rule of three) and says nothing finer than that. The limits above apply: the
person's check was not blind, and for 36 of the 47 rows it rests on the author's statement.

No row was changed as a result of this check.
