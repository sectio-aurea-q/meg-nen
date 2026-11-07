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
   is rounded or averaged; a value read off a plot is marked as such in `notes`.
5. **Observed or intrinsic.** A value is `intrinsic` only when the source says it is.
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
