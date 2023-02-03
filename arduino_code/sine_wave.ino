#include <math.h>

void setup() {
  Serial.begin(9600);
}
void loop() {
  float amplitude = 100.0;
  float frequency = 0.1;
  float time = millis() / 1000.0;
  float sine_val = amplitude * sin(2 * M_PI * frequency * time);

  Serial.println(sine_val); //prints amplitude values on a sine wave with respect to time
  delay(100);
}
