import RPi.GPIO as GPIO
import time
import Adafruit_ADS1x15.ads1115 as ADS

GAIN = 1


# Set GPIO mode
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# Define GPIO pins for each servo
servo_pins = [18, 17]  # Add more GPIO pins as needed

# Set up each pin as an output and set PWM frequency
for pin in servo_pins:
    GPIO.setup(pin, GPIO.OUT)
    servo = GPIO.PWM(pin, 50)  # 50 Hz PWM frequency
    servo.start(0)  # Initialize to 0% duty cycle
    servos.append(servo)

def set_angle(servo, angle):
    duty = 2 + (angle / 18)  # Convert angle to duty cycle
    servo.ChangeDutyCycle(duty)
    time.sleep(0.5)
    servo.ChangeDutyCycle(0)

try:
    while True:
        for servo in servos:
            set_angle(servo, 90)  # Move to 90 degrees
            time.sleep(1)
            set_angle(servo, 0)  # Move to 0 degrees
            time.sleep(1)

except KeyboardInterrupt:
    pass

# Clean up
for servo in servos:
    servo.stop()
GPIO.cleanup()