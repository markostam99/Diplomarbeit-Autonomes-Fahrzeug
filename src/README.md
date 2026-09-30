# Fahrzeugsoftware

Dieser Ordner enthält den Quellcode für die Steuerungssoftware des autonomen Fahrzeugs.

Die Software ist modular aufgebaut. Die einzelnen Module übernehmen klar definierte Aufgaben wie Hardwareansteuerung, Abstandserfassung, Bildverarbeitung, Navigation und Zustandssteuerung.

Die zentrale Fahrzeuglogik wird durch eine State Machine mit den Zuständen `INIT`, `READY`, `DRIVE`, `CORRECTION`, `TURN`, `EVADE`, `END` und `ERROR` umgesetzt. Die einzelnen Funktionen werden in den jeweiligen Modulen ausgeführt und über `main.py` zur vollständigen autonomen Fahrzeugsteuerung zusammengeführt.

Die Software wird auf der realen Teststrecke schrittweise validiert und anhand der Praxisergebnisse bei Bedarf optimiert.
