from ast import While
import time
import os
import pigpio
os.system("sudo pigpiod")  # Launching GPIO library
time.sleep(1)
pi = pigpio.pi()
STEER = 18 # сервопривод
time.sleep(1)
pi.set_servo_pulsewidth(STEER, 0)
time.sleep(2)
while (True):
    angle=int(input())
    pi.set_servo_pulsewidth(STEER,angle)

