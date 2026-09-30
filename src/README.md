# Fahrzeugsoftware

Dieser Ordner enthält den Quellcode für die Steuerungssoftware des autonomen Fahrzeugs.

Die Software ist modular aufgebaut und in mehrere Bereiche unterteilt. Dadurch können die einzelnen Funktionen unabhängig entwickelt und getestet und anschliessend zur vollständigen Fahrzeugsteuerung zusammengeführt werden.

## Ordnerstruktur

### `hardware/`

Enthält die Module für den direkten Zugriff auf die Hardwarekomponenten des Fahrzeugs. Dazu gehören die Ansteuerung der Motoren und Status-LEDs, die Abfrage des Starttasters und der Ultraschallsensoren sowie die Kamerasteuerung.

### `vision/`

Enthält die Funktionen zur Verarbeitung und Auswertung der Kamerabilder. Dazu gehören die Bildvorverarbeitung sowie die Erkennung der farbigen Kurvenmarkierungen und Hindernisse.

### `control/`

Enthält die übergeordnete Fahr- und Steuerungslogik. In `navigation.py` sind die Bewegungsfunktionen wie Geradeausfahrt, Wandkorrekturen, 90°-Kurven und Ausweichmanöver zusammengefasst.

Die Datei `state_machine.py` verbindet die einzelnen Hardware-, Vision- und Navigationsfunktionen. Die Fahrzeugsteuerung basiert auf den Zuständen `INIT`, `READY`, `DRIVE`, `CORRECTION`, `TURN`, `EVADE`, `END` und `ERROR`.

## Hauptprogramm

`main.py` bildet den Einstiegspunkt der Fahrzeugsoftware. Das Hauptprogramm startet die State Machine und führt diese kontinuierlich aus. Dadurch werden die einzelnen Module zu einer vollständigen autonomen Fahrzeugsteuerung zusammengeführt.

## Validierung

Die einzelnen Module wurden zunächst separat getestet. Nach der Zusammenführung wird die vollständige Software auf der realen Teststrecke validiert. Die Fahrparameter und Funktionen werden anhand der Praxisergebnisse bei Bedarf gezielt optimiert.
