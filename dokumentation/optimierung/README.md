# Optimierungen

Während der praktischen Umsetzung und den Testfahrten wurden einzelne Bereiche des Aufbaus angepasst und optimiert. Die vorgenommenen Änderungen werden in diesem Ordner dokumentiert.

## Plötzlicher Reboot auf der Teststrecke

Während der ersten Fahrversuche auf der Teststrecke trat vereinzelt ein unerwarteter Neustart des Raspberry Pi auf. Besonders bei Wandkontakt und der damit verbundenen höheren Belastung der Motoren konnte dieses Verhalten beobachtet werden.

### Ausgangssituation

Der Motortreiber war ursprünglich auf dem Breadboard montiert und ein Teil der Verdrahtung wurde über das Breadboard geführt. Dazu gehörten Verbindungen auf der Motor-Leistungsseite sowie die 3,3-V-Versorgung des Motortreibers.

### Durchgeführte Optimierungen

Zur Verbesserung der elektrischen Verbindung und Betriebssicherheit wurden folgende Anpassungen vorgenommen:

- Leitungen der Motor-Leistungsseite vom Breadboard entfernt und direkt verdrahtet.
- VCC des TB6612FNG-Motortreibers direkt mit dem 3,3-V-Anschluss (Pin 1) des Raspberry Pi verbunden.
- Beide Ultraschallsensoren werden neu über die 3,3-V-Verteilung des Breadboards versorgt.
- Die gemeinsame Masse zwischen Raspberry Pi, Motortreiber und Motorversorgung wurde beibehalten.
- Die Verdrahtung wurde anschliessend bei mehreren Fahrversuchen erneut überprüft.

### Ergebnis

Nach den Anpassungen wurden mehrere Fahrversuche sowie gezielte Belastungstests durchgeführt. Dabei trat bisher kein weiterer unerwarteter Reboot des Raspberry Pi auf.

Da der Fehler zuvor nur sporadisch auftrat, kann die genaue Ursache nicht abschliessend bestätigt werden.

Der angepasste Aufbau wird für die weiteren Tests auf der Teststrecke verwendet.

#

## Optimierung des Stützrades

Bei den Fahrversuchen zeigte sich, dass das ursprünglich verwendete schwenkbare Stützrad das Fahrverhalten nach einer 90°-Kurve negativ beeinflusste. Nach dem Kurvenmanöver blieb das Rad kurzzeitig in der vorherigen Fahrtrichtung ausgerichtet. Dadurch wurde das Fahrzeug beim anschliessenden Geradeausfahren seitlich abgelenkt.

Verschiedene Anpassungen der Fahrparameter und zusätzliche Korrekturbewegungen konnten dieses Verhalten nicht zuverlässig beheben. Aus diesem Grund wurde das bisherige Stützrad durch einen frei beweglichen Ball Caster ersetzt.

Mit dem neuen Ball Caster tritt das zuvor beobachtete Verklemmen nach der Kurvenfahrt nicht mehr auf. Durch die veränderte Mechanik des Fahrzeugs mussten die Parameter für die Geradeausfahrt und die 90°-Kurven anschliessend neu bestimmt werden.

### Neue Fahrparameter

| Fahrmanöver | PWM links | PWM rechts | Dauer |
|---|---:|---:|---:|
| Geradeausfahrt | 70 % | 71 % | abhängig vom Fahrablauf |
| 90°-Linkskurve | 10 % | 73 % | 1,0 s |
| 90°-Rechtskurve | 73 % | 10 % | 1,0 s |

Die neuen Parameter wurden durch praktische Fahrversuche auf der Teststrecke ermittelt. Sowohl die Links- als auch die Rechtskurve konnten mit dem Ball Caster zuverlässig ausgeführt werden. Gleichzeitig wurde ein sauberer Übergang von der Kurvenfahrt zurück in die Geradeausfahrt erreicht.

### Aktuell
Robotik Fahrzeug hat anhand dieser Optimierungen einen ganzen Testtag ohne Reboot überstanden, es wird davon ausgegangen das die Motorströme kein Problem mehr verursachen. Sollte das nicht der Fall sein, wird in diesem Abschnitt weiter darauf eingegangen. 

Das ursprünglich verwendete Stützrad wurde durch einen Ball Caster ersetzt. Dadurch konnte das problematische Fahrverhalten nach den Kurven behoben werden. Die Geradeausfahrt sowie die Links- und Rechtskurve wurden anschliessend neu kalibriert und erfolgreich getestet.
