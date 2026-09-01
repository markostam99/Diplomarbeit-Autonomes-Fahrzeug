# Pinbelegung

Diese Datei dokumentiert die im Fahrzeug verwendeten GPIO- und Versorgungspins des Raspberry Pi 4.

Die Pinbelegung basiert auf der tatsächlich realisierten Verdrahtung und dient als Referenz für die Hardwareansteuerung und die spätere Softwareentwicklung.

## GPIO- und Pinbelegung

| Physischer Pin | GPIO / Versorgung | Komponente | Anschluss / Funktion |
|---:|---|---|---|
| 1 | 3,3 V | Ultraschall links | VCC |
| 6 | GND | Ultraschall links | GND |
| 11 | GPIO17 | Ultraschall links | SIG |
| 17 | 3,3 V | Breadboard | 3,3-V-Zuleitung |
| 13 | GPIO27 | Ultraschall rechts | SIG |
| 14 | GND | Ultraschall rechts | GND |
| 15 | GPIO22 | TB6612FNG | STBY |
| 16 | GPIO23 | TB6612FNG | BIN1 |
| 18 | GPIO24 | TB6612FNG | BIN2 |
| 20 | GND | TB6612FNG | GND / gemeinsame Masse |
| 29 | GPIO5 | TB6612FNG | AIN1 |
| 31 | GPIO6 | TB6612FNG | AIN2 |
| 32 | GPIO12 | TB6612FNG | PWMA |
| 33 | GPIO13 | TB6612FNG | PWMB |
| 36 | GPIO16 | Rote Status-LED | über 220-Ohm-Widerstand |
| 38 | GPIO20 | Grüne Status-LED | über 220-Ohm-Widerstand |
| 40 | GPIO21 | Starttaster | Eingang |
| 30 | GND | Starttaster | GND |
| 34 | GND | Rote Status-LED | GND |
| 39 | GND | Grüne Status-LED | GND |

## 3,3-V-Verteilung

Der physische Pin 17 des Raspberry Pi stellt die 3,3-V-Versorgung für eine Breadboard-Verteilung bereit.

Über diese Verteilung werden folgende Komponenten versorgt:

- VCC des rechten Grove Ultrasonic Ranger
- VCC des TB6612FNG-Motortreibers

Der linke Grove Ultrasonic Ranger wird separat direkt über den physischen Pin 1 des Raspberry Pi mit 3,3 V versorgt.

Grund dafür ist, die fehlende Anzahl 3.3V Pins

## Weitere Schnittstellen

Die Raspberry Pi Camera Module 3 Wide ist nicht über die GPIO-Pinleiste angeschlossen. Die Verbindung zum Raspberry Pi erfolgt über die CSI-Schnittstelle.

Die Spannungsversorgung des Raspberry Pi erfolgt über eine Nitecore NB10000 Gen4 Powerbank und den USB-C-Stromanschluss.

Die beiden DC-Motoren werden über den TB6612FNG angesteuert und über einen separaten 4×AA-NiMH-Akkupack versorgt.
