import serial
import pyautogui

serial_comm = serial.Serial('COM3', 115200, timeout = 1)

# Get resolution of computer screen
computer_resolution = [pyautogui.size().width, pyautogui.size().height]
print("The computer's resolution is: ", computer_resolution) #This line is for debug only...remove later

# Get resolution of projector screen, only one point is needed since values are wrt LIDAR sensor in bottom left corner
projector_resolution = [400, 300]

# Calculate conversion factor from projector screen to computer screen
x_conv = (computer_resolution[0]/projector_resolution[0])
y_conv = (computer_resolution[1]/projector_resolution[1])

while True:
    if serial_comm.in_waiting:
        packet = serial_comm.readline()
        coordinate_string = packet.decode("utf-8").strip('\n') # Receive coordinate as a string
        coordinate_array = list(map(int, coordinate_string.split(", "))) # Convert string to an array [x, y]
        print(coordinate_array)
        pyautogui.moveTo(coordinate_array[0]*x_conv, coordinate_array[1]*y_conv, duration=0.0, tween=None, logScreenshot=False, _pause=False)
