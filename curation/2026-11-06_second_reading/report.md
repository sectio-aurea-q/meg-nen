# Second reading (ai-2): report

Conventions: °C → K by +273.15, given to 4 s.f. as SCHEMA.md asks (25 °C → 298.2 K); kelvin as printed.
kJ/mol ÷ 4.184, 4 s.f. (errors too). Eyring results (A′H:A′D, ΔΔH‡) in AH_AX / dEa_kcal; Ea_light left
empty where only ΔH‡H is given (ΔH‡ ≠ Ea). `error` = ± as printed; SD vs SE is never stated. Text from
pdftotext -layout in work/r2/; every entered number checked on the rendered page. Five files were
already in reading2/work/ (S002.txt, S006.txt, s002_p3text.png, s002_tab1.png, s002p3-3.png, 19:38);
origin unknown, not opened.

## S002 — Meyer, Tomchick, Klinman 2008 (SLO-1 I553 mutants)
Included: temperature.csv 3 rows — Table 1 experimental Arrhenius parameters (Ea(H), Ea(D)−Ea(H), AH/AD)
for I553V, I553L, I553G; noncompetitive (p. 1151); 10–50 °C (p. 1147). measurements.csv: 0 rows.
Left out: Table 1 rows WT and I553A (‡ "Data from ref. 15"); calculated/input columns (Morse-oscillator
model; WT/I553A from ref. 16); all p. 1146 numbers (kH/kD ≈80, WT Ea and ΔEa 0.9 ± 0.2 — ref. 8; L546A/L754A
ΔEa 1.9 ± 0.6 / 2.0 ± 0.5, I553A 4.0 ± 0.3, KIEs ≈80–100 — refs. 8, 15); model-reaction KIE 2.7 (ref. 32);
"KIE of close to 100" for L546A/L754A (ref. 15). Per-temperature D(kcat) only in SI Tables 2–4 (not in the
PDF) and in Fig. 3 (plot; nothing read off).
Judgement: quantity kcat (text ties Table 1 to the kcat / D(kcat) fits); transfer PCET (paper: proton-coupled
electron transfer from C-11 to the ferric hydroxide); Arrhenius per table title, though the text calls Ea(H)
"enthalpies of activation"; pH, buffer, n_temperatures not in the main text.
Unclear: p. 1148 text "AH/AD (I553L and I553V) = 0.3 ± 0.30" vs Table 1 0.3 ± 0.2 (V), 0.3 ± 0.4 (L) — table
entered. WT Ea/ΔEa cited to ref. 8 on p. 1146, to ref. 15 in Table 1. Ea(H) near zero for I553L (0.4 ± 0.7)
and I553G (0.03 ± 0.04).

## S006 — Basran, Harris, Sutcliffe, Scrutton 2003 (MR, PETN reductase)
Included: measurements.csv 10 rows, temperature.csv 4 rows.
- MR reductive half-reaction (NADH → FMN N5, stopped-flow): KIE on klim 3.9 ± 0.1 (25 °C); SIE 1.05 ± 0.02;
  KIE 4.4 ± 0.13 (4 °C, kobs1 with stoichiometric NADH, Fig. 6A); Eyring A′H:A′D 0.126 ± 0.005,
  ΔΔH‡ 8.2 ± 0.27 kJ/mol, 5–36 °C (p. 43975).
- PETN reductase reductive half-reaction: Eyring A′H:A′D 4.1 ± 0.3, ΔΔH‡ 0.20 ± 0.01 kJ/mol.
- MR oxidative half-reaction (FMN N5 → 2-cyclohexenone, double mixing): KIE 3.8 ± 0.4 (24 °C), 3.7 ± 0.3 (4 °C).
- MR steady state, Table I (25 °C, pH 7.0): KIE 3.52 ± 0.23 (H2O), 3.56 ± 0.7 (2H2O); SIE 2.28 ± 0.25 (NADH),
  2.32 ± 0.35 (NAD2H); double isotope effect 8.18 ± 1.36.
- MR steady state, Eyring (Fig. 8): KIE A′H:A′D 3.7 ± 2.1, ΔΔH‡ −0.52 ± 0.05 kJ/mol; SIE A′H:A′D 3.1 ± 2.0,
  ΔΔH‡ −0.90 ± 0.05 kJ/mol.
Left out: PETN "KIE (~4.1)" (summary of the series, no temperature); "solvent isotope effect remains constant
(~2)" over pH 7–9 (approximate, no single pH); klim/kobs pairs in Fig. 2A, 3A, 6 legends (rates; the PETN ratio
at 25 °C is not printed and was not computed); Fig. 4 klim/K; Table I turnover numbers a–d (rates); ln(KIE)
insets. No isotope number in this paper is marked as earlier work.
Judgement: Table I/Fig. 8 KIEs → hydride FMN N5 → 2-cyclohexenone, SIEs → protonation of 2-cyclohexenone by
an unidentified active-site acid (as the paper assigns them); double IE kie_type other on the hydride step;
SIE 1.05 on the reductive hydride step; substrate = hydrogen donor (NADH, NADPH, FMNH2, the acid) per SCHEMA;
NAD(P)H "C4" is my reading of "A-side NAD2H"; PETN acceptor only "FMN" in the paper; single_turnover for
stopped-flow, kcat for Table I/Fig. 8 (turnover numbers at 150 µM coenzyme); noncompetitive (word not used);
pH 7.0 also for 2H2O rows (paper: pD 7.0); T range empty for PETN and both steady-state series.
Unclear: 4 °C oxidative KIE 3.7 ± 0.3 (text) vs 3.7 ± 0.05 (Fig. 6B legend; legend aging time 30 s for NAD2H,
text implies 10 s) — text entered. SIE 1.05 has no stated temperature. All ΔΔH‡ errors (±0.27, ±0.01, ±0.05,
±0.05 kJ/mol) are far smaller than the errors on the individual ΔH‡ (±0.5–0.9). Fig. 8 legend ln(A′H) 2.3 (H2O)
and 1.4 (2H2O) do not obviously give the printed SIE ratio 3.1 (own check, nothing entered). Fig. 3 legend:
rates "measured at 5 mM coenzyme" but klim above 30 °C from fits to Eq. 1. Steady-state pH range 5.5–9 in
Experimental Procedures, pH independence reported for 7–9.

## S007 — Basran, Sutcliffe, Scrutton 2001 (TMADH H172Q, Y169F)
Included: measurements.csv 11 rows — Table I KIE column, H172Q, pH 6.0–11.0, 5 °C, KIE on k3, trimethyl-d9-amine.
temperature.csv 2 rows — Table II H172Q pH 9.5 (A′H:A′D 7.8 ± 1.0, ΔΔH‡ 0.5 ± 5.2 kJ/mol, 277–297 K from the
abstract) and Y169F pH 11.0 (2.5 ± 0.2; 3.0 ± 2.5 kJ/mol).
Mixed table: k3H and KdH carry footnote a "Data taken from Ref. 30, except for data at pH 11"; k3D, KdD and KIE
are new. KIEs at pH 6.0–10.5 thus combine earlier protium rates with new deuterium rates; at pH 11 both are new.
The KIE column is not marked as earlier work, so it is included, with this stated in every row.
Left out: native "primary KIE (~7)" (ref. 30); native Table II rows (deuterium only); "KIE approaches a
constant value of ~4.5" (summary of Table I); "the KIE (4.6 ± 0.4)" on p. 24585 (= Table I, pH 9.5); pKa shifts
with perdeuterated substrate (6.8/7.4, Fig. 1B, 9.8/10.1) — isotope effects on ionization, not requested.
Judgement: kind intrinsic at pH 9.5–11.0 (text: intrinsic isotope effect realized at pH ≥ 9.5, "Fig. 1C and
Table I"), observed below; Eyring rows observed. transfer unknown (no species named; Fig. 2 is a "possible
mechanism"); acceptor N5 from Fig. 2/Concluding Remarks; primary as the paper says (all nine methyl H labelled);
5 °C and buffers from Experimental Procedures.
Unclear: Y169F ΔΔH‡ 3.02 ± 2.5 (text p. 24585) vs 3.0 ± 2.5 (Table II) — table entered. k3H identical at pH 8.5
and 9.5 (74.8 ± 4.9, ref. 30 data). T range stated only for H172Q (277–297 K); Experimental Procedures mention
K checks at 5 and 35 °C. Fig. 1C legend calls the KIEs "observed". Text calls A′H:A′D 7.8 "similar to the KIE (4.6)".

## S009 — Wang, Goodey, Benkovic, Kohen 2006 (ecDHFR G121V–M42W)
Included: temperature.csv 3 rows — Table 1 column "G121V–M42W (This work)": AH/AT 0.1 ± 0.1 with ΔEaT-H
3.6 ± 0.3 kcal/mol; AH/AD 0.04 ± 0.03; AD/AT 0.25 ± 0.09; intrinsic, competitive, kcat/KM.
measurements.csv: 0 rows (single-temperature KIEs only in Fig. 2, a plot).
Left out: Table 1 columns WT (35), G121V (41), M42W (44) (headed with reference numbers); S.C. range
(refs. 46, 49, 51); kH* row (pre-steady-state rates, ref. 33); Table 2 (activation parameters of kcat, no
isotope effect); KIEs and Cf in Figs. 2–4 (plots).
Judgement: intrinsic because the paper fits the intrinsic KIEs (p. 15754; Methods, Eq. 5); ΔEa for H/D and D/T
empty ("data not shown"); T range, n and pH of the KIE experiments not stated in this paper; Ea_light empty
(Table 2 Ea 3.91 ± 0.18 kcal/mol is for kcat at pH 9, separate measurements).
Unclear: initial-velocity range 5–45 °C (Results) vs 5–40 °C (Methods). Reference numbers of the comparison
enzymes differ: text G121V ref. 40, M42W ref. 41, but Table 1 G121V (41), M42W (44); WT ref. 35 in Table 1 and
text, ref. 37 in Figs. 3 and 4 (affects only excluded columns).
