#define PIN_LEFT_MOTOR_SPEED 5
#define PIN_LEFT_MOTOR_FORWARD A0            
#define PIN_LEFT_MOTOR_REVERSE A1
#define PIN_LEFT_ENCODER 2
   
#define PIN_RIGHT_MOTOR_SPEED 6
#define PIN_RIGHT_MOTOR_FORWARD A2            
#define PIN_RIGHT_MOTOR_REVERSE A3
#define PIN_RIGHT_ENCODER 3

#define SERIAL_BAUD_RATE 9600

void setup() {
  Serial.begin(SERIAL_BAUD_RATE);
  
  pinMode(PIN_LEFT_MOTOR_SPEED, OUTPUT);
  analogWrite(PIN_LEFT_MOTOR_SPEED, 0);
  pinMode(PIN_LEFT_MOTOR_FORWARD, OUTPUT);
  pinMode(PIN_LEFT_MOTOR_REVERSE, OUTPUT);

  pinMode(PIN_RIGHT_MOTOR_SPEED, OUTPUT);
  analogWrite(PIN_RIGHT_MOTOR_SPEED, 0);
  pinMode(PIN_RIGHT_MOTOR_FORWARD, OUTPUT);
  pinMode(PIN_RIGHT_MOTOR_REVERSE, OUTPUT);
}

void analog_write_to_motors(int left, int right) {
  digitalWrite(PIN_LEFT_MOTOR_FORWARD, HIGH);
  digitalWrite(PIN_LEFT_MOTOR_REVERSE, LOW);
  analogWrite(PIN_LEFT_MOTOR_SPEED, left_speed);

  digitalWrite(PIN_RIGHT_MOTOR_FORWARD, HIGH);
  digitalWrite(PIN_RIGHT_MOTOR_REVERSE, LOW);
  analogWrite(PIN_RIGHT_MOTOR_SPEED, right_speed);
}

void write_info_to_serial() {
  Serial.println("ROBOT NAME  - GANDALF");
  Serial.println("LEFT MOTOR  - y = 1.4392087912087914 * x + 104.1178021978023");
  Serial.println("RIGHT MOTOR - y = 1.7475954592363252 * x + 112.79119367045064");
  Serial.println("AUTHOR 1    - S20205");
  Serial.println("AUTHOR 2    - S20335");
}

bool left_in_range(int x)  { return x >= 259 && x <= 447; }
bool right_in_range(int x) { return x >= 137 && x <= 519; }

double left(int x)  { return (x - 104.1178021978023)  / 1.4392087912087914; }
double right(int x) { return (x - 112.79119367045064) / 1.7475954592363252; }

void loop() {
  while (Serial.available() <= 0) { /* WAIT */ }

  // Serial.parseInt - this shit broken 
  String inbud = Serial.readString();
  while (Serial.available() > 0) { // clean up
    Serial.read();
  }

  int speed = inbud.toInt(); // in the case of garbage we get 0
  if (inbud == "INFO\n") {
    write_info_to_serial();
  } else if (speed != 0) {
    if (left_in_range(speed) && right_in_range(speed))) {
      analog_write_to_motors((int) left(speed), (int) right(speed));
      Serial.println("VELOCITY SET");
    } else {
      Serial.println("OUT OF RANGE <137; 447>");
    }
  } else {
    analog_write_to_motors(0, 0); // stop
  }
}
