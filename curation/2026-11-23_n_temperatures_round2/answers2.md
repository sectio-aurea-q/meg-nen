# Leser 2 – Anzahl der Messtemperaturen je Reihe

## S016 (Sharma 2008, JACS) – T0021
Gedruckt ist nur der Bereich: Table 1, Fußnote a „Data were collected from 15 to 50 °C." (ebenso im Fließtext zu Figure 1). Eine Anzahl, eine Liste oder eine Schrittweite fehlt; die Legende von Figure 1 spricht nur von „Data points" für H und D. Die Abbildung selbst liegt nicht vor (HTML enthält nur die Legende), das Zusatzmaterial (Assay-Details) auch nicht. Kein Hinweis auf ausgelassene Temperaturen oder einen Knick. `n_temperatures` bleibt leer.

## S018 (Nagel 2012, Biochemistry) – T0022 bis T0025
Der Artikel druckt für die kcat-Messungen weder Anzahl noch Liste noch Bereich der Temperaturen. Er verweist auf das Zusatzmaterial („Kinetic parameters for all ht-ADH variants are available in Tables S2–S5"; „rate constants and kinetic isotope effects at each temperature in the experimental range"), das nicht vorliegt. Die Reihen gelten nur oberhalb des Knicks bei 30 °C (Titel von Table 2; Legende Figure 3 trennt Daten ober- und unterhalb farblich) – wie viele Temperaturen oberhalb liegen, ist nicht gedruckt. Auffällig: Table 2 der PMC-Fassung enthält nur [Ea(D) – Ea(H)] und Log(Aobs), keine Spalte AH/AD. Alle vier Zeilen bleiben leer.

## S024 (Valley 2004, JACS) – T0051
Gedruckt ist gar nichts zur Temperaturreihe: keine Anzahl, keine Liste, kein Bereich; die einzigen Temperaturen sind die Bezugswerte „25 °C" und „27 °C" in den Fußnoten von Table 1. ΔEa und AH/AD stammen aus dem Fit der KIE gegen 1/T (Legende Figure 2: „fits of the deuterium kinetic isotope effect at each temperature"), nicht aus getrennten H-/D-Fits. Auffällig ist Note 31: drei Enzympräparationen wurden getrennt ausgewertet und gemittelt – es gibt also drei Fits, deren Temperaturzahl jeweils unbekannt ist. Abbildungen liegen nicht vor. Leer.

## S057 (Offenbacher 2017, ACS Cent. Sci.) – T0115 bis T0120
Hier ist alles gedruckt: Table S7 im Zusatzmaterial (PDF-Seiten 45–46) gibt je Variante kcat(H) und kcat(D) für jede Temperatur. WT, S749A, S749G, Y317S und Y317F haben je 8 Temperaturen (10, 15, …, 45 °C), Y317L hat 7 (15–45 °C; die Zeile 10 °C fehlt) – H und D jeweils gleich besetzt. Das passt zur Fußnote b von Table 1 („across 7 to 8 (depending on mutant) temperatures (10–45 °C); see Table S7 for complete kcat data"); die SI-Methoden nennen daneben nur die Untergrenze „at least seven temperatures". Kein Hinweis auf ausgelassene Temperaturen, kein Knick. Auffällig: Table S7 ist nicht eisenkorrigiert, Table 1 ist es – bei Y317S ist der Unterschied groß (83 gegen 330 s⁻¹ bei 30 °C).

## S059 (Zaragoza 2023, PNAS) – T0133, T0134
Gedruckt ist nur eine Untergrenze: SI Materials and Methods, „Enzyme Kinetics" (PDF-Seite 3): „from at least seven temperatures for each variant reported" – wörtlich für Ea(H); für D steht keine eigene Zahl da. Der Bereich ist „10 – 40 ˚C", ohne Schrittweite für die Kinetik (die 5-°C-Schritte im SI gehören zu den Fluoreszenzmessungen), deshalb leite ich keine genaue Zahl ab und trage >=7 ein. Eine Tabelle mit kcat je Temperatur gibt es im SI nicht (Tables S1–S12 durchgesehen). Auffällig: Fußnote * von Table 1 sagt, die temperaturabhängigen Kinetikdaten seien schon in Ref. 35 berichtet worden – dort wären die Einzelwerte zu suchen.

## S061 (Anoz-Carbonell 2020, Antioxidants) – T0138
Gedruckt ist nur der Bereich: „at different temperatures in the 5.3−20 °C range" (Methoden); Table 2 gibt kobs nur für 6 °C. Keine Anzahl, keine Liste, keine Schrittweite. In Figure 9A (g009.jpg im ZIP) zähle ich je 6 Punkte für H und für D der Stufe B→C – das ist gezählt, nicht gedruckt, deshalb bleibt `n_temperatures` leer. Das ZIP enthält nur Abbildungen, keine Tabellen; kein Hinweis auf ausgelassene Temperaturen oder einen Knick.
