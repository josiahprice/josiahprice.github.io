
int pushbutton = 6;
int fan = 7;
int buzzer = 8;
int greenlight = 11;
int yellowlight = 9;
int redlight = 10;



void setup() {
 
  // put your setup code here, to run once:
pinMode(pushbutton, INPUT_PULLUP);
pinMode(fan, OUTPUT);
pinMode(buzzer, OUTPUT);
pinMode(greenlight, OUTPUT);
pinMode(yellowlight, OUTPUT);
pinMode(redlight, OUTPUT);

}

void loop() {
  
  // put your main code here, to run repeatedly:
  if (digitalRead(pushbutton)==LOW)
  {
    digitalWrite(fan, HIGH);
    digitalWrite(redlight, HIGH);
    delay (5000);
    digitalWrite(redlight, LOW);
    digitalWrite (yellowlight, HIGH);
    delay (5000);
    digitalWrite(yellowlight, LOW);
    digitalWrite(buzzer, HIGH);
    digitalWrite(greenlight, HIGH);
    delay (2000);
    digitalWrite (greenlight, LOW);
    digitalWrite (fan, LOW);
  }
}
