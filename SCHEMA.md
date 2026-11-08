# Schema

Four tables in `data/`, CSV, UTF-8. The unit of the database is one **hydrogen-transfer
step**: one enzyme variant, one substrate, one hydrogen moving from a donor atom to an
acceptor atom. Every isotope effect belongs to one step and comes from one primary source.

## `enzymes.csv`: one row per enzyme or variant

| field | meaning |
|---|---|
| `enzyme_id` | unique short id, e.g. `SLO1_SOYBN_WT` |
| `name` | name as used in the source |
| `ec` | EC number as UniProt gives it now, may be empty; a different number printed by the source goes into `notes` |
| `organism` | species |
| `uniprot` | UniProt accession |
| `variant` | `WT` or the mutation(s), e.g. `I553A`; several mutations joined by `/` (e.g. `G121V/M42W`), in the numbering of the source; a truncated construct as the source names it (e.g. `Δ117`, `102–416`); an isotope-labelled protein by its labels (e.g. `heavy (13C, 15N, 2H)`) |
| `pdb` | PDB entries of exactly this variant, separated by `;`; sequence differences that RCSB lists but the study did not engineer go into `notes`; for a wild type with very many entries the field stays empty and `notes` names the entries the source uses; entries of a shorter construct (a truncation or a single domain) are named in `notes`, not listed, while a missing initiator Met, tags or a removed transit peptide do not count |
| `status` | `verified`, `single` or `disputed` (see CURATION.md) |
| `notes` | free text |

## `steps.csv`: one row per hydrogen-transfer step

| field | meaning |
|---|---|
| `step_id` | unique id, e.g. `SLO1_SOYBN_WT_LA` |
| `enzyme_id` | refers to `enzymes.csv` |
| `substrate` | the hydrogen donor molecule, as named in the source |
| `donor` | the atom the hydrogen leaves, e.g. `linoleic acid C11` |
| `acceptor` | the atom the hydrogen goes to, e.g. `Fe(III)–OH oxygen` |
| `transfer` | `H_atom`, `hydride`, `proton`, `PCET` or `unknown`, as the source assigns it |
| `status`, `notes` | as above |

## `measurements.csv`: one isotope effect at one temperature

| field | meaning |
|---|---|
| `meas_id` | unique id, e.g. `M0001` |
| `step_id` | refers to `steps.csv` |
| `labelled_position` | where the heavy isotope sits, e.g. `C11, both H (11,11-d2)` |
| `kie_type` | `primary` (the transferred hydrogen), `secondary` (a hydrogen that is not transferred), `solvent` (D2O) or `other` |
| `isotopes` | `H/D`, `H/T` or `D/T`; effects of labelling the protein itself (heavy-enzyme effects) are not entered |
| `quantity` | the rate the effect is on: `kcat`, `kcat/KM`, `single_turnover` (a single-turnover or pre-steady-state rate constant) or `other`; an intrinsic value calculated from competitive kcat/KM KIEs (Northrop method) keeps `kcat/KM` |
| `method` | `noncompetitive` (light and heavy measured separately), `competitive` (both in one mixture, also intramolecular competition within one molecule) or `other` |
| `kind` | `intrinsic` only when the source says so, otherwise `observed` |
| `value` | the isotope effect, light over heavy |
| `error` | the ± value as printed, empty if none is given |
| `temperature_K` | in kelvin |
| `pH` | as a number |
| `conditions` | buffer and anything else the source states |
| `doi` | DOI of the primary source |
| `location` | where the number stands: `Table 1`, `Fig. 3`, `p. 1148` |
| `as_printed` | the number exactly as printed, with its unit, at most 15 words |
| `extracted_by` | who read it first |
| `checked_by` | who read it a second time, independently |
| `status` | `verified`, `single` or `disputed` |
| `notes` | free text, e.g. whether `error` is a standard deviation or a standard error |

## `temperature.csv`: one temperature series, as fitted in the source

Isotope effects on the Arrhenius parameters. Fields that also occur in `measurements.csv`
mean the same.

| field | meaning |
|---|---|
| `temp_id` | unique id, e.g. `T0001` |
| `step_id`, `labelled_position`, `kie_type`, `isotopes`, `quantity`, `method`, `kind` | as above |
| `T_min_K`, `T_max_K` | measured range, in kelvin; both empty if the source does not state it |
| `n_temperatures` | number of temperatures, empty if not stated |
| `AH_AX`, `AH_AX_error` | ratio of the Arrhenius pre-factors, light over heavy (A_H/A_D for H/D) |
| `dEa_kcal`, `dEa_error` | E_a(heavy) − E_a(light), in kcal/mol |
| `Ea_light_kcal`, `Ea_light_error` | E_a of the light isotope, in kcal/mol |
| `pH`, `conditions`, `doi`, `location`, `as_printed`, `extracted_by`, `checked_by`, `status`, `notes` | as above |

## Units and derived quantities

Temperatures in kelvin, energies in kcal/mol. A value given in °C or kJ/mol is converted
(T + 273.15, given to two decimals; kJ/mol ÷ 4.184, given to four significant figures); the
original stays in `as_printed`. Results of an Eyring analysis (A′H:A′D and ΔΔH‡) go into `AH_AX` and `dEa_kcal`,
since the isotope differences are the same as in an Arrhenius analysis; `notes` says so.

Derived quantities, such as Swain–Schaad exponents or whether a step counts as tunnelling,
are not stored. They are computed from these tables by code.
