# S016 – Sharma & Klinman 2008, JACS 130, 17632–17633 – Leser 1

Quellen: Artikel (PMC2671078, HTML), Seitentext des Zusatzmaterials (SI, S2–S7, Kopie vom 23.11.2026).
Rechenskripte: `<workdir>/l1/rechnung/calc.py`, `calc2.py`, `calc3.py`.

## A. Tabellen S1 und S2

- `tableS1.csv`: 8 Zeilen (15–50 °C in 5-°C-Schritten), Korrekturfaktoren wie gedruckt (3 Nachkommastellen).
- `tableS2.csv`: 8 Zeilen (15–50 °C). Der Spaltenkopf ist im kopierten Text umgebrochen: „Dkcat" steht am Ende der ersten Kopfzeile, „D(kcat/KM)" allein in der zweiten. Zuordnung der 12 Zahlen je Zeile: kcat(H), kcat(D), KM(H), KM(D), Dkcat, D(kcat/KM), je mit Fehler in Klammern. Die Zuordnung ist durch Nachrechnen gesichert (kcat(H)/kcat(D) ergibt die 5. Spalte, nicht die 6.).
- Einheiten: kcat in s⁻¹, KM in µM (im Text „M-BM-5M" = µM, als µ korrekt kopiert).
- Nachgestellte Nullen wurden übernommen: 0.0150 (0.0005), 0.0010 (Fehler kcat(D) bei 45 °C).

## B. Zahl der Temperaturen im Arrhenius-Fit (T0021)

- **n_temperatures = 8** (H: 15, 20, 25, 30, 35, 40, 45, 50 °C; D: dieselben 8).
- Grundlage: Tabelle S2 druckt je Temperatur einen kcat(H)- und einen kcat(D)-Wert, 15 bis 50 °C in 5-°C-Schritten. Artikel, Tabelle 1, Fußnote a: „Data were collected from 15 to 50 °C." Text: „The temperature dependencies of kcat for both H• and D• abstraction were fitted to the empirical Arrhenius equation to yield Ea and the Arrhenius prefactor, A."
- **Ob alle tabellierten Temperaturen in den Fit eingingen, steht nicht ausdrücklich da.** Es wird auch keine Auslassung genannt (weder für H noch für D). Figure 1 (Arrhenius-Auftragung) liegt nur als Bild vor; die Zahl der Punkte ist im Text nicht angegeben.
- Keine Untergrenze „>=": Unsicher wäre höchstens, ob weniger Punkte eingingen, nicht ob mehr eingingen. Da keine Auslassung erwähnt wird und die Nachrechnung (siehe C) mit allen 8 Punkten Tabelle 1 trifft, trage ich 8 ein. Vermerk: Die volle Aufnahme in den Fit ist erschlossen, nicht gedruckt.

## C. Prüfung der Tabelle S2

### C1. Quotienten je Zeile (Rundung geprüft: Spanne aus ±½ letzter Stelle der Eingangswerte)

| T °C | kcatH/kcatD | gedr. Dkcat | D(kcat/KM) berechnet | gedr. |
|---|---|---|---|---|
| 15 | 137.6 (136.5–138.8) | 137 | 52.0 (51.2–52.7) | 51 |
| 20 | 145.9 | 146 | 21.5 | 22 |
| 25 | 143.3 | 143 | 15.3 | 15 |
| 30 | 128.5 (127.8–129.2) | 128 | 25.6 (25.1–26.1) | 25 |
| 35 | 115.5 | 115 | 22.7 | 23 |
| 40 | 102.3 | 102 | 26.6 | 27 |
| 45 | 86.9 | 87 | 36.2 (35.4–36.9) | 35 |
| 50 | **91.9 (91.6–92.2)** | **91** | 54.4 | 54 |

- **Dkcat 50 °C passt nicht:** 2.95/0.0321 = 91.9. Auch mit der ungünstigsten Rundung der Eingangswerte kommt man auf mindestens 91.6, gedruckt ist 91 (erwartet 92). Knapp, aber außerhalb der Rundung.
- Grenzfälle innerhalb der Rundung: 15 °C Dkcat (137.6, gerundet wäre 138), D(kcat/KM) bei 15 °C (52.0 statt 51), 45 °C (36.2 statt 35, passt nur am Rand: 35.43), 30 °C (25.6 statt 25). Mögliche Ursache: Die Isotopeneffekte wurden aus ungerundeten Werten oder getrennt gefittet. Das wird nicht gesagt.

### C2. Fehler bei Dkcat

Gedruckt sind 1 bis 3. Fortgepflanzt aus den Fehlern von kcat(H) und kcat(D) (relative Fehler quadratisch addiert), eigene Rechnung:

| T °C | 15 | 20 | 25 | 30 | 35 | 40 | 45 | 50 |
|---|---|---|---|---|---|---|---|---|
| gedruckt | 1 | 2 | 1 | 3 | 1 | 1 | 1 | 1 |
| fortgepflanzt | 5.7 | 7.5 | 5.5 | 5.7 | 3.3 | 3.0 | 3.6 | 2.9 |

Die gedruckten Fehler sind 2- bis 5,7-mal kleiner als die fortgepflanzten. Bei D(kcat/KM) ist es ähnlich: gedruckt 1–3, fortgepflanzt 3.0–8.6. Wie der Fehler von Dkcat entstand, sagt die Quelle nicht. Der Dkcat-Fehler ist also **nicht** der aus kcat(H) und kcat(D) fortgepflanzte Fehler.

Art der Fehler und Zahl der Messungen: Weder im Artikel noch im SI steht, ob die Klammerwerte Standardabweichung, Standardfehler oder Fitfehler sind. Auch die Zahl der Wiederholungen wird nicht genannt. Einzige Aussage, SI S3: „The errors associated with each kcat measurements were used to weight the exponential Arrhenius fit." Fußnote (6) im SI verweist auf KaleidaGraph (Fitprogramm). Die kinetischen Parameter stammen aus Michaelis-Menten-Fits der Anfangsgeschwindigkeiten („The initial rates were fitted to the Michaelis-Menten equation to obtain the kinetic parameters kcat and kcat/KM."). Vermutlich sind die Klammerwerte also Fitfehler, das ist aber nicht gedruckt.

### C3. Korrigiert oder unkorrigiert?

Was der Text sagt:
- Eisengehalt (SI S3): „The rate constants were corrected for the iron content of the mutant enzyme as determined by ICP". Das gilt allgemein für die Geschwindigkeitskonstanten, also H und D. Es ist ein temperaturunabhängiger Faktor. Er ändert also weder den Isotopeneffekt noch Ea; er ändert nur die absoluten kcat- und A-Werte.
- O2-Sättigung (SI S3–S4): Die Korrektur gilt **nur für H**: „A correction was applied … to account for a small degree of subsaturating O2 using the protio-substrate." Für D: „the greatly reduced Km for O2 with the dideutero-substrate ensured saturating conditions at all temperatures investigated". Der Faktor je Temperatur steht in Tabelle S1 („Correction of empirical rate constants"). Er ist temperaturabhängig und nicht monoton (1.025 … 1.195 bei 25 °C … 1.022). Er **ändert also den Isotopeneffekt** (Dkcat × Faktor) und **die Steigung** von kcat(H).
- Tabelle S2 heißt „Empirical rate constants …". Zusammen mit dem Titel von S1 bedeutet das: S2 ist **vor** der O2-Korrektur. Ob S2 für den Eisengehalt korrigiert ist, sagt die Quelle nicht.
- Widerspruch: SI S3 sagt „All data presented herein were obtained under ambient atmosphere (20.8% O2) and corrected to O2 saturation as needed". Tabelle S2 ist aber ausdrücklich „empirical".

Tabelle 1 gegen S2, bei 30 °C:
- kcat 2.21 (0.09) und KIE 128 (3) in Tabelle 1 sind **identisch** mit den unkorrigierten S2-Werten. Mit S1-Faktor 1.116 wäre es kcat(H) = 2.47 und Dkcat = 143.4.
- kcat/KM 0.11 (0.02): unkorrigiert 2.21/21.6 = 0.102 (fortgepflanzt ±0.018), korrigiert 0.114. Das ist nicht eindeutig; beides liegt innerhalb des gedruckten Fehlers.

**Nachrechnung (keine gedruckte Angabe)**: Arrhenius-Fits von kcat(H) und kcat(D) aus Tabelle S2 über alle 8 Temperaturen, R = 1.987 cal mol⁻¹ K⁻¹, T + 273.15. Gedruckt in Tabelle 1: Ea(H) 3.8 (0.4), ΔEa 2.8 (0.4), AH 1.1×10³ (5×10²), AH/AD 1.05 (0.45).

| Variante | Ea(H) | ΔEa | AH | AH/AD |
|---|---|---|---|---|
| ohne Korrektur, exponentiell, gewichtet (1/σ²) – wie im SI beschrieben | 3.57 (0.42) | 2.89 (0.69) | 776 | 1.02 |
| ohne Korrektur, ln k gegen 1/T, gewichtet | 3.48 | 3.02 | 675 | 0.82 |
| **ohne Korrektur, ln k gegen 1/T, ungewichtet** | **3.77 (0.46)** | **2.86 (0.62)** | **1.09×10³** | **1.048** |
| ohne Korrektur, exponentiell, ungewichtet | 3.52 | 3.03 | 723 | 0.80 |
| mit S1 auf kcat(H), exponentiell, gewichtet | 3.36 (0.68) | 3.10 (0.87) | 586 | 0.77 |
| mit S1 auf kcat(H), ln k, gewichtet | 3.10 | 3.39 | 395 | 0.48 |
| mit S1 auf kcat(H), ln k, ungewichtet | 3.70 (0.76) | 2.93 (0.86) | 1.04×10³ | 1.004 |
| mit S1 auf kcat(H), exponentiell, ungewichtet | 3.24 | 3.31 | 493 | 0.54 |

Ergebnis:
- Die gedruckten Werte der Tabelle 1 trifft nur **die unkorrigierte Rechnung (ohne S1), ungewichteter linearer Fit von ln k gegen 1/T**: 3.77 → 3.8, 1.09×10³ → 1.1×10³, 1.048 → 1.05. Nur ΔEa 2.86 würde zu 2.9 statt 2.8 runden. Das ist ein kleiner Rest, vielleicht wegen ungerundeter Rohdaten.
- Der im SI beschriebene gewichtete Exponentialfit ergibt ohne Korrektur Ea(H) 3.6 und AH 7.8×10², trifft also Tabelle 1 nicht. AH/AD 1.02 läge noch im Fehler.
- Alle Varianten mit S1-Korrektur verfehlen Ea(H) oder AH/AD. Die ungewichtete mit Korrektur kommt nahe (3.7 / 2.9 / 1.0×10³ / 1.00), trifft aber Ea(H) und AH nicht als gedruckte Rundung.
- Folgerung: Tabelle 1 (kcat, Dkcat, Ea, ΔEa, A) beruht nach dieser Nachrechnung auf den **unkorrigierten** Werten der Tabelle S2. Der Text sagt dagegen, die Daten seien korrigiert und gewichtet gefittet. Ob für den Eisengehalt korrigiert wurde, lässt sich an Ea, ΔEa und AH/AD nicht prüfen, weil ein konstanter Faktor sie nicht ändert.
- Die gedruckten Fehler (0.4; 0.4; 5×10²; 0.45) reproduziert keine Variante genau. Ungewichtet ergibt sich 0.46 / 0.62 / 8×10² / 1.07; die Fehlerdefinition ist unbekannt.

### C4. Bedingungen

- pH 9.00, 100 mM Borat (SI S3); im Artikel „0.1 M borate buffer (pH 9.0)".
- Substrat: Linolsäure 0.50–80 µM (H: protio-LA; D: 11,11-²H₂-LA). Für die O2-Korrekturmessung 80 µM LA in Boratpuffer pH 9.00.
- Atmosphäre: Umgebungsluft („ambient atmosphere (20.8% O2)"). kcat(H) wird mit dem Faktor aus Tabelle S1 auf O2-Sättigung korrigiert; die Korrekturfaktoren wurden durch Vergleich mit 100 % O2 bestimmt (Clark-Elektrode, gerührt, ca. 5 min äquilibriert, Start mit 2–4 µL konzentriertem Enzym per gasdichter Spritze).
- Messung: Cary 50, Einzelwellenlänge, Produkt 13-(S)-HPOD bei 234 nm, ε234 = 23,600 M⁻¹ cm⁻¹. Temperatur über einen wassertemperierten Küvettenhalter, 15–50 °C.
- Lag-Phase: länger bei 11,11-²H₂-LA, niedriger Konzentration und T ≤ 30 °C. Bei T ≥ 45 °C und LA > 20 µM viel kleiner.
- Enzym: Fe-Gehalt per ICP (Perkin Elmer Optima 3000 DV) bestimmt.

## D. Auffälligkeiten

Widersprüche Artikel ↔ Zusatzmaterial / Text ↔ Zahlen
1. Tabelle 1 (30 °C: kcat 2.21 (0.09), KIE 128 (3)) entspricht genau den **unkorrigierten** Werten der Tabelle S2. Laut SI wurden die Daten aber auf O2-Sättigung korrigiert („corrected to O2 saturation as needed"). Korrigiert wäre es 2.47 s⁻¹ und 143.
2. Ea(H), ΔEa, AH und AH/AD der Tabelle 1 lassen sich nur mit einem **ungewichteten** Fit der **unkorrigierten** Daten nachrechnen. Das SI beschreibt einen gewichteten Exponentialfit (Nachrechnung, keine gedruckte Angabe).
3. Der Wortlaut des SI („All data presented herein … corrected to O2 saturation") widerspricht dem Titel von Tabelle S2 („Empirical rate constants").
4. Ob Tabelle S2 für den Eisengehalt korrigiert ist, wird nicht gesagt.
5. Die Dkcat-Fehler in S2 (1–3) sind deutlich kleiner als der fortgepflanzte Fehler (2.9–7.5). Die Herkunft wird nicht erklärt. Fehlerart und Zahl der Wiederholungen werden nirgends genannt.
6. Dkcat bei 50 °C: gedruckt 91, berechnet 91.9, auch an der Rundungsgrenze ≥ 91.6. Am Rand liegen außerdem Dkcat bei 15 °C (137.6 → 138) und D(kcat/KM) bei 15 °C (52.0 statt 51) und 45 °C (36.2 statt 35).
7. ΔEa: Die Nachrechnung ergibt 2.86 (→ 2.9), gedruckt ist 2.8.
8. Tabelle S1 ist nicht monoton (25 °C: 1.195, Nachbarn 1.055 und 1.116). Das sieht nach Messstreuung aus, kein offensichtlicher Druckfehler. Wer S1 anwendet, verändert dadurch die Form der H-Arrhenius-Kurve.
9. Artikel: „decreased one hundred fifty-fold from that of WT and the single mutant Ile553Ala". Aus Tabelle 1 ergibt sich 297/2.21 = 134 und 280/2.21 = 127, also eher ~130-fach.

Druckfehler im Artikel
10. Fußnote d der Tabelle 1: „ΔEa = Ea(D) − ΔEa(H)" statt Ea(D) − Ea(H).
11. „linoleic acid (9,12-(Z,Z)-octadecanoic acid)" statt octadecadienoic acid.
12. „this term is temperature dependent but only weakly isotope independent" – gemeint ist wohl „weakly isotope dependent".
13. „In the case of WT SLO-1, the magnitude and nearly temperature-dependent KIEs" – gemeint ist wohl „temperature-independent". Vorher steht: „KIEs that are largely temperature-independent".

Zusatzmaterial / kopierter Text
14. Der Spaltenkopf der Tabelle S2 ist umgebrochen: „D(kcat/KM)" steht allein in der zweiten Zeile, die hochgestellten D-Präfixe sind verloren („Dkcat" = ᴰkcat).
15. Eine einzelne Ziffer „6" steht allein mitten im Satz („The initial / 6 / rates were fitted"). Das ist die hochgestellte Fußnote 6 = KaleidaGraph (Ref. 6). Sie gehört zum Satz über den Fit.
16. Gradzeichen fehlen („37 C", „-80 C", „Temperature C", „T, C"). Hoch- und Tiefstellungen fehlen („OD600", „M-1 cm-1", „s-1", „ε234", „11,11-" / „2H2-LA" über einen Zeilenumbruch getrennt = 11,11-²H₂-LA, „O2"). Die Fußnotenziffern hängen an Wörtern („protocol1", „gene.2", „previously3,4", „adjustments.5", „).3").
17. Sonderzeichen korrekt erhalten: µ, ε, ≤ (T ≤ 30 °C), ≥ (T ≥ 45 °C), † bei beiden Autoren, ′ in 5′/3′.
18. Primer für Position 553: Das „3" am Ende hat keinen Strich (5′ … 3 statt 3′), anders als bei den Primern für 546.
19. Inhaltsverzeichnis „Kinetic Measurements: S3", die Überschrift lautet aber „Kinetics Measurements". „QuickChange II protocol" im Text, „QuikChange" in der Literaturliste.
20. Die Literaturliste ist beim Kopieren zerfallen: Die Nummern „(1)…(6)" stehen zusammen in einer Zeile. Die Reihenfolge der Einträge entspricht 1–6.
Zur Datenbank (task.md)
21. Der Eintrag Dkcat 128 (3) bei 30 °C ist der unkorrigierte S2-Wert. Mit O2-Korrektur nach S1 wäre er 143. Das sollte vermerkt werden.
