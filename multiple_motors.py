from gpiozero import Servo
from time import sleep

# Initialize servos for each finger
servo_thumb = Servo(17)   # GPIO pin for the thumb
servo_point = Servo(7)   # GPIO pin for the point finger
servo_middle = Servo(22)  # GPIO pin for the middle finger

def gesture_grab():
    """Simulate a grabbing gesture by closing all three fingers."""
    servo_thumb.min()
    servo_point.min()
    servo_middle.min()
    
    sleep(1)

def gesture_point():
    """Simulate a pointing gesture by extending the point finger while the others are retracted."""
    servo_thumb.max()
    servo_point.min()  # Extend the point finger
    servo_middle.max()

    sleep(1)

def gesture_release():
    """Simulate releasing an object by opening all three fingers."""
    servo_thumb.max()
    servo_point.max()
    servo_middle.max()

    sleep(1)

def get_user_input():
    """Collect user input to control the hand."""
    command = input("Enter command (grab, point, release, quit): ").lower()
    return command

# Main loop to perform gestures based on user input
print("Control the hand: type 'grab', 'point', 'release', or 'quit'.")
while True:
    action = get_user_input()
    if action == "grab":
        gesture_grab()
    elif action == "point":
        gesture_point()
    elif action == "release":
        gesture_release()
    elif action == "quit":
        print("Quitting program.")
        break
    else:
        print("Invalid command. Please try again.")
