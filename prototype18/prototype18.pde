// variable to store the data from the serial port

enum {_pinMode,_digitalWrite,_digitalRead,_analogReference,_analogRead,_analogWrite,_tone,_noTone,_shiftOut,_shiftIn,_pulseIn,_millis,_micros,_delay,_delayMicroseconds,_pulseOut};

int getCmd(){
  
  int inByte,chunk=0;
  //int x=128-Serial.available();
  //if (x>70)
   // Serial.println("G");
  //else
    //Serial.println("N");  
  
  do {
  while(Serial.available()<=0){
    
   
  
  
  }
  inByte=Serial.read();
  if  (inByte!=44) {    chunk=10*chunk+inByte-48;}
  }
  while (inByte!=44 );
  
  return chunk;
}

int getCmd2(){
  
  int inByte,chunk=0;
  //int x=128-Serial.available();
  //if (x>70)
   // Serial.println("G");
  //else
    //Serial.println("N");  
  
  
  while(Serial.available()<=0){  }
  inByte=Serial.read();
  chunk=inByte-65;
   
   
   
   while(Serial.available()<=0){  }
   inByte=Serial.read();
   
   
  
  return chunk;
}

int getChunk(){
  int inByte,chunk=0;
  
  do {
  while(Serial.available()<=0){}
  inByte=Serial.read();
  
  if ( inByte!=44)  {    chunk=10*chunk+inByte-48;}
  }
  while (inByte!=44 );
  
  return chunk;
}



void setup() {
  // connect to the serial port
  Serial.begin(115200);
  Serial.println("Go");
  // confirm ready state
    
 
}

void loop()
{
 
  int cmd,pin,val,dataPin,clkPin,bitOrder,dur,freq;
  unsigned long val2;
  while(1==1) {
    cmd=getCmd2();
    switch(cmd) {
      case _pinMode:
        
        pin=getChunk();
        val=getChunk();
        if (val==0)
          pinMode(pin,INPUT);
        else
          pinMode(pin,OUTPUT);
          
       break;
      case _digitalWrite:
        pin=getChunk();
        val=getChunk();
        if (val==0)
          digitalWrite(pin,LOW);
        else
          digitalWrite(pin,HIGH);
         
        break;
      case _digitalRead:
        pin=getChunk();
        val=digitalRead(pin);
        if (val==HIGH)
           Serial.println("1");
        else
           Serial.println("0");   
        break;
        
        case _analogRead:
          pin=getChunk();
          val=analogRead(pin);
          Serial.println(val);
        break;   
        case _analogWrite:
          pin=getChunk();
          val=getChunk();
          val=constrain(val,0,255);
          analogWrite(pin,val);
        break;
        case _tone:
          pin=getChunk();
          freq=getChunk();
          dur=getChunk();
          tone(pin,freq,dur);
          break;
        case _noTone:
          pin=getChunk();
          noTone(pin);
        break;
        case _shiftOut:
          dataPin=getChunk();
          clkPin=getChunk();
          bitOrder=getChunk();
          
          if (bitOrder==1)
            bitOrder=MSBFIRST;
          else
            bitOrder=LSBFIRST;
          val=getChunk();
          val=constrain(val,0,255);  
          
          shiftOut(dataPin,clkPin,bitOrder,val);
        break;
        
        
        case _pulseIn:
          pin=getChunk();
          val=getChunk();
          dur=getChunk();
          if (val==1)
            val2=pulseIn(pin,HIGH,dur);
          else
            val2=pulseIn(pin,LOW,dur);
          
          Serial.println(val2);
          break;
          
        case _millis:
            val=millis();
            Serial.println(val);
        break;
        case _micros:
          val2=micros();
          Serial.println(val2);
        break;
        case _delay:
          val=getChunk();
          delay(val);
        break;
        case _delayMicroseconds:
          val=getChunk();
          delayMicroseconds(val);
        break;
        case _pulseOut:
        pin=getChunk();
        dur=getChunk();
        digitalWrite(pin,HIGH);
        delayMicroseconds(dur);
        digitalWrite(pin,LOW);
        
        break;
    }
  }
} 

