#!/usr/bin/env python3
#import RPi.GPIO as


from gpiozero import Servo
from time import sleep
import sys
from gpiozero.pins.pigpio import PiGPIOFactory

factory = PiGPIOFactory()

# Setup your servo motor
servo_pin_1 = Servo(18,pin_factory = factory)
servo_pin_2 = Servo(17,pin_factory = factory)
servo_pin_3 = Servo(23,pin_factory = factory)

# Adjust this to your GPIO pin connected to the servo
#servo = Servo(servo_pin)

def simulate_sensor_trigger():
    """Function to simulate sensor trigger via keyboard input."""
    user_input = input("Press Enter to simulate the sensor being triggered (type 'q' and Enter to quit): ")
    if user_input.lower() == 'q':
        return False
    return True

def grab_object():
    """Function to rotate servo to grab object."""
    print("Grabbing object...")
    servo_pin_1.min()  # Adjust as necessary for your servo's grabbing position
    servo_pin_2.min()
    servo_pin_3.min()
    sleep(2)  # Adjust timing as necessary
    print("Releasing object...")
    servo_pin_1.max()  # Adjust to return servo to starting position
    servo_pin_2.max()
    servo_pin_3.max()
    sleep(2)  # Adjust timing as necessary

print("Press Enter to simulate the sensor being triggered.")
print("Starting simulation. Type 'q' and Enter to quit.")
while True:
    if simulate_sensor_trigger():
        grab_object()
    else:
        print("Quitting simulation.")
        sys.exit(0)


'''
# Setup the GPIO pin for the servo 
servo_pin = 17 # Change to the GPIO pin you are using 
GPIO.setmode(GPIO.BCM) # Use Broadcom pin numbering 
GPIO.setup(servo_pin, GPIO.OUT) 

# Initialize PWM on the servo pin with a frequency of 50Hz 
pwm = GPIO.PWM(servo_pin, 50) 
pwm.start(0) 
def set_servo_angle(angle): 
	# Convert the angle to duty cycle 
	# 2.5 is the duty cycle for 0 degrees 
	# 12.5 is the duty cycle for 180 degrees 
	# These values might need slight adjustment for your specific servo 
	duty = (angle / 18) + 2.5 
	pwm.ChangeDutyCycle(duty) 
	time.sleep(1) # Wait 1 second for the servo to reach the angle 
	pwm.ChangeDutyCycle(0) # Stop sending the PWM signal 

try: 
	# Rotate the servo to different angles 
	set_servo_angle(0) # 0 degrees 
	set_servo_angle(90) # 90 degrees 
	set_servo_angle(180) # 180 degrees 
finally: 
	# Cleanup the GPIO pin and stop PWM 
	pwm.stop() 
	GPIO.cleanup() 
'''
