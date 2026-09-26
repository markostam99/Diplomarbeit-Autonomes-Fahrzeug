## Erster Test der Fahrkorrektur

Das folgende Video zeigt den ersten praktischen Versuch einer automatischen Korrektur während der Geradeausfahrt. Nähert sich das Fahrzeug einer seitlichen Wand auf weniger als 10 cm, wird eine kurze Korrekturbewegung in die entgegengesetzte Richtung ausgeführt.

Für die Korrektur wird der wandabgewandte Motor mit 75 % PWM und der wandzugewandte Motor mit 45 % PWM angesteuert. Die Korrekturdauer beträgt 0,25 Sekunden. Es wurde festgestellt das später eine kurze gegen Lenkung Implementiert werden muss da sich das Fahrzeug nach der Korrektur nicht Geradeaus Richtet. Dieser Test war dafür da, eine erste Korrektur auf der Teststrecke zu testen. 

Für diesen Versuch wurde mit `Korrektur_test.py` ein separates Testprogramm erstellt. Die dabei gewonnenen Erkenntnisse und ermittelten Parameter dienen später als Grundlage für die Umsetzung der Fahrkorrektur in der eigentlichen Fahrzeugsoftware.

### Video – erste Fahrkorrektur

https://github.com/user-attachments/assets/15a75ac7-7106-420e-80ce-4fb328d9c8f7
