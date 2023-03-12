import serial
import pyautogui
import time
import math
import random

# Define voltage range of PSD 
min_voltage = 83
max_voltage = 90

# Define angle range to map the voltage to - get these values via calibration
min_angle = 0
max_angle = 90

serial_comm = serial.Serial('COM7', 115200, timeout = 1)
pyautogui.FAILSAFE = False

# Get resolution of computer screen
computer_resolution = [pyautogui.size().width, pyautogui.size().height]
print("The computer's resolution is: ", computer_resolution) #This line is for debug only...remove later

# Get resolution of projector screen, only one point is needed since values are wrt LIDAR sensor in bottom left corner
projector_resolution = [400, 300]

# Calculate conversion factor from projector screen to computer screen
x_conv = (computer_resolution[0]/projector_resolution[0])
y_conv = (computer_resolution[1]/projector_resolution[1])

time.sleep(5)
while True:
    if serial_comm.in_waiting:
        packet = serial_comm.readline()
        # print(packet)
        coordinate_string = packet.decode("utf-8").strip('\n') # Receive coordinate as a string
        print(coordinate_string)
        voltage = float(coordinate_array[1])
        angle = ((voltage - min_voltage) / (max_voltage - min_voltage)) * (max_angle - min_angle) + min_angle #linear interpolation
        if (len(coordinate_string)>1): 
            coordinate_array = list(map(int, coordinate_string.split(", "))) # Convert string to an array [x, y]
            x_val = coordinate_array[0] * math.cos(coordinate_array[1])
            y_val = coordinate_array[0] * math.sin(coordinate_array[1])
            # y_val = coordinate_array[0] * math.sin(random.uniform(0, 6.28))
            if (computer_resolution[0]<x_val or computer_resolution[1]<y_val or x_val<0 or y_val<0):
                pyautogui.moveTo(x = x_val * x_conv, y = y_val * y_conv)
            #   pyautogui.mouseDown(button='left', x=x_val*x_conv, y=y_val*y_conv, duration=0.0, tween=None, logScreenshot=False, _pause=False)
    else:
        pyautogui.mouseUp() # If there's no data waiting in the serial port, lift the left mouse button up

