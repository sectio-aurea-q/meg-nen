# Second reading of S013 (7 November 2026)

First reading `ai-1`, second reading `ai-2`. Both readers worked from the PMC page of the author manuscript
(PMC2553318), saved on 7 November 2026; the published PDF was not read. The second reader worked from that page
alone and did not see the first reading. Files in this folder:

- `reading2_measurements.csv`, `reading2_temperature.csv`, `report.md`: the second reading as delivered
  (`report.md` was saved by the curator from the second reader's answer)
- `comparison.md`: row-by-row comparison of both readings, before the decisions below

## Result

All 8 rows agree in their numbers (value, error, temperature, pH, Arrhenius parameters and temperature range) and in
quantity, method and kind. Both readers left out the same values. The step agrees as well: hydride transfer from
the pro-R hydrogen at NADPH C4 to C6 of 7,8-dihydrofolate (si face). Decisions:

1. **`as_printed`** of M0022–M0025 and T0013–T0015: the second reading's wording is taken. For the 2° KIEs it keeps
   "for H- and D-transfer", which says which number belongs to which experiment; for Table 1 it marks that the unit
   comes from footnote a and is not printed in the cell.
2. **Notes taken over from the second reading:** the ± on the intrinsic 1° KIEs are standard errors; H and D were not
   competed directly; the pH 7 next to the value 4.9 refers to the pre-steady-state rate of ref. 11; the Fig. 1
   caption names the wrong equation for the fit; the direction of ΔEa comes only from the Methods definition; the
   commitments are called "reported above" but do not appear earlier; the two synthesis paragraphs describe one
   labelled reference compound by different routes.
3. **Judgement calls confirmed by both readers:** `quantity` kcat/KM for the intrinsic values (as for the intrinsic
   DHFR values of S009), ΔEa as Ea(heavy) − Ea(light), pH 8.0 and 278.15–318.15 K from Methods and Results,
   `Ea_light_kcal` empty because the only Ea in the text belongs to kcat at pH 9.

All 5 isotope effects, 3 temperature series and the step are now `verified`. The enzyme row stays `single`: its UniProt
identifier was looked up once and has not been checked a second time.
