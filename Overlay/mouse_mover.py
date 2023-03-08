import serial
import pyautogui
import time
import math

serial_comm = serial.Serial('COM5', 115200, timeout = 1)

# Get resolution of computer screen
computer_resolution = [pyautogui.size().width, pyautogui.size().height]
print("The computer's resolution is: ", computer_resolution) #This line is for debug only...remove later

# Get resolution of projector screen, only one point is needed since values are wrt LIDAR sensor in bottom left corner
projector_resolution = [400, 300]

# Calculate conversion factor from projector screen to computer screen
x_conv = (computer_resolution[0]/projector_resolution[0])
y_conv = (computer_resolution[1]/projector_resolution[1])

# We need to map PSD voltage to angle values here (in radians)

time.sleep(5)

while True:
    if serial_comm.in_waiting:
        packet = serial_comm.readline()
        coordinate_string = packet.decode("utf-8").strip('\n') # Receive coordinate as a string
        coordinate_array = list(map(int, coordinate_string.split(", "))) # Convert string to an array [x, y]
        # print(coordinate_array)
        x_val = coordinate_array[0] * math.cos(coordinate_array[1])
        y_val = coordinate_array[1] * math.sin(coordinate_array[1])
        pyautogui.mouseDown(button='left', x=x_val*x_conv, y=y_val*y_conv, duration=0.0, tween=None, logScreenshot=False, _pause=False)
    else:
        pyautogui.mouseUp() # If there's no data waiting in the serial port, lift the left mouse button up
