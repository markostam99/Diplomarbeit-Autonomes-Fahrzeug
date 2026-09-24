import lgpio
from config import BUTTON

#GPIO Chip öffnen
h = lgpio.gpiochip_open(0)

#Starttaster als Eingang mit Pull-up
lgpio.gpio_claim_input(h, BUTTON, lgpio.SET_PULL_UP)    

def is_pressed():
    #Tasterzustand auslesen
    return lgpio.gpio_read(h, BUTTON) == 0

def shutdown():
    #GPIO freigeben
    lgpio.gpio_free(h, BUTTON)

    #GPIO Chip schliessen
    lgpio.gpiochip_close(h)
        
        
