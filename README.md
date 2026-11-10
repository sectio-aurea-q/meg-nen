# MEG-NEN

A curated database of measured hydrogen isotope effects in enzymes: kinetic isotope effects
and their temperature dependence, each value traced to the table or page of its primary
source. It is the data basis of
[tunnelling informatics](https://sectio-aurea-q.github.io/tunnelling-informatics.html):
deciding from open data and stated rules what the measurements say about hydrogen tunnelling
in enzymes.

**Status:** under construction, no release yet.

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
| `TIMESTAMPS.md` | the digest and Bitcoin block of each stamped working archive |
| `seed/` | the old, unchecked MEG-APSU table, used only to find papers; not part of a release |
| `tools/validate.py` | checks every row |

`SCHEMA.md` describes every field, `CURATION.md` how a value gets in.

## Principles

- Every number carries its DOI, its place in the source and the number as printed.
- Two readings, the second blind to the first, before a value counts as verified. Both are
  machine readings by the same model; blind is not independent (see `CURATION.md`, rule 2).
- Whether a step counts as tunnelling is not stored and not computed here (`CURATION.md`, rule 7).

## Check

```
python3 tools/validate.py
```

## Not part of the release

`seed/` holds the old, unchecked MEG-APSU table. It only said which papers to read; none of its numbers
enters `data/` without being read again in the source, and its own figures are not checked against any
source. It stays with the author and is not released. The reading list that replaced it, with checked
DOIs, is `sources/first_sources.csv`.

## License

Curation (`data/`, `sources/`, `curation/` and the documentation): CC BY 4.0, see
[`data/LICENSE.md`](data/LICENSE.md). The wording quoted from the primary sources in `as_printed`,
`notes` and `conditions` is excluded and stays with its rightsholders.
Code (`tools/`): AGPL-3.0, as MEG-APSU, see [`LICENSE`](LICENSE).

## Author

Sabrina Hackfort (MEG)
