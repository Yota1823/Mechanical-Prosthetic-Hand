import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import pigpio

# GPIO setup for the servos
servo_pins = [12, 13, 18, 19, 20]  # List of GPIO pins for the servos

# Initialize pigpio library
pi = pigpio.pi()

# I2C setup
i2c = busio.I2C(board.SCL, board.SDA)

# Create an ADS1115 instance
ads = ADS.ADS1115(i2c)
chan = AnalogIn(ads, ADS.P0)  # Assuming muscle sensor is connected to A0

# Initialize the current servo index
current_servo_index = 0

def read_muscle_sensor():
    # Read the ADC value from the specified channel
    return chan.voltage

def map_muscle_to_servo(voltage):
    # Map the muscle voltage (0-3.3V) to a servo pulse width (500-2500 microseconds)
    pulse_width = int((voltage / 3.3) * 2000 + 500)
    return pulse_width

try:
    while True:
        # Read the muscle sensor voltage
        muscle_voltage = read_muscle_sensor()
        print("Muscle Sensor Voltage: ", muscle_voltage)

        # Map the muscle voltage to a servo pulse width
        pulse_width = map_muscle_to_servo(muscle_voltage)

        # Set the current servo position
        pi.set_servo_pulsewidth(servo_pins[current_servo_index], pulse_width)

        # Check if the muscle voltage crosses a threshold to switch to the next servo
        if muscle_voltage < 1.0:  # Example threshold
            current_servo_index = (current_servo_index + 1) % len(servo_pins)
            time.sleep(1)  # Small delay to prevent rapid switching

        time.sleep(0.1)  # Small delay to prevent overloading the servo

except KeyboardInterrupt:
    pass

finally:
    for pin in servo_pins:
        pi.set_servo_pulsewidth(pin, 0)  # Turn off all servos
    pi.stop()
