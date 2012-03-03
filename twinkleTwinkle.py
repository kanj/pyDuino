#!/usr/bin/python
#   Connect a buzzer to pin 10
#   The song is a list of tuples containing a frequency and duration in milliseconds
#   To test noTone the tone is interrupted half way thru    

from arduino18 import *
import signal
import sys

def signal_handler(signal, frame):
        print 'You pressed Ctrl+C!'
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)


my_board = Arduino('/dev/ttyUSB0')
print my_board

def setup():
    #specify the port as an argument
    
    my_board.pinMode(10,OUTPUT)




def loop():
    twinkle=[(2093,500),(2093,500),(3136,500),(3136,500),(3520,500),(3520,500),(3136,1000)]
    for i in twinkle:
        print i[0],i[1]
        my_board.tone(10,i[0],i[1])
                                                                                                                                                                                                                 
        my_board.delay(i[1]//2)
        my_board.noTone(10)
        my_board.delay(i[1]//2)
    
    
    
setup()

while(True):
    loop()    
