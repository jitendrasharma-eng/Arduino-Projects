const int yellowLED = 12;  // Pin for yellow LED
const int redLED = 11;     // Pin for red LED
const int blueLED = 10;    // Pin for blue LED

void setup() {
  Serial.begin(9600);      // Set the baud rate to match the Python script
  pinMode(yellowLED, OUTPUT);
  pinMode(redLED, OUTPUT);
  pinMode(blueLED, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();  // Read incoming byte

    // Turn off all LEDs initially
    digitalWrite(yellowLED, LOW);
    digitalWrite(redLED, LOW);
    digitalWrite(blueLED, LOW);

    // Control LEDs based on the command received
    if (command == '1') {
      digitalWrite(blueLED, HIGH);          // Blue only
    } 
    else if (command == '2') {
      digitalWrite(redLED, HIGH);           // Red only
    } 
    else if (command == '3') {
      digitalWrite(yellowLED, HIGH);        // Yellow only
    } 
    else if (command == '4') {
      digitalWrite(redLED, HIGH);           // Red and Blue
      digitalWrite(blueLED, HIGH);
    } 
    else if (command == '5') {
      digitalWrite(yellowLED, HIGH);        // Yellow and Blue
      digitalWrite(blueLED, HIGH);
    } 
    else if (command == '6') {
      digitalWrite(yellowLED, HIGH);        // Yellow and Red
      digitalWrite(redLED, HIGH);
    } 
    else if (command == '7') {
      digitalWrite(yellowLED, HIGH);        // Yellow, Red, and Blue
      digitalWrite(redLED, HIGH);
      digitalWrite(blueLED, HIGH);
    }
    // If command is '0' or any other, all LEDs remain off
    /*// Control LEDs based on the command received
    switch (command) {
      case '1':
        digitalWrite(blueLED, HIGH);          // Blue only
        break;
      case '2':
        digitalWrite(redLED, HIGH);           // Red only
        break;
      case '3':
        digitalWrite(yellowLED, HIGH);        // Yellow only
        break;
      case '4':
        digitalWrite(redLED, HIGH);           // Red and Blue
        digitalWrite(blueLED, HIGH);
        break;
      case '5':
        digitalWrite(yellowLED, HIGH);        // Yellow and Blue
        digitalWrite(blueLED, HIGH);
        break;
      case '6':
        digitalWrite(yellowLED, HIGH);        // Yellow and Red
        digitalWrite(redLED, HIGH);
        break;
      case '7':
        digitalWrite(yellowLED, HIGH);        // Yellow, Red, and Blue
        digitalWrite(redLED, HIGH);
        digitalWrite(blueLED, HIGH);
        break;
      default:
        // Turn off all LEDs if no color is detected (command '0')
        break;*/
  }
}
