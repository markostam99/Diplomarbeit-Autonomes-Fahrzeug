# HF Diplomarbeit – Autonomes Robotikfahrzeug

## Projektbeschreibung

Im Rahmen dieser Diplomarbeit wird ein autonomes Robotikfahrzeug entwickelt und praktisch umgesetzt. Das Fahrzeug basiert auf einem Raspberry Pi 4 und soll eine definierte Teststrecke selbstständig befahren.

Die Navigation erfolgt durch das Zusammenspiel von Kamera, Ultraschallsensoren und Motorsteuerung. Die Kamera dient zur Erkennung der blauen und orangen Kurvenmarkierungen sowie der roten und grünen Hindernisse. Zwei Ultraschallsensoren erfassen den seitlichen Abstand zur Umgebung.

Die Entwicklung erfolgt schrittweise. Nach Planung und Konzeption wurden zunächst der mechanische Aufbau, die elektrische Verdrahtung und die Inbetriebnahme der einzelnen Hardwarekomponenten durchgeführt. Anschliessend wird die Software modular entwickelt, getestet und schrittweise zu einem Gesamtsystem zusammengeführt.


## Hardware

Für das Fahrzeug werden folgende Hauptkomponenten eingesetzt:

- Raspberry Pi 4 Model B (4 GB)
- Raspberry Pi Camera Module 3 Wide
- 2× Grove Ultrasonic Ranger
- TB6612FNG Motortreiber
- Joy-IT Robot05 Fahrplattform
- 2× DC-Motor
- Nitecore NB10000 Gen4 Powerbank
- 4× AA NiMH Akkus
- Rote Status-LED
- Grüne Status-LED
- Starttaster

Die Versorgung des Raspberry Pi und des Antriebs erfolgt getrennt. Der Raspberry Pi wird über eine USB-C-Powerbank versorgt, während die beiden DC-Motoren über einen separaten 4×AA-NiMH-Akkupack gespeist werden. Beide Bereiche besitzen eine gemeinsame Masse.


## Aufbau

Das Fahrzeug basiert auf einer zweirädrigen Differentialantriebsplattform mit zusätzlichem Stützrad. Die beiden DC-Motoren werden über den TB6612FNG-Motortreiber vom Raspberry Pi angesteuert.

Die Kamera ist im vorderen Bereich des Fahrzeugs montiert und über die CSI-Schnittstelle mit dem Raspberry Pi verbunden. Zwei seitlich montierte Ultraschallsensoren dienen zur Abstandserfassung.

Die elektrische Verdrahtung wurde nach der mechanischen Integration der Komponenten schrittweise aufgebaut und durch Einzeltests überprüft. Der endgültige Verdrahtungsplan basiert auf der tatsächlich realisierten Hardwareverdrahtung.


## Software

Die Software wird in Python entwickelt und modular aufgebaut. Dadurch können einzelne Funktionen zunächst unabhängig getestet und anschliessend in die Gesamtsteuerung integriert werden.

Geplante Hauptbereiche der Software sind:

- Hardwareansteuerung
- Kamera und Bildverarbeitung
- Ultraschall-Abstandsmessung
- Motorsteuerung
- Erkennung der Kurvenmarkierungen
- Erkennung und Umfahrung von Hindernissen
- Zustandsbasierte Fahrzeugsteuerung
- Sicherheits- und Fehlerbehandlung

Die übergeordnete Fahrzeuglogik wird über eine State Machine umgesetzt. Die einzelnen Softwaremodule werden zunächst separat entwickelt und getestet, bevor die vollständige Integration erfolgt.


## Aktueller Projektstand

### Abgeschlossen

- Planung und Systemkonzeption
- Auswahl und Beschaffung der Hardware
- Mechanischer Aufbau des Fahrzeugs
- Einrichtung des Raspberry Pi
- Inbetriebnahme der Kamera
- Inbetriebnahme beider Ultraschallsensoren
- Inbetriebnahme des TB6612FNG-Motortreibers
- Einzel- und gemeinsamer Test der beiden DC-Motoren
- Inbetriebnahme der roten und grünen Status-LED
- Elektrische Verdrahtung der Hardware
- Erstellung des finalen Verdrahtungsplans
- Grundlegende Hardwaretests
- Erster Aufbau und Dokumentation des GitHub-Repositories

### Aktuell

Strukturierung der Softwaremodule

### Nächste Schritte

- Entwicklung der einzelnen Hardwaremodule
- Entwicklung der Bildverarbeitung
- Umsetzung der Kurvenmarkierungserkennung
- Umsetzung der Hinderniserkennung
- Implementierung der State Machine
- Integration und Test des Gesamtsystems auf der Teststrecke
