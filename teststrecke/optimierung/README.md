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

### Aktuell
Robotik Fahrzeug hat anhand dieser Optimierungen einen ganzen Testtag ohne Reboot überstanden, es wird davon ausgegangen das die Motorströme kein Problem mehr verursachen. Sollte das nicht der Fall sein, wird in diesem Abschnitt weiter darauf eingegangen. 
