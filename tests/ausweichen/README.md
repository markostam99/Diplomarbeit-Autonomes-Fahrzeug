# Ausweichmanöver

In diesem Ordner wird die praktische Entwicklung und Erprobung der Ausweichmanöver für farbige Hindernisse dokumentiert.

Die Farbe des erkannten Hindernisses bestimmt die Ausweichrichtung:

- Grünes Hindernis → Ausweichen nach links
- Rotes Hindernis → Ausweichen nach rechts

Die Ausweichbewegung besteht aus drei aufeinanderfolgenden Fahrabschnitten. Zuerst fährt das Fahrzeug einen Bogen in die entsprechende Ausweichrichtung. Anschliessend erfolgt ein längerer Gegenbogen, um das Hindernis zu passieren und das Fahrzeug wieder in Richtung der ursprünglichen Fahrspur zu führen. Eine abschliessende Korrektur richtet das Fahrzeug für die anschliessende Geradeausfahrt aus.

## Ermittelte Parameter

| Manöver | PWM links | PWM rechts | Dauer |
|---|---:|---:|---:|
| Ausweichen links – Linksbogen | 40 % | 80 % | 1,0 s |
| Ausweichen links – Rechtsbogen | 75 % | 40 % | 2.35 s |
| Ausweichen links – Endkorrektur | 40 % | 80 % | 1,2 s |
| Ausweichen rechts – Rechtsbogen | 79 % | 40 % | 1,0 s |
| Ausweichen rechts – Linksbogen | 40 % | 76 % | 2,35 s |
| Ausweichen rechts – Endkorrektur | 79 % | 40 % | 1,2 s |

Nach Abschluss des Ausweichmanövers wird wieder auf die kalibrierten Werte der Geradeausfahrt von 70 % links und 71 % rechts gewechselt.

Die Parameter wurden durch wiederholte praktische Fahrversuche bestimmt. Beide Ausweichrichtungen konnten mit den ermittelten Werten erfolgreich durchgeführt werden.

## Praktischer Fahrversuch

Das folgende Video zeigt die praktische Erprobung der Ausweichmanöver mit den ermittelten Parametern.

https://github.com/user-attachments/assets/f023ab3f-1362-4068-949b-3b5b697bc2dc

