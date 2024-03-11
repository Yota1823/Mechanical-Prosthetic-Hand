#!/usr/bin/env python3
#import RPi.GPIO as GPIO 
import pigpio
import time 

pi = pigpio.pi()
servo_pin = 17

pi.set_servo_pulsewidth(servo_pin,1500)
time.sleep(1)

pi.set_servo_pulsewidth(servo_pin,2000)
time.sleep(1)

pi.set_servo_pulsewidth(servo_pin,2000)
pi.stop()

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
