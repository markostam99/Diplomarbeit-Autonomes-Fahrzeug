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
PWM_RECHTS_GERADE = 71

# Rechtskurve
PWM_LINKS_KURVE = 73
PWM_RECHTS_KURVE = 10
KURVENZEIT = 1

# Orangenerkennung
SCHWELLENWERT = 13000

# Verzögerung nach Erkennung
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
# HSV-Bereich Orange
# -----------------------------

orange_unten = np.array([3, 120, 120])
orange_oben = np.array([12, 255, 255])

print("Test Kurvenauslösung Orange gestartet.")
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

        # Orange Farbmaske
        maske_orange = cv2.inRange(
            hsv,
            orange_unten,
            orange_oben
        )

        # Orange Pixel zählen
        orange_pixel = cv2.countNonZero(
            maske_orange
        )

        print(f"Orange Pixel: {orange_pixel}")

        # -----------------------------
        # Kurvenmarkierung erkannt
        # -----------------------------

        if orange_pixel >= SCHWELLENWERT:

            print("-----------------------------")
            print("ORANGE MARKIERUNG ERKANNT")
            print(f"Pixel: {orange_pixel}")
            print("-----------------------------")

            # Noch geradeaus weiterfahren
            time.sleep(VERZOEGERUNG)

            # -----------------------------
            # Rechtskurve ausführen
            # -----------------------------

            print("Rechtskurve wird ausgeführt.")

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
