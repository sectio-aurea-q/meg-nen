#!/usr/bin/env python3
"""Checks the four data tables against SCHEMA.md. Exit code 0 means every row passes."""
import csv, math, re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOI = re.compile(r'^10\.\d{4,9}/\S+$')

HEADERS = {
    'enzymes.csv': 'enzyme_id,name,ec,organism,uniprot,variant,pdb,status,notes',
    'steps.csv': 'step_id,enzyme_id,substrate,donor,acceptor,transfer,status,notes',
    'measurements.csv': 'meas_id,step_id,labelled_position,kie_type,isotopes,quantity,method,kind,'
                        'value,error,temperature_K,pH,conditions,doi,location,as_printed,'
                        'extracted_by,checked_by,status,notes',
    'temperature.csv': 'temp_id,step_id,labelled_position,kie_type,isotopes,quantity,method,kind,'
                       'T_min_K,T_max_K,n_temperatures,AH_AX,AH_AX_error,dEa_kcal,dEa_error,'
                       'Ea_light_kcal,Ea_light_error,pH,conditions,doi,location,as_printed,'
                       'extracted_by,checked_by,status,notes',
}
ALLOWED = {
    'status': {'verified', 'single', 'disputed'},
    'transfer': {'H_atom', 'hydride', 'proton', 'PCET', 'unknown'},
    'kie_type': {'primary', 'secondary', 'solvent', 'other'},
    'isotopes': {'H/D', 'H/T', 'D/T'},
    'quantity': {'kcat', 'kcat/KM', 'single_turnover', 'other'},
    'method': {'noncompetitive', 'competitive', 'other'},
    'kind': {'observed', 'intrinsic'},
}

errors = []


def err(table, row, msg):
    errors.append(f'{table} row {row}: {msg}')


def load(name):
    with open(ROOT / 'data' / name, newline='', encoding='utf-8') as f:
        if f.readline().strip() != HEADERS[name]:
            err(name, 1, 'header differs from SCHEMA.md')
            return []
        f.seek(0)
        return list(csv.DictReader(f))


def allowed(table, i, r, *fields):
    for f in fields:
        if r[f] not in ALLOWED[f]:
            err(table, i, f'{f} {r[f]!r} is not one of {sorted(ALLOWED[f])}')


def number(table, i, r, field, lo=None, hi=None, required=False):
    v = r[field].strip()
    if not v:
        if required:
            err(table, i, f'{field} is empty')
        return None
    try:
        x = float(v)
    except ValueError:
        err(table, i, f'{field} is not a number: {v!r}')
        return None
    if lo is not None and x < lo:
        err(table, i, f'{field} = {v} is below {lo}')
    elif hi is not None and x > hi:
        err(table, i, f'{field} = {v} is above {hi}')
    return x


def unique(table, rows, key):
    seen = set()
    for i, r in enumerate(rows, 2):
        if not r[key].strip():
            err(table, i, f'{key} is empty')
        elif r[key] in seen:
            err(table, i, f'{key} {r[key]} appears twice')
        seen.add(r[key])
    return seen


def source(table, i, r):
    if not DOI.match(r['doi'].strip()):
        err(table, i, f'doi {r["doi"]!r} is not a DOI')
    for f in ('location', 'as_printed', 'extracted_by'):
        if not r[f].strip():
            err(table, i, f'{f} is empty')
    if len(r['as_printed'].split()) > 15:
        err(table, i, 'as_printed is longer than 15 words')
    if r['status'] == 'verified':
        first, second = r['extracted_by'].strip(), r['checked_by'].strip()
        if not second:
            err(table, i, 'verified, but there is no second reading (checked_by)')
        elif first == second:
            err(table, i, 'verified needs two different readers')


enzymes = load('enzymes.csv')
enzyme_ids = unique('enzymes.csv', enzymes, 'enzyme_id')
for i, r in enumerate(enzymes, 2):
    allowed('enzymes.csv', i, r, 'status')

steps = load('steps.csv')
step_ids = unique('steps.csv', steps, 'step_id')
for i, r in enumerate(steps, 2):
    allowed('steps.csv', i, r, 'transfer', 'status')
    if r['enzyme_id'] not in enzyme_ids:
        err('steps.csv', i, f'enzyme_id {r["enzyme_id"]!r} is not in enzymes.csv')

tables = {}
for name, key in (('measurements.csv', 'meas_id'), ('temperature.csv', 'temp_id')):
    rows = tables[name] = load(name)
    unique(name, rows, key)
    for i, r in enumerate(rows, 2):
        if r['step_id'] not in step_ids:
            err(name, i, f'step_id {r["step_id"]!r} is not in steps.csv')
        allowed(name, i, r, 'kie_type', 'isotopes', 'quantity', 'method', 'kind', 'status')
        source(name, i, r)
        number(name, i, r, 'pH', 0, 14)
        if name == 'measurements.csv':
            number(name, i, r, 'value', 0, required=True)
            number(name, i, r, 'error', 0)
            number(name, i, r, 'temperature_K', 200, 400, required=True)
        else:
            lo = number(name, i, r, 'T_min_K', 200, 400)
            hi = number(name, i, r, 'T_max_K', 200, 400)
            if (lo is None) != (hi is None):
                err(name, i, 'give both T_min_K and T_max_K, or neither')
            elif lo is not None and lo >= hi:
                err(name, i, 'T_min_K is not below T_max_K')
            n = number(name, i, r, 'n_temperatures', 2)
            if n is not None and n != int(n):
                err(name, i, 'n_temperatures is not a whole number')
            number(name, i, r, 'AH_AX', 0)
            number(name, i, r, 'dEa_kcal')
            number(name, i, r, 'Ea_light_kcal')
            for f in ('AH_AX_error', 'dEa_error', 'Ea_light_error'):
                number(name, i, r, f, 0)
            if not (r['AH_AX'].strip() or r['dEa_kcal'].strip()):
                err(name, i, 'neither AH_AX nor dEa_kcal is given')

# Sign and unit convention, checked against the data (CURATION.md rule 10).
# Where a temperature series and a single-temperature value cover the same step, isotope pair,
# effect type, quantity, method and kind (observed or intrinsic) in the same paper, and the value's temperature
# falls inside (or within 1 K of)
# the series' fitted range, the series must reproduce the value:
#     KIE = (A_light / A_heavy) * exp(dEa / RT),      dEa = Ea(heavy) - Ea(light).
# A sign slip inverts the exponential and a unit slip scales dEa by 4.184, so either shows up
# at once. Series and value come from different fits, so the test is deliberately loose.
R_KCAL = 1.98720425e-3  # kcal / (mol K)
TOLERANCE = 3.0
MATCH = ('step_id', 'isotopes', 'kie_type', 'quantity', 'method', 'kind', 'doi')


def num(value):
    try:
        return float(value)
    except ValueError:
        return None


checked = 0
for i, s in enumerate(tables['temperature.csv'], 2):
    a, d = num(s['AH_AX']), num(s['dEa_kcal'])
    lo, hi = num(s['T_min_K']), num(s['T_max_K'])
    if None in (a, d, lo, hi) or a <= 0:
        continue
    for m in tables['measurements.csv']:
        if any(m[f] != s[f] for f in MATCH):
            continue
        t, observed = num(m['temperature_K']), num(m['value'])
        if None in (t, observed) or observed <= 0 or not lo - 1 <= t <= hi + 1:
            continue
        checked += 1
        ratio = a * math.exp(d / (R_KCAL * t)) / observed
        if not 1 / TOLERANCE <= ratio <= TOLERANCE:
            err('temperature.csv', i,
                f'{s["temp_id"]} predicts {a * math.exp(d / (R_KCAL * t)):.3g} at '
                f'{t:.1f} K, but {m["meas_id"]} prints {observed:.3g} '
                f'(factor {ratio:.2f}); check the sign of dEa_kcal and its unit')

if errors:
    print('\n'.join(errors))
    print(f'\n{len(errors)} problem(s)')
    sys.exit(1)
print(f'all rows pass: {len(enzymes)} enzymes, {len(steps)} steps, '
      f'{len(tables["measurements.csv"])} isotope effects, '
      f'{len(tables["temperature.csv"])} temperature series')
print(f'sign and unit convention: {checked} series/value pairs agree within a factor '
      f'of {TOLERANCE:g}')
