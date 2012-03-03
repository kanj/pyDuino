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
    
    
    print min(1,5)
    print max(1,5)
    print abs(-5)
    print constrain(5,1,2)
    print "aMap",aMap(6,0,0,5,5)
    print pow(2,3)
    print sq(5)
    print sqrt(4)
    print sin(3.1415/4)
    print cos(3.1415/4)
    print tan(3.1415/4)
    randomSeed(my_board.micros())
    print randomMax(50)
    print random(50,100)


def loop(i):
   exit()
    
    
        
    
    
setup()
i=0
while(True):
    i=i+1
    loop(i)    
