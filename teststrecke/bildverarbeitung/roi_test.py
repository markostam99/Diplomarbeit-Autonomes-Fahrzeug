import cv2
import os

bilder_ordner = "bilder"

bilder = [
    "blau_weit.jpg",
    "blau_mittel.jpg",
    "blau_nah.jpg",
    "blau_schraeg_links.jpg",
    "blau_schraeg_rechts.jpg"
    "weit_block.jpg",
]

ausgabe_ordner = os.path.join(bilder_ordner, "roi_test")
os.makedirs(ausgabe_ordner, exist_ok=True)

for dateiname in bilder:
    pfad = os.path.join(bilder_ordner, dateiname)
    bild = cv2.imread(pfad)

    if bild is None:
        print(f"Fehler: {pfad} konnte nicht geladen werden.")
        continue

    hoehe, breite = bild.shape[:2]

    # Testweise beginnt der relevante Bildbereich bei 33 % der Bildhöhe
    y_start = int(hoehe * 0.33)

    cv2.rectangle(
        bild,
        (0, y_start),
        (breite - 1, hoehe - 1),
        (0, 255, 0),
        3
    )

    ausgabe = os.path.join(ausgabe_ordner, f"roi_{dateiname}")
    cv2.imwrite(ausgabe, bild)

    print(f"Erstellt: {ausgabe}")