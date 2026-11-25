#!/usr/bin/env python3
"""Search of every text field of measurements.csv and temperature.csv for the spellings of heavy water.
Writes hits.csv next to this file. Run from anywhere: python3 search.py
The decision column is filled by the rule below for solvent effects and by hand for every other hit
(DECISIONS); a hit without a decision stops the script."""
import csv, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE.parent.parent / 'data'
FIELDS = ('labelled_position', 'conditions', 'notes', 'as_printed', 'location')
TERMS = [
    r'D2O', r'D₂O', r'2H2O', r'²H₂O', r'²H2O', r'2H₂O', r'\[2H\]\s*water',
    r'[Dd]euterium oxide', r'[Hh]eavy water',
    r'[Dd]euterated (?:water|buffer|solvent|medium|solution)',
    r'(?<![A-Za-z0-9])p(?:D|2H|²H|L)(?![A-Za-z0-9])',     # pD, p2H, pL as words; not NADP2H
    r'[Ss]olvent isotope', r'[Pp]roton inventor',
]
PATTERN = re.compile('|'.join(TERMS))

# Every hit in a row that is not a solvent effect, decided by hand from the row itself.
DECISIONS = {
    'M0006': ('D2O', 'conditions: the light and the heavy coenzyme were both measured in D2O'),
    'M0271': ('D2O', 'labelled_position and conditions: the same reaction in MOPS-2H2O'),
    'M0009': ('', 'light reaction in H2O, heavy reaction in D2O: the solvent is part of the substitution '
                  '(kie_type other, double isotope effect)'),
}

out = []
for table, key in (('measurements.csv', 'meas_id'), ('temperature.csv', 'temp_id')):
    with open(DATA / table, newline='', encoding='utf-8') as f:
        for r in csv.DictReader(f):
            words = sorted({m.group(0) for field in FIELDS for m in PATTERN.finditer(r[field])})
            # Self-test of the word list: every solvent effect in the collection must be found by it.
            assert words or r['kie_type'] != 'solvent', f'{r[key]}: a solvent effect the word list does not find'
            if not words:
                continue
            where = [field for field in FIELDS if PATTERN.search(r[field])]
            if r['kie_type'] == 'solvent':
                value, why = '', 'solvent effect: heavy water is the isotope substitution itself'
            else:
                value, why = DECISIONS[r[key]]
            out.append((table, r[key], r['step_id'], r['kie_type'], ' / '.join(words), ' / '.join(where), value, why))

with open(HERE / 'hits.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f, lineterminator='\n')
    w.writerow(('table', 'id', 'step_id', 'kie_type', 'words_found', 'fields', 'heavy_solvent', 'decision'))
    w.writerows(out)
solvent = sum(1 for o in out if o[3] == 'solvent')
print(f'{len(out)} rows with a hit: {solvent} solvent effects, {len(out) - solvent} others '
      f'({", ".join(o[1] for o in out if o[3] != "solvent")}); filled: '
      f'{", ".join(o[1] for o in out if o[6])}')
