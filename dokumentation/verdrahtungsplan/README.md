# Verdrahtungsplan

Dieser Ordner enthält den finalen Verdrahtungsplan des autonomen Robotikfahrzeugs.

Der Verdrahtungsplan wurde nach dem mechanischen Aufbau und der Inbetriebnahme der einzelnen Hardwarekomponenten erstellt. Er basiert auf der tatsächlich realisierten Verdrahtung des Fahrzeugs und dokumentiert die elektrischen Verbindungen zwischen dem Raspberry Pi 4, der Sensorik, dem Motortreiber und den Aktoren.

## Dargestellte Komponenten

- Raspberry Pi 4 Model B
- 2× Grove Ultrasonic Ranger
- TB6612FNG Motortreiber
- 2× DC-Motor
- 4× AA NiMH Motorversorgung
- Breadboard zur 3,3-V-Verteilung
- Rote Status-LED
- Grüne Status-LED
- Starttaster

## Spannungsversorgung

Die Versorgung des Antriebs und des Raspberry Pi erfolgt getrennt.

Der TB6612FNG und die beiden DC-Motoren werden über einen separaten 4×AA-NiMH-Akkupack versorgt.
Die 3,3-V-Logikversorgung des Motortreibers sowie ein Ultraschallsensor werden über eine Breadboard-Verteilung vom Raspberry Pi gespeist. Da keine 3,3V Pins mehr vorhanden waren im Pin Layout des Raspberry Pi´s.

Die verschiedenen Schaltungsteile besitzen eine gemeinsame Masse.

## Erstellung

Der Verdrahtungsplan wurde mit KiCad erstellt.

Die PDF-Datei stellt den dokumentierten Stand der realisierten Hardwareverdrahtung dar.

#
![Verdrahtungsplan als PDF öffnen](Verdrahtungsplan.pdf)
