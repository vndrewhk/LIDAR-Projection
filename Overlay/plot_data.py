import serial
import matplotlib.pyplot as plt
import numpy as np
import time

ser = serial.Serial("COM3", 9600) # Change serial port and baud rate to match arduino code
times = []
sine_wave = []
start_time = 0

while True:
  data = ser.readline().decode("utf-8").strip()
  if start_time == 0:
    start_time = time.time()
  current_time = time.time() - start_time
  if data:
    sine_wave.append(float(data))
    times.append(current_time)
    plt.clf()
    plt.plot(times, sine_wave)
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.pause(0.01)
