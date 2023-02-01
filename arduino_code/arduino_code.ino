int x = 200;
int y = 150;

void setup() {
	Serial.begin(115200); // use the same baud-rate as the python side

  delay(10);

  // Test highlighting
  // for (int i = 0; i < 100; i++) {
  //   x++;
  //   char buffer[10];
  //   sprintf(buffer, "%d, %d", x, y);
  //   Serial.println(buffer);
  // }

  // Test button pressing
  for (int i = 0; i < 100; i++) {
    char buffer[10];
    sprintf(buffer, "%d, %d", 7, 2);
    Serial.println(buffer);
  }
}
void loop() {
  
}
