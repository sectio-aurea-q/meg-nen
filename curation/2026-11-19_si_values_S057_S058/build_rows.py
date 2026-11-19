#!/usr/bin/env python3
"""Builds the rows of measurements.csv and rates.csv from reading1.csv (identical to reading2.csv in every cell).
Run once, from the repository root: python3 curation/2026-11-19_si_values_S057_S058/build_rows.py"""
import csv, pathlib
HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE.parent.parent / 'data'
r1 = list(csv.DictReader(open(HERE / 'reading1.csv', encoding='utf-8')))
r2 = list(csv.DictReader(open(HERE / 'reading2.csv', encoding='utf-8')))
key = lambda r: (r['table'], r['variant'], r['pressure_bar'], r['temperature_printed'])
b = {key(r): r for r in r2}
F = ('kcatH', 'kcatH_err', 'kcatD', 'kcatD_err', 'Dkcat', 'Dkcat_err')
assert len(r1) == len(r2) == 107 and all(r[f].strip() == b[key(r)][f].strip() for r in r1 for f in F)

SRC = {
    'S058': dict(doi='10.1002/anie.201603592', lp_d='all H (perdeutero linoleic acid, D-LA; SI: Section 1.1)',
                 lp_h='unlabelled linoleic acid (H-LA)',
                 cond='0.1 M borate, pH 9.0 at 1 bar (the pH falls by about 0.3 up to about 1 kbar, neglected by the '
                      'source); steady state in a high-pressure cell, initial rates at 248 nm, concentrations '
                      'corrected for compression; kcat from Michaelis-Menten fits with H- and with D-linoleic acid',
                 et='not_stated', n='', file='NIHMS817928-supplement-Supporting_Information.docx from PMC5040518'),
    'S057': dict(doi='10.1021/acscentsci.7b00142', lp_d='all H (perdeuterated D31-LA; SI: Table S7 footnote b)',
                 lp_h='unlabelled linoleic acid (protio-LA; SI: Table S7 footnote a)',
                 cond='0.1 M sodium borate, pH 9.0; steady state, kcat from non-linear fits with protio-LA and with '
                      'D31-LA; rate constants not corrected for iron content (SI: Table S7 footnotes)',
                 et='se', n='3', file='oc7b00142_si_001.pdf from PMC5492416'),
}
STEP = {v: f'SLO1_SOYBN_{v}_LA' for v in ('WT', 'I553V', 'L546A', 'S749A', 'S749G', 'Y317S', 'Y317L', 'Y317F')}
UNIT = {('S3', 'H'): ('s-1', False), ('S3', 'D'): ('s-1', False), ('S4', 'H'): ('s-1', False), ('S4', 'D'): ('s-1', True),
        ('S5', 'H'): ('s-1', True), ('S5', 'D'): ('10-2 s-1', True), ('S7', 'H'): ('s-1', True), ('S7', 'D'): ('s-1', True)}
ODD = {('S5', 'L546A', '1', '293 K'): '7.17 / 0.0557 = 128.7', ('S5', 'L546A', '344', '293 K'): '7.07 / 0.0660 = 107.1'}

def kelvin(t):
    n, u = t.split()
    return f'{float(n) + (0.15 if u == "K" else 273.15):.2f}'

def where(r, block):
    if r['source'] == 'S058':
        return f"SI: Table {r['table']}, block {block}, row {r['pressure_bar']} bar, column {r['temperature_printed']}"
    return f"SI: Table {r['table']}, block {r['variant']}, row {r['temperature_printed'].split()[0]} °C, column {block}"

def load(name):
    with open(DATA / name, newline='', encoding='utf-8') as f:
        rd = csv.DictReader(f); return rd.fieldnames, list(rd)

mf, M = load('measurements.csv'); rf, R = load('rates.csv')
if 'pressure_bar' not in rf:
    i = rf.index('conditions') + 1; rf = rf[:i] + ['pressure_bar'] + rf[i:]
    for x in R: x['pressure_bar'] = ''
assert M[-1]['meas_id'] == 'M0520' and R[-1]['rate_id'] == 'R0044'
mi, ri = 520, 44
for r in r1:
    s = SRC[r['source']]; T = kelvin(r['temperature_printed']); mi += 1; mid = f'M{mi:04d}'
    tnote = 'temperature printed as ' + r['temperature_printed'].replace(' C', ' °C') + (' (the text gives 15 to 35 °C)' if r['source'] == 'S058' else '')
    note = f"supporting information; {tnote}; "
    note += ('the meaning of the parentheses is not stated' if s['et'] == 'not_stated' else 'mean ± s.e.m. of three measurements (SI, kinetics section)')
    if key(r) in ODD:
        note += f"; the printed rate constants of the same table give {ODD[key(r)]}, not the printed value; entered as printed"
    if r['source'] == 'S057' and r['temperature_printed'] == '30 C':
        note += '; Table 1 of the article prints the 30 °C value corrected for iron content as a separate number'
    ids = []
    for iso, v, e, lp in (('H', r['kcatH'], r['kcatH_err'], s['lp_h']), ('D', r['kcatD'], r['kcatD_err'], s['lp_d'])):
        ri += 1; rid = f'R{ri:04d}'; ids.append(rid); unit, printed = UNIT[(r['table'], iso)]
        block = f'kcat-{iso}' if r['source'] == 'S058' else f'kcat ({iso})'
        R.append(dict(rate_id=rid, step_id=STEP[r['variant']], labelled_position=lp, isotope=iso, quantity='kcat',
                      value=v, error=e, error_type=s['et'], n_measurements=s['n'], unit=unit, temperature_K=T, pH='9.0',
                      conditions=s['cond'], pressure_bar=r['pressure_bar'], doi=s['doi'], location=where(r, block),
                      as_printed=f'{v} ({e})', extracted_by='ai-1', checked_by='ai-2', status='verified',
                      notes=f"supporting information; {tnote}; " + ('' if printed else 'no unit is printed for this block, s-1 as in the other tables of the file; ')
                            + f"the isotope effect of the same cell is {mid}; file {s['file']}"))
    M.append(dict(meas_id=mid, step_id=STEP[r['variant']], labelled_position=s['lp_d'], kie_type='primary', isotopes='H/D',
                  quantity='kcat', method='noncompetitive', kind='observed', value=r['Dkcat'], error=r['Dkcat_err'],
                  error_type=s['et'], n_measurements=s['n'], temperature_K=T, pH='9.0', conditions=s['cond'],
                  pressure_bar=r['pressure_bar'], cosolvent='', heavy_other='30', heavy_solvent='', value_origin='ratio',
                  doi=s['doi'], location=where(r, 'Dkcat'), as_printed=f"{r['Dkcat']} ({r['Dkcat_err']})",
                  extracted_by='ai-1', checked_by='ai-2', status='verified',
                  notes=note + f"; rate constants of the same cell: {ids[0]}, {ids[1]}; file {s['file']}"))
for name, fn, rows in (('measurements.csv', mf, M), ('rates.csv', rf, R)):
    with open(DATA / name, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fn, lineterminator='\n'); w.writeheader(); w.writerows(rows)
print(len(M), 'isotope effects,', len(R), 'rate constants')
