# Bildverarbeitung

Dieser Ordner dokumentiert die Entwicklung und praktische Erprobung der kamerabasierten Bildverarbeitung des Fahrzeugs. Die Kamera wird zur Erkennung definierter farbiger Elemente auf der Teststrecke eingesetzt. Die verwendeten Verfahren und Parameter werden schrittweise anhand von Referenzbildern und anschliessenden Fahrversuchen bestimmt.

## Kurvenmarkierungserkennung

Die blauen und orangen Markierungen auf der Teststrecke dienen zur Erkennung bevorstehender Kurven. Abhängig von der Fahrtrichtung wird eine der beiden Farben ausgewertet. Eine erkannte blaue Markierung löst eine Linkskurve aus, während eine erkannte orange Markierung eine Rechtskurve auslöst.

### Vorgehen

Zur Entwicklung der Farberkennung wurden zunächst Referenzbilder der Kurvenmarkierungen aufgenommen. Anschliessend wurden geeignete Bildbereiche ausgewählt und die HSV-Werte der jeweiligen Farbe untersucht. Auf Grundlage dieser Messungen wurden HSV-Bereiche für Blau und Orange festgelegt und mithilfe von Farbmasken überprüft.

Für die eigentliche Erkennung wird das Kamerabild um 180° gedreht und auf einen relevanten Bildbereich begrenzt. Dabei werden die unteren 67 % des Kamerabildes ausgewertet. Das Bild wird anschliessend vom BGR- in den HSV-Farbraum umgewandelt und eine Farbmaske für die gesuchte Markierungsfarbe erstellt. Die Anzahl der erkannten Pixel dient als Kriterium für die Kurvenerkennung.

### Ermittelte Parameter

Für die blaue Markierung wurde ein HSV-Bereich von [108, 80, 40] bis [118, 255, 255] festgelegt. Die Kurvenmarkierung gilt ab 15'000 erkannten blauen Pixeln als erkannt.

Für die orange Markierung wurde ein HSV-Bereich von [3, 120, 120] bis [12, 255, 255] festgelegt. Aufgrund des unterschiedlichen Erkennungsverhaltens wurde für Orange ein eigener Schwellenwert von 13'000 Pixeln bestimmt.

Nach Überschreiten des jeweiligen Schwellenwerts fährt das Fahrzeug noch 0,8 s geradeaus weiter. Dadurch erreicht es eine geeignete Position für das anschliessende Kurvenmanöver. Die Kurvenfahrt wird ebenfalls für 0,8 s ausgeführt.

### Testergebnis

Die Erkennung wurde zunächst statisch und anschliessend während der Fahrt geprüft. Bei den dynamischen Versuchen stieg die Anzahl der erkannten Pixel beim Annähern an die jeweilige Kurvenmarkierung deutlich an und fiel nach dem Überfahren wieder ab.

### Praktischer Fahrversuch

Der abschliessende Fahrversuch bestätigt die Funktionsfähigkeit der entwickelten Kurvenmarkierungserkennung unter realen Fahrbedingungen. Die Markierung wird während der Geradeausfahrt erkannt und das entsprechende Kurvenmanöver automatisch ausgelöst.

https://github.com/user-attachments/assets/d5abb610-ea77-4954-816a-fa9f234d1dbb




