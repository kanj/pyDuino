#!/usr/bin/env python

import serial, time
from datetime import datetime
from math import sin,cos,tan,sqrt
from random import *
OUTPUT=True
INPUT=False
HIGH=True
LOW=False
sep=","
MSBFIRST=1
LSBFIRST=0
   
class Arduino(object):
    
    
    lastUse=datetime.now()
    myDelay=0
    
    
    # Private Functions
    
    def __init__(self, port, baudrate=115200):
        self.serial = serial.Serial(port, baudrate)
        #toggle DTR to reset
        
        self.serial.setDTR(False)
        self.serial.flushInput()
        self.serial.setDTR(True)
        self.serial.readline()
        # Dont initialize until receive data from Arduino
       
        self.serial.timeout=0.1
        self.lastUse=datetime.now()
    
    def __str__(self):
        return "Arduino is on port %s at %d baudrate" %(self.serial.port, self.serial.baudrate)

 
    def __sendData(self, serial_data):
        
        # This slows traffic to the rate at which the arduino can process it
        
        dTime=datetime.now()-self.lastUse
        
        while dTime.seconds*1000000+dTime.microseconds<self.myDelay:
            dTime=datetime.now()-self.lastUse
        self.lastUse=datetime.now()    
        self.serial.write(serial_data)
        self.myDelay=len(serial_data)*8000000/self.serial.baudrate
        
        
        
    
       
            
    def __getData(self):
        
        y=self.serial.readline().rstrip()
       
        if len(y)==0:
            return -1
        else:
            return y
        

    #Public Functions
    
    def pinMode(self,pin,value):
        string="A"+sep+str(pin)+sep
        if value:
            string=string+"1"+sep
        else:
            string=string+"0"+sep
        
        self.__sendData(string)
     
    def digitalWrite(self,pin,value):
        string="B"+sep+str(pin)+sep
        if value:
            string=string+"1"+sep
        else:
            string=string+"0"+sep
        self.__sendData(string)
    
    def digitalRead(self,pin):
        string="C"+sep+str(pin)+sep
        self.__sendData(string)   
        
        if self.__getData()=="1" :
            return True
        else:
            return False
            
        
    def analogRead(self,pin):
        string="E"+sep+str(pin)+sep
        self.__sendData(string)   
            
        return int(self.__getData())
           
    
    def analogWrite(self,pin,val):
        string="F"+sep+str(pin)+sep+str(val)+sep
        self.__sendData(string)
            
    def tone(self,pin,freq,duration=1000):
        string="G"+sep+str(pin)+sep+str(freq)+sep+str(duration)+sep
        self.__sendData(string)
        
    def noTone(self,pin):
        string="H"+sep+str(pin)+sep
        self.__sendData(string)
        
    def shiftOut(self,dataPin,clkPin,bitOrder,val):
        string="I"+sep+str(dataPin)+","+str(clkPin)+","+str(bitOrder)+","+str(val)+","
        self.__sendData(string)
        
    def pulseIn(self,pin,direction,duration=1000000):
        string="K"+sep+str(pin)+sep+str(direction)+sep+str(duration)+sep
        self.__sendData(string)
        return int(self.__getData())
        
    def millis(self):
        string="L"+sep
        self.__sendData(string)   
  
        return int(self.__getData())                     
   
    def micros(self):
        string="M"+sep
        self.__sendData(string)   
            
        return int(self.__getData())      
   
    def delay(self,value):
        string="N"+sep+str(value)+sep
        self.__sendData(string)   
        self.myDelay=self.myDelay+value*1000
        
        
            
    def delayMicroseconds(self,value):
        string="O"+sep+str(value)+sep
        self.__sendData(string)
        self.myDelay=self.myDelay+value
        
    def pulseOut(self,pin,dur):
        string="P"+sep+str(pin)+sep+str(dur)+sep    
        self.__sendData(string)
        self.myDelay=self.myDelay+dur

# Arduino Library
        
def constrain(x,a,b):
    return min(max(x,a),b)
def aMap(x,a,b,a1,b1):
    slope=(b1-b)/(a1-a)
    intercept=b-a*slope
    return slope*x+intercept
def sq(x):
    return x*x

def randomSeed(x=50000):
    seed(x) 
    
def randomMax(x):
    return randint(0,x)
def random(a,b):    
    return randint(a,b)
