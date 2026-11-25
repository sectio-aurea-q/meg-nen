# Second check of the enzyme rows (ai-2), report as delivered

(Saved by the curator from the second checker's final answer; the checker wrote it in German. Sources used by the
checker: UniProt REST, ExPASy ENZYME, RCSB Search v2 and Data GraphQL, and the texts of S002, S007, S009, S013.)

## Bericht je Zeile

**SLO1_SOYBN_I553V / I553L / I553G (S002, Meyer/Tomchick/Klinman 2008)**
- Name im Paper: „soybean lipoxygenase-1 (SLO-1)", sonst durchgehend SLO-1 / WT-SLO-1.
- UniProt **P08170 (LOX1_SOYBN)**, Swiss-Prot, *Glycine max*, 839 aa. Richtig, weil: einzige reviewte 13S-Lipoxygenase-1 des Sojabohnensamens (EC 1.13.11.12), und Position 553 = Ile sowie alle weiteren im Paper genannten Reste (L546, L754, H499, Q495, Q697) stimmen residuengenau. Kein Offset — Paper- = UniProt-Nummerierung. Eine Kultivarangabe nennt das Paper nicht (Methoden verweisen nur auf Lit. 1, 2, 6).
- EC: Paper druckt keine EC-Nummer. UniProt und ExPASy heute **1.13.11.12** (ExPASy: „Formerly EC 1.13.1.13 and EC 1.99.2.1").
- Mutationsschreibweise im Paper: I553V / I553L / I553G im Text, „Ile553 → Val/Leu/Gly" in Table 1.
- PDB: **3BND (I553V, 1.60 Å), 3BNB (I553L, 1.45 Å), 3BNC (I553G, 1.65 Å)** — alle zitieren DOI 10.1073/pnas.0710643105, also die Strukturen dieses Papers; zusätzlich **5TQP** (I553G, 300 K, DOI 10.1021/acscentsci.7b00142, späteres Paper). Das Paper selbst nennt keine PDB-ID (nur SI Table 5 + APS 19-ID), die Auflösungen im Text (1.45/1.60/1.40/1.65 Å für I553L/I553V/I553A/I553G) passen aber exakt zu 3BNB/3BND/3BNE/3BNC.
- Wichtig: RCSB führt bei 3BNB/3BNC/3BND/3BNE neben I553X zusätzlich **S160E**. Das ist keine zweite Absichtsmutation, sondern eine Klon-/Variantendifferenz zu P08170: alle rekombinanten SLO-1-Einträge inklusive WT (3PZW, 5T5V, 4WFO, 9O4S, 9O4T) tragen E160, die pflanzlich gereinigten 1YGE/1F8N tragen S160, und die TrEMBL-Soja-LOX1-Sequenzen D6PAW3, A0A445IEH7, A0A0R0H569 haben an 160 ebenfalls E.

**DHFR_ECOLI_G121V_M42W (S009, Wang/Goodey/Benkovic/Kohen 2006) und DHFR_ECOLI_G121V (S013, Wang/Tharp/Selzer/Benkovic/Kohen 2006)**
- Name: S009 „dihydrofolate reductase", „Escherichia coli DHFR (ecDHFR)"; S013 „E. coli dihydrofolate reductase (ecDHFR)", Mutante als „G121V-ecDHFR".
- UniProt **P0ABQ4 (DYR_ECOLI)**, Swiss-Prot, *E. coli* K12, 159 aa. Position 121 = G, Position 42 = M, Position 20 = M — alle konsistent, kein Offset (Initiator-Met wird mitgezählt, kein „Initiator methionine removed"-Feature). Das zweite reviewte Entry P0ABQ5 (DYR_ECOL6, CFT073) hat dieselbe Sequenz, ist aber PE=3 und ohne PDB-Querverweise; beide Paper nennen keinen Stamm.
- EC: kein Abdruck im Paper; heute **1.5.1.3** (ExPASy: „Formerly EC 1.5.1.4").
- Schreibweise: S009 schreibt **„G121V–M42W"** (Halbgeviertstrich) bzw. „G121V, M42W" — nie mit Schrägstrich. Das „G121V/M42W" in der Eingabeliste ist also eine Umschreibung, nicht die Quellschreibweise. S013: „G121V".
- PDB: **keine** Struktur für G121V und keine für G121V–M42W. Geprüft durch Alignment aller 182 Entities, die auf P0ABQ4 abbilden, gegen die UniProt-Sequenz: keine Substitution an 121; die einzige Änderung an 42 überhaupt ist M42Y in 2D0K (methioninfreie Siebenfachmutante) — andere Mutation, anderes Konstrukt. RCSB-Volltext „G121V" und „M42W": 0 Treffer. Keines der beiden Paper nennt eine PDB-ID.

**TMADH_METME_H172Q und TMADH_METME_Y169F (S007, Basran/Sutcliffe/Scrutton 2001)**
- Name: „trimethylamine dehydrogenase (TMADH)". Organismus im Paper: WT „purified from *Methylophilus methylotrophus* (sp. W3A1)"; die Mutanten sind rekombinant (Verweis auf Lit. 30, 40).
- UniProt **P16099 (DHTM_METME)**, Swiss-Prot, *Methylophilus methylotrophus* („Bacterium W3A1", Taxon 17; Stamm-Taxon 2327 = W3A1), 730 aa. Einziges reviewtes TMADH-Entry.
- **Nummerierungs-Offset +1**: P16099 ist der Präkursor mit „Initiator methionine 1 Removed", Chain 2–730. Das Paper zählt das reife Protein: His-172 (Paper) = **UniProt H173**, Tyr-169 = **UniProt Y170**, Asp-267 = UniProt D268, kovalentes 6-S-Cysteinyl-FMN Cys30 = UniProt C31 (UniProt „Modified residue 31"). In Paper-Nummerierung sind die Wildtyp-Reste an 172 His und an 169 Tyr — H172Q und Y169F sind damit konsistent. Die PDB-Autorennummerierung folgt dem Paper (auth 172 = H, auth 169 = Y in 2TMD, 1DJN, 1DJQ, 1O94, 1O95).
- EC: Paper druckt **EC 1.5.99.7**; dieser Eintrag ist bei ExPASy heute nur noch „Transferred entry: 1.5.8.2". Aktuell: **EC 1.5.8.2** („Formerly EC 1.5.99.7", DR P16099).
- PDB: **keine** Struktur von H172Q oder Y169F. Nur fünf Entities bilden auf P16099 ab: 2TMD, 1DJN, 1O94, 1O95 (Wildtyp-Sequenz) und 1DJQ (C30A im Paper-System = C31A in UniProt-Nummerierung). Volltext „H172Q" liefert allein 8EHJ (SARS-CoV-2-Hauptprotease), „Y169F" sieben fremde Proteine (Cel6A, UbiX, Prion-Segmente, NADPH-Dehydrogenase). Das Paper nennt keine PDB-ID.

## Unclear

- **S160E bei 3BNB/3BNC/3BND**: Ich führe die Einträge als „exakt diese Variante" und vermerke S160E. Wer streng nach „keine weitere Mutation" filtert, müsste alle drei Zellen leer lassen — dann hätte aber auch kein rekombinanter WT-SLO-1-Eintrag Bestand. Entscheidung durch die Kuratorin nötig.
- **5TQP als zweiter I553G-Eintrag**: andere Publikation (ACS Cent Sci 2017, 300 K). Ob `pdb` nur die Strukturen der Quelle oder alle Strukturen der Variante aufnehmen soll, legt SCHEMA.md nicht fest; ich habe beide genannt.
- **Variantenschreibweise G121V/M42W**: in S009 steht nie ein Schrägstrich. Falls das `variant`-Feld „wie in der Quelle" sein soll, müsste die Zeile `G121V–M42W` (oder `G121V-M42W`) heißen; die ID darf unverändert bleiben.
- **Stämme**: Weder S009 noch S013 nennen einen *E.-coli*-Stamm für das *folA*-Gen; ich habe P0ABQ4 (K12) als Swiss-Prot-Entry gewählt, die Sequenz ist mit P0ABQ5 identisch, der Sequenz-Check unterscheidet die beiden also nicht.
- **S002-SI nicht vorhanden**: Die SI (Table 5 mit den Kristallografie-Details, evtl. mit PDB-Codes) liegt nicht in `in/`. Dass die Strukturen dieses Papers 3BNB/3BNC/3BND/3BNE sind, stützt sich auf die RCSB-Zitation (gleiche DOI) und die übereinstimmenden Auflösungen, nicht auf eine im Text gedruckte ID.
- **S013-Quelle** ist das PMC-Autorenmanuskript, nicht die Verlagsfassung; Seiten-/Tabellenzählung kann abweichen (für diese Tabelle ohne Folgen, da keine Messwerte).
