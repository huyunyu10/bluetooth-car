"""Simple test for using adafruit_motorkit with a DC motor"""
import time
from adafruit_motorkit import MotorKit

def go():
    kit = MotorKit()
    kit.motor1.throttle = 0.493
    kit.motor2.throttle = -0.5

def left():
    kit = MotorKit()
    kit.motor1.throttle = 0.8
    kit.motor2.throttle = 0
    time.sleep(0.45)
    kit.motor1.throttle = 0
    kit.motor2.throttle = 0


#time.sleep(0.8)
#kit.motor1.throttle = 0.8
#kit.motor2.throttle = -0.855

def right():
    kit = MotorKit()

    kit.motor1.throttle = 0
    kit.motor2.throttle = -0.8
    time.sleep(0.45)
    kit.motor1.throttle = 0
    kit.motor2.throttle = 0


#time.sleep(0.6)
#kit.motor1.throttle = 0.8
#kit.motor2.throttle = -0.855
def stop():
    kit = MotorKit()
    time.sleep(3)
    kit.motor1.throttle = 0
    kit.motor2.throttle = 0

go()
time.sleep(15)
stop()


