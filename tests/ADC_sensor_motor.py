#Dont forget to sudo systemctl enable pigpiod and sudo systemctl start pigpiod before run this code
import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

from gpiozero import Servo
from time import sleep
import math
import sys
from gpiozero.pins.pigpio import PiGPIOFactory

factory = PiGPIOFactory()

servo_pin_1 = Servo(12,pin_factory = factory)
servo_pin_2 = Servo(18,pin_factory = factory)
servo_pin_3 = Servo(13,pin_factory = factory)
servo_pin_4 = Servo(19,pin_factory = factory)
servo_pin_5 = Servo(20,pin_factory = factory)


def grab_object():
    """Function to rotate servo to grab object."""
    print("Grabbing object...")
    servo_pin_1.min()  # Adjust as necessary for your servo's grabbing position
    servo_pin_2.min()
    servo_pin_3.min()
    servo_pin_4.min()
    servo_pin_5.min()
    sleep(2)  # Adjust timing as necessary
    print("Releasing object...")
    servo_pin_1.max()  # Adjust to return servo to starting position
    servo_pin_2.max()
    servo_pin_3.max()
    servo_pin_4.max()
    servo_pin_5.max()
    sleep(2)  # Adjust timing as necessary

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1115(i2c)

# Create single-ended input on channel 0
chan = AnalogIn(ads, ADS.P0)


# Create differential input between channel 0 and 1
#chan = AnalogIn(ads, ADS.P0, ADS.P1)

print("{:>5}\t{:>5}".format('raw', 'v'))



while True:
    print("{:>5}\t{:>5.3f}".format(chan.value, chan.voltage))
    if chan.value<500:
        grab_object()
#     else:
#         print("Quitting simulation.")
#         sys.exit(0)
    time.sleep(0.5)
    