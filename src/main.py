from control.state_machine import StateMachine
from hardware.motor import stop
from hardware.led import leds_off


def main():
    #State Machine erstellen
    state_machine = StateMachine()

    try:
        #State Machine kontinuierlich ausführen
        while True:
            state_machine.run()

    except KeyboardInterrupt:
        pass

    finally:
        #Fahrzeug immer sicher stoppen
        stop()
        leds_off()


if __name__ == "__main__":
    main()