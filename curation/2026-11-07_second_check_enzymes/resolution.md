# Second check of the enzyme rows (7 November 2026)

First reading `ai-1`, second check `ai-2`. The second checker saw only the enzyme names, variants and source papers
(not the identifiers of the first reading) and looked everything up again in UniProt, ExPASy ENZYME and RCSB PDB,
including a sequence check of every mutated residue. Files in this folder:

- `reading2_enzymes.csv`, `report.md`: the second check as delivered (`report.md` saved by the curator from the
  checker's answer, in German)
- `comparison.md`: comparison of both readings, before the decisions below

A first attempt covered all 9 rows but was stopped by an automatic safety check before it wrote its results; nothing
from it is used. The repeat covered 7 rows. `MR_PSEPU_WT` and `PETNR_ENTCL_WT` were left out of the repeat and stay
`single` until a person checks them.

## Result

UniProt accession, EC number, organism and variant agree in all 7 rows; every mutated residue is the stated wild-type
residue in the UniProt sequence. Decisions:

1. **`SLO1_SOYBN_I553G`**: the second check found a second structure of exactly this variant, 5TQP (300 K, released
   2017, later study), confirmed in RCSB by the curator. `pdb` is now `3BNC;5TQP`, because SCHEMA.md asks for the
   entries of this variant, not only those of the source.
2. **`DHFR_ECOLI_G121V_M42W`**: the source writes G121V–M42W. The database keeps `G121V/M42W`; SCHEMA.md now states
   that several mutations are joined by `/`.
3. **Notes taken over from the second check**: TMADH is numbered as the mature protein in the source (His-172 and
   Tyr-169 are H173 and Y170 in UniProt); the DHFR sources name no strain (P0ABQ4 is the K-12 entry, P0ABQ5 has the
   same sequence); 3BNB, 3BNC and 3BND cite the source DOI, though the source prints no PDB ID. The S160E difference
   that RCSB lists for the SLO-1 structures was already noted; it occurs in every recombinant SLO-1 entry, including
   the wild type, and is not an engineered mutation.
4. **SCHEMA.md**: `pdb` now says "exactly this variant", with non-engineered sequence differences in `notes`.

7 of 9 enzyme rows are now `verified`.
