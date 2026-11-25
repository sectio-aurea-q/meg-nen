# Task: one blind reading of printed isotope effects for the MEG-NEN collection

You are one of two independent readers. You must NOT look at any other reading, at <workdir>/reading_* folders other than your own, or at any file outside the ones named here. Work only from the page photos listed in papers.txt for YOUR group.

Rules: read <workdir>/SCHEMA.md and <workdir>/CURATION.md completely first. Follow them strictly, especially:
- rule 4: only numbers printed as numbers (text, tables, figure legends). Nothing read off a plot. Nothing you calculate yourself (no differences, no ratios, no unit conversions except those the schema prescribes: °C -> K (T+273.15), kJ/mol -> kcal/mol (divide by 4.184, 4 significant figures)).
- rule 5: observed vs intrinsic exactly as defined (hedged statements stay observed).
- rule 10: dEa_kcal = Ea(heavy) - Ea(light); Eyring A'H:A'D and ΔΔH‡ go into AH_AX and dEa_kcal with a note.
- rule 11: a single-temperature value only if the source states its temperature (look in methods, legends, text).
- rule 12: error_type (sd/se/ci95/other/conflicting/not_stated/none) and n_measurements as the source states them for that value.
- rule 4b rates: only if printed for the same step at >= 2 temperatures.
- Values that a paper attributes to other work are not entered.
Reuse enzyme_id / step_id from enzymes.csv / steps.csv where the same enzyme variant and step already exist (e.g. SLO1_SOYBN_WT_LA, SLO1_SOYBN_L546A_LA, MR_PSEPU_WT_RED, PETNR_ENTCL_WT_RED). Otherwise propose new ids in the same style.

Output (write into your folder, given in your prompt):
1. measurements.csv  – columns exactly as SCHEMA measurements.csv, meas_id = "new1", "new2", ...; extracted_by = your reader tag; checked_by empty; status "single".
2. temperature.csv   – same, temp_id "newT1", ...
3. rates.csv         – same, rate_id "newR1", ... (may be empty except header)
4. enzymes_new.csv and steps_new.csv – only NEW rows you need (schema columns), status "single".
5. report.md – per paper: which pages you could read, every number you considered and did NOT enter with the reason (one line each), anything illegible, and the exact sentences that decide observed/intrinsic, temperature, pH, error meaning.
Use CSV quoting for fields with commas. Be complete: enter every eligible printed value. Doi: take it from the printed page where visible.
