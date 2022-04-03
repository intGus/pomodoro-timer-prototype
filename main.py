# Pomodoro Timer main.py

# This is the main file for a Pomodoro Timer in micropython
# running on a RP2040 compatible circuit board.

import time
from machine import Pin
from lcd1602 import LCD

#Functions
def Timer(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        lcd.message('\n' + timeformat)
        time.sleep(1)
        time_sec -= 1
        #TO-DO check for button state to pause/reset
        if button1.value() == 1:
            time.sleep(0.5)
            raise RestartExecution
    print("timer stop")#sound the buzzer

def Pomodoro():
    print('Pomodoro Start')
    print(f'Focus for {pomodoroTimer} minutes')
    #led.on()
    lcd.clear()
    lcd.message('   Stay Focus   ')
    Timer(pomodoroTimer)#*60 for debug

def Breaks(count):
    if count % longAfterPomodoros == 0:
        msgBreak = 'Long break Started'
        minutes = longBreak
    else:
        msgBreak = 'Break Started'
        minutes = shortBreak
    lcd.clear()
    lcd.message(msgBreak)
    print(f'Unwind yourself for {minutes} minutes')
    #led.off()
    Timer(minutes)#*60 for debug

#Classes
class RestartExecution(RuntimeError):
    pass

#IO Configuration
lcd = LCD()
led = Pin(6, Pin.OUT)
button1 = Pin(7, Pin.IN)
button2 = Pin(11, Pin.IN)
button3 = Pin(15, Pin.IN)

#Configuration
pomodoroTimer = 25
shortBreak = 5
longBreak = shortBreak * 2
longAfterPomodoros = 4
pomodoroCount = 0
msg = ' Pomodoro Timer \nauto|manual|conf'

#main
lcd.message(' Pomodoro Timer \n  version 0.1')
time.sleep(3)
lcd.clear()
lcd.message(msg)
while (True):
    if button1.value() == 1:
        time.sleep(0.5)
        while(True):
            try:
                Pomodoro()
                pomodoroCount+=1
                Breaks(pomodoroCount)
            except RestartExecution:
                lcd.message(msg)
                break
    elif button2.value() == 1:
        time.sleep(0.5)
        while(True):
            try:
                input('Press enter to start Pomodoro')
                Pomodoro()
                pomodoroCount+=1
                input('Press enter to start break')
                Breaks(pomodoroCount)
            except RestartExecution:
                lcd.message(msg)
                break
    elif button3.value() == 1:
        time.sleep(0.5)
        print('pomodoro timer configuration not available')
        lcd.message(msg)
        led.off()
