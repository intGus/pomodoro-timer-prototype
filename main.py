# Pomodoro Timer prototype
# This is a prototype for a Pomodoro Timer circuit board

import time
#import sys
from machine import Pin

#Functions
def Timer(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        #sys.stdout.write('\r' + timeformat + 's')
        print(timeformat)
        time.sleep(1)
        time_sec -= 1
        #TO-DO check for button state to pause/reset
        stopp = input('leave loop?')
        if stopp == 'yes':
            raise RestartExecution
    print("timer stop")#sound the buzzer

def Pomodoro():
    print('Pomodoro Start')
    print(f'Focus for {pomodoroTimer} minutes')
    led.on()
    Timer(pomodoroTimer)#*60 for debug

def Breaks(count):
    if count == 4:
        msg = 'Long break Started'
        minutes = longBreak
    else:
        msg = 'Break Started'
        minutes = shortBreak
    print(msg)
    print(f'Unwind yourself for {minutes} minutes')
    led.off()
    Timer(minutes)#*60 for debug
    pomodoroCount = 0

#Classes
class RestartExecution(RuntimeError):
    pass

#IO Configuration
led = Pin(6, Pin.OUT)

#Configuration
pomodoroTimer = 25
shortBreak = 5
longBreak = shortBreak * 2
longAfterPomodoros = 4
pomodoroCount = 0

while (True):
    selection = input('start timer: 1 auto | 2 manual | 3 config')
    if selection == '1':
        while(True):
            try:
                Pomodoro()
                pomodoroCount+=1
                Breaks(pomodoroCount)
            except RestartExecution:
                break
    if selection == '2':
        while(True):
            try:
                input('Press enter to start Pomodoro')
                Pomodoro()
                input('Press enter to start break')
                Breaks(pomodoroCount)
            except RestartExecution:
                break
    else:
            print('pomodoro timer configuration not available')
            led.off()


