int x = 200;
int y = 150;

void setup() {
	Serial.begin(115200); // use the same baud-rate as the python side

  delay(5);

  for (int i = 0; i < 100; i++) {
    x++;
    char buffer[10];
    sprintf(buffer, "%d, %d", x, y);
    Serial.println(buffer);
    delay(100);
  }
}
void loop() {
  
}
