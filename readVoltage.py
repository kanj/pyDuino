#!/usr/bin/python
#   Connect the wiper from a potentiometer to pin A2
#   The reading will vary as you adjust the pot
#   The LED on pin 13 will light up when reading is above 512

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
    
    
    my_board.pinMode(13,OUTPUT)




def loop():
    
    print my_board.analogRead(2)
    if my_board.analogRead(2)>512:
        my_board.digitalWrite(13,HIGH)
    else:
        my_board.digitalWrite(13,LOW)    
    my_board.delay(100)
    
   
    
    
    
    
setup()

while(True):
    loop()    
