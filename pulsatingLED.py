#!/usr/bin/python
#   Connect an LED to pin 10 thru a 220 ohm resistor. 
#   The intensity will progressively rise and then turn off and then repeat cycle.


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
    for i in range(0,255,10):
        
        my_board.analogWrite(10,i)
        my_board.delay(100)
    
    
    
setup()

while(True):
    loop()    
