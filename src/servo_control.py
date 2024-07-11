#Code to control servo motors.
import pigpio

class ServoController:
    def __init__(self, servo_pins):
        self.servo_pins = servo_pins
        self.pi = pigpio.pi()
        self.setup_servos()

    def setup_servos(self):
        for pin in self.servo_pins:
            self.pi.set_mode(pin, pigpio.OUTPUT)
            self.pi.set_PWM_frequency(pin, 50)  # 50Hz for servo motors

    def set_servo_position(self, pin, pulse_width):
        self.pi.set_servo_pulsewidth(pin, pulse_width)

    def cleanup(self):
        for pin in self.servo_pins:
            self.pi.set_servo_pulsewidth(pin, 0)
        self.pi.stop()

if __name__ == "__main__":
    servo_pins = [12, 13, 18, 19, 20]
    controller = ServoController(servo_pins)
    try:
        # Example: move the first servo to 90 degrees
        controller.set_servo_position(servo_pins[0], 1500)
    except KeyboardInterrupt:
        pass
    finally:
        controller.cleanup()
