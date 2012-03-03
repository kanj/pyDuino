#!/usr/bin/python
#   This uses the onboard LED connected to pin 13

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
    
    my_board.pinMode(13,OUTPUT)




def loop():
    my_board.digitalWrite(13,HIGH)
    my_board.delay(1000)
    my_board.digitalWrite(13,LOW)
    my_board.delay(1000)
    
    
setup()

while(True):
    loop()    
