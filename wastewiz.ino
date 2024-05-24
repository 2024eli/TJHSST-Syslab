#include <LiquidCrystal.h>

const int rs = 13, en = 12, d4 = 4, d5 = 5, d6 = 6, d7 = 7;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

#define dirPin 8
#define stepPin 9
#define stepsPerRevolution 200
#define stepsPerRecycle 60

#define takePicPin 11

#define buttonPin 3
volatile bool shouldMoveMotor = false;

bool recycleIt = false;
bool trashIt = false;
int buttonCounter = 0;
int recycleCounter = 0;

void setup() {
  lcd.begin(16, 2);
  Serial.begin(9600);

  pinMode(buttonPin, INPUT);
  pinMode(stepPin, OUTPUT);
  pinMode(dirPin, OUTPUT);
  pinMode(takePicPin, OUTPUT);

  attachInterrupt(digitalPinToInterrupt(buttonPin), triggerMotor, RISING);
}

void loop() {
  if(shouldMoveMotor) {
    shouldMoveMotor = false;
    moveStepper();
    }
  else {
  lcd.clear();
  lcd.setCursor(3,0);
  lcd.print("Place waste");
  lcd.setCursor(3,1);
  lcd.print("inside bin");
  delay(1400);
  lcd.clear();
  lcd.setCursor(1,0);
  lcd.print("Press button to");
  lcd.setCursor(1,1);
  lcd.print("sort & dispose");
  delay(2000);
  //Serial.println(buttonCounter);
  }
}

void triggerMotor() {
  shouldMoveMotor = true;
  digitalWrite(takePicPin, HIGH);
}

void moveStepper() {
  while(!recycleIt || !trashIt)
    {
      int piRecycle = analogRead(A0);
      int piTrash = analogRead(A1);
      lcd.clear();
      lcd.setCursor(1,0);
      lcd.print("Processing...");
      Serial.println(piRecycle);
      if(piRecycle >= 1023){
        recycleIt = true;
        lcd.print("Recyclable");
      }
      if(piTrash >= 1023){
        trashIt = true;
        lcd.print("Trash");
      }
    }
  digitalWrite(takePicPin, LOW);
 
  if(recycleIt){
    digitalWrite(dirPin, HIGH);
    for (int i = 0; i < stepsPerRecycle; i++) {
      digitalWrite(stepPin, HIGH);
      delayMicroseconds(2000);
      digitalWrite(stepPin, LOW);
      delayMicroseconds(2000);
    }  
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print("Items");
  lcd.setCursor(0,1);
  lcd.print("Recycled: ");
  lcd.print(recycleCounter);
  recycleCounter++;
  delay(2000);
  lcd.setCursor(10,1);
  lcd.print(recycleCounter);

  digitalWrite(dirPin, LOW);
  for (int i = 0; i < stepsPerRecycle; i++) {
    digitalWrite(stepPin, HIGH);
    delayMicroseconds(2000);
    digitalWrite(stepPin, LOW);
    delayMicroseconds(2000);
    }  
  delay(1500);
  lcd.clear();
  }
  else{
    digitalWrite(dirPin,LOW);
    for (int i = 0; i < stepsPerRecycle; i++) {
      digitalWrite(stepPin, HIGH);
      delayMicroseconds(2000);
      digitalWrite(stepPin, LOW);
      delayMicroseconds(2000);    
    }
    delay(2000);
      digitalWrite(dirPin, HIGH);
    for (int i = 0; i < stepsPerRecycle; i++) {
      digitalWrite(stepPin, HIGH);
      delayMicroseconds(2000);
      digitalWrite(stepPin, LOW);
      delayMicroseconds(2000);
      }  
  }
  recycleIt = false;
  trashIt = false;
}

 
