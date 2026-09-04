## Vergleich der Geradeausfahrt

Zur Dokumentation der Optimierung wurden zwei Testfahrten aufgezeichnet.

### Vor der Kalibrierung

Zu Beginn zeigte das Fahrzeug eine deutliche Abweichung von der geraden Fahrtrichtung.

https://github.com/user-attachments/assets/739729cc-13d2-4a3b-8b5b-1298de153b4f

### Nach der Kalibrierung

Nach mehreren Testfahrten und der schrittweisen Anpassung der Motoransteuerung wurde mit 70 % PWM links und 67 % PWM rechts eine deutlich gleichmässigere Geradeausfahrt erreicht.

https://github.com/user-attachments/assets/77c66974-9f9c-476e-b656-dc1fa83be461

## Testprogramm und Motoransteuerung

Für die Versuche wurde das Testprogramm `geradeausfahrt_test.py` erstellt. Dieses ermöglicht die getrennte PWM-Ansteuerung des linken und rechten DC-Motors über den TB6612FNG-Motortreiber.

Die PWM-Werte beider Motoren können im Programm unabhängig voneinander angepasst werden. Dadurch wurde die Motorleistung während der Testfahrten schrittweise verändert und das resultierende Fahrverhalten beobachtet.

Als geeignete Grundeinstellung wurden 70 % PWM für den linken und 67 % PWM für den rechten Motor ermittelt. Die unterschiedliche Ansteuerung gleicht das abweichende Laufverhalten der beiden Motoren aus und führt zu einer möglichst gleichmässigen Geradeausfahrt.


