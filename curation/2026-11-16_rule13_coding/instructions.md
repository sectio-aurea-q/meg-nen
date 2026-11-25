# Coding task: four new fields for MEG-NEN (rule 13)

Code every row of `measurements.csv` (520 rows, id `meas_id`) and `temperature.csv` (175 rows, id `temp_id`)
from the row text alone: `labelled_position`, `kie_type`, `conditions`, `location`, `as_printed`, `notes`
(and `steps.csv` for what is transferred). Do not use outside knowledge of the papers. Never guess: if the row
does not say, use the "not determinable" value.

## Fields (both tables)
1. `pressure_bar` — the pressure the source states for this value or series, in bar (1 kbar = 1000 bar;
   1 atm ≈ 1.013, write 1). Empty when the row states no pressure (ordinary conditions). Write a number only if the
   row states a pressure explicitly (e.g. high-pressure studies, "1 bar", "2 kbar").
2. `cosolvent` — added cosolvent or viscogen stated in the row, short, as "<name> <amount>", e.g. `glycerol 30 %`,
   `DMSO 10 %`, `sucrose 20 %`. Empty when none is stated. Buffer salts, reducing agents, detergents for
   solubilising enzyme, and the substrates are NOT cosolvents. Cryosolvent mixtures count (e.g. `glycerol 50 %`).
3. `heavy_other` — only for rows with `kie_type` = primary: the number of NON-transferred atom positions in the
   reacting molecule whose isotope differs between the light and the heavy reaction. Examples: single label at the
   transferred position, compared with the unlabelled molecule ((R)-[4-2H]NADH vs NADH, 11-(S)-[2H] vs protio) -> 0;
   dideuterated reacting centre vs protio (11,11-d2, α,α-d2, [4,4-2H2]) -> 1; CD3 vs CH3 -> 2; intramolecular
   competition within one CH2D group (H vs D abstraction from the same group; the light path leaves CHD, the heavy
   path leaves CH2) -> 1; toluene-d3 (CD3) vs d0 -> 2; fully deuterated molecule vs protio -> count if the row
   makes it clear, else `nd`. `nd` if the row does not let you count. Empty for rows whose `kie_type` is not primary.
4. (temperature.csv only) `T_break_K` — the break temperature in K if the row says the fitted series is one branch
   of a broken (biphasic) Arrhenius/Eyring plot; empty otherwise. `branch` — `high` if the series is the branch
   above the break, `low` if below, empty if no break.

## Output
Write two CSV files into your output folder:
- `measurements_code.csv` with header `meas_id,pressure_bar,cosolvent,heavy_other,remark`
- `temperature_code.csv` with header `temp_id,pressure_bar,cosolvent,heavy_other,T_break_K,branch,remark`
One line per row of the input, in the same order. `remark`: short, only when you hesitated.
