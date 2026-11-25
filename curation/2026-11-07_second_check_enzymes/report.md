# Second check of the enzyme rows (ai-2), report

(English translation of the second checker's report, made on 24 November 2026; the German original as delivered is
`report_de.md`. Sources used by the checker: UniProt REST, ExPASy ENZYME, RCSB Search v2 and Data GraphQL, and the
texts of S002, S007, S009, S013.)

## Report by row

**SLO1_SOYBN_I553V / I553L / I553G (S002, Meyer/Tomchick/Klinman 2008)**
- Name in the paper: "soybean lipoxygenase-1 (SLO-1)", otherwise SLO-1 / WT-SLO-1 throughout.
- UniProt **P08170 (LOX1_SOYBN)**, Swiss-Prot, *Glycine max*, 839 aa. Correct because it is the only reviewed seed 13S-lipoxygenase-1 of soybean (EC 1.13.11.12), and position 553 = Ile and all other residues named in the paper (L546, L754, H499, Q495, Q697) agree residue by residue. No offset: paper numbering = UniProt numbering. The paper names no cultivar (the methods refer only to refs. 1, 2, 6).
- EC: the paper prints no EC number. UniProt and ExPASy today **1.13.11.12** (ExPASy: "Formerly EC 1.13.1.13 and EC 1.99.2.1").
- Spelling of the mutations in the paper: I553V / I553L / I553G in the text, "Ile553 → Val/Leu/Gly" in Table 1.
- PDB: **3BND (I553V, 1.60 Å), 3BNB (I553L, 1.45 Å), 3BNC (I553G, 1.65 Å)**; all cite DOI 10.1073/pnas.0710643105, so they are the structures of this paper; in addition **5TQP** (I553G, 300 K, DOI 10.1021/acscentsci.7b00142, a later paper). The paper itself names no PDB ID (only SI Table 5 and APS 19-ID), but the resolutions in the text (1.45/1.60/1.40/1.65 Å for I553L/I553V/I553A/I553G) match 3BNB/3BND/3BNE/3BNC exactly.
- Important: for 3BNB/3BNC/3BND/3BNE, RCSB lists **S160E** in addition to I553X. This is not a second intended mutation but a clone or variant difference from P08170: all recombinant SLO-1 entries including WT (3PZW, 5T5V, 4WFO, 9O4S, 9O4T) carry E160, the plant-purified 1YGE/1F8N carry S160, and the TrEMBL soybean LOX1 sequences D6PAW3, A0A445IEH7, A0A0R0H569 also have E at 160.

**DHFR_ECOLI_G121V_M42W (S009, Wang/Goodey/Benkovic/Kohen 2006) and DHFR_ECOLI_G121V (S013, Wang/Tharp/Selzer/Benkovic/Kohen 2006)**
- Name: S009 "dihydrofolate reductase", "Escherichia coli DHFR (ecDHFR)"; S013 "E. coli dihydrofolate reductase (ecDHFR)", the mutant as "G121V-ecDHFR".
- UniProt **P0ABQ4 (DYR_ECOLI)**, Swiss-Prot, *E. coli* K12, 159 aa. Position 121 = G, position 42 = M, position 20 = M; all consistent, no offset (the initiator Met is counted; there is no "Initiator methionine removed" feature). The second reviewed entry P0ABQ5 (DYR_ECOL6, CFT073) has the same sequence but is PE=3 and has no PDB cross-references; neither paper names a strain.
- EC: not printed in the papers; today **1.5.1.3** (ExPASy: "Formerly EC 1.5.1.4").
- Spelling: S009 writes **"G121V–M42W"** (en dash) or "G121V, M42W", never with a slash. The "G121V/M42W" of the input list is therefore a rewriting, not the spelling of the source. S013: "G121V".
- PDB: **no** structure of G121V and none of G121V–M42W. Checked by aligning all 182 entities that map to P0ABQ4 against the UniProt sequence: no substitution at 121; the only change at 42 at all is M42Y in 2D0K (a methionine-free sevenfold mutant), which is a different mutation in a different construct. RCSB full text "G121V" and "M42W": 0 hits. Neither paper names a PDB ID.

**TMADH_METME_H172Q and TMADH_METME_Y169F (S007, Basran/Sutcliffe/Scrutton 2001)**
- Name: "trimethylamine dehydrogenase (TMADH)". Organism in the paper: WT "purified from *Methylophilus methylotrophus* (sp. W3A1)"; the mutants are recombinant (reference to refs. 30, 40).
- UniProt **P16099 (DHTM_METME)**, Swiss-Prot, *Methylophilus methylotrophus* ("Bacterium W3A1", taxon 17; strain taxon 2327 = W3A1), 730 aa. The only reviewed TMADH entry.
- **Numbering offset +1**: P16099 is the precursor with "Initiator methionine 1 Removed", chain 2–730. The paper counts the mature protein: His-172 (paper) = **UniProt H173**, Tyr-169 = **UniProt Y170**, Asp-267 = UniProt D268, covalent 6-S-cysteinyl-FMN Cys30 = UniProt C31 (UniProt "Modified residue 31"). In the paper's numbering the wild-type residues are His at 172 and Tyr at 169, so H172Q and Y169F are consistent. The PDB author numbering follows the paper (auth 172 = H, auth 169 = Y in 2TMD, 1DJN, 1DJQ, 1O94, 1O95).
- EC: the paper prints **EC 1.5.99.7**; at ExPASy this entry is today only "Transferred entry: 1.5.8.2". Current: **EC 1.5.8.2** ("Formerly EC 1.5.99.7", DR P16099).
- PDB: **no** structure of H172Q or Y169F. Only five entities map to P16099: 2TMD, 1DJN, 1O94, 1O95 (wild-type sequence) and 1DJQ (C30A in the paper's system = C31A in UniProt numbering). Full text "H172Q" returns only 8EHJ (SARS-CoV-2 main protease), "Y169F" seven unrelated proteins (Cel6A, UbiX, prion segments, NADPH dehydrogenase). The paper names no PDB ID.

## Unclear

- **S160E in 3BNB/3BNC/3BND**: the checker lists the entries as "exactly this variant" and notes S160E. A strict filter for "no further mutation" would leave all three cells empty, but then no recombinant WT SLO-1 entry would stand either. A decision by the curator is needed.
- **5TQP as a second I553G entry**: a different publication (ACS Cent. Sci. 2017, 300 K). `SCHEMA.md` does not say whether `pdb` should hold only the structures of the source or all structures of the variant; both are named here.
- **Spelling of the variant G121V/M42W**: S009 never uses a slash. If the `variant` field is meant "as in the source", the row would have to read `G121V–M42W` (or `G121V-M42W`); the ID can stay unchanged.
- **Strains**: neither S009 nor S013 names an *E. coli* strain for the *folA* gene; P0ABQ4 (K12) was chosen as the Swiss-Prot entry. Its sequence is identical to P0ABQ5, so the sequence check does not tell the two apart.
- **SI of S002 not available**: the SI (Table 5 with the crystallographic details, possibly with PDB codes) was not among the files. That the structures of this paper are 3BNB/3BNC/3BND/3BNE rests on the RCSB citation (same DOI) and the matching resolutions, not on an ID printed in the text.
- **Source of S013** is the PMC author manuscript, not the version of record; page and table numbering may differ (without consequence for this table, which holds no measured values).
