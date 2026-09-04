# Geradeausfahrt

## Ziel

Ziel des Tests war die Ermittlung geeigneter PWM-Werte für eine möglichst gleichmässige Geradeausfahrt des Fahrzeugs.

## Durchführung

Das Fahrzeug wurde auf einem geraden Abschnitt der Teststrecke mehrfach mit unterschiedlichen PWM-Werten angesteuert. Die Ansteuerung des linken und rechten Motors wurde schrittweise angepasst und das Fahrverhalten bei mehreren Testfahrten beobachtet.

Zu Beginn zeigte sich, dass der linke Motor bei gleicher PWM-Ansteuerung langsamer anlief und das Fahrzeug dadurch nach links zog. Die PWM-Werte wurden deshalb schrittweise angepasst. Für die abschliessenden Versuche wurde die Testdauer auf 7 Sekunden erhöht, um das Fahrverhalten über eine längere Strecke beurteilen zu können.

## Ergebnis

Als geeignete Grundeinstellung für die Geradeausfahrt wurden folgende PWM-Werte ermittelt:

| Parameter | Wert |
|---|---:|
| PWM linker Motor | 70 % |
| PWM rechter Motor | 67 % |

Mit dieser Einstellung fährt das Fahrzeug überwiegend gerade. Zwischen einzelnen Fahrten können leichte Abweichungen auftreten. Die ermittelten Werte bilden deshalb die Grundeinstellung der Motoransteuerung. Eine zusätzliche Korrektur des Fahrverhaltens soll später mithilfe der Ultraschallsensoren erfolgen.

## Testprogramm

Das verwendete Testprogramm befindet sich in diesem Ordner:

`geradeausfahrt_test.py`
