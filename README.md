# pomodoro-timer-prototype

This is a MicroPython Pomodoro-Timer Prototype for the Arduino RP2040 Connect/Raspberry Pi Pico compatible boards.

At this current state there is no screen to output so everything is displayed on the Serial Terminal of the IDE.
The usage of the onboard LED pin should vary from board to board, in this case is for the Arduino RP2040 Connect.

The next implementation of this prototype is to include a LCD screen to display the timer, a buzzer and a couple
buttons to control the timer (Start, Stop, Reset) with the corresponding breadboard diagram.

The last implementation would be running in C/C++ instead of MicroPython
