# S018 – Leser 1 – Nagel et al. 2012, Biochemistry 51, 4147–4156

Dateien: tableS1.csv … tableS5.csv, reading.csv (dieser Ordner). Hilfsskripte in skripte/ (s5.py Abschrift S5, chk.py Quotientenprüfung, fit.py unverbindliche Arrhenius-Nachrechnung).

## A. Abschrift

- Tabelle S5: 40 Zeilen – L176V 10, L176A 8, L176G 7, L176Δ 7, V260A 8. Eine ND-Zeile (L176Δ, 10 °C: kcat(D), Fehler, Dkcat, Fehler = ND).
- Tabelle S1, S2: je 6 Zeilen (WT + 5 Varianten). Klammern nur in der WT-Zeile, und nur um die Fehler von Ea(D) und Ea(D)−Ea(H).
- Tabelle S3: 8 Zeilen (5–60), 5 °C = ND/ND. Tabelle S4: 8 Zeilen (5–60). In beiden fehlt der Spaltenkopf der Temperaturspalte (im kopierten Text steht kein „T“); die Spalte heißt in meiner CSV daher `T_C_ohne_Spaltenkopf`.
- Variantenname L176Δ steht so in der CSV (im kopierten Text als Δ, U+0394).

## B. Oberer Ast (n_temperatures)

| temp_id | Variante | n | Temperaturen oberer Ast (°C) | Grundlage |
|---|---|---|---|---|
| T0022 | L176V | 5 | 33; 37.5; 42; 45; 52 | abgeleitet: Knick 30 °C, kein Punkt bei 30 |
| T0023 | L176A | 4 | 33; 37.5; 45; 52 | abgeleitet: Knick 30 °C, kein Punkt bei 30 |
| T0024 | L176G | >=3 | 37.5; 46; 52 (+30?) | Punkt genau bei 30 °C, Zugehörigkeit nicht gedruckt: 3 oder 4 |
| T0025 | L176Δ | >=3 | 40; 50; 60 (+30?) | Punkt genau bei 30 °C: 3 oder 4; ND bei 10 °C betrifft nur den unteren Ast |
| T0026 | V260A | 3 | 45; 50; 58 | abgeleitet: Knick 40 °C (Fußnote a zu Tab. 2), kein Punkt bei 40 |

Die Quelle nennt nirgends ausdrücklich die Fitbereiche und sagt nichts darüber, zu welchem Ast ein Punkt am Knick gehört. Gedruckt sind nur: Titel von Tab. 2 „above the 30 °C break“, Fußnote a „The breakpoint for this mutant is at 40 °C“ (V260A), Titel von S1/S2 „below/above the breakpoint temperature“, Abbildung 3: „Data collected above and below the Arrhenius break are indicated in red and blue“ (Farben sind im HTML-Text nicht lesbar).

Unverbindliche Nachrechnung (nicht gedruckt, nicht in die Datenbank übernehmen): Arrhenius-Fits durch Tab. S5. Für L176G und L176Δ trifft ein mit 1/Fehler² gewichteter Fit **einschließlich 30 °C** die gedruckten S2-Werte für H und D genau (L176G 16.6/17.8; L176Δ 13.5/15.2), und einige S1-Werte werden genau mit einem Fit getroffen, der 30 °C ebenfalls enthält (L176G Ea(D) 28.1; L176Δ Ea(H) 35.4). Das deutet darauf hin, dass der 30-°C-Punkt in **beiden** Ästen steckt (dann n = 4). Bei L176A trifft 28.5–52 °C Ea(H) = 15.9 genau (33–52 °C: 15.8), also bleibt offen, ob 28.5 °C mitgefittet wurde. Bei V260A trifft keine Bereichswahl die S2-Werte eindeutig.

## C. Vergleich S1/S2 mit task.csv und Tabelle 2

- task.csv (dEa_kcal, dEa_error, as_printed) stimmt für alle fünf Reihen mit Tab. 2 des Artikels **und** mit Tab. S2 überein: L176V 1.3 (1.1), L176A 1.4 (0.9), L176G 1.2 (1.0), L176Δ 1.7 (0.4), V260A 1.9 (1.0). as_printed gibt auch das fehlende Leerzeichen bei „1.4(±0.9)“ richtig wieder.
- task.csv betrifft nur den oberen Ast; Tab. S1 (unterer Ast) hat andere Werte (L176V 2.4 ± 1.5; L176A 0.6 ± 0.9; L176G 0.8 ± 1.9; L176Δ 1.2 ± 3.4; V260A 0.2 ± 2.0) – diese stehen nicht im Artikel.
- T_break_K in task.csv (303.15 / 313.15) passt zu „30 °C break“ bzw. Fußnote a (40 °C).
- Einheit: In S1 und S2 steht **keine** Einheit. kcal/mol ergibt sich nur aus dem Artikel (Tab. 2 „kcal/mol“; Text „0.1 kcal/mol for the wild-type enzyme“, was zu S2 WT 0.1 passt).
- Zusatzgrößen in S1/S2, die im Artikel fehlen: Ea(H) mit Fehler und Ea(D) mit Fehler je Ast, außerdem der ganze untere Ast für Ea(D)−Ea(H). task.csv hat die Spalten Ea_light_kcal / Ea_light_error leer; aus S2 wären das für den oberen Ast: L176V 18.6 ± 0.6, L176A 15.9 ± 0.5, L176G 16.6 ± 0.5, L176Δ 13.5 ± 0.4, V260A 14.2 ± 1.0. Ea(D) − Ea(H) aus den gedruckten Ea-Werten nachgerechnet stimmt in 10 von 12 Zeilen genau; zwei Zeilen weichen um 0.1 ab (vermutlich Rundung der ungerundeten Ea-Werte): **S1 L176V** 30.0 − 27.5 = 2.5, gedruckt 2.4; **S2 L176A** 17.2 − 15.9 = 1.3, gedruckt 1.4 (dieser gedruckte Wert 1.4 steht so auch in Tab. 2 und task.csv).
- Fehlerfortpflanzung √(σH² + σD²): stimmt für S2 (z. B. L176V √(0.6²+0.9²) = 1.08 ≈ 1.1) und für S1 (L176Δ √(1.6²+3.0²) = 3.4) – die Fehler von ΔEa sind also fortgepflanzt („propagated errors“, Fußnote a).
- AH/AD steht weder in Tab. 2 noch in S1/S2 (nur im Text qualitativ: „values less than unity in the mutants“).

## D. Dkcat = kcat(H)/kcat(D) nachgerechnet

Alle 39 Zeilen mit Zahlen passen innerhalb der Rundung (Prüfung: Intervall aus ± einer halben letzten Stelle von kcat(H) und kcat(D) gegen Dkcat ± halbe letzte Stelle). **Keine Zeile ist ein klarer Fehler.** Knapp, nur durch grobe Rundung gedeckt:
- L176V 12.5 °C: 0.12/0.025 = 4.80, gedruckt 5.0 (Rundungsband 4.51–5.10).
- V260A 10 °C: 0.04/0.011 = 3.64, gedruckt 4.04 (Rundungsband 3.04–4.29; kcat(H) nur mit einer gültigen Ziffer gedruckt).
- L176V 20 °C: 0.48/0.11 = 4.36, gedruckt 4.5 (Band 4.13–4.62).
- V260A 20 °C: 0.41/0.11 = 3.73, gedruckt 3.87 (Band 3.52–3.95).
- L176Δ 20 °C: 0.065/0.016 = 4.06, gedruckt 4.2 (Band 3.91–4.23).
- L176V 28.5 °C: 1.7/0.40 = 4.25, gedruckt 4.1 (Band 4.07–4.43).

Auffällig: Der Fehler von Dkcat in S5 ist durchweg viel kleiner, als die Fehler von kcat(H) und kcat(D) ergeben würden (z. B. L176Δ 30 °C: fortgepflanzt ≈ 1.4, gedruckt 0.3). Dkcat wurde also offenbar nicht als Quotient der Spalten mit unabhängigen Fehlern bestimmt (wie genau, steht nirgends). In Tab. 1 des Artikels (30 °C) sind die Dkcat-Fehler dagegen genau die fortgepflanzten Werte (L176Δ 4.4 ± 1.4; L176G 4.0 ± 1.1; L176A 4.1 ± 0.6; L176V 4.1 ± 0.4; V260A 4.1 ± 0.4).

Art der Fehler / Zahl der Messungen: Weder im Artikel noch im Zusatzmaterial steht, ob ± eine Standardabweichung, ein Standardfehler oder ein Fitfehler ist, und auch nicht, wie oft gemessen wurde. Gedruckt ist nur: „While the propagated errors for Ea(D)–Ea(H) are large, the trends are apparent“ (S1/S2, Fußnote a), „Despite the size of the propagated errors“ (Artikel, Ergebnisse) sowie bei Abb. 3: „error bounds have been omitted because the calculation introduces errors that are not representative of experimental data“ (nur WT kcat(D)).

Bedingungen für Tab. S5: In S5 selbst steht nichts (kein pH, kein Puffer, keine Einheiten). Im Artikel: Oxidation von Benzylalkohol (bzw. α,α-d2) mit NAD+, „as previously described (21)“; „final ionic strength, between 110 and 160 mM, depending on the NAD+ concentration“; pH 7.0 nur indirekt: „This is the reason for our extensive characterizations at pH 7.0“. Ein Puffer wird im Artikel nicht genannt (nur über Ref. 21). Einheiten von kcat (s⁻¹) und T (°C) stehen nur in Tab. 1 des Artikels bzw. ergeben sich aus dem Zusammenhang.

## E. Auffälligkeiten

1. **Knicktemperatur V260A:** Titel Tab. 2 „above the 30 °C break“ gilt laut Fußnote a nicht für V260A (40 °C). Im Text (Ergebnisse/Diskussion) wird nur „30 °C“ genannt; der 40-°C-Knick steht ausschließlich in Fußnote a. Bei V260A gibt es in S5 keinen Punkt bei 40 °C, sondern 38 °C (alle anderen Varianten 37.5 °C).
2. **WT-Wert:** Tab. 2 gibt für WT 0.2 (±0.2) mit Fußnote b „Ea(T) – Ea(H)“; der Text sagt „0.1 kcal/mol for the wild-type enzyme“ und S2 hat WT Ea(D)−Ea(H) = 0.1 (0.6). Zwei verschiedene Größen für WT, im Text als Ea(D)−Ea(H) angesprochen.
3. **Tab. 1 „at 30 °C“ gegen S5:** L176V und L176A haben in S5 keinen Messpunkt bei 30 °C. Die Werte in Tab. 1 entsprechen den 28.5-°C-Zeilen (L176V kcat 1.7 ± 0.1 vs. S5 28.5 °C 1.7 ± 0.12, Dkcat 4.1; L176A kcat 2.8 ± 0.3 vs. S5 28.5 °C 2.9 ± 0.34, Dkcat 4.1). Für L176G, L176Δ, V260A stimmen Tab. 1 und die 30-°C-Zeile von S5 überein (V260A 2.4 vs. 2.44).
4. **Unterschiedliche Fehler von Dkcat:** dieselbe Messung (z. B. L176Δ 30 °C, Dkcat 4.4) hat in Tab. 1 ± 1.4, in S5 ± 0.3 (siehe D).
5. **Verweis im Artikel:** „Kinetic parameters for all ht-ADH variants are available in Tables S2–S5“ – S1 fehlt im Verweis; S3/S4 enthalten nur WT-Daten aus Ref. 1 (= Ref. 21 des Artikels, Kohen et al. 1999), keine Varianten.
6. **Fußnote b in S1/S2** („Estimated from the calculated values of kcat(D) in Table S4“) steht am Spaltenkopf Ea(D), gilt sachlich aber nur für die WT-Zeile (nur WT hat berechnetes kcat(D)); vermutlich deshalb die Klammern in der WT-Zeile – erklärt wird die Klammer nirgends.
7. **Druckfehler S2 Fußnote b:** „Estmated“ statt „Estimated“ (S1: richtig).
8. **Unklare Zeichen im kopierten Text:** Spaltenkopf in S1 und S2 „Ea(D)- ‐Ea(H)“ (Bindestrich, geschütztes Leerzeichen, Unicode-Hyphen U+2010 – also ein zerlegtes Minus). Im Titel von S1 steht „Ea(D) - Ea(H)“ mit ASCII-Bindestrich, in S2 und den Fußnoten mit Halbgeviertstrich „–“. Das hochgestellte „a“ der Fußnote steht als eigene Zeile über dem Kopf (Zuordnung zur Spalte Ea(D)−Ea(H) nur aus dem Fußnotentext). „Ea(D)b“, „kcat(H)a“, „kcat(D)calcb“: Fußnotenbuchstaben an das Wort angeklebt. Spaltenköpfe „kcat (H)“ in S5 über zwei Zellen zerrissen. Vor jeder Zelle nach dem Tabulator steht ein geschütztes Leerzeichen (U+00A0). Seitenzahlen 1–4 als einzelne Zeilen. Zeilennummern aus dem Kopiervorgang habe ich in dieser Datei nicht gefunden.
9. **Keine Einheiten** in S1–S5 (weder kcal/mol noch s⁻¹ noch °C).
10. **S4 Fußnote a:** kcat(H) „ca. 2-fold less than values reported in reference (1)“; S4 kcat(H) 30 °C = 24.9 ± 0.8, Tab. 1 WT 25 (±3) – gleicher Wert, unterschiedlicher Fehler.
11. **Uneinheitliche Stellen in S5:** V260A mit zwei Nachkommastellen (14.20, 32.77, 4.04), übrige Varianten mit 1–2 gültigen Ziffern; L176A Fehler kcat(H) 5 °C „0.01“ bei kcat 0.069 (Stellenzahl ungleich).
12. **Differenzen S1/S2 um 0.1:** S1 L176V (2.5 gerechnet / 2.4 gedruckt), S2 L176A (1.3 / 1.4) – siehe C.
13. **„ca. 30 °C“** (Einleitung: „transition temperature of ca. 30 °C“) – sonst immer „30 °C“ ohne Toleranz; für die Zuordnung der Punkte 28.5 °C (L176V, L176A) unerheblich nach gedruckter Regel, aber Grund zur Vorsicht (siehe Nachrechnung in B).
