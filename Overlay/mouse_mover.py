import pyautogui
import time

# Current X and Y coordinates will be obtained via PySerial from microcontroller
x = 200 # function call from PySerial
y = 150 # function call from PySerial

# Get resolution of computer screen
computer_resolution = [pyautogui.size().width, pyautogui.size().height]
print("The computer's resolution is: ", computer_resolution) #This line is for debug only...remove later

# Get resolution of projector screen, only one point is needed since values are wrt LIDAR sensor in bottom left corner
projector_resolution = [400, 300]

# Convert coordinates from project screen to computer screen
x_conv = (computer_resolution[0]/projector_resolution[0]) * x
y_conv = (computer_resolution[1]/projector_resolution[1]) * y

# Infinite loop to read data from microcontroller. Microcontroller will send (0, 0) if no input is received on LIDAR sensor
while True:
    if (x != 0 and y != 0):
        pyautogui.click(x_conv, y_conv)
        time.sleep(5) #This line is for debug only...remove later

# Current test:
#   -The projector resolution is currently assumed to be 400 x 300
#   -I set the X and Y coordinates from the microcontroller to be at the middle of this (200, 150)
#   -The program will move the mouse to the middle of my computer monitor
