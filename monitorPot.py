#!/usr/bin/python
#   Needs a potentiometer and LED
#   The potentiometer wiper is connected to pin A0
#   The LED is connected to pin 10, thru a 220 ohm resistor. 
#   As you rotate the wiper the LED changes brightness

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
    
    
    my_board.pinMode(10,OUTPUT)




def loop():
    x=my_board.analogRead(0)
    my_board.analogWrite(10,x/4)
    my_board.delay(100)
    
    
    
setup()

while(True):
    loop()    
