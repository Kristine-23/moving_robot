# These lines import nessesary libaries to run this code
import time
import board
import digitalio
import pwmio

from adafruit_motor import motor #Imports a function from the adafruit_moter libaries

Right_foward = board.GP12 # initializes the variable right_forward  and attaches it to GP12
Right_backward = board.GP13 # initalizes the varible right_backward and attaches it to GP13
Left_foward = board.GP14 # initalizes the varible right_backward and attaches it to GP14
Left_backward = board.GP15 # initalizes the varible right_backward and attaches it to GP15

right_foward = pwmio.PWMOut(Right_foward, frequency=10000) # Tells the controller that the moter is an output
right_backward = pwmio.PWMOut(Right_backward, frequency=10000) # Tells the controller that the moter is an output
left_foward = pwmio.PWMOut(Left_foward, frequency=10000) # Tells the controller that the moter is an output
left_backward = pwmio.PWMOut(Left_backward, frequency=10000) # Tells the controller that the moter is an output

Left_Motor = motor.DCMotor(left_foward, left_backward) #Configuration line (it is required)
Left_Motor_speed = 0 # Initiates the varible for the Left_motor_speed
Right_Motor = motor.DCMotor(right_foward, right_backward) #Configuration line (it is required)
Right_Motor_speed = 0  # Initiates the varible for the Left_motor_speed

while True:

    Left_Motor_speed = -1 #Makes left motor roll forward
    Left_Motor.throttle = Left_Motor_speed
    time.sleep(2)
    Left_Motor_speed = 1 #Makes left motor roll backwards
    Left_Motor.throttle = Left_Motor_speed
    time.sleep(2)
    Right_Motor_speed = -1 #Makes right motor roll forward
    Right_Motor.throttle = Right_Motor_speed
    time.sleep(2)
    Right_Motor_speed = 1 #Makes right motor roll backwards
    Right_Motor.throttle = Right_Motor_speed
    time.sleep(2)
