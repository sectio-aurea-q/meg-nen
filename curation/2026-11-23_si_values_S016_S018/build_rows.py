#!/usr/bin/env python3
"""Builds the rows of measurements.csv and rates.csv from the transcriptions of SI Table S2 of S016 and SI Table S5 of
S018 (reading1 and reading2 of each agree in every cell; checked again here).
Run once, from the repository root: python3 curation/2026-11-23_si_values_S016_S018/build_rows.py"""
import csv, math, pathlib
HERE = pathlib.Path(__file__).resolve().parent
CUR = HERE.parent
DATA = CUR.parent / 'data'

def table(d, name):
    a = list(csv.DictReader(open(CUR / d / f'reading1_{name}.csv', encoding='utf-8')))
    b = list(csv.DictReader(open(CUR / d / f'reading2_{name}.csv', encoding='utf-8')))
    num = [k for k in a[0] if k != 'klammer']
    assert len(a) == len(b) and all(x[k].strip() == y[k].strip() for x, y in zip(a, b) for k in num), name
    return [{k: v.strip() for k, v in r.items()} for r in a]

def load(name):
    with open(DATA / name, newline='', encoding='utf-8') as f:
        rd = csv.DictReader(f); return rd.fieldnames, list(rd)
mf, M = load('measurements.csv'); rf, R = load('rates.csv'); tf, T = load('temperature.csv')
assert M[-1]['meas_id'] == 'M0678' and R[-1]['rate_id'] == 'R0360'
mi, ri = 678, 360
byid = {m['meas_id']: m for m in M}
TK = lambda t: f'{float(t) + 273.15:.2f}'
def sig2(x): return f'{float(f"{x:.2g}"):g}' if x >= 1 else f'{x:.2g}'

# ---- S016, Sharma & Klinman 2008: SI Table S2 ----
F16 = 'text of NIHMS91462-supplement-1_si_001.pdf (PMC2671078), copied from the PDF on 23 Nov 2026'
S2 = table('2026-11-23_S016_supporting_information', 'tableS2'); assert len(S2) == 8
art = byid['M0026']; assert art['doi'] == '10.1021/ja806354w' and (art['value'], art['error'], art['pH']) == ('128', '3', '9.0')
cond16 = ('100 mM borate, pH 9.00, ambient atmosphere (20.8 % O2); 0.50–80 µM linoleic acid; kcat and kcat/KM from Michaelis–Menten fits of the '
          'initial rates with protio and with dideutero linoleic acid; empirical rate constants, without the O2 correction of SI Table S1')
n16m = n16r = 0
for r in S2:
    t = r['T_C']; tk = TK(t); same = (t == '30')
    if same:
        assert (r['Dkcat'], r['Dkcat_fehler']) == (art['value'], art['error']); mid = 'M0026'
    else:
        mi += 1; mid = f'M{mi:04d}'
    ids = []
    for iso, v, e, lp in (('H', r['kcatH'], r['kcatH_fehler'], 'unlabelled linoleic acid (protio substrate)'), ('D', r['kcatD'], r['kcatD_fehler'], art['labelled_position'])):
        ri += 1; rid = f'R{ri:04d}'; ids.append(rid); n16r += 1
        R.append(dict(rate_id=rid, step_id=art['step_id'], labelled_position=lp, isotope=iso, quantity='kcat', value=v, error=e,
                      error_type='not_stated', n_measurements='', unit='s-1', temperature_K=tk, pH='9.0', conditions=cond16, pressure_bar='',
                      doi=art['doi'], location=f"SI: Table S2, row {t} °C, column kcat({iso})", as_printed=f"{v} ({e})",
                      extracted_by='ai-1', checked_by='ai-2', status='verified',
                      notes=f"supporting information; table headed 'Empirical rate constants'; the SI describes a correction of the protio rate to O2 saturation (Table S1, factor "
                            f"{dict((x['T_C'], x['korrekturfaktor']) for x in table('2026-11-23_S016_supporting_information', 'tableS1'))[t]} at this temperature), which this value does not contain; "
                            f"the meaning of the error in parentheses and the number of measurements are not stated; the isotope effect of the same row is {mid}; {F16}"))
    prop = float(r['Dkcat']) * math.hypot(float(r['kcatH_fehler']) / float(r['kcatH']), float(r['kcatD_fehler']) / float(r['kcatD']))
    if same:
        art['notes'] += f"; SI Table S2 prints the same value and error at 30 °C, not entered a second time; rate constants of the same row: {ids[0]}, {ids[1]}"
    else:
        n16m += 1
        M.append(dict(art, meas_id=mid, value=r['Dkcat'], error=r['Dkcat_fehler'], temperature_K=tk, conditions=cond16,
                      location=f"SI: Table S2, row {t} °C, column Dkcat", as_printed=f"{r['Dkcat']} ({r['Dkcat_fehler']})",
                      extracted_by='ai-1', checked_by='ai-2', status='verified',
                      notes=f"supporting information; Dkcat of the table headed 'Empirical rate constants and isotope effects', without the O2 correction of the protio rate that the SI describes "
                            f"(SI Table S1); the error in parentheses is entered as printed: it is smaller than the error propagated from the two rate constants of the row ({sig2(prop)}), and what it is, "
                            f"is not stated; number of measurements not stated; rate constants of the same row: {ids[0]}, {ids[1]}"
                            + ("; 2.95/0.0321 gives 91.9, printed 91" if t == '50' else '') + f"; {F16}"))
    mi += 1; n16m += 1
    M.append(dict(art, meas_id=f'M{mi:04d}', quantity='kcat/KM', value=r['DkcatKM'], error=r['DkcatKM_fehler'], temperature_K=tk, conditions=cond16,
                  location=f"SI: Table S2, row {t} °C, column D(kcat/KM)", as_printed=f"{r['DkcatKM']} ({r['DkcatKM_fehler']})",
                  extracted_by='ai-1', checked_by='ai-2', status='verified',
                  notes=f"supporting information; D(kcat/KM) of the table headed 'Empirical rate constants and isotope effects'; KM(H) {r['KMH']} ({r['KMH_fehler']}) and KM(D) {r['KMD']} ({r['KMD_fehler']}) µM "
                        f"of the same row are not held in this collection; the meaning of the error in parentheses and the number of measurements are not stated; {F16}"))
assert (n16m, n16r) == (15, 16)

# ---- S018, Nagel et al. 2012: SI Table S5 ----
F18 = 'text of NIHMS376254-supplement-1_si_001.pdf (PMC3498984), copied from the PDF on 23 Nov 2026'
S5 = table('2026-11-23_S018_supporting_information', 'tableS5'); assert len(S5) == 40
V = {'L176V': 'M0029', 'L176A': 'M0030', 'L176G': 'M0031', 'L176Δ': 'M0032', 'V260A': 'M0033'}
SAME = {'L176V': '28.5', 'L176A': '28.5', 'L176G': '30', 'L176Δ': '30', 'V260A': '30'}   # the row that Table 1 of the article prints
assert set(r['variante'] for r in S5) == set(V)
n18m = n18r = 0
for r in S5:
    v, t = r['variante'], r['T_C']; a = byid[V[v]]; tk = TK(t)
    assert a['doi'] == '10.1021/bi3001352' and a['pH'] == '7.0' and a['temperature_K'] == '303.15'
    nd = r['kcatD'] == 'ND'; same = (t == SAME[v])
    assert (r['Dkcat'] == 'ND') == nd
    cond = a['conditions'] + '; the values per temperature are those of SI Table S5, which prints no pH, buffer or unit'
    if not nd and not same:
        mi += 1; mid = f'M{mi:04d}'
    else:
        mid = V[v] if same else None
    ids = []
    for iso, x, e, lp in (('H', r['kcatH'], r['kcatH_fehler'], 'unlabelled benzyl alcohol'), ('D', r['kcatD'], r['kcatD_fehler'], a['labelled_position'])):
        if x == 'ND': continue
        ri += 1; rid = f'R{ri:04d}'; ids.append(rid); n18r += 1
        R.append(dict(rate_id=rid, step_id=a['step_id'], labelled_position=lp, isotope=iso, quantity='kcat', value=x, error=e,
                      error_type='not_stated', n_measurements='', unit='s-1', temperature_K=tk, pH='7.0', conditions=cond, pressure_bar='',
                      doi=a['doi'], location=f"SI: Table S5, block {v}, row {t} °C, column kcat ({iso})", as_printed=f"{x}, Error {e}",
                      extracted_by='ai-1', checked_by='ai-2', status='verified',
                      notes="supporting information; Table S5 prints no unit, s-1 as for kcat in Table 1 of the article; the meaning of the error and the number of measurements are not stated"
                            + (f"; the isotope effect of the same row is {mid}" if mid else "; kcat (D) and D kcat of this row are printed ND") + f"; {F18}"))
    if nd: continue
    prop = float(r['Dkcat']) * math.hypot(float(r['kcatH_fehler']) / float(r['kcatH']), float(r['kcatD_fehler']) / float(r['kcatD']))
    if same:
        # Table 1 prints this determination with its absolute error: the error propagated from the rate constants of Table S5 must give it
        assert abs(prop - float(a['error'])) <= 0.15, (v, prop, a['error'])
        a['notes'] += (f"; SI read on 23 Nov 2026 (two blind readings): SI Table S5 has no row at 30 °C for this variant; its row at {t} °C prints D kcat {r['Dkcat']} and rate constants whose "
                       f"propagated error ({sig2(prop)}) is the error printed here; read as the determination that Table 1 heads 'at 30 °C' and not entered a second time; rate constants of that row ({t} °C): {ids[0]}, {ids[1]}"
                       if t != '30' else
                       f"; SI read on 23 Nov 2026 (two blind readings): SI Table S5 prints D kcat {r['Dkcat']} at 30 °C with 'Error' {r['Dkcat_fehler']}; the error propagated from its rate constants ({sig2(prop)}) is the "
                       f"error printed here; not entered a second time; rate constants of the same row: {ids[0]}, {ids[1]}")
        continue
    n18m += 1
    M.append(dict(a, meas_id=mid, value=r['Dkcat'], error=sig2(prop), temperature_K=tk, conditions=cond,
                  location=f"SI: Table S5, block {v}, row {t} °C, column Dkcat", as_printed=f"{r['Dkcat']}, Error {r['Dkcat_fehler']}",
                  extracted_by='ai-1', checked_by='ai-2', status='verified',
                  notes=f"supporting information; D kcat as printed; the column 'Error' of D kcat ({r['Dkcat_fehler']}) is not an absolute error: for the five values that Table 1 of the article prints, "
                        f"the absolute error of Table 1 is the error propagated from kcat (H) and kcat (D) of the same row of Table S5, and 'Error' matches the relative one; the error entered ({sig2(prop)}) "
                        f"is therefore propagated from the rate constants of this row ({ids[0]}, {ids[1]}), a calculation of the curation; what the ± of the rate constants is and the number of measurements "
                        f"are not stated; kcat (H)/kcat (D) of the row gives {float(r['kcatH']) / float(r['kcatD']):.3g}; {F18}"))
assert (n18m, n18r) == (34, 79), (n18m, n18r)

# ---- notes of the temperature series ----
k = 0
for t in T:
    if t['temp_id'] == 'T0021':
        assert 'the single values of Table S2 are not entered yet' in t['notes']
        t['notes'] = t['notes'].replace('the single values of Table S2 are not entered yet', 'the single values of Table S2 were entered on 23 Nov 2026 (the value at 30 °C is M0026)'); k += 1
    if t['temp_id'] in ('T0022', 'T0023', 'T0024', 'T0025', 'T0026'):
        assert 'the single values of Table S5 are not entered yet' in t['notes']
        t['notes'] = t['notes'].replace('the single values of Table S5 are not entered yet', 'the single values of Table S5 were entered on 23 Nov 2026 (the value of Table 1 is not entered a second time)'); k += 1
assert k == 6
for name, fn, rows in (('measurements.csv', mf, M), ('rates.csv', rf, R), ('temperature.csv', tf, T)):
    with open(DATA / name, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fn, lineterminator='\n'); w.writeheader(); w.writerows(rows)
print(len(M), 'isotope effects,', len(R), 'rate constants;', M[-1]['meas_id'], R[-1]['rate_id'])
