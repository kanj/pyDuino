#!/usr/bin/python
#   This uses a ds1620 digital thermometer.

from arduino18 import *
import time


# Allows for graceful exit from loop
import signal
import sys

def signal_handler(signal, frame):
        print 'You pressed Ctrl+C!'
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)



# initial my_board
my_board = Arduino('/dev/ttyUSB0')


rstPin=9
clkPin=8
dqPin=7
tPin=11
def setup():
    my_board.pinMode(rstPin,OUTPUT)
    my_board.pinMode(clkPin,OUTPUT)
    my_board.pinMode(dqPin,OUTPUT)
    my_board.pinMode(tPin,INPUT)
    my_board.pinMode(rstPin,LOW)
    my_board.delay(20)
    my_board.digitalWrite(rstPin,HIGH)
    my_board.shiftOut(dqPin,clkPin,LSBFIRST,12)
    my_board.delay(20)
    my_board.shiftOut(dqPin,clkPin,LSBFIRST,0)
    my_board.delay(20)
    my_board.shiftOut(dqPin,clkPin,LSBFIRST,2)
    my_board.delay(20)
    my_board.shiftOut(dqPin,clkPin,LSBFIRST,0X0C)
    my_board.delay(20)
    my_board.shiftOut(dqPin,clkPin,LSBFIRST,0x01)
    my_board.delay(20)
    my_board.shiftOut(dqPin,clkPin,LSBFIRST,0XEE)
    my_board.delay(20)
    my_board.digitalWrite(rstPin,LOW)
    my_board.digitalWrite(clkPin,LOW)
def loop():

    
    
    print my_board.digitalRead(tPin)
    
    
    my_board.delay(1000)
    
    
    
setup()

while(True):
    loop()    
