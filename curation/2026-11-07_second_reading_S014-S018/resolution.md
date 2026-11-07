# Second reading of S014–S018 (7 November 2026)

First reading `ai-1`, second reading `ai-2`. Both readers worked from the PMC pages of the five papers, saved on
7 November 2026 (S014 and S017 as publisher versions, S015, S016 and S018 as author manuscripts); the published PDFs
and the supporting information were not read. The second reader worked from those pages alone, did not see the first
reading, and looked up UniProt and RCSB PDB again for every new enzyme variant. Files in this folder:

- `reading2_measurements.csv`, `reading2_temperature.csv`, `reading2_enzymes.csv`, `report.md`: the second reading as
  delivered (`report.md` saved by the curator from the second reader's answer; the list of the reader's working files
  and a closing remark were removed)
- `comparison.md`: row-by-row comparison of both readings, before the decisions below

## Result

All 19 rows (8 isotope effects, 11 temperature series) agree in their numbers (value, error, temperature, pH,
Arrhenius parameters and temperature range) and in quantity, method and kind. Both readers left out the same values:
everything the papers take from other papers (the WT and G121V columns of S014, the WT and I14A columns of S015, the
WT, 546A and 553A rows of S016, the WT row of S017, the wild-type values of S018, which that paper calculates from the
H/T KIEs of its ref. 21), values given only in the supporting information or in figures, and rates that are not
isotope effects. The ten enzyme variants agree in UniProt accession, EC number, organism and variant, and after
decision 3 also in their PDB entries; the ten steps agree in substrate, donor, acceptor and transfer. Decisions:

1. **`as_printed`:** the first reading's wording is kept; the second reading mostly adds the row or column label,
   which `location` already gives. Two cases were checked character by character in the HTML: M0027 takes the second
   reading's "Dkcat= 729 ± 26" (footnote d prints no space before "="); T0023 keeps the first reading's "1.4(±0.9)",
   as Table 2 of S018 prints it.
2. **Judgement calls made the same way by both readers:**
   - S014: intrinsic, kcat/KM and competitive for the A_l/A_h of M42W; 278.15–318.15 K and pH 8.0 from Methods; no
     ΔEa, because the paper does not summarize it.
   - S015: ΔEa taken as printed (the paper defines ΔE_ah-l = E_ah − E_al); temperature range and pH left empty, because
     the main text gives them only for the stopped-flow rates.
   - S016: 30 °C for the KIE 128 from footnote b, which stands on the kcat column; footnote d's
     "ΔEa = Ea(D) − ΔEa(H)" read as Ea(D) − Ea(H).
   - S017: 537 (55) entered as `single_turnover` at 308.15 K (pre-steady-state at 35 °C, although the table labels it
     Dkcat), pH empty; 729 ± 26 as steady-state `kcat` at 303.15 K and pH 9 (Fig. 2A); transfer PCET, although the
     paper does not name the mechanism (as assigned for SLO-1 in S002 and S016).
   - S018: pH 7.0 for the Table 2 series from the Results; no temperature range, because only "above the 30 °C break"
     (40 °C for V260A) is stated; `kie_type` primary for α,α-d2-benzyl alcohol, as the paper calls these KIEs.
3. **PDB entries of I14V and I14G (correction):** the second reading found 4QLG (I14V) and 4QLF (I14G) by a
   sequence-identity search. RCSB maps them to UniProt U6N356 instead of P0ABQ4, so the first reading, which searched
   only by accession, missed them. The curator confirmed both: the sequence equals P0ABQ4 except at residue 14, and
   both cite 10.1021/jp5059963 (Doron et al., J. Phys. Chem. B, with Stojković and Kohen among the authors), not
   S015. `pdb` and
   `notes` of `DHFR_ECOLI_I14V` and `DHFR_ECOLI_I14G` are corrected. A repeated sequence search found no entry for
   M42W, L546A/I553A or the ht-ADH variants, and none for the earlier rows G121V and G121V/M42W either; L546A/L754A
   has 4WHA (which cites S017) and 5TQO.
4. **Notes taken over from the second reading:** S018 calls the errors of its temperature series propagated errors;
   in S015 the Methods sentence on standard deviations follows the stopped-flow description and need not cover the
   fitted parameters; S018 builds its structural models from PDB 1RJW, an entry of P42328 (strain LLD-R).
5. **Steps:** both readings describe the same chemistry; the first reading's wording is kept, in line with the
   existing DHFR and SLO-1 steps. For S014 the curator checked Scheme 1 (an image): it shows the pro-R hydrogen moving
   from NADPH C4 to C6 of dihydrofolate; the si face is stated in S013 and S015, not in S014.

## Inconsistencies inside the papers

None of them changes an entered value. All were checked by the curator in the HTML.

- **S014** prints values for G121V that it takes from Wang et al. 2006 (6.7 ± 0.8, 3.8 ± 0.4 and 1.76 ± 0.07 for
  H/T, H/D and D/T); the published paper (S013, Table 1; T0013–T0015) prints 6.6 ± 1.3, 3.7 ± 0.5 and 1.8 ± 0.1. The
  published values stand. The text says Fig. 2 shows G121V, its caption says M42W; "M42V" stands for M42W; endnote 1
  names equation (2.1) for the equation that is (2.3); the Fig. 1 caption prints "1r×2" for PDB 1RX2.
- **S015:** footnote e attributes the WT parameters to ref. 47, a synthesis paper, while the Fig. 3 caption attributes
  the WT data to ref. 38; the text says the single-turnover rates were measured for the wild type as well, while
  Table 1 cites the WT k_H to ref. 58.
- **S016:** footnote d prints "ΔEa = Ea(D) − ΔEa(H)"; linoleic acid is called "9,12-(Z,Z)-octadecanoic acid"
  (octadecadienoic); kcat of the double mutant is called "one hundred fifty-fold" lower than that of WT and I553A,
  where Table 1 gives about 130-fold; the text cites ref. 4 for the L546A data, Table 1 cites ref. 10a. The printed
  Arrhenius parameters give a KIE of about 110 at 30 °C against the printed 128 (3), which is within their errors.
- **S017:** the 35 °C single-turnover value stands in the Dkcat column next to parameters at 30 °C, and only footnote d
  says so; the protio single-turnover rate at 35 °C, on which the value rests, is not printed.
- **S018:** the text gives 0.1 kcal/mol for the wild-type Ea(D) − Ea(H), Table 2 prints 0.2 (±0.2) and calls it
  Ea(T) − Ea(H) (footnote b); kcat is said to fall 5- to 50-fold, Table 1 gives 3.2- to 58-fold; the Discussion cites
  Table 1 where Table 2 is meant; the supporting tables are named S2–S5 in one place and S1 and S2 in another.

All 8 isotope effects, 11 temperature series, 10 enzyme variants and 10 steps of S014–S018 are now `verified`.
