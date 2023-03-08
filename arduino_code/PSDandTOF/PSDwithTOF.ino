#include <Wire.h>
#include <VL53L1X.h>
#include <ADC.h>

VL53L1X sensor;
int PSD_pin = A1;
int PSD_val = 0;
int TOF_val = 0;

int time = 0;
int delay_time = 10;

ADC *adc = new ADC();

void setup()
{
  while (!Serial) {}
  Serial.begin(115200);
  Wire.begin();
  Wire.setClock(400000); // use 400 kHz I2C
  adc->adc1->setAveraging(16);
  adc->adc1->setResolution(16);
  adc->adc1->setConversionSpeed(ADC_CONVERSION_SPEED::VERY_HIGH_SPEED);
  adc->adc1->setSamplingSpeed(ADC_SAMPLING_SPEED::VERY_HIGH_SPEED);
  sensor.setTimeout(500);
  if (!sensor.init())
  {
    Serial.println("Failed to detect and initialize sensor!");
    while(1);
  }

  // Use long distance mode and allow up to 50000 us (50 ms) for a measurement.
  // You can change these settings to adjust the performance of the sensor, but
  // the minimum timing budget is 20 ms for short distance mode and 33 ms for
  // medium and long distance modes. See the VL53L1X datasheet for more
  // information on range and timing limits.
  sensor.setDistanceMode(VL53L1X::Long);
  sensor.setMeasurementTimingBudget(50000);

  // Start continuous readings at a rate of one measurement every 50 ms (the
  // inter-measurement period). This period should be at least as long as the
  // timing budget.
  sensor.startContinuous(50);
}

void loop()
{ 
   char buffer[10];
   PSD_val = analogRead(PSD_pin);        // reading psd
   TOF_val = sensor.read();
   sprintf(buffer, "%d, %d", TOF_val, PSD_val); 
   SerialUSB.println(buffer);
   if (sensor.timeoutOccurred()) { Serial.print(" TIMEOUT"); }
//   SerialUSB.println(time);
   Serial.println();
}
