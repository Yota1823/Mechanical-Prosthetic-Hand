import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import pigpio
import collections

# GPIO setup for the servos
servo_pins = [12, 13, 18, 19, 20]  # List of GPIO pins for the servos

# Initialize pigpio library
pi = pigpio.pi()

# I2C setup
i2c = busio.I2C(board.SCL, board.SDA)

# Create ADS1115 instance for pressure sensor
ads_pressure = ADS.ADS1115(i2c, address=0x49)  # Pressure sensor ADC
chan_pressure = AnalogIn(ads_pressure, ADS.P0)  # Pressure sensor connected to A0

# Parameters
PRESSURE_THRESHOLD = 0.7  # Adjust threshold voltage depending on which power supply using for pi boost
HOLD_DURATION = 1  # seconds
SMOOTHING_WINDOW = 10  # Number of readings to average

# Initialize counters and timers
pressure_held_start_time = None
hand_command_count = 0
hand_closed = False

# Smoothing window
pressure_readings = collections.deque(maxlen=SMOOTHING_WINDOW)

def read_pressure_sensor():
    return chan_pressure.voltage

def close_fingers():
    for pin in servo_pins:
        pi.set_servo_pulsewidth(pin, 500)  # Move servos to 0 degrees (closed position)
    print("Fingers closed")

def open_fingers():
    for pin in servo_pins:
        pi.set_servo_pulsewidth(pin, 1500)  # Move servos to neutral position (open)
    print("Fingers opened")

def is_pressure_held():
    """ Check if the pressure sensor is held above the threshold for the duration. """
    global pressure_held_start_time
    avg_pressure = sum(pressure_readings) / len(pressure_readings)
    print(f"Avg Pressure: {avg_pressure}, Threshold: {PRESSURE_THRESHOLD}")
    if avg_pressure > PRESSURE_THRESHOLD:
        if pressure_held_start_time is None:
            pressure_held_start_time = time.time()
            print("Pressure above threshold, starting timer.")
        elif time.time() - pressure_held_start_time >= HOLD_DURATION:
            print("Pressure held for duration, trigger action.")
            return True
    else:
        pressure_held_start_time = None
    return False

try:
    # Open fingers at the start
    open_fingers()
    time.sleep(2)  # Give the servos time to move to the initial position
    print("{:>5}\t{:>5}".format('raw', 'v'))

    while True:
        pressure_voltage = read_pressure_sensor()
        pressure_readings.append(pressure_voltage)
        print(f"Pressure Sensor Voltage: {pressure_voltage}")

        if len(pressure_readings) == SMOOTHING_WINDOW:
            if is_pressure_held():
                if not hand_closed:
                    print("Pressure held above threshold for 1 second, closing fingers")
                    close_fingers()
                    hand_closed = True
                else:
                    print("Pressure held above threshold for 1 second, opening fingers")
                    open_fingers()
                    hand_closed = False
                pressure_held_start_time = None  # Reset the start time after action

        time.sleep(0.1)  # Small delay to prevent overloading the system

except KeyboardInterrupt:
    pass

finally:
    for pin in servo_pins:
        pi.set_servo_pulsewidth(pin, 0)  # Turn off all servos
    pi.stop()
