# How a number gets in

1. **Primary source only.** Every value comes from the paper that measured it, with its DOI
   and the exact place (table, figure, page). Reviews only point to primary sources.
2. **Two independent readings.** Every value is read twice; the second reader does not see
   the first reading. A row is `verified` only when both readings agree, `single` with one
   reading, and `disputed` when they differ, until the source settles it.
3. **Readers are named.** `extracted_by` and `checked_by` name the reader; AI-assisted
   readings are marked `ai-1` and `ai-2`. Before each release a person checks a random sample
   of at least 10 % of the verified rows against the sources, and the error rate found is
   published with the release. Every second reading is kept in `curation/`, together with the
   comparison of both readings and the decisions taken on each difference.
4. **As printed.** `as_printed` holds the number exactly as it stands in the source. Nothing
   is rounded or averaged; a value that can only be read off a plot is not entered, while a number printed in a figure legend is printed text and is entered.
5. **Observed or intrinsic.** A value is `intrinsic` when the source says so of that value, or when it comes
   from a competitive measurement that the source reports as yielding intrinsic effects. A statement that a
   method *can* yield intrinsic effects is not enough: it must be said of the measurement. Where the second
   limb is used, `notes` should record the source's statement; 22 rows do not yet do so and are to be closed
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
7. **Labels are computed.** Whether a step counts as tunnelling is never typed in. It is
   computed from the data by documented rules, so anyone can change a threshold and see
   what follows.
8. **PDFs are not published.** The papers stay with the curator; the database holds numbers,
   places and short quotes only.
9. **Changes are visible.** A wrong value is corrected in a commit that names the reason,
   never removed silently.

`tools/validate.py` checks every row before a release.
