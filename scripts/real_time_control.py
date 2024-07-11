import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import pigpio
import joblib

# Load the trained model
model = joblib.load('../models/servo_model.pkl')

# GPIO setup for the servos
servo_pins = [12, 13, 18, 19, 20]  # Adjust GPIO pins as necessary

# Initialize pigpio library
pi = pigpio.pi()

# I2C setup
i2c = busio.I2C(board.SCL, board.SDA)

# Create an ADS1115 instance
ads = ADS.ADS1115(i2c)
chan = AnalogIn(ads, ADS.P0)  # Assuming muscle sensor is connected to A0

def read_muscle_sensor():
    return chan.voltage

def predict_servo_position(voltage):
    return model.predict([[voltage]])[0]

try:
    while True:
        muscle_voltage = read_muscle_sensor()
        servo_position = predict_servo_position(muscle_voltage)
        pulse_width = int((servo_position / 180) * 2000 + 500)  # Adjust this mapping based on your servo

        # Set the servo position for each motor
        for pin in servo_pins:
            pi.set_servo_pulsewidth(pin, pulse_width)

        time.sleep(0.1)

except KeyboardInterrupt:
    pass

finally:
    for pin in servo_pins:
        pi.set_servo_pulsewidth(pin, 0)  # Turn off all servos
    pi.stop()
