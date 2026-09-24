import lgpio
from config import BUTTON

#GPIO Chip öffnen
lgpio.gpiochip_open(0)

#Starttaster als Eingang mit Pull-up
lgpio.gpio_claim_input(h, BUTTON, lgpio.SET_PULL_UP)    

def is_pressed():
        #Tasterzustand auslesen
        
