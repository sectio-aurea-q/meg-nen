# MEG-NEN

A curated database of measured hydrogen isotope effects in enzymes: kinetic isotope effects
and their temperature dependence, each value traced to the table or page of its primary
source. It is the data basis of
[tunnelling informatics](https://sectio-aurea-q.github.io/tunnelling-informatics.html):
deciding from open data and stated rules what the measurements say about hydrogen tunnelling
in enzymes.

**Status:** in construction, no release yet.

## Contents

| path | content |
|---|---|
| `data/enzymes.csv` | enzymes and variants |
| `data/steps.csv` | hydrogen-transfer steps |
| `data/measurements.csv` | isotope effects at one temperature |
| `data/temperature.csv` | temperature series (Arrhenius parameters) |
| `sources/` | reading list with checked DOIs |
| `curation/` | each second reading, the comparison of both readings and the decisions taken |
| `CHANGELOG.md` | what changed, with date and time |
| `seed/` | the old, unchecked MEG-APSU table, used only to find papers |
| `tools/validate.py` | checks every row |

`SCHEMA.md` describes every field, `CURATION.md` how a value gets in.

## Principles

- Every number carries its DOI, its place in the source and the number as printed.
- Two independent readings before a value counts as verified.
- Whether a step counts as tunnelling is not stored; it is computed from the data by
  documented rules.

## Check

```
python3 tools/validate.py
```

## Not part of the release

`seed/` holds the old, unchecked MEG-APSU table. It only said which papers to read; none of its numbers
enters `data/` without being read again in the source, and its own figures are not checked against any
source. It stays with the curator and is not released. The reading list that replaced it, with checked
DOIs, is `sources/first_sources.csv`.

## License

Curation (`data/`, `sources/`, `curation/` and the documentation): CC BY 4.0, see
[`data/LICENSE.md`](data/LICENSE.md). The wording quoted from the primary sources in `as_printed`,
`notes` and `conditions` is excluded and stays with its publishers.
Code (`tools/`): AGPL-3.0, as MEG-APSU, see [`LICENSE`](LICENSE).

## Author

Sabrina Hackfort (MEG)
