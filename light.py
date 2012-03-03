#!/usr/bin/python
#   This uses a Parallax TSL230R Light to Frequency Converter

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
    
    my_board.pinMode(9,INPUT)




def loop(i):
    x=my_board.pulseIn(9,1,1000000)
    print i,x
    my_board.delay(10)
    i=i+1
    if x==-1:
        z=input("oops")
    
    
        
    
    
setup()
i=0
while(True):
    i=i+1
    loop(i)    
