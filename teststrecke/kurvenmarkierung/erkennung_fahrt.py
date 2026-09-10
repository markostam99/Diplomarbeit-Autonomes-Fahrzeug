from picamera2 import Picamera2
import cv2
import numpy as np
import lgpio
import time

# -----------------------------
# GPIO-Belegung TB6612FNG
# -----------------------------

AIN1 = 5
AIN2 = 6
PWMA = 12

BIN1 = 23
BIN2 = 24
PWMB = 13

STBY = 22

PWM_FREQUENZ = 1000

# -----------------------------
# Fahrparameter
# -----------------------------

# Geradeausfahrt
PWM_LINKS_GERADE = 70
PWM_RECHTS_GERADE = 67

# Linkskurve
PWM_LINKS_KURVE = 20
PWM_RECHTS_KURVE = 70
KURVENZEIT = 0.8

# Blauerkennung
SCHWELLENWERT = 15000

# Hier ermittelten Wert eintragen
VERZOEGERUNG = 0.8

# -----------------------------
# GPIO initialisieren
# -----------------------------

h = lgpio.gpiochip_open(0)

for gpio in [AIN1, AIN2, BIN1, BIN2, STBY]:
    lgpio.gpio_claim_output(h, gpio)

lgpio.gpio_claim_output(h, PWMA)
lgpio.gpio_claim_output(h, PWMB)

lgpio.gpio_write(h, STBY, 1)

# Vorwärtsrichtung
lgpio.gpio_write(h, AIN1, 0)
lgpio.gpio_write(h, AIN2, 1)

lgpio.gpio_write(h, BIN1, 0)
lgpio.gpio_write(h, BIN2, 1)

# -----------------------------
# Kamera initialisieren
# -----------------------------

picam2 = Picamera2()

config = picam2.create_preview_configuration(
    main={"format": "RGB888", "size": (640, 480)}
)

picam2.configure(config)
picam2.start()

time.sleep(2)

# -----------------------------
# HSV-Bereich Blau
# -----------------------------

blau_unten = np.array([108, 80, 40])
blau_oben = np.array([118, 255, 255])

print("Test Kurvenauslösung gestartet.")
print(f"Schwellenwert: {SCHWELLENWERT} Pixel")

try:

    # -----------------------------
    # Geradeausfahrt starten
    # -----------------------------

    lgpio.tx_pwm(
        h, PWMA,
        PWM_FREQUENZ,
        PWM_LINKS_GERADE
    )

    lgpio.tx_pwm(
        h, PWMB,
        PWM_FREQUENZ,
        PWM_RECHTS_GERADE
    )

    while True:

        # Aktuelles Kamerabild
        bild = picam2.capture_array()

        # Kamera um 180° drehen
        bild = cv2.rotate(
            bild,
            cv2.ROTATE_180
        )

        # -----------------------------
        # ROI
        # -----------------------------

        hoehe, breite = bild.shape[:2]
        y_start = int(hoehe * 0.33)

        roi = bild[
            y_start:hoehe,
            0:breite
        ]

        # -----------------------------
        # BGR -> HSV
        # -----------------------------

        hsv = cv2.cvtColor(
            roi,
            cv2.COLOR_BGR2HSV
        )

        # Blaue Farbmaske
        maske_blau = cv2.inRange(
            hsv,
            blau_unten,
            blau_oben
        )

        # Blaue Pixel zählen
        blaue_pixel = cv2.countNonZero(
            maske_blau
        )

        # -----------------------------
        # Kurvenmarkierung erkannt
        # -----------------------------

        if blaue_pixel >= SCHWELLENWERT:

            print("-----------------------------")
            print("BLAUE MARKIERUNG ERKANNT")
            print(f"Pixel: {blaue_pixel}")
            print("-----------------------------")

            # Noch geradeaus weiterfahren
            time.sleep(VERZOEGERUNG)

            # -----------------------------
            # Linkskurve ausführen
            # -----------------------------

            print("Linkskurve wird ausgeführt.")

            lgpio.tx_pwm(
                h, PWMA,
                PWM_FREQUENZ,
                PWM_LINKS_KURVE
            )

            lgpio.tx_pwm(
                h, PWMB,
                PWM_FREQUENZ,
                PWM_RECHTS_KURVE
            )

            time.sleep(KURVENZEIT)

            # -----------------------------
            # Nach der Kurve stoppen
            # -----------------------------

            lgpio.tx_pwm(
                h, PWMA,
                PWM_FREQUENZ, 0
            )

            lgpio.tx_pwm(
                h, PWMB,
                PWM_FREQUENZ, 0
            )

            print("Kurvenfahrt abgeschlossen.")
            break

except KeyboardInterrupt:
    print("\nTest manuell beendet.")

finally:

    # Motoren sicher stoppen
    lgpio.tx_pwm(
        h, PWMA,
        PWM_FREQUENZ, 0
    )

    lgpio.tx_pwm(
        h, PWMB,
        PWM_FREQUENZ, 0
    )

    lgpio.gpio_write(h, STBY, 0)

    picam2.stop()
    lgpio.gpiochip_close(h)

    print("Test beendet.")