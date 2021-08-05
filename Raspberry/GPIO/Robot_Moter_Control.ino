#define ckwiseA 22
#define c_ckwiseA 23
#define Enable_A 2

#define ckwiseB 27
#define c_ckwiseB 26
#define Enable_B 4

#define ckwiseC 30
#define c_ckwiseC 31
#define Enable_C 6

byte straight = 100;

byte corner = 80;

void setup() {

pinMode(ckwiseC,OUTPUT);

pinMode(c_ckwiseC,OUTPUT);

pinMode(Enable_C,OUTPUT);

pinMode(ckwiseB,OUTPUT);

pinMode(c_ckwiseB,OUTPUT);

pinMode(Enable_B,OUTPUT);

pinMode(ckwiseA,OUTPUT);

pinMode(c_ckwiseA,OUTPUT);

pinMode(Enable_A,OUTPUT);
}

void motor_speed(int spd)  
{  
  analogWrite(Enable_A,spd);  
  analogWrite(Enable_B,spd);  
  analogWrite(Enable_C,spd);  
}  

void motor_dir(int dir)

{

if(dir == 0) //FORWARD

{

digitalWrite(ckwiseA,LOW);

digitalWrite(c_ckwiseA,LOW);

digitalWrite(ckwiseB,LOW);

digitalWrite(c_ckwiseB,HIGH);

digitalWrite(ckwiseC,HIGH);

digitalWrite(c_ckwiseC,LOW);

}

else if(dir == 1) //turn right

{


digitalWrite(ckwiseA,LOW);

digitalWrite(c_ckwiseA,HIGH);

digitalWrite(ckwiseB,LOW);

digitalWrite(c_ckwiseB,HIGH);

digitalWrite(ckwiseC,LOW);

digitalWrite(c_ckwiseC,HIGH); 

}

else if(dir == 2) //turn left

{
  
digitalWrite(ckwiseA,HIGH);

digitalWrite(c_ckwiseA,LOW);

digitalWrite(ckwiseB,HIGH);

digitalWrite(c_ckwiseB,LOW);

digitalWrite(ckwiseC,HIGH);

digitalWrite(c_ckwiseC,LOW);

}

else if(dir == 3) //backward

{
digitalWrite(ckwiseA,LOW);

digitalWrite(c_ckwiseA,LOW);

digitalWrite(ckwiseB,HIGH);

digitalWrite(c_ckwiseB,LOW);

digitalWrite(ckwiseC,LOW);

digitalWrite(c_ckwiseC,HIGH);

}

else if(dir == 4) //default

{

digitalWrite(ckwiseA,LOW);

digitalWrite(c_ckwiseA,LOW);

digitalWrite(ckwiseB,LOW);

digitalWrite(c_ckwiseB,LOW);

digitalWrite(ckwiseC,LOW);

digitalWrite(c_ckwiseC,LOW);
}

}

void loop()

{

  if(analogRead(A1)>900) // move forward

  {

motor_dir(0);
motor_speed(straight);

delay(100);

}

else if(analogRead(A1)<300) // move backward

{

motor_dir(3);

motor_speed(straight);

delay(100);

}

else if(analogRead(A0)>900) // turn right

{

motor_dir(1);

motor_speed(corner);

delay(100);

}

else if(analogRead(A0)<300) // turn left

{

motor_dir(2);

motor_speed(corner);

delay(100);

}

else

  {

motor_dir(4);

motor_speed(straight);

delay(100);

  }

}
