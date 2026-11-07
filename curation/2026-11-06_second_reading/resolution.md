# Second reading of S002, S006, S007, S009 (6 November 2026)

First reading `ai-1`, second reading `ai-2`. The second reader worked from the PDFs alone and did not
see the first reading. Files in this folder:

- `reading2_measurements.csv`, `reading2_temperature.csv`, `report.md`: the second reading as delivered
- `comparison.md`: row-by-row comparison of both readings, before the decisions below

## Result

All 32 rows agree in their numbers (value, error, temperature, pH, Arrhenius or Eyring parameters) and
in quantity and method. One row differed in `kind`, two steps in the acceptor, and the second reader
entered one value the first reader had left out. Decisions, each settled by the source:

1. **T0011** (TMADH H172Q, temperature series at pH 9.5): `kind` intrinsic in the first reading,
   observed in the second. The source states that the intrinsic isotope effect is realized at pH 9.5
   and above for Table I (5 °C), but does not call the temperature series intrinsic. Settled as
   observed.
2. **Acceptor of the reductive half-reactions** of MR and PETN reductase: the source names FMN and does
   not state N5. Both steps now give FMN.
3. **Solvent isotope effect 1.05 ± 0.02** on flavin reduction in MR (S006, p. 43976): entered only in
   the second reading. Both readers found that the source states no temperature. `temperature_K` is
   required, so the value is not entered; it is recorded in the notes of step `MR_PSEPU_WT_RED`.
4. **`as_printed`**: the same numbers with more or fewer surrounding words. Where the second reading kept
   the printed labels more exactly (T0001–T0003, T0007, T0011, T0012), its wording was taken.
5. **Notes taken over from the second reading**: S002 Table 1 does not name the rate; the ΔΔH‡ errors in
   S006 are much smaller than the errors of the single ΔH‡ values; the S006 Fig. 8 legend does not fit
   the printed solvent A′ ratio; the S007 Fig. 1C legend calls the high-pH values observed.

All 20 isotope effects, 12 temperature series and 10 steps are now `verified`. The enzyme rows stay
`single`: their UniProt and PDB identifiers were looked up once and have not been checked a second time.
