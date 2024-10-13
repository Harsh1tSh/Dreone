from djitellopy import tello
import KeyPressModule as kp
from time import sleep
import cv2
import time
kp.init()
me = tello.Tello()
me.connect()
print(me.get_battery())
me.streamon()

def getKeyBoardInput():
    # lr = left, right
    # ud = up, down
    # fb = forward, backward
    # yv = your velocity
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50
    if kp.getKey("LEFT"): lr = -speed
    elif kp.getKey("RIGHT"): lr = speed

    if kp.getKey("UP"): fb = speed
    elif kp.getKey("DOWN"): fb = -speed

    if kp.getKey("w"): ud = speed
    elif kp.getKey("s"): ud = -speed

    if kp.getKey("a"): yv = speed
    elif kp.getKey("d"): yv = -speed

    if kp.getKey("q"): return me.land()
    sleep(3)
    # print("Land the fricking Drone")

    if kp.getKey("e"): return me.takeoff()
    print("Let's goo")


    # Capturing the images
    if kp.getKey("z"):
        cv2.imwrite(f'Resources/Images/{time.time()}.jpg', img)
        sleep(0.3)


    return [lr, fb, ud, yv]
    

while True:
    # you see i dont have a drone soooooooooo
    # for this to work one must have a tello drone
    # Then extablish the connection with the drone and this project
    vals = getKeyBoardInput()
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    img = me.get_frame_read().frame
    img = cv2.resize(img, (640, 480))
    cv2.imshow("Image", img)
    cv2.waitKey(1)