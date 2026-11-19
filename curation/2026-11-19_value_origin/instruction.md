# Coding instruction: `value_origin` (MEG-NEN, 19 November 2026)

You code ONE new field for every row of `rows.csv` (520 single-temperature isotope effects from enzyme papers).
Work ONLY from the text of each row (labelled_position, conditions, location, as_printed, notes, and the
fields kind/method/quantity). Do not use outside knowledge of the papers. Do not open any other file.

`value_origin` says how the SOURCE obtained the printed number:

- `ratio` — the ratio of two quantities measured for the light and the heavy isotope (or a competitive
  measurement of both in one mixture), as the source reports it. Each quantity may come from a kinetic fit of the
  source's own data at that temperature (Michaelis–Menten, Hill, single/double exponential, hyperbolic, global fit of
  traces, burst amplitude...). This is the normal case of a reported observed isotope effect. Use it also when the
  row simply presents the value as the measured / observed isotope effect and mentions no further calculation.
- `corrected` — a measured ratio that the source then corrected (for isotopic impurity, label or deuterium
  abundance, solvent viscosity, enzyme iron content, ...). A row that says the value was NOT corrected is not this.
- `combined` — calculated by the source from OTHER isotope effects or kinetic parameters, not measured as a ratio
  itself: intrinsic values by the Northrop method from H/T and D/T, Swain–Schaad relations, commitment corrections,
  products of primary and secondary effects, values from equations applied to observed effects, mechanism-based
  calculations.
- `fit_T` — calculated by the source from the fit of a temperature series (Arrhenius/Eyring parameters) and stated
  at one temperature, rather than measured at that temperature.
- `extrapolated` — extrapolated by the source beyond its measured conditions (to 0 bar, 0 °C, zero concentration...).
- `nd` — the row does not allow a decision (e.g. a value called intrinsic with no word on how it was obtained, or
  contradictory statements).

Rules:
1. Code the value of THIS row only. Statements about other values in the same paper that were "not entered" do not
   count (e.g. "the 30 °C values are extrapolated ... and not entered" says nothing against this row).
2. If two apply, the later step wins: corrected before combined (a commitment-corrected intrinsic value is
   `combined`); `fit_T` and `extrapolated` win over everything else.
3. `kind` = intrinsic alone is NOT enough for `combined`; the row must say how. Without that: `nd`.
4. Write a SHORT reason (max 20 words) quoting the words of the row that decide it.

Output: a CSV file with header `meas_id,value_origin,reason`, exactly 520 rows, same order as rows.csv,
written to the path given in your task. Then reply with the counts per category only.
