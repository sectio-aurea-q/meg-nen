# S016 Sharma und Klinman 2008 – Leser 2 – Antworten

Quellen: Artikel (PMC-HTML, PMC2671078), Seitentext des Zusatzmaterials (S2 bis S7).
Gedruckte Angaben und eigene Nachrechnungen sind getrennt gekennzeichnet.
Rechenskripte: <workdir>/l2scripts/calc.py, calc2.py, calc3.py.

## A. Tabellen

- tableS1.csv: 8 Zeilen (15 bis 50 °C in 5-Grad-Schritten), Korrekturfaktor mit drei Nachkommastellen.
- tableS2.csv: 8 Zeilen, dieselben Temperaturen. Spaltenkopf im Seitentext umgebrochen
  ("Dkcat" am Zeilenende, "D(kcat/KM)" in eigener Zeile); Zuordnung der sechs Wertepaare je Zeile:
  kcat(H), kcat(D), KM(H), KM(D), Dkcat, D(kcat/KM). Geprüft über die Quotienten (siehe C1): passt nur in dieser Reihenfolge.
- Nachgestellte Nullen wie gedruckt: 0.0150 (25 °C), 0.0010 (45 °C).

## B. n_temperatures für T0021

**8** (H: 15, 20, 25, 30, 35, 40, 45, 50 °C; D: dieselben).

- Gedruckt: Tabelle S2 mit je einem kcat(H) und kcat(D) je Temperatur, 8 Zeilen. Artikel, Tabelle 1 Fußnote a:
  "Data were collected from 15 to 50 °C." Artikeltext: "The rate of catalysis for the double mutant … between 15 and 50 °C is shown in Figure 1."
- Keine ausdrückliche Zahl der Fit-Punkte, keine Schrittweite im Text (sie ergibt sich nur aus der Tabelle).
- Die Quelle sagt **nicht** ausdrücklich, dass alle tabellierten Temperaturen in den Fit eingingen, und nennt **keinen** Ausschluss – weder für H noch für D.
- Abb. 1 liegt im HTML nur als Bild vor; Punkte daraus nicht gezählt.
- Stütze durch Nachrechnung (keine gedruckte Angabe): der Fit über alle 8 Punkte trifft Tabelle 1 (siehe C3). Die Auslassprobe trennt aber nicht scharf:
  ohne 30 °C (3.80; AH/AD 1.08) oder ohne 35 °C (3.81; 1.01) käme man gerundet ebenfalls in die Nähe; nur alle 8 treffen Ea(H), AH und AH/AD zugleich genau.

## C1. Innere Stimmigkeit der Tabelle S2

Dkcat = kcat(H)/kcat(D), nachgerechnet aus den gedruckten Werten:

| T | H/D | gedruckt | Urteil |
|---|---|---|---|
| 15 | 137.62 | 137 | innerhalb der Eingaberundung (136.45–138.81); abgeschnitten statt gerundet |
| 20 | 145.95 | 146 | passt |
| 25 | 143.33 | 143 | passt |
| 30 | 128.49 | 128 | passt |
| 35 | 115.51 | 115 | passt (Grenzfall) |
| 40 | 102.30 | 102 | passt |
| 45 | 86.94 | 87 | passt |
| 50 | 91.90 | **91** | **passt nicht**: aus 2.95/0.0321 folgt 91.9; mit Eingaberundung 91.60–92.20, gerundet stets 92 |

D(kcat/KM) = [kcat(H)/KM(H)]/[kcat(D)/KM(D)]:

| T | berechnet | Spanne aus Eingaberundung | gedruckt | Urteil |
|---|---|---|---|---|
| 15 | 51.96 | 51.24–52.68 | 51 | um 1 daneben (52 erwartet), noch in der Spanne |
| 20 | 21.48 | 21.11–21.86 | 22 | knapp, in der Spanne |
| 25 | 15.32 | 15.01–15.62 | 15 | passt |
| 30 | 25.58 | 25.09–26.07 | 25 | knapp (26 erwartet), in der Spanne |
| 35 | 22.72 | 22.05–23.41 | 23 | passt |
| 40 | 26.63 | 26.15–27.12 | 27 | passt |
| 45 | 36.15 | 35.43–36.89 | **35** | um 1 daneben (36 erwartet); nur am unteren Rand der Spanne erreichbar |
| 50 | 54.39 | 53.47–55.32 | 54 | passt |

Ergebnis: Die Spaltenzuordnung ist gesichert. Eine Zeile passt streng nicht (50 °C, Dkcat 91 statt 92). Mehrere Werte wirken abgeschnitten
statt gerundet (15 °C: 137; 50 °C: 91; D(kcat/KM) bei 15, 30, 45 °C) – oder sie wurden aus ungerundeten kcat/KM gebildet. Aus der Quelle nicht entscheidbar.

Verlauf: Dkcat ist nicht monoton (137, 146, 143, 128, 115, 102, 87, 91); kcat(H) fällt von 30 auf 35 °C (2.21 → 2.16).

## C2. Fehler in Klammern bei Dkcat

Vergleich gedruckter Fehler mit dem aus kcat(H) und kcat(D) fortgepflanzten (Nachrechnung, relative Fehler quadratisch addiert):

| T | Dkcat gedruckt | fortgepflanzt | D(kcat/KM) gedruckt | fortgepflanzt (mit KM-Fehlern) |
|---|---|---|---|---|
| 15 | 137 (1) | 5.7 | 51 (2) | 8.3 |
| 20 | 146 (2) | 7.5 | 22 (2) | 5.5 |
| 25 | 143 (1) | 5.5 | 15 (1) | 3.0 |
| 30 | 128 (3) | 5.7 | 25 (3) | 5.0 |
| 35 | 115 (1) | 3.2 | 23 (1) | 3.4 |
| 40 | 102 (1) | 3.0 | 27 (1) | 3.6 |
| 45 | 87 (1) | 3.6 | 35 (1) | 7.1 |
| 50 | 91 (1) | 2.9 | 54 (3) | 8.6 |

- Die gedruckten Fehler der Isotopeneffekte sind 2- bis 7-mal kleiner als die fortgepflanzten. Sie sind also **nicht** die Fehlerfortpflanzung der daneben gedruckten kcat-Fehler. Was sie sind, sagt die Quelle nicht.
- Art der Fehler: weder Artikel noch Zusatzmaterial nennen sie (Standardabweichung, Standardfehler des Michaelis-Menten-Fits, Vertrauensbereich – nichts gedruckt). Einziger Satz dazu (Zusatzmaterial S3):
  "The errors associated with each kcat measurements were used to weight the exponential Arrhenius fit."
- Zahl der Messungen/Wiederholungen: **nirgends angegeben**. Achtung Lesefalle: im Seitentext steht "The initial / 6 / rates were fitted to the Michaelis-Menten equation" –
  die 6 ist die hochgestellte Fußnotenziffer (Lit. 6 = KaleidaGraph), keine Anzahl von Raten.
- Folge für die Datenbank: Dkcat 128 (3) bei 30 °C trägt einen Fehler unbekannter Art; fortgepflanzt wären es etwa ±6.

## C3. Korrigiert oder unkorrigiert

Was der Text sagt (Zusatzmaterial S3/S4):
- Eisengehalt: "The rate constants were corrected for the iron content of the mutant enzyme as determined by ICP" – ohne Zahl; ob Tabelle S2 diese Korrektur schon enthält, steht nicht da. Sie wäre ein gemeinsamer Faktor für H und D und änderte weder Isotopeneffekt noch Steigung.
- O2-Sättigung: "A correction was applied for the Leu546Ala/Ile553Ala SLO double mutant to account for a small degree of subsaturating O2 using the protio-substrate."
  Für D: "the greatly reduced Km for O2 with the dideutero-substrate ensured saturating conditions at all temperatures investigated." Also laut Text **nur H** korrigiert, D nicht.
  Faktoren je Temperatur in Tabelle S1 (1.022 bis 1.195), gemessen mit Clark-Elektrode, 80 µM LA, Umgebungsluft gegen 100 % O2.
- Tabelle S2 heißt "Empirical rate constants", Tabelle S1 "Correction of empirical rate constants" – S2 ist danach hinsichtlich O2 unkorrigiert.

Was gedruckt ist (Befund):
- Tabelle 1 des Artikels, Zeile 546A/553A: kcat 2.21 (0.09) und KIE 128 (3) bei 30 °C sind **wortgleich** die "empirischen" Werte der Tabelle S2.
  Mit Faktor 1.116 wären es kcat 2.47 und Dkcat 143. Die Einzelwerte der Tabelle 1 sind also **nicht** O2-korrigiert.
- kcat/KM in Tabelle 1: 0.11 (0.02). Aus Tabelle S2: 2.21/21.6 = 0.102 (fortgepflanzt ±0.018); mit Faktor 1.116: 0.114. Gedruckt 0.11 passt besser zum korrigierten Wert, 0.10 wäre der unkorrigierte – nicht entscheidbar (kcat/KM kann direkt aus dem Fit stammen).

Ändert die Korrektur der Tabelle S1 Isotopeneffekt und Steigung? Ja, rechnerisch beides: Sie wirkt nur auf H, ist temperaturabhängig und nicht monoton (Höchstwert 1.195 bei 25 °C).
Dkcat würde 141, 154, 171, 143, 122, 111, 95, 94 statt 137 … 91.

Nachrechnung der Arrhenius-Fits (**eigene Rechnung, keine gedruckte Angabe**; R = 1.9872 cal/(mol K); T = °C + 273.15):

| Variante | Ea(H) | Ea(D) | ΔEa | AH (s-1) | AH/AD |
|---|---|---|---|---|---|
| **gedruckt, Tabelle 1** | 3.8 (0.4) | – | 2.8 (0.4) | 1.1e3 (5e2) | 1.05 (0.45) |
| gewichtet, exponentiell (nichtlinear), ohne S1 | 3.57 (0.11) | 6.45 (0.18) | 2.89 (0.21) | 776 | 1.02 (0.35) |
| gewichtet, exponentiell, mit S1 auf H | 3.36 (0.11) | 6.45 | 3.10 (0.21) | 586 | 0.77 (0.26) |
| gewichtet, linear in ln k, ohne S1 | 3.48 (0.12) | 6.50 (0.17) | 3.02 (0.21) | 675 | 0.82 (0.28) |
| gewichtet, linear in ln k, mit S1 auf H | 3.10 (0.12) | 6.50 | 3.39 (0.21) | 395 | 0.48 (0.16) |
| **ungewichtet, linear in ln k, ohne S1** | **3.77 (0.46)** | **6.63 (0.41)** | **2.86 (0.62)** | **1.09e3 (8e2)** | **1.05 (1.07)** |
| ungewichtet, linear in ln k, mit S1 auf H | 3.70 (0.76) | 6.63 | 2.93 (0.86) | 1.04e3 | 1.00 (1.43) |
| ungewichtet, exponentiell, ohne S1 | 3.52 (0.43) | 6.54 (0.55) | 3.03 | 723 | 0.80 |
| ungewichtet, exponentiell, mit S1 auf H | 3.24 (0.72) | 6.54 | 3.31 | 493 | 0.54 |

(Fehler in Klammern: bei gewichteten Fits aus den gedruckten Fehlern; bei ungewichteten aus der Streuung. Reduziertes Chi-Quadrat der gewichteten Fits 9 bis 14 ohne S1, 37 bis 39 für H mit S1 –
die gedruckten kcat-Fehler sind viel kleiner als die Streuung um die Gerade; die Korrektur macht die H-Gerade schlechter, nicht besser.)

Klares Ergebnis:
- Die gedruckten Werte der Tabelle 1 trifft der **ungewichtete lineare Fit von ln kcat gegen 1/T über alle 8 Temperaturen mit den unkorrigierten Werten der Tabelle S2**:
  Ea(H) 3.77 → 3.8; AH 1.09e3 → 1.1e3; AH/AD 1.048 → 1.05; ΔEa 2.86, gedruckt 2.8 = 6.6 − 3.8 (Differenz der gerundeten Ea).
- Die Fits **mit** Korrekturfaktor S1 treffen Tabelle 1 in keiner Variante so gut (ungewichtet: 3.7 / 1.0e3 / 1.00; gewichtet: weit daneben).
- Die im Text behauptete Gewichtung mit den kcat-Fehlern lässt sich nicht bestätigen: gewichtete Fits geben Ea(H) 3.5 bis 3.6 und AH um 700 bis 800, nicht 3.8 und 1.1e3.
  (Nur AH/AD 1.02 und ΔEa 2.89 des gewichteten Exponentialfits ohne S1 lägen nahe; Ea(H) und AH nicht.)
- Die gedruckten Fehler (0.4; 0.4; 5e2; 0.45) werden von keiner Variante genau getroffen (ungewichtet: 0.46 für Ea(H) passt, ΔEa 0.62 und AH/AD ±1.07 sind größer als gedruckt).
- Schluss für T0021: Ea(H), ΔEa und AH/AD der Tabelle 1 stammen nach der Nachrechnung aus den **unkorrigierten** ("empirischen") kcat der Tabelle S2;
  die im Zusatzmaterial beschriebene O2-Korrektur ist in Tabelle 1 nicht sichtbar. Das widerspricht dem Satz "corrected to O2 saturation as needed" nicht dem Wortlaut nach, aber der Erwartung. Kennzeichnung in der Datenbank empfohlen.

## C4. Bedingungen

- pH 9.00 (Zusatzmaterial), 9.0 (Tabelle 1); Puffer 100 mM Borat ("0.1 M borate buffer").
- Substrat: Linolsäure 0.50 bis 80 µM (so gedruckt: "0.50-80 µM"); deuteriert: 11,11-2H2-LA. O2-Elektroden-Versuche: 80 µM LA.
- Atmosphäre: Umgebungsluft, "ambient atmosphere (20.8% O2)"; Vergleichsmessung unter 100 % O2 nur für die Korrektur.
- Messung: UV 234 nm, Bildung von 13-(S)-HPOD, ε234 = 23,600 M-1 cm-1, Cary 50; Temperatur über wassergekühlten Küvettenhalter.
- Temperaturen 15 bis 50 °C. Verzögerungsphase (lag), länger bei D, niedriger Konzentration und T ≤ 30 °C; ausgewertet wird die lineare Phase danach.
- Hinweis: KM(H) bis 39.4 µM bei höchstens 80 µM Substrat – bei 15 bis 25 °C liegt die höchste Konzentration nur beim etwa Zweifachen von KM; kcat ist dort stark extrapoliert.

## D. Auffälligkeiten

Zusatzmaterial / Seitentext:
1. Tabelle S2, 50 °C: Dkcat 91 gedruckt, aus kcat folgt 92 (siehe C1). D(kcat/KM) bei 15, 30, 45 °C je um 1 unter dem Quotienten.
2. Fehler der Isotopeneffekte viel kleiner als fortgepflanzt; Art der Fehler und Zahl der Messungen fehlen ganz.
3. Fußnotenziffer "6" als eigene Zeile mitten im Satz ("The initial 6 rates") – ist Lit. 6 (KaleidaGraph), keine Zahl von Messungen.
4. "11,11-" / "2H2-LA": Hochstellung der 2 verloren und Zeilenumbruch; gemeint 11,11-²H₂-LA.
5. Gradzeichen fehlen durchweg ("37 C", "15 C", "-80 C", "T ≤ 30 C", "T ≥ 45 C", Tabellenköpfe "Temperature C", "T, C"); Einheiten ohne Hochstellung ("s-1", "M-1 cm-1"). "OD600", "ε234" tiefgestellt gemeint.
6. Primer: bei zwei Sequenzen fehlt der Strich hinter der End-3 ("TTT TTG C 3", "TTA G C 3").
7. "QuickChange II" im Text, "QuikChange" im Literaturverzeichnis. Literaturliste: Nummern (1) bis (6) stehen gebündelt in einer Zeile, Zuordnung nur über die Reihenfolge.
8. Überschrift "Kinetics Measurements", im Inhaltsverzeichnis "Kinetic Measurements". "each kcat measurements" (Grammatik). "SLO double mutant" statt SLO-1.
9. Seite S2 endet nach dem Zentrifugieren des Lysats; die Reinigung selbst (Säulen) wird im kopierten Text nicht beschrieben, Seite S3 beginnt gleich mit der Kinetik. Ob im Original Text fehlt oder die Beschreibung dort endet, ist am Seitentext nicht zu erkennen.
10. Korrekturfaktor S1 nicht monoton (1.025, 1.055, 1.195, 1.116, 1.053, 1.088, 1.089, 1.022); ohne Fehlerangabe. "corrected … as needed" lässt offen, wo korrigiert wurde.
11. Eisengehalt: Korrektur behauptet, aber kein Wert gedruckt.

Artikel:
12. Tabelle 1, Fußnote d: "ΔEa = Ea(D) − ΔEa(H)" – Druckfehler, gemeint Ea(D) − Ea(H).
13. Text: "the magnitude and nearly temperature-dependent KIEs" für WT – gemeint "temperature-independent" (davor steht "largely temperature-independent").
14. Text zu Gl. 1: "only weakly isotope independent" – gemeint wohl "weakly isotope dependent".
15. "9,12-(Z,Z)-octadecanoic acid" für Linolsäure – richtig octadecadienoic.
16. "decreased one hundred fifty-fold from that of WT and … Ile553Ala": aus Tabelle 1 folgt 297/2.21 = 134 und 280/2.21 = 127; mit O2-korrigiertem kcat (2.47) 120 und 113. "two-fold" gegen 546A: 4.8/2.21 = 2.2, passt.
17. Tabelle 1 bringt für die Doppelmutante die unkorrigierten Werte (kcat 2.21 (0.09), KIE 128 (3)); Arrhenius-Größen laut Nachrechnung aus unkorrigierten, ungewichtet gefitteten Daten – im Widerspruch zur Beschreibung im Zusatzmaterial (O2-Korrektur für H, gewichteter Fit).
18. AH/AD 1.05 (0.45): der Artikel nennt selbst 0.8 bis 1.4 als "unity"-Bereich; der gedruckte Fehler reicht darüber hinaus (0.60 bis 1.50), der aus der Streuung gerechnete ist noch größer (±1.07). Mit O2-Korrektur läge AH/AD je nach Fit bei 0.5 bis 1.0.
19. Der Artikel selbst nennt weder Fehlerart noch Zahl der Messungen noch die Zahl der Temperaturen; Abb. 1: "error bars are obscured by the symbol".
20. HTML ist das NIH-Autorenmanuskript (NIHMS91462), nicht die Verlagsfassung; Abweichungen zur gedruckten JACS-Seite nicht geprüft.

Datenbank (task.md):
21. Eintrag T0021 (3.8 (0.4); 2.8 (0.4); 1.05 (0.45); 15 bis 50 °C; Dkcat 128 (3)) stimmt mit Tabelle 1 überein. Vorschlag n_temperatures = 8.
