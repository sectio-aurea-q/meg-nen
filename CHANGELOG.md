# Changelog

What changed in MEG-NEN, newest first. Times are Central European Time. Every second reading, comparison and
decision is kept in `curation/`.

## 2026-11-08 02:54
- S034–S038 entered and read twice: E. coli DHFR distal and double mutants (W133F, F125M, G121V/F125M, M42W/F125M,
  I14A/G121V; intrinsic H/T Arrhenius parameters), E. coli DHFR at pH 7.0 and the humanized mutants N23PP and
  N23PP/G51PEKN, native and heavy human DHFR, and soybean LOX-1 with ten variants (Dkcat and Dkcat/Km at 10 and
  40 °C, solvent isotope effects): 56 isotope effects and 9 temperature series, all `verified`, with 19 new enzyme
  variants and 19 steps. Both readings agree in every number and category. The second reading added the PDB entry
  4GH8 of N23PP/G51PEKN and seven wild-type entries of soybean LOX-1. SCHEMA.md: heavy-enzyme effects are not
  entered. See `curation/2026-11-07_second_reading_S034-S038/`.

## 2026-11-07 21:54
- S029–S033 entered and read twice: morphinone reductase at 1 bar and 2 kbar (Eyring series under pressure), the
  glucose dehydrogenase of Bacillus megaterium (commercial enzyme, no accession), ht-ADH W87F, W87L, W87A and Y25A
  and ps-ADH A25Y (Dkcat from 5 to 52 °C), half-heavy and heavy formate dehydrogenase (intrinsic H/T ΔEa) and four
  plant lipoxygenases, among them a wild-type row for soybean LOX-1: 28 isotope effects and 9 temperature series,
  all `verified`, with 12 new enzyme variants and 12 steps. The second reading added the D(kcat/KM) of soybean LOX-1,
  removed a pH the source does not state for S031 and set the range of the BmGDH series. `MR_PSEPU_WT` gains the PDB
  entries 1GWJ and 2R14, and the acceptor of its reductive half-reaction becomes FMN N5, as S029 names it.
  SCHEMA.md: conventions for EC numbers and isotope-labelled proteins written down.
  See `curation/2026-11-07_second_reading_S029-S033/`.

## 2026-11-07 21:01
- S024–S028 entered and read twice: nitroalkane oxidase (Fusarium oxysporum; proton abstraction from nitroethane),
  the aromatic amino acid hydroxylases (rat PheH and Δ117PheH, rat TyrH, rabbit TrpH102–416; benzylic H-atom
  abstraction, intrinsic primary and α-secondary effects), formate dehydrogenase (Candida boidinii; intrinsic H/T,
  H/D and D/T temperature dependence), the cyanobacterial lipoxygenase NspLOX (wild type, I219A) and soybean
  lipoxygenase-1 L546A/L754A at six temperatures: 25 isotope effects and 11 temperature series, all `verified`, with
  8 new enzyme variants and 8 steps. After the second reading the CD3 isotope effects of S025 count as
  `noncompetitive`, and rat PheH and TyrH list only PDB entries of the same construct; a later paper of the same group
  shows that S026 used a commercial FDH of unknown sequence, so no PDB entry is assigned. SCHEMA.md: conventions for
  truncated constructs written down. See `curation/2026-11-07_second_reading_S024-S028/`.

## 2026-11-07 20:02
- S019–S023 entered and read twice: E. coli DHFR (wild type, G121V; pre-steady state and pH 9.5), E. coli
  thymidylate synthase (wild type, Y94F; proton abstraction and hydride transfer), glutamate mutase (GlmES fusion;
  H-atom transfer), four protochlorophyllide oxidoreductases (hydride transfer and solvent isotope effects) and
  phosphite dehydrogenase (17X, T104S, T104A, T104G): 45 isotope effects and 24 temperature series, all
  `verified`, with 12 new enzyme variants and 17 steps. The second reading corrected the organism of the glutamate
  mutase (Clostridium tetanomorphum) and added PDB entries of the PORs and of 17X-PTDH. SCHEMA.md: conventions for
  `quantity` of intrinsic values, intramolecular competition and wild-type PDB entries written down.
  See `curation/2026-11-07_second_reading_S019-S023/`.

## 2026-11-07 18:43
- S014–S018 entered and read twice: five open-access papers on E. coli DHFR (M42W; I14V, I14G), soybean
  lipoxygenase-1 (L546A/I553A; L546A/L754A) and ht-ADH (L176V, L176A, L176G, L176Δ, V260A): 8 isotope effects and
  11 temperature series, all `verified`, with 10 new enzyme variants and their steps. The second reading found the
  PDB entries 4QLG and 4QLF of I14V and I14G, which the first reading had missed.
  See `curation/2026-11-07_second_reading_S014-S018/`.

## 2026-11-07 13:41
- Second check of 7 enzyme rows (`ai-2`): UniProt, EC, organism and variant agree in all 7; `SLO1_SOYBN_I553G` gains
  PDB 5TQP; notes on the TMADH residue numbering and the E. coli strain. `MR_PSEPU_WT` and `PETNR_ENTCL_WT` stay
  `single` until a person checks them. SCHEMA.md: rules for `variant` and `pdb` made precise.
  See `curation/2026-11-07_second_check_enzymes/`.

## 2026-11-07 12:45
- S013 (Wang et al. 2006, E. coli DHFR G121V) entered and read twice: 5 isotope effects and 3 temperature series,
  all `verified`. See `curation/2026-11-07_second_reading_S013/`.

## 2026-11-06
- Database set up: schema, curation rules, validator, licences, reading list.
- S002, S006, S007 and S009 entered and read twice: 20 isotope effects and 12 temperature series, all `verified`.
  See `curation/2026-11-06_second_reading/`.
