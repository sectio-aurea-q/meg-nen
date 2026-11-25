# Decisions taken (by the model on the curator's behalf; rule 3)

1. **Values already in the collection.** Where the article itself prints an isotope effect for the same step, isotope
   pair, quantity, kind, pH and temperature, the supporting value is not entered a second time; the existing row
   keeps its value and its `notes` now quote what the supporting table prints. Seven rows:
   M0021 (article 4.9 ±0.2, SI 4.91 ± 0.07), M0034 (2.7±0.2, SI 2.7 ± 0.2), M0035 (3.0±0.2, SI 3.0 ± 0.2),
   M0036 (2.2±0.2, SI 2.2 ± 0.1), M0037 (2.72±0.1, SI 2.718 ± 0.073), M0038 (1.450±0.042, SI the same),
   M0189 (3.9 ± 0.2, SI the same). In three of them the supporting table prints another error or more digits than
   the article; nothing was changed in `value` or `error`.
2. **S013, two files.** The `.doc` and the `.pdf` hold the same tables; entered once, `notes` name both files.
3. **S013, meaning of ±.** The introduction of the file speaks of standard errors; the text after Table 3S says of the
   45 °C H/T value (9.44 ±0.29, the entry of Table 2S) that the error is at the 95 % confidence interval. The file
   contradicts itself; `notes` of the intrinsic rows quote both statements. Not settled.
4. **S019.** The KIE columns are entered as `observed`, `noncompetitive`, with the quantity of the series of the same
   step (`single_turnover` for the pre-steady-state tables, `kcat` for the steady-state table at pH 9.5). The captions
   do not say whether the KIE was formed from the two rate columns; `notes` say that the table lists both.
5. **S040.** Observed and intrinsic values are told apart by the header of Table S2. `notes` of the intrinsic H/D and
   D/T rows state that they are calculated from the intrinsic H/T value by the Swain–Schaad relationship (footnote a).
   pH is left empty, as in the series of this step: the supporting information states none.
6. **S041, `labelled_position` of the observed rows.** Given from the conditions of the article: [5-3H]dUMP with
   [2-14C]dUMP (H/T) or with [2-14C,5-2H]dUMP (D/T).
7. **Existing series.** `notes` of T0013–T0015, T0027–T0029 and T0081–T0083 now say that the per-temperature values
   were read and where the rows are. `n_temperatures` set from the supporting tables for T0013–T0015 (5), T0027 (8)
   and T0029 (7); left empty for T0028, whose fit uses only part of the tabulated range. `T_min_K` and `T_max_K` of
   T0081 set to 278.15 and 308.15 from SI Table S2 (5 to 35 °C), which lowers the count in rule 11 from 46 to 45.
   No isotope effect, error or Arrhenius parameter of these series changes.
8. **`tools/validate.py`.** The check of rule 10 compared a series with every single value of the same step, isotope
   pair, effect type, quantity, method and paper. With observed and intrinsic values of one step now side by side it
   compared an intrinsic series (T0082) with observed values (M0408, M0409) and reported them. `kind` was added to
   the fields that must match. With it, 109 series/value pairs are compared and all agree within a factor of 3;
   among them are the new intrinsic rows against the article's own Arrhenius parameters.
9. **Not entered.** Rate constants (S019), commitments (S040), the 95 % confidence intervals of Table 3S (S013),
   and anything shown only in a figure.
