
//Definerer pins som vi skal bruke til sensoren
#define echoPin 3	
#define trigPin 2
#define ena 11

//Definerer pins for motorene
#define in1 13 
#define in2 12
#define in3 8
#define in4 9

float airspeed = 0.034;
/*340 m/s = 34 000 cm/s = 34 cm/ms = 0.034 cm/µs*/

float duration, distance; //avstanden distance er i centimeter. Formelen s = vt for strekning, velocity og 



//Det som kjøres før hovedløkken. Definerer hvilke pins som skal ha input og output
void setup() {
  pinMode(echoPin, INPUT);
  pinMode(trigPin, OUTPUT);
  Serial.begin(9600);
  pinMode(ena, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
}

//Hovedløkken som kjører
void loop() {
//Finner distansen fra sensoren og objektet.
digitalWrite(trigPin, LOW);
delayMicroseconds(5);
digitalWrite(trigPin, HIGH);
delayMicroseconds(10);
digitalWrite(trigPin, LOW);
duration = pulseIn(echoPin, HIGH); //mikrosekunder
distance = airspeed * duration/2; //Beregner avstand
Serial.println(String(distance)+" cm");

delay(100);
int v = 200;
//definerer motorstyring
analogWrite(ena,v);
analogWrite(enb,v);
//Definerer retningen til motorene
digitalWrite(in1,HIGH);
digitalWrite(in2,LOW);
digitalWrite(in3,HIGH);
digitalWrite(in4,LOW);
}
