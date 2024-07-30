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

# Create ADS1115 instance for muscle sensor
ads_muscle = ADS.ADS1115(i2c, address=0x48)  # Default I2C address
chan_muscle = AnalogIn(ads_muscle, ADS.P0)   # Muscle sensor connected to A0

# Initialize counters and timers
muscle_drop_count = 0
muscle_drop_start_time = None

def read_muscle_sensor():
    return chan_muscle.voltage

def close_fingers():
    for pin in servo_pins:
        pi.set_servo_pulsewidth(pin, 500)  # Move servos to 0 degrees (closed position)
    print("Fingers closed")

def open_fingers():
    for pin in servo_pins:
        pi.set_servo_pulsewidth(pin, 1500)  # Move servos to neutral position (open)
    print("Fingers opened")

try:
    # Open fingers at the start
    open_fingers()
    time.sleep(2)  # Give the servos time to move to the initial position

    while True:
        # Read muscle sensor data
        muscle_voltage = read_muscle_sensor()
        print(f"Muscle Sensor Voltage: {muscle_voltage}")

        # Check muscle sensor condition
        if muscle_voltage < 0.1:
            if muscle_drop_start_time is None:
                muscle_drop_start_time = time.time()
            elif time.time() - muscle_drop_start_time <= 5:
                muscle_drop_count += 1
                muscle_drop_start_time = None

        # Check if conditions are met to close fingers
        if muscle_drop_count >= 2:
            print("Voltage dropped below 0.1V, closing fingers")
            close_fingers()
            muscle_drop_count = 0
            muscle_drop_start_time = None

        # Check if conditions are met to open fingers
        if muscle_voltage > 4.5:
            print("Voltage above 4.5V, opening fingers")
            open_fingers()

        time.sleep(0.1)  # Small delay to prevent overloading the system

except KeyboardInterrupt:
    pass

finally:
    for pin in servo_pins:
        pi.set_servo_pulsewidth(pin, 0)  # Turn off all servos
    pi.stop()
