# Validierung des autonomen Fahrzeugs

Dieser Ordner dokumentiert die abschliessende praktische Validierung des autonomen Fahrzeugs.

Nach der Entwicklung und Optimierung der einzelnen Softwarefunktionen wurde das Gesamtsystem auf der definierten Teststrecke getestet. Die Videos zeigen ausgewählte Testfahrten und dienen als praktischer Nachweis der implementierten Fahrzeugfunktionen.

## 1. Grundfahrt – Modus Blau

https://github.com/user-attachments/assets/4c5d375d-1d75-49ab-bea0-19f1792be3d8

Das Video zeigt eine vollständige autonome Fahrt im Modus Blau.  
Die blaue Kurvenmarkierung löst eine Linkskurve aus. Das Fahrzeug durchfährt die Teststrecke selbstständig und führt die vorgesehenen Fahrfunktionen aus.

## 2. Grundfahrt – Modus Orange

https://github.com/user-attachments/assets/0b787873-dcef-47c2-a840-132f19966520

Das Video zeigt eine vollständige autonome Fahrt im Modus Orange.  
Die orange Kurvenmarkierung löst eine Rechtskurve aus. Auch in diesem Fahrmodus wird die Teststrecke selbstständig durchfahren.

## 3. Gesamtfahrt mit Hindernissen

https://github.com/user-attachments/assets/b78d7b7e-8be3-4291-a3e9-2672fc33bae3

Bei dieser Testfahrt befinden sich zusätzlich rote und grüne Hindernisblöcke auf der Strecke. Die Hindernisse werden über die Kamera erkannt und lösen abhängig von ihrer Farbe das entsprechende Ausweichmanöver aus.

Nach dem Ausweichmanöver setzt das Fahrzeug die autonome Fahrt selbstständig fort.

## 4. Wandkorrektur

https://github.com/user-attachments/assets/6d48485a-ec4c-4c29-93ba-2f76893bee24

Dieser Test zeigt gezielt die Funktion der Wandabstandskontrolle. Das Fahrzeug wird bewusst in Richtung einer Wand ausgerichtet.

Wird der definierte Mindestabstand unterschritten, erfolgt automatisch eine Korrektur der Fahrtrichtung. Dadurch wird verhindert, dass das Fahrzeug während der autonomen Fahrt die seitliche Begrenzung berührt.

## Ergebnis

Die Testfahrten zeigen, dass die grundlegenden Funktionen der Fahrzeugsteuerung im Gesamtsystem umgesetzt werden konnten. Dazu gehören die autonome Grundfahrt, die beiden Fahrmodi, die Kurvenfahrt, die Wandkorrektur sowie die Erkennung und Umfahrung der farbigen Hindernisse.

Bei der Validierung wurden ebenfalls Grenzen des zeitbasierten Steuerungskonzepts festgestellt. Insbesondere kann eine ungünstige Anfahrposition zu einem Hindernis die Qualität des anschliessenden Ausweichmanövers beeinflussen. Diese Beobachtungen und die Ergebnisse der systematischen Validierung werden in der Diplomarbeit ausgewertet und diskutiert.
