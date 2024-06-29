#Before you run the code
#cd ~/Mechanical-Prosthetic-Hand
#source venv/bin/activate
import RPi.GPIO as GPIO
import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Set up GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Define GPIO pins for each servo motor
servo_pins = [12, 13, 18, 19, 20]

# Set up each GPIO pin as an output and initialize PWM
pwm_instances = []
for pin in servo_pins:
    GPIO.setup(pin, GPIO.OUT)
    pwm = GPIO.PWM(pin, 50)  # 50Hz frequency
    pwm.start(0)
    pwm_instances.append(pwm)

# Set up I2C bus and ADS1115
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)
chan = AnalogIn(ads, ADS.P0)

def read_pressure_sensor():
    # Read the ADC value from the specified channel
    return chan.value

try:
    while True:
        # Read the pressure sensor value from channel 0
        pressure_value = read_pressure_sensor()
        print("Pressure Sensor Value: ", pressure_value)

        if pressure_value < 500:
            # Move all motors to 0 degrees
            for pwm in pwm_instances:
                pwm.ChangeDutyCycle(2.5)  # Duty cycle for 0 degrees
            time.sleep(1)

            # Move all motors to 90 degrees
            for pwm in pwm_instances:
                pwm.ChangeDutyCycle(7.5)  # Duty cycle for 90 degrees
            time.sleep(1)

            # Move all motors to 180 degrees
            for pwm in pwm_instances:
                pwm.ChangeDutyCycle(12.5)  # Duty cycle for 180 degrees
            time.sleep(1)

except KeyboardInterrupt:
    for pwm in pwm_instances:
        pwm.stop()
    GPIO.cleanup()
