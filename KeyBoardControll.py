import KeyPressModule as kp
from time import sleep

kp.init()

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

    if kp.getKey("q"): return print("Land the fricking Drone")

    return [lr, fb, ud, yv]
    

while True:
    # you see i dont have a drone soooooooooo
    vals = getKeyBoardInput()
    print(kp.getKey("s"))