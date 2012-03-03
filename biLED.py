#!/usr/bin/python
#import the lib
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
    my_board.pinMode(11,OUTPUT)



def loop():
    my_board.digitalWrite(10,HIGH)
    my_board.digitalWrite(11,LOW)
    my_board.delay(1000)
    my_board.digitalWrite(10,LOW)
    my_board.digitalWrite(11,HIGH)
    my_board.delay(1000)
    
    
setup()

while(True):
    loop()    
