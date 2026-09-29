from control.state_machine import StateMachine
from hardware.motor import stop


def main():
    #State Machine erstellen
    state_machine = StateMachine()

    try:
        #State Machine kontinuierlich ausführen
        while True:
            state_machine.run()

    except KeyboardInterrupt:
        #Programm sicher beenden
        stop()


if __name__ == "__main__":
    main()
