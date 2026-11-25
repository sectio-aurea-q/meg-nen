# S018 (Nagel et al. 2012, Biochemistry 51, 4147–4156) — Leser 2

Quellen: Artikel (HTML von PubMed Central) und Seitentext des Zusatzmaterials (Kopie der Kuratorin vom 23.11.2026).
Abb. 3 (Bild) lag nicht vor; alles, was nur dort zu sehen wäre (Farben rot/blau der Punkte), ist nicht gelesen.

## A. Abschriften

| Datei | Zeilen |
|---|---|
| tableS1.csv | 6 (WT, L176V, L176A, L176G, L176Δ, V260A) |
| tableS2.csv | 6 |
| tableS3.csv | 8 (5–60 °C; Zeile 5: ND, ND) |
| tableS4.csv | 8 |
| tableS5.csv | 40: L176V 10, L176A 8, L176G 7, L176Δ 7, V260A 8 |

Die Dateien sind per Skript aus dem Seitentext erzeugt (nicht abgetippt); Zahlen wie gedruckt, nachgestellte Nullen erhalten.
Hinweise zur Abschrift:
- S1/S2: Klammern stehen nur in der WT-Zeile, jeweils um den Fehler von Ea(D) und um den Fehler von Ea(D)−Ea(H): S1 (0.7), (1.0); S2 (0.3), (0.6). Spalte `klammer` nennt die betroffenen Felder. Eine Erklärung der Klammern ist nicht gedruckt.
- S3/S4: die erste Spalte (Temperatur) hat im Druck keine Überschrift; in der CSV habe ich sie `T` genannt. In S4 heißen im Druck vier Spalten gleich „error"; in der CSV zur Unterscheidung `error_<Größe>`.
- S5: die Spaltenköpfe „kcat" und „(H)"/„(D)" sind im kopierten Text auf zwei Zellen verteilt; Spalte T ohne Einheit gedruckt (in der CSV laut Vorgabe `T_C`).

## B. Zahl der Temperaturen im oberen Ast (reading.csv)

Was die Quelle druckt:
- Knick: Tabelle 2, Titel: „Temperature dependence of KIEs for ht-ADH mutants above the 30 °C break." Fußnote a an V260A: „The breakpoint for this mutant is at 40 °C." Im Text einmal nur „the transition temperature of ca. 30 °C".
- Bereiche der Fits: nicht gedruckt. Weder Artikel noch Zusatzmaterial nennen die Temperaturen, die in den oberen oder unteren Fit eingehen. Einziger Hinweis ist die Legende zu Abb. 3: „Data collected above and below the Arrhenius break are indicated in red and blue, respectively." (nur im Bild ablesbar).
- Zugehörigkeit des Punktes am Knick: nichts gesagt.

| temp_id | Variante | n_temperatures | sicher oberhalb (H = D) | Punkt am Knick |
|---|---|---|---|---|
| T0022 | L176V | 5 (abgeleitet) | 33; 37.5; 42; 45; 52 | keiner bei 30 °C (28.5 / 33) |
| T0023 | L176A | 4 (abgeleitet) | 33; 37.5; 45; 52 | keiner bei 30 °C (28.5 / 33) |
| T0024 | L176G | >=3 | 37.5; 46; 52 | 30 °C gemessen, Zugehörigkeit offen: 3 oder 4 |
| T0025 | L176Δ | >=3 | 40; 50; 60 | 30 °C gemessen, Zugehörigkeit offen: 3 oder 4 |
| T0026 | V260A | 3 (abgeleitet) | 45; 50; 58 | keiner bei 40 °C (38 / 45) |

H und D unterscheiden sich im oberen Ast nirgends. Die einzige ND-Zeile (L176Δ, 10 °C, kcat(D) und Dkcat) liegt im unteren Ast.

### Vorbehalt aus eigener Nachrechnung (NICHT Quelle, nur Plausibilitätsprüfung)
Ich habe aus Tabelle S5 Arrhenius-Geraden gerechnet (ln kcat gegen 1/T, gewichtet mit den gedruckten Fehlern, R = 1.9872 cal/(mol K)) und mit S1/S2 verglichen:

| Variante | Tabelle S2 gedruckt Ea(H)/Ea(D)/Diff. | ohne knicknahen Punkt | mit knicknahem Punkt |
|---|---|---|---|
| L176V | 18.6 / 19.9 / 1.3 | 33–52 (n=5): 18.8 / 20.8 / 1.9 | 28.5–52 (n=6): 18.4 / 19.4 / 0.9 |
| L176A | 15.9 / 17.2 / 1.4 | 33–52 (n=4): 15.8 / 16.4 / 0.6 | 28.5–52 (n=5): 15.9 / 16.9 / 1.0 |
| L176G | 16.6 / 17.8 / 1.2 | 37.5–52 (n=3): 17.0 / 18.1 / 1.2 | 30–52 (n=4): 16.6 / 17.8 / 1.2 |
| L176Δ | 13.5 / 15.2 / 1.7 | 40–60 (n=3): 13.0 / 14.9 / 1.9 | 30–60 (n=4): 13.5 / 15.2 / 1.7 |
| V260A | 14.2 / 16.1 / 1.9 | 45–58 (n=3): 13.3 / 15.8 / 2.5 | 38–58 (n=4): 14.5 / 16.4 / 2.0 |

Zugleich trifft der untere Ast Tabelle S1, wenn derselbe Punkt auch dort mitgerechnet wird (L176G 10–30: 27.2/28.1 gegen 27.3/28.1; L176Δ 10–30: 35.4/36.5 gegen 35.4/36.6; L176A 5–28.5: 26.4/26.9 gegen 26.4/27.0; V260A 10–38: 32.8/32.4 gegen 32.9/33.1; L176V 12.5–28.5: 27.9/30.4 gegen 27.5/30.0).

Lesart: Bei L176G und L176Δ wird S2 mit dem 30-°C-Punkt im oberen Ast auf die Nachkommastelle getroffen; das spricht dafür, dass der Punkt am Knick in BEIDE Fits eingeht (also 4 statt 3). Bei L176A und V260A liegt die Rechnung mit dem knicknahen Punkt (28.5 bzw. 38 °C) näher an S2, bei L176V ist es unentschieden. Die nach Regel abgeleiteten Zahlen 5, 4, 3 für T0022, T0023, T0026 sind deshalb möglicherweise um eins zu klein (6, 5, 4). Das ist ein Rechenindiz, kein Druck; in reading.csv stehen die regelgemäß abgeleiteten Werte, der Vorbehalt im Feld `vermerk`. Die genaue Fit-Methode der Autoren (Gewichtung, ungerundete Werte) ist unbekannt, die Nachrechnung also nicht beweisend.

## C. Tabellen S1/S2 gegen task.csv und Tabelle 2

Tabelle S2 (oberer Ast), Spalten Ea(D)−Ea(H) und Fehler, gegen task.csv und Tabelle 2:

| Variante | S2 | Tabelle 2 | task.csv dEa_kcal / dEa_error | stimmt |
|---|---|---|---|---|
| L176V | 1.3 / 1.1 | 1.3 (±1.1) | 1.3 / 1.1 | ja |
| L176A | 1.4 / 0.9 | 1.4(±0.9) | 1.4 / 0.9 | ja |
| L176G | 1.2 / 1.0 | 1.2 (±1.0) | 1.2 / 1.0 | ja |
| L176Δ | 1.7 / 0.4 | 1.7 (±0.4) | 1.7 / 0.4 | ja |
| V260A | 1.9 / 1.0 | 1.9 (±1.0) | 1.9 / 1.0 | ja |

- `as_printed` in task.csv entspricht dem Wortlaut von Tabelle 2 (auch das fehlende Leerzeichen bei „1.4(±0.9)").
- T_break_K in task.csv (303.15; V260A 313.15) entspricht Tabellentitel und Fußnote a.
- Tabelle S1 (unterer Ast) steht nicht in task.csv und nicht in Tabelle 2; dort keine Vergleichszahl. Tabelle 2 gibt für den unteren Ast nur Log(Aobs) der Protio-Reihe (aus Ref. 40).
- WT: S2 druckt 0.1 (0.6); Tabelle 2 druckt 0.2 (±0.2) mit Fußnote b „Ea(T) – Ea(H); this parameter sets an upper limit on Ea(D) – Ea(H)". Das sind verschiedene Größen; der Fließtext nennt für WT 0.1 kcal/mol und verweist dabei auf Tabelle 2 (siehe E). WT ist nicht in task.csv.
- Einheit: in S1 und S2 ist KEINE Einheit gedruckt (weder im Titel noch im Spaltenkopf noch in den Fußnoten). kcal/mol ergibt sich nur mittelbar aus der Übereinstimmung der Differenzen mit Tabelle 2, deren Spaltenkopf „kcal/mol" trägt.
- Größen, die im Artikel fehlen und in S1/S2 stehen: Ea(H) mit Fehler und Ea(D) mit Fehler je Variante und je Ast, sowie Ea(D)−Ea(H) mit Fehler für den unteren Ast. Für die leeren Felder Ea_light_kcal / Ea_light_error in task.csv liefert S2: L176V 18.6 / 0.6; L176A 15.9 / 0.5; L176G 16.6 / 0.5; L176Δ 13.5 / 0.4; V260A 14.2 / 1.0.
- Innere Stimmigkeit: die gedruckten Fehler der Differenz sind in allen 12 Zeilen die Wurzel aus der Quadratsumme der Einzelfehler (z. B. L176V oben √(0.6²+0.9²) = 1.08 → 1.1). Differenz aus den gerundeten Ea weicht zweimal um 0.1 ab: S2 L176A 17.2 − 15.9 = 1.3 (gedruckt 1.4); S1 L176V 30.0 − 27.5 = 2.5 (gedruckt 2.4). Beides mit Rundung vereinbar.

## D. Prüfung Dkcat = kcat(H)/kcat(D) in Tabelle S5; Fehler; Bedingungen

Prüfung: Für jede Zeile den Bereich des Quotienten berechnet, den die Rundung von kcat(H) und kcat(D) auf die gedruckte Stellenzahl zulässt, und mit dem gedruckten Dkcat (± halbe letzte Stelle) verglichen.
Ergebnis: Alle 39 Zeilen mit Zahlen sind innerhalb der Rundung vereinbar; keine Zeile passt nicht. (L176Δ 10 °C: ND, nicht prüfbar.)

Zeilen, bei denen der Quotient der gedruckten Zahlen um mehr als 0.1 vom gedruckten Dkcat abweicht (erklärbar durch Rundung, der Vollständigkeit halber):

| Variante | T | kcat(H) | kcat(D) | H/D gerechnet | gedruckt | zulässiger Bereich |
|---|---|---|---|---|---|---|
| L176V | 12.5 | 0.12 | 0.025 | 4.80 | 5.0 | 4.51–5.10 |
| L176V | 20 | 0.48 | 0.11 | 4.36 | 4.5 | 4.13–4.62 |
| L176V | 28.5 | 1.7 | 0.40 | 4.25 | 4.1 | 4.07–4.43 |
| L176A | 12.5 | 0.26 | 0.063 | 4.13 | 4.0 | 4.02–4.24 |
| L176Δ | 20 | 0.065 | 0.016 | 4.06 | 4.2 | 3.91–4.23 |
| V260A | 10 | 0.04 | 0.011 | 3.64 | 4.04 | 3.04–4.29 |
| V260A | 20 | 0.41 | 0.11 | 3.73 | 3.87 | 3.52–3.95 |

Bei V260A 10 °C ist kcat(H) nur mit einer geltenden Ziffer gedruckt (0.04), Dkcat aber mit drei (4.04); aus den gedruckten Zahlen lässt sich Dkcat dort nicht nachvollziehen, nur nicht widerlegen.

Fehler der Spalte Dkcat (eigene Rechnung): Der gedruckte „Error" von Dkcat ist in allen 39 Zeilen etwa der RELATIVE fortgepflanzte Fehler √((σH/kH)² + (σD/kD)²), nicht mit Dkcat malgenommen (Verhältnis gerechnet/gedruckt 0.76 bis 1.47 bei einstelligem Druck; einzige gröbere Abweichung L176A 5 °C: gerechnet 0.20, gedruckt 0.1). Beispiele: L176V 12.5 °C: relativ 0.092 (gedruckt 0.09), absolut wäre 0.44; L176G 30 °C: relativ 0.28 (gedruckt 0.3), absolut 1.13; L176Δ 20 °C: relativ 0.51 (gedruckt 0.5), absolut 2.06; V260A 58 °C: relativ 0.116 (gedruckt 0.11), absolut 0.40. Tabelle 1 des Artikels druckt für dieselben Messungen bei 30 °C die absoluten Werte: L176G 4.0 (±1.1), L176Δ 4.4 (±1.4), V260A 4.1 (±0.4). Die Dkcat-Fehler in S5 sind also um etwa den Faktor Dkcat (rund 4) kleiner als ein absoluter Fehler; eine Kennzeichnung als relativer Fehler ist nicht gedruckt.

Art der Fehler (±) und Zahl der Messungen:
- Nicht angegeben. Weder Artikel noch Zusatzmaterial sagen, ob ± Standardabweichung, Standardfehler oder Fit-Fehler ist, und nirgends steht eine Zahl von Wiederholungen. Die Spalten heißen nur „Error".
- Einzige Aussagen: Zusatzmaterial, Fußnote a zu S1/S2: „While the propagated errors for Ea(D)–Ea(H) are large, the trends are apparent, cf. Figure 3 of text." Artikel: „Despite the size of the propagated errors, there are distinct patterns in the temperature dependence of the KIE above and below the break".
- Methode nur durch Verweis: „Kinetic data were collected for the oxidation of benzyl alcohol (or its α,α-d2 isotopolog) to benzaldehyde with concomitant reduction of NAD+ to NADH, as previously described (21), and activation parameters, KIEs, Ea(D) − Ea(H) and the parameter AH/AD were calculated as described previously (43)."

Bedingungen von Tabelle S5:
- Tabelle S5 selbst druckt keine Bedingungen (kein pH, kein Puffer, keine Einheiten; Titel nur „Kinetic parameters for ht-ADH variants at all temperatures.").
- pH: aus dem Artikel mittelbar pH 7.0: „This is the reason for our extensive characterizations at pH 7.0, enabling the properties of the hydride transfer step to be directly studied." Tabelle 1 (30 °C), Fußnote a: „At pH 7.0." Die 30-°C-Zeilen von S5 stimmen mit Tabelle 1 überein (L176G 7.7 ± 1.4; L176Δ 0.43 ± 0.10; V260A 2.44 ± 0.17 gegen 2.4 (±0.2)), was die Zuordnung stützt. Ein ausdrücklicher Satz „Tabelle S5 bei pH 7.0" fehlt.
- Puffer: nicht genannt, weder im Artikel noch im Zusatzmaterial (nur Verweis auf Ref. 21, Kohen et al. 1999).
- Ionenstärke: „There was a small variation in the final ionic strength, between 110 and 160 mM, depending on the NAD+ concentration."
- Einheit von kcat: in S5 nicht gedruckt; Tabelle 1 des Artikels gibt kcat in s−1.

## E. Auffälligkeiten

Druckfehler und Lücken im Zusatzmaterial
1. S2, Fußnote b: „Estmated" (statt „Estimated"; in S1 richtig geschrieben).
2. S1/S2: Fußnote b („Estimated from the calculated values of kcat(D) in Table S4") hängt am Spaltenkopf Ea(D), gilt sachlich aber nur für WT; für die Varianten ist kcat(D) in S5 gemessen. Die Klammern in der WT-Zeile sind nicht erklärt.
3. S1/S2: Fußnotenzeichen a steht hinter dem Tabellentitel in eigener Zeile; keine Einheit gedruckt.
4. S4: Spaltenkopf „kcat(D)calcb" verweist auf eine Fußnote b, gedruckt ist nur Fußnote a (die den Inhalt von b mit enthält: „kcat(D)calc was obtained by dividing ...").
5. S3/S4: Temperaturspalte ohne Überschrift und ohne Einheit. S3, Zeile 5: beide Werte ND.
6. S5: keine Einheiten, keine Bedingungen; Stellenzahl uneinheitlich (V260A zwei Nachkommastellen bei Dkcat, sonst eine; „14.20", „51.0").
7. S5: Dkcat-Fehler ist dem Betrag nach ein relativer Fehler (siehe D), ohne dass das gesagt wird; Widerspruch in der Größe zu Tabelle 1 (z. B. L176Δ 30 °C: S5 4.4 ± 0.3, Tabelle 1 4.4 (±1.4)).
8. S5, V260A 10 °C: kcat(H) 0.04 (eine geltende Ziffer) neben Dkcat 4.04.

Widersprüche und Unschärfen zwischen Artikel und Zusatzmaterial
9. WT, oberer Ast: Fließtext „[Ea(D) − Ea(H)] increases from 0.1 kcal/mol for the wild-type enzyme ... (Table 2)", Tabelle 2 druckt für WT aber 0.2 (±0.2) mit Fußnote b (Ea(T) – Ea(H)); 0.1 steht nur in Tabelle S2 (0.1, Fehler (0.6)). Betrifft task.csv nicht (WT nicht enthalten).
10. Artikel: „Kinetic parameters for all ht-ADH variants are available in Tables S2–S5" — Tabelle S1 fehlt in dieser Aufzählung; später „Tables S1 and S2".
11. Tabelle 2, Titel „above the 30 °C break" gilt pauschal, Fußnote a setzt für V260A 40 °C; im Text sonst durchgehend 30 °C, einmal „ca. 30 °C". Für L176V und L176A gibt es keinen Messpunkt bei 30 °C (28.5 und 33), für V260A keinen bei 40 °C (38 und 45).
12. Tabelle 1 „Parameters for ht-ADH mutants at 30 °C": S5 hat für L176V und L176A keine Zeile bei 30 °C. Die Werte von Tabelle 1 entsprechen dort den Zeilen bei 28.5 °C (L176V: kcat 1.7 (±0.1) und Dkcat 4.1 gegen S5 28.5 °C 1.7 ± 0.12 und 4.1; L176A: 2.8 (±0.3) und 4.1 gegen S5 28.5 °C 2.9 ± 0.34 und 4.1 — kcat um 0.1 verschieden).
13. WT kcat bei 30 °C: Tabelle 1 25 (±3), Tabelle S4 24.9 mit Fehler 0.8 (Wert gleich, Fehler verschieden).
14. Zugehörigkeit des Knickpunktes und Fitbereiche nirgends gedruckt; eigene Nachrechnung deutet auf Doppelverwendung des knicknahen Punktes in beiden Ästen (siehe B). Das berührt n_temperatures aller fünf Reihen.

Zeichen im kopierten Text
15. Spaltenkopf der Differenz in S1/S2 steht als „Ea(D)- ‐Ea(H)" (Bindestrich, geschütztes Leerzeichen, Zeichen U+2010); in Titel und Fußnote als Halbgeviertstrich „–". Gemeint ist überall das Minuszeichen.
16. Jede Tabellenzelle steht in eigener Zeile, Fortsetzungszeilen beginnen mit Leerzeichen und geschütztem Leerzeichen (U+00A0); Seitenzahlen 1–4 als eigene Zeilen.
17. Hoch- und Tiefstellungen sind verloren: „Dkcat" (hochgestelltes D), „Ea", „kcat", „kH/kDcalc", Fußnotenzeichen („Ea(D)b", „kcat(H)a", „kcat(D)calcb").
18. Δ in „L176Δ" ist richtig angekommen. Vorangestellte Zeilennummern aus dem Kopiervorgang habe ich in dieser Datei nicht gefunden; alle Zeilen, die mit einer Zahl beginnen, sind Temperaturwerte oder Seitenzahlen.
19. Die Abschrift ist eine Kopie aus der PDF, kein Blick auf die PDF selbst: Stellen, an denen Zeichen beim Kopieren verändert wurden, kann ich nur am Text, nicht am Druckbild prüfen.
