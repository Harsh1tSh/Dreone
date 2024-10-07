from djitellopy import tello
import cv2



#For tello drone
me = tello.Tello()
me.connect()
print(me.get_battery())

me.streamon()

while True:
    img = me.get_frame_read().frame
    img = cv2.resize(img, (640, 480))
    cv2.imshow("Image", img)
    cv2.waitKey(1)




