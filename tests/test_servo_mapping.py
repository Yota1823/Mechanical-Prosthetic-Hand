import unittest
from src.servo_mapping import map_muscle_to_servo, movement_to_servo

class TestServoMapping(unittest.TestCase):
    def test_map_muscle_to_servo(self):
        voltage = 2.5
        pulse_width = map_muscle_to_servo(voltage)
        self.assertTrue(500 <= pulse_width <= 2500)
    
    def test_movement_to_servo(self):
        voltage = 3.5
        finger = movement_to_servo(voltage)
        self.assertEqual(finger, "middle_finger")

if __name__ == '__main__':
    unittest.main()
