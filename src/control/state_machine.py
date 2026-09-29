import time
from enum import Enum
from config import DOUBLE_PRESS_TIME, WALL_DIST, MAX_CURVES, END_TIME
from hardware.camera import start as camera_start
from hardware.led import green_on, red_on, leds_off
from hardware.motor import stop
from hardware.button import is_pressed
from hardware.camera import capture_frame
from hardware.ultrasonic import get_left, get_right
from vision.image_processing import preprocess
from vision.curve_detection import detect_blue, detect_orange
from vision.obstacle_detection import detect_red, detect_green
from control.navigation import drive_straight, correct_left, correct_right, turn_left, turn_right

class State(Enum):
    INIT = 1
    READY = 2
    DRIVE = 3
    CORRECTION = 4
    TURN = 5
    EVADE = 6
    END = 7
    ERROR = 8

class StateMachine:

  def __init__(self):
      #Aktueller Zustand
      self.state = State.INIT

      #Gewählter Fahrmodus
      self.mode = None

      #Kurvenzähler
      self.curve_count = 0

      #Erkannte Hindernisfarbe
      self.obstacle = None

      #Seite für Wandkorrektur
      self.correction_side = None

  def init_state(self):
      #System initialisieren
      try:
          stop()
          leds_off()
          camera_start()

          #In READY wechslen
          self.state = State.READY

      except Exception:
          #Bei Fehler in ERROR wechslen
          self.state = State.ERROR

  def ready_state(self):
      #Betriebsbereit
      green_on()

      #Auf Benutzereingabe warten
      if not is_pressed():
          return

      #Erste Tasterbetätigung
      while is_pressed():
          time.sleep(0.01)

      press_count = 1
      start_time = time.time()

      #Zweite Tasterbetätigung
      while time.time() - start_time < DOUBLE_PRESS_TIME:
          if is_pressed():
              while is_pressed():
                  time.sleep(0.01)

              press_count = 2
              break

          time.sleep(0.01)

      #Fahrmodus wählen
      if press_count == 1:
          self.mode = "BLUE"

      elif press_count == 2:
          self.mode = "ORANGE"

      #Kurvenzähler auf 0
      self.curve_count = 0 

      #In DRIVE wechslen
      self.state = State.DRIVE 

  def drive_state(self):
      #Kamerabilder aufnehmen und verarbeiten
      frame = capture_frame()
      hsv = preprocess(frame)

      #Hindernisse erkennen
      red_detected = detect_red(hsv)
      green_detected = detect_green(hsv)

      #Wandabstände messen
      left_distance = get_left()
      right_distance = get_right()

      #Kurvenmarkierung
      if self.mode == "BLUE":
          curve_detected = detect_blue(hsv)

      elif self.mode == "ORANGE":
          curve_detected = detect_orange(hsv)

      #Ultraschallmessung prüfen
      if left_distance is None or right_distance is None:
          self.state = State.ERROR
          return

      #Hindernis
      if red_detected:
          self.obstacle = "RED"
          self.state = State.EVADE
          return

      elif green_detected:
          self.obstacle = "GREEN"
          self.state = State.EVADE
          return

      #Wandabstand
      if left_distance < WALL_DIST:
          self.correction_side = "LEFT"
          self.state = State.CORRECTION
          return

      elif right_distance < WALL_DIST:
          self.correction_side = "RIGHT"
          self.state = State.CORRECTION
          return

      #Kurvenmarkierung
      if curve_detected:
          self.state = State.TURN
          return

      #Geradeausfahrt
      drive_straight()  

  def correction_state(self):
      #Wand links gering
      if self.correction_side == "LEFT":
          correct_right()

      #Wand rechts gering
      elif self.correction_side == "RIGHT":
          correct_left()

      else:
          self.state = State.ERROR
          return

      #Korrekturseite zurücksetzen
      self.correction_side = None

      #In DRIVE wechseln
      self.state = State.DRIVE

  def turn_state(self):
      #Kurve anhand des Fahrmodus ausführen
      if self.mode == "BLUE":
          turn_left()

      elif self.mode == "ORANGE":
          turn_right()

      else:
          self.state = State.ERROR
          return

      #Kurvenzähler +1
      self.curve_count += 1 

      #Kurvenzähler prüfen
      if self.curve_count >= MAX_CURVES:
          self.state = State.END

      else:
          self.state = State.DRIVE
          

      


      
          






















      
