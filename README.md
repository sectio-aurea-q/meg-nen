# MEG-NEN

A curated database of measured hydrogen isotope effects in enzymes: kinetic isotope effects
and their temperature dependence, each value traced to the table or page of its primary
source. It is the data basis of
[tunnelling informatics](https://sectio-aurea-q.github.io/tunnelling-informatics.html):
deciding from open data and stated rules what the measurements say about hydrogen tunnelling
in enzymes.

**Status:** under construction; no numbered release yet. The data note, in all its versions, is
[doi:10.5281/zenodo.24116484](https://doi.org/10.5281/zenodo.24116484); version 1 describes the state of
10 November 2026.

## Contents

| path | content |
|---|---|
| `data/enzymes.csv` | enzymes and variants |
| `data/steps.csv` | hydrogen-transfer steps |
| `data/measurements.csv` | isotope effects at one temperature |
| `data/temperature.csv` | temperature series (Arrhenius parameters) |
| `data/rates.csv` | rate constants of the light and the heavy isotope at one temperature (since 12 November 2026) |
| `sources/` | reading list with checked DOIs |
| `curation/` | each second reading, the comparison of both readings and the decisions taken; the sample check |
| `CHANGELOG.md` | what changed, with date and time |
| `TIMESTAMPS.md` | the digest and Bitcoin block of each stamped working archive |
| `seed/` | the old, unchecked MEG-APSU table, used only to find papers; not part of the data |
| `CITATION.cff` | how to cite |
| `tools/validate.py` | checks every row |

`SCHEMA.md` describes every field, `CURATION.md` how a value gets in.

## Principles

- Every number carries its DOI, its place in the source and the number as printed.
- Two readings, the second blind to the first, before a value counts as verified. Both are
  machine readings by the same model; blind is not independent (see `CURATION.md`, rule 2).
- A person checks a random sample of at least 10 % of the verified rows before a release. A first check of
  a sample of 47 rows, on 10 and 11 November 2026, found no discrepancy, but only 11 of the rows have a
  row-by-row record of the person's comparison; it will be repeated with every row recorded before a numbered
  release. What it covered and what it did not is in `curation/2026-11-11_person_check/report.md`.
- Whether a step counts as tunnelling is not stored and not computed here (`CURATION.md`, rule 7).

## Check

```
python3 tools/validate.py
```

## Not part of the data

`seed/` holds the old, unchecked MEG-APSU table. It only said which papers to read; none of its numbers
enters `data/` without being read again in the source, and its own figures are not checked against any
source. It is kept in this repository only to show where the reading list came from: it is not part of
the data, `tools/validate.py` does not read it, and its numbers should not be used or cited. The reading
list that replaced it, with checked DOIs, is `sources/first_sources.csv`.

## License

Curation (`data/`, `sources/`, `curation/` and the documentation): CC BY 4.0, see
[`data/LICENSE.md`](data/LICENSE.md). The wording quoted from the primary sources in `as_printed`,
`notes` and `conditions` is excluded and stays with its rightsholders.
Code (`tools/`): AGPL-3.0, as MEG-APSU, see [`LICENSE`](LICENSE).

## How to cite

Sabrina Hackfort (MEG), *MEG-NEN: a curated database of measured hydrogen isotope effects in enzymes — data
note and status*, Zenodo, 2026, [doi:10.5281/zenodo.24116484](https://doi.org/10.5281/zenodo.24116484)
(all versions; give the version you used).
Please cite the primary sources of the values you use as well. See `CITATION.cff`.

## Author

Sabrina Hackfort (MEG)
