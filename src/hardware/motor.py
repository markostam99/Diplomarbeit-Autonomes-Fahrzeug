import lgpio  
from config import AIN1, AIN2, PWMA, BIN1, BIN2, PWMB, STBY, PWM_FREQ

#GPIO Chip öffnen
h = lgpio.gpiochip_open(0)
lgpio.gpio_claim_output(h, AIN1)
lgpio.gpio_claim_output(h, AIN2)
lgpio.gpio_claim_output(h, PWMA)
lgpio.gpio_claim_output(h, BIN1)
lgpio.gpio_claim_output(h, BIN2)
lgpio.gpio_claim_output(h, PWMB)
lgpio.gpio_claim_output(h, STBY)

#Motortreiber aktivieren
lgpio.gpio_write(h, STBY, 1) 


def set_motors(left_speed, right_speed):
    #Fahrtrichtung vorwärts bestimmen
    lgpio.gpio_write(h, AIN1, 0)
    lgpio.gpio_write(h, AIN2, 1)
    lgpio.gpio_write(h, BIN1, 0)
    lgpio.gpio_write(h, BIN2, 1)
  
    #Motorgeschwindigkeit
    lgpio.tx_pwm(h, PWMA, PWM_FREQ, left_speed)
    lgpio.tx_pwm(h, PWMB, PWM_FREQ, right_speed)

def stop():
    #PWM stoppen
    lgpio.tx_pwm(h, PWMA, PWM_FREQ, 0)
    lgpio.tx_pwm(h, PWMB, PWM_FREQ, 0)

def shutdown():
    #Motoren stoppen
    stop()

    #Motortreiber deaktivieren
    lgpio.gpio_write(h, STBY, 0)

    #GPIO Chip schliessen
    lgpio.gpiochip_close(h)










