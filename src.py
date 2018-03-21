#!/usr/bin/env python3

from ev3dev.ev3 import *
from time import sleep

SENSOR_PORT = "in1"
MOTOR_LEFT_PORT = "outA"
MOTOR_RIGHT_PORT = "outB"

sensor = UltrasonicSensor(SENSOR_PORT)
motorLeft = LargeMotor(MOTOR_LEFT_PORT)
motorRight = LargeMotor(MOTOR_RIGHT_PORT)
button = Button()
lcd = Screen()
ts = TouchSensor("in2")

motorRight.stop();
motorLeft.stop();

run = True

desiredLength = 15

baseSpeed = 500
baseSpeedRight = baseSpeed
baseSpeedLeft = baseSpeed

threshold = 20
error = 0
lastError = 0
proportional = 0
integral = 0
derivative = 0

maxPidValue = 900-baseSpeed
pidValue = 0

kP = 11.6
kI = 0.058
kD = 65

lcd.clear()
lcd.draw.text((10, 15),"Initialization is completed")
lcd.draw.text((10, 100),"kP = " + str(kP) + " kI = " + str(kI) + " kD = " + str(kD))
lcd.update()
Sound.beep()
sleep(1.5)

motorLeft.run_forever(speed_sp=(baseSpeedLeft))
motorRight.run_forever(speed_sp=(baseSpeedRight))

while run:
    sensorValue = sensor.value() / 10  # Distance in cm
    print("Current = " + str(sensorValue) + " of " + str(desiredLength))
    lcd.clear()
    lcd.draw.text((10, 15), "Current distance: " + str(sensorValue))
    lcd.draw.text((10, 35), "Desired distance: " + str(desiredLength))
    lcd.draw.text((10, 100),"kP = " + str(kP) + " kI = " + str(kI) + " kD = " + str(kD))
    lcd.update()


    # PID calculations
    error = sensorValue - desiredLength
    if abs(error) < threshold:
        integral += error
    else:
        integral = 0
    derivative = error - lastError
    lastError = error
    pidValue = error*kP + integral*kI + derivative*kD

    if pidValue > maxPidValue:
        pidValue = maxPidValue
    elif pidValue < -1 * maxPidValue:
        pidValue = -1*maxPidValue
    # PID calculated

    motorRight.run_forever(speed_sp=(baseSpeedRight + pidValue))
    motorLeft.run_forever(speed_sp=(baseSpeedLeft - pidValue))

    if ts.value():
    	run = False

Sound.tone(2000, 300).wait()
Sound.tone(200, 100)
lcd.clear()
lcd.draw.text((10, 15), "Program stopped by button")
lcd.update()


motorRight.stop()
motorLeft.stop()
