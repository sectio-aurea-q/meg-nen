# Comparison of the two readings of S001, S008, S010, S011 and S012 (10 November 2026)

Reading 1 `ai-1`, reading 2 `ai-2` (`reading2_*.csv` in this folder). Rows are matched by source, enzyme variant,
effect type, isotope pair, quantity, value and error (series: prefactor ratio and ΔEa); `location`, `as_printed`,
`conditions`, `labelled_position` and `notes` are expected to differ, because both readers wrote them themselves.
The decisions taken on these differences are in `resolution.md`.

## measurements: all 16 rows of reading 1 have a partner in reading 2 with the same numbers and categories; 14 rows only in reading 2

Value, error, temperature, pH, effect type, isotope pair, quantity, method and kind agree in all 16 pairs
(S001 4, S008 6, S011 2, S012 4).

Only in reading 2, all from S012 (the individual experiments of Tables 2 and 3, of which reading 1 entered the
starred averages and listed the experiments in `notes`):

- Table 2, primary (kD/kT)obs: 1.72 ± 0.03; 1.70 ± 0.03; 1.76 ± 0.03; 1.72 ± 0.05
- Table 2, primary (kH/kT)obs: 7.15 ± 0.17; 7.00 ± 0.07; 7.23 ± 0.10
- Table 3, secondary (kD/kT)obs: 1.03 ± 0.01; 1.03 ± 0.01; 1.03 ± 0.004; 1.04 ± 0.02
- Table 3, secondary (kH/kT)obs: 1.37 ± 0.02; 1.33 ± 0.01; 1.35 ± 0.04

## temperature: all 16 series in both readings; prefactor ratios, ΔEa and their errors agree in all 16; 4 rows differ in another field

- S010, Table 2, 5–30 °C (kcat, H/D): Ea_light_kcal '23.6' ± '0.6' vs empty
- S010, Table 2, 30–65 °C (kcat, H/D): Ea_light_kcal '14.6' ± '0.3' vs empty
- S011, intrinsic H/T series: T_max_K '318.15' vs '313.15'; n_temperatures empty vs '4'
- S011, intrinsic D/T series: T_max_K '318.15' vs '313.15'; n_temperatures empty vs '4'

## steps

- S001, all four variants: transfer 'H_atom' in reading 2; reading 1 used the steps already in the collection, which
  carry 'PCET'.

## enzymes: the same eight enzymes and variants in both readings

Reading 1 took name, organism and variant from the sources and left accession, EC number and PDB entries empty
where the source prints none; reading 2 looked them up (P08170, P0ABQ4, P42328, P0A884, P00330). Six of the eight
are already in the collection with these accessions. For S012 the source names neither species nor isozyme, and
P00330 is the second reader's assignment.

## Judgement calls on which both readings agree

Both readers, each without seeing the other: entered the WT-SLO and Leu546→Ala rows of S001 with the credit of footnote e recorded
and asked for a decision under rule 1; assigned 30 °C to the KIE column of S001 Table 1; established the sign of
ΔEa in S008 by recomputing the printed intrinsic H/D effect; did not enter the observed primary effects of S008
that are given for a range of temperatures; entered the corrected secondary effects of S008 as intrinsic and the
calculated secondary H/D effect of 1.13; took the Results values of S011 where its Abstract differs; read
3.3 ± 1.3 kJ/mol in S012 from the running text and not from the damaged figure legend; left out the two H/D values
of note 28 of S012.
