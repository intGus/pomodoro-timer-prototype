# Pomodoro Timer prototype

import time
import sys
from machine import Pin

# This is a prototype for a Pomodoro Timer circuit
led = Pin(6, Pin.OUT)

#functions
def timer(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        #sys.stdout.write('\r' + timeformat + 's')
        print(timeformat)
        time.sleep(1)
        time_sec -= 1

    print("stop")

#Configuration
pomodoroTimer = 25
breakTimer = 5
longBreak = breakTimer * 2

while (True):
   pomodoroCount = 0
   startTimer = input('start timer? y/n')
   if (startTimer.lower() == 'y'):
       print('pomodoro timer started')
       led.on()
       timer(pomodoroTimer)#*60
       pomodoroCount+=1
       timer(breakTimer)#*60
   else:
       print('pomodoro timer not started')
       led.off()


