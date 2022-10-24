import time
import board
import usb_hid
import adafruit_hcsr04
#import adafruit_vcnl4040
from mouse_abs import Mouse

mouse = Mouse(usb_hid.devices)
# Note: Values are NOT pixels! 32767 = 100% (to right or to bottom) 

def scale_distance_to_mouse(dist):
    max_mouse = 32767
    min_dist = 5.0
    max_dist = 40.0
    percentage = (max_dist - dist)/(max_dist - min_dist)
    return int(percentage * max_mouse)

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D1, echo_pin=board.D2)
while True:
    measured_value = sonar.distance
    scaled_value = scale_distance_to_mouse(measured_value)
    mouse.move(x=20000, y=scaled_value)

    time.sleep(0.5)
    try:
        print((int(measured_value), scaled_value))
    except RuntimeError:
        print("Retrying!")


# i2c = board.I2C()
# sensor = adafruit_vcnl4040.VCNL4040(i2c)
#
# while True:
#     print("Proximity:", sensor.proximity)
#     #print("Light:", sensor.light)
#     #print("White:", sensor.white)
#     time.sleep(0.3)
