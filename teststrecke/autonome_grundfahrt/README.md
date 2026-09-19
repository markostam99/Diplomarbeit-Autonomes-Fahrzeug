# Autonome Grundfahrt

In diesem Ordner wird die schrittweise Entwicklung und Erprobung der autonomen Grundfahrt auf der Teststrecke dokumentiert.

Dazu werden die zuvor einzeln getesteten Funktionen für die Geradeausfahrt, Wandabstandskorrektur, Kurvenmarkierungserkennung und Kurvenfahrt schrittweise zu einem gemeinsamen Fahrablauf zusammengeführt.

Ziel ist es, eine vollständige Runde auf der Teststrecke autonom und ohne Hindernisse zu befahren. Das Fahrzeug soll dabei selbstständig den Wandabstand überwachen, die farbigen Kurvenmarkierungen erkennen und die entsprechenden Kurvenmanöver ausführen.

## Vorgehen

Die autonome Grundfahrt wird schrittweise aus den zuvor einzeln getesteten Funktionen aufgebaut. Für die beiden Fahrtrichtungen werden zunächst zwei separate Testprogramme verwendet:

- `grundfahrt_blau.py` – autonome Grundfahrt mit Erkennung der blauen Kurvenmarkierungen
- `grundfahrt_orange.py` – autonome Grundfahrt mit Erkennung der orangen Kurvenmarkierungen

Die Entwicklung erfolgt schrittweise:

1. Geradeausfahrt mit den ermittelten Fahrparametern integrieren.
2. Ultraschallsensoren einbinden und Wandabstandskorrektur während der Fahrt testen.
3. Kurvenmarkierungserkennung der jeweiligen Fahrtrichtung integrieren.
4. Nach erkannter Markierung die Positionierung vor der Kurve und das entsprechende 90°-Kurvenmanöver ausführen.
5. Nach der Kurve automatisch in die Geradeausfahrt und Wandabstandskorrektur zurückkehren.
6. Mehrere aufeinanderfolgende Kurven auf der Teststrecke erproben.
7. Eine vollständige autonome Runde ohne Hindernisse durchführen.
