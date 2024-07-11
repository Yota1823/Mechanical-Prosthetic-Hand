import time
import pigpio

pi = pigpio.pi() # connect to local pi

pi.set_servo_pulsewidth(12, 1000)
time.sleep(0.5)
pi.set_servo_pulsewidth(12, 1500)
