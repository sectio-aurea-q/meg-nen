#!/usr/bin/env python3
"""Builds the rows of measurements.csv and rates.csv from reading1.csv (identical to reading2.csv in every cell).
Run once, from the repository root: python3 curation/2026-11-21_si_values_S052_S065/build_rows.py"""
import csv, pathlib
HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE.parent.parent / 'data'
r1 = list(csv.DictReader(open(HERE / 'reading1.csv', encoding='utf-8')))
r2 = list(csv.DictReader(open(HERE / 'reading2.csv', encoding='utf-8')))
key = lambda r: (r['source'], r['table'], r['variant'], r['temperature_printed'])
b = {key(r): r for r in r2}
assert len(r1) == len(r2) == 220 and all(r[f].strip() == b[key(r)][f].strip() for r in r1 for f in ('value', 'error'))
C = {key(r): r for r in r1}

def load(name):
    with open(DATA / name, newline='', encoding='utf-8') as f:
        rd = csv.DictReader(f); return rd.fieldnames, list(rd)
mf, M = load('measurements.csv'); rf, R = load('rates.csv'); tf, T = load('temperature.csv')
assert M[-1]['meas_id'] == 'M0627' and R[-1]['rate_id'] == 'R0258'
mi, ri = 627, 258
byid = {m['meas_id']: m for m in M}

# ---- S052, Guo et al. 2014: SI Tables S2 (kH), S3 (kD), S4 (KIE) ----
V = {'BsDHFR': ('DHFR_GEOSE_WT_NADPH', 'M0203'), 'L20M': ('DHFR_GEOSE_L20M_NADPH', 'M0204'),
     'A104Q': ('DHFR_GEOSE_A104Q_NADPH', 'M0205'), 'L20M/A104Q': ('DHFR_GEOSE_L20M_A104Q_NADPH', 'M0206'),
     'P122E': ('DHFR_GEOSE_P122E_NADPH', 'M0207'), 'P129D': ('DHFR_GEOSE_P129D_NADPH', 'M0208'),
     'P122E/P129D': ('DHFR_GEOSE_P122E_P129D_NADPH', 'M0209')}
COL = {v: 'BsDHFR' if v == 'BsDHFR' else 'BsDHFR-' + v for v in V}
F52 = 'file bi500238q_si_001.pdf from PMC4065160 (Europe PMC supplementary files)'
ODD = {('S2', 'L20M', '15 C'): 'the error is printed with more decimals than the value',
       ('S2', 'L20M', '30 C'): 'the error is printed with more decimals than the value',
       ('S3', 'BsDHFR', '20 C'): 'the error is printed without a decimal'}
n52m = n52r = 0
for v, (step, m20) in V.items():
    art = byid[m20]; assert art['step_id'] == step and art['doi'] == '10.1021/bi500238q' and art['pH'] == '7'
    for t in ('5', '10', '15', '20', '25', '30', '35', '40', '45', '50'):
        tp = t + ' C'; h, d, k = (C[('S052', tab, v, tp)] for tab in ('S2', 'S3', 'S4'))
        nd = [x['value'] == 'nd' for x in (h, d, k)]; assert all(nd) or not any(nd), (v, t)
        if all(nd): continue
        TK = f'{float(t) + 273.15:.2f}'
        if t == '20':   # the article prints the same isotope effect in Table 5; not entered a second time
            assert (k['value'], k['error']) == (art['value'], art['error']); mid = m20
        else:
            mi += 1; mid = f'M{mi:04d}'
        ids = []
        for iso, x, tab, lp in (('H', h, 'S2', 'NADPH C4 (unlabelled NADPH)'), ('D', d, 'S3', art['labelled_position'])):
            ri += 1; rid = f'R{ri:04d}'; ids.append(rid); n52r += 1
            odd = ODD.get((tab, v, tp))
            hdr = ' (printed BsDHFR-P122EP129D in this table)' if (tab, v) == ('S3', 'P122E/P129D') else ''
            R.append(dict(rate_id=rid, step_id=step, labelled_position=lp, isotope=iso, quantity='single_turnover',
                          value=x['value'], error=x['error'], error_type='not_stated', n_measurements='', unit='s-1',
                          temperature_K=TK, pH='7', conditions=art['conditions'], pressure_bar='', doi=art['doi'],
                          location=f"SI: Table {tab}, row {t} °C, column {COL[v]}{hdr}", as_printed=f"{x['value']}±{x['error']}",
                          extracted_by='ai-1', checked_by='ai-2', status='verified',
                          notes=f"supporting information; k{iso} of the pre-steady-state hydride transfer; the meaning of the ± and the number of measurements are not stated"
                                + (f"; {odd}; entered as printed" if odd else '') + f"; the isotope effect of the same temperature is {mid}; {F52}"))
        if t == '20': continue
        n52m += 1
        M.append(dict(art, meas_id=mid, value=k['value'], error=k['error'], temperature_K=TK,
                      location=f"SI: Table S4, row {t} °C, column {COL[v]}", as_printed=f"{k['value']}±{k['error']}",
                      extracted_by='ai-1', checked_by='ai-2', status='verified',
                      notes=f"supporting information; KIE on kH, the hydride-transfer rate constant measured by stopped flow with NADPH and NADPD separately; the meaning of the ± and the number of measurements are not stated; rate constants of the same temperature: {ids[0]}, {ids[1]}; {F52}"))
    r20 = [r['rate_id'] for r in R if r['step_id'] == step and r['temperature_K'] == '293.15' and r['doi'] == art['doi']]
    art['notes'] = art['notes'].replace('KIEs at other temperatures in Fig. 4C and the SI, with salts and cosolvents in Figs. 5 and 6 (not read)',
                                        'KIEs at other temperatures in Fig. 4C and in SI Table S4 (entered on 21 Nov 2026), with salts and cosolvents in Figs. 5 and 6 (not read)') \
        + f"; SI Table S4 prints the same value and error at 20 °C, not entered a second time; rate constants of the same temperature from SI Tables S2 and S3: {r20[0]}, {r20[1]}"
assert (n52m, n52r) == (44, 102)

# ---- S065, Rapp et al. 2022: SI Table S1 (VH/VD at one saturating concentration) ----
F65 = 'file cs2c00257_si_001.pdf from PMC9207888 (Europe PMC supplementary files)'
a20, a60, a80, a40 = byid['M0265'], byid['M0267'], byid['M0269'], byid['M0283']
s1 = {r['temperature_printed']: r for r in r1 if r['source'] == 'S065'}
assert (s1['293.15 K']['value'], s1['293.15 K']['error']) == (a20['value'], a20['error'])
assert (s1['353.15 K']['value'], s1['353.15 K']['error']) == (a80['value'], a80['error'])
assert (s1['333.15 K']['value'], s1['333.15 K']['error']) == ('4.29', '0.28') and (a60['value'], a60['error']) == ('4.30', '0.30')
cond65 = ('100 mM MOPS, pH 7.5; 4.00 mM CDP-glucose or CDP-[2-2H]glucose (95 % deuterium) with 1.0 mg/mL (25.4 µM) TaCPa2E at one '
          'saturating substrate concentration; the KIE is the ratio of the initial rates VH and VD (SI: Table S1)')
n65 = 0; new65 = {}
for tk in ('298.15', '303.15', '308.15', '313.15', '318.15', '323.15', '343.15'):
    x = s1[tk + ' K']; mi += 1; mid = f'M{mi:04d}'; n65 += 1; new65[tk] = mid
    M.append(dict(a20, meas_id=mid, value=x['value'], error=x['error'], error_type='not_stated', n_measurements='',
                  temperature_K=tk, conditions=cond65, location=f"SI: Table S1, row {tk} K", as_printed=f"{x['value']} ± {x['error']}",
                  extracted_by='ai-1', checked_by='ai-2', status='verified',
                  notes="supporting information; KIE (VH VD-1) from repeated measurements at one saturating substrate concentration; the table does not say what the ± is "
                        "(the Methods speak of N ≥ 4 repeated measurements, the Figure 4 legend of S.D. with N = 4 for the same profile)"
                        + ("; the Figure 3 legend omits 25 °C from the Arrhenius plot of kcat for a low coefficient of determination" if tk == '298.15' else '')
                        + ("; the text and the Abstract print this maximum as 6.1 (M0283)" if tk == '313.15' else '') + f"; {F65}"))
assert n65 == 7
for a, t in ((a20, '20'), (a80, '80')):
    a['notes'] += f"; SI Table S1 (single saturating concentration) prints the same value and error at {t} °C, not entered a second time (reading of 21 Nov 2026)"
a60['notes'] += "; SI Table S1 prints 4.29 ± 0.28 at 60 °C, read as the same determination with more digits and not entered a second time (reading of 21 Nov 2026)"
a40['notes'] += f"; SI Table S1 prints the value with its error, 6.13 ± 0.19, entered as {new65['313.15']} (reading of 21 Nov 2026)"
a40['conditions'] = a40['conditions'].replace('the series of Figure 4 and Table S1 (not read)', 'the series of Figure 4 and Table S1')

# ---- notes of the temperature series ----
for t in T:
    if t['temp_id'] in ('T0104', 'T0105', 'T0106', 'T0107', 'T0108', 'T0109', 'T0110'):
        assert 'Table S4 prints the isotope effect at each of these temperatures (not entered yet)' in t['notes']
        t['notes'] = t['notes'].replace('(not entered yet)', '(entered on 21 Nov 2026)')
    if t['temp_id'] in ('T0150', 'T0151'):
        assert 'Table S1 prints VH/VD at each temperature (not entered yet)' in t['notes']
        t['notes'] = t['notes'].replace('(not entered yet)', '(entered on 21 Nov 2026, except the values the article prints as well)')
for name, fn, rows in (('measurements.csv', mf, M), ('rates.csv', rf, R), ('temperature.csv', tf, T)):
    with open(DATA / name, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fn, lineterminator='\n'); w.writeheader(); w.writerows(rows)
print(len(M), 'isotope effects,', len(R), 'rate constants;', M[-1]['meas_id'], R[-1]['rate_id'])
