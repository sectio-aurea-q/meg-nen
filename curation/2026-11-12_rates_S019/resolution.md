# Decisions taken (by the model on the curator's behalf; rule 3)

1. **Step and quantity.** As for the isotope effects of the same tables: Tables 1 and 3 are `single_turnover`
   (wild type and G121V), Table 2 is `kcat` of the wild type. The caption of Table 2 says "steady state rates", not
   kcat; `notes` say so.
2. **`isotope`.** kH and Rate (NADPH) are `H`, kD and Rate (NADPD) are `D`. The captions of Tables 1 and 3 name
   only NADPH; that kD was measured with NADPD follows from the column header and from the article.
3. **`conditions`, `pH`.** Taken from the series of the same step and paper (T0027, T0028, T0029), without the
   words about the fit.
4. **`as_printed`.** Value and ± as in the second reading, followed by the unit of the column header (`s-1`).
5. **Table 3.** The rate constants of G121V (0.086 to 0.235 s-1) are about a thousand times smaller than those of
   the wild type in Table 1. As printed; the article assigns them to the slow phase of the stopped-flow trace.
6. **Nothing derived.** No activation energy was fitted or stored. `Ea_light_kcal` of T0027 and T0029 remains what
   the article prints.
