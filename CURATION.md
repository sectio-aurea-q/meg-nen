# How a number gets in

1. **Primary source only.** Every value comes from the paper that measured it, with its DOI
   and the exact place (table, figure, page). Reviews only point to primary sources. A value a
   paper attributes to other work is not entered; where a paper reprints such a value in its own
   table without attribution, or forms an isotope effect from a rate constant published elsewhere,
   the row is entered and the credit is recorded in `notes`.
2. **Two readings, the second blind.** Every value is read twice; the second reader does not see
   the first reading. Blind is not independent: both readings so far were made by the same model
   from the same sources under the same rules. A row is `verified` when both readings produced it and either agreed or the
   difference between them was settled against the source; `disputed` while such a difference is
   still open; and `single` in every other case — either because only one reading has produced the
   row, where `notes` say whether the other reading has since checked it against the source, or
   because the row is held at `single` on purpose until a person has checked it. `notes` say which
   case applies. Every
   reading so far, and every settlement of a difference between two readings, is the work of the
   model; what a person has still to do is in rule 3.
3. **Readers are named.** `extracted_by` and `checked_by` name the reader; AI-assisted
   readings are marked `ai-1` and `ai-2`. Where a record in `curation/` says that *the curator* did
   something — settled a difference between the readings, read an equation or a scheme from an image,
   compared two sequences, looked a PDB entry up again — that work was done by the model on the
   author's behalf, outside the two blind readings. It is a third machine look, not a check by a
   person, and it does not make a row `verified` on its own. Where a person is meant, these files say
   *a person*. Before each release a person checks a random sample
   of at least 10 % of the verified rows against the sources, and the error rate found is
   published with the release. A first check was made on 11 November 2026
   (`curation/2026-11-11_person_check/`); only part of it is recorded row by row, and it will be repeated
   with every row recorded before a numbered release. Every second reading is kept in `curation/`, together with the
   comparison of both readings and the decisions taken on each difference.
4. **As printed.** `as_printed` holds the number exactly as it stands in the source. Nothing
   is rounded or averaged in curating; where a source prints individual experiments together with
   their average, the average is entered and the experiments are listed in `notes`. A value that a
   source calculates only as the prediction of a relation it is testing (a Swain–Schaad estimate printed
   beside the measured effect) is not entered, and neither is a number used as an input to a correction
   without its origin. A value that a source calculates from its own measurements and reports as an
   isotope effect of the step (an intrinsic effect by Northrop's method, or an effect for one isotope
   pair obtained from that for another) is entered, and `notes` say that it is calculated. A value that can only be read off a plot is not entered, in the article or in its
   supporting information, while a number printed in a figure legend is printed text and is entered.
   A value that appears only in the supporting information is entered under rule 4a and not otherwise. The collection holds isotope effects on rate constants and on
   Arrhenius or Eyring parameters and nothing else: an isotope effect on another quantity, such as an
   activation volume or a pressure derivative, has no field here and is not entered.
4a. **Supporting information (rule added on 12 November 2026).** Until this date no value from supporting
   information was entered. From now on a value printed in a *table* of a source's supporting information
   may be entered, under the same two readings as any other value, on three conditions: the file read is
   the supporting information as published with the article, and `curation/` records its file name and
   where it was obtained; `location` begins with `SI:` followed by the table and, where it has them, its
   row and column; and `notes` begin with `supporting information`. Rows entered under this rule are
   counted separately in every summary of the collection, so that the counts of values printed in the
   articles themselves stay comparable between versions. The reason for the rule is that many sources
   print the isotope effect at each temperature only there, while the article gives the fitted
   Arrhenius parameters. At the time the rule was added no such row had been entered.
5. **Observed or intrinsic.** A value is `intrinsic` when the source says so of that value, when the source
   reports it as corrected for the commitment to catalysis, or when it comes
   from a competitive measurement that the source reports as yielding intrinsic effects. A statement that a
   method *can* yield intrinsic effects is not enough: it must be said of the measurement. Where the last of
   these three cases is used, `notes` should record the source's statement; 20 rows do not yet do so and are to be closed
   before release. A source also says so of a value when it asserts, of that measurement or of the conditions
   under which it was made for the same enzyme and step, that what is measured there *is*, reflects or is
   realized as the intrinsic effect; such an assertion carries to a temperature series fitted from those same
   measurements. It stays `observed` when the source also prints, for the same step, an intrinsic value obtained
   by another route, which the database holds as its own row, when the identification is hedged ("essentially", "approaches", "likely to be",
   "largely revealed"), or when it is made of the system, the method or earlier work and not of this
   measurement.
6. **No value without a source.** Numbers from memory, "typical" values and values copied
   from other databases stay out. The table in `seed/` is the old, unchecked MEG-APSU table:
   it only says which papers to read, and none of its numbers enters `data/` without being
   read again in the source.
7. **No derived labels.** The database holds measured quantities and the categories its sources
   state, and nothing inferred from them. In particular no row carries a label saying whether a step
   counts as tunnelling, and none is computed: deciding what the measurements can determine is the
   work this collection is meant to serve, not an input to it. Should such a label ever be added, it
   is to be computed from the data by documented rules and never typed in, so that anyone can change
   a threshold and see what follows.
8. **PDFs are not published.** The papers stay with the author; the database holds numbers,
   places and short quotes only. ("The author" is the person; "the curator" in the records under
   `curation/` is the model, as rule 3 says.)
9. **Changes are visible.** A wrong value is corrected in a commit that names the reason,
   never removed silently.

10. **One sign, one unit.** `dEa_kcal` is E_a(heavy) − E_a(light) in kcal/mol throughout, whatever
   the source's own convention. That convention is established before the value is entered: from the
   paper's own equations or definitions where it gives any, otherwise by recomputing the printed
   isotope effect from the printed parameters and seeing which direction reproduces it. Where a paper
   gives neither, the direction is read as heavy minus light, and `notes` record that it was read that
   way rather than taken from the source, which is the case for 15 of the 167 series.
   kJ/mol is converted by dividing by 4.184, to four significant figures. `as_printed` keeps the printed
   number with the unit the source printed, so every conversion can be recomputed from the row itself.
11. **No value without its temperature.** A single-temperature isotope effect is not entered unless
   its source states the temperature at which it was measured; `tools/validate.py` rejects a row
   without one. A temperature series is entered even where its source states no fitted range: `T_min_K`
   and `T_max_K` are then left empty rather than guessed, which is the case for 45 of the 167 series.

`tools/validate.py` checks every row before a release. Besides the schema it checks the sign and unit
convention against the data: where a temperature series and a single-temperature value cover the same
step, isotope pair, effect type, quantity and method in the same paper, and the value's temperature
falls inside the series' fitted range or within 1 K of it, the series must reproduce the value through
KIE = (A_light/A_heavy) · exp(dEa/RT), within a factor of three. The pairs are not matched on `kind`, so an
intrinsic series may be compared with an observed value of the same step.
