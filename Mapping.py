# This file will have the code formmapping along the cartesiuan plane
# The dron e wiill move forward, backward, up, down but we also have 
# assumne the change in angle during the rotation of drone on its axis
# Currently we will go with the backwar and forward as the up and down will
# require us to implement in 3-D

from djitellopy import tello
import KeyPressModule as kp
from time import sleep
import numpy as np 
import cv2
import math

####### Parameters ########
fspeed = 117/10 # Forward speed in cm/s  (15cm/s)
aspeed = 360/10 # angular speed Degrees/s
interval = 0.25

dInterval = fspeed * interval
aInterval = aspeed * interval

###########################

x,y = 500, 500
a = 0
yaw = 0
kp.init()
# me = tello.Tello()
# me.connect()
# print(me.get_battery())

def getKeyBoardInput():
    # lr = left, right
    # ud = up, down
    # fb = forward, backward
    # yv = your velocity
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50
    d = 0
    global yaw, x, y, a

    if kp.getKey("LEFT"): 
        lr = -speed
        d = dInterval
        a = -180

    elif kp.getKey("RIGHT"): 
        lr = speed
        d = -dInterval
        a = 180

    if kp.getKey("UP"): 
        fb = speed
        d = dInterval
        a = 270

    elif kp.getKey("DOWN"): 
        fb = -speed
        d = -dInterval
        a = -90

    if kp.getKey("w"): 
        ud = speed
    elif kp.getKey("s"): 
        ud = -speed

    if kp.getKey("a"): 
        yv = -speed
        yaw += aInterval
    elif kp.getKey("d"): 
        yv = speed
        yaw -= aInterval

    if kp.getKey("q"): 
        # return me.land()
        print("Land the fricking Drone")

    if kp.getKey("e"):
         #return me.takeoff()
        print("Let's goo")

    a += yaw
    x += int(d * math.cos(math.radians(a)))
    y += int(d * math.sin(math.radians(a)))

    return [lr, fb, ud, yv, x, y]
    
def drawpoint(img, points):
    cv2.circle(img,(points[0],points[1]), 5, (0,0,255), cv2.FILLED) # BGR


while True:
    
    vals = getKeyBoardInput()
    # me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    # print(vals)
    
    img = np.zeros((1000,1000,3), np.uint8) # values between 0 t0 255
    points = (vals[4],vals[5])
    drawpoint(img, points)
    cv2.imshow("Output", img)
    cv2.waitKey(1)