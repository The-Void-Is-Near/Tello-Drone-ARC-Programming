#imports#
from djitellopy import Tello
from time import sleep
import cv2 as cv

#define Drone
me = Tello()
me.connect()
me.streamon()

#Set up camera
while True:
    me.rotate_counter_clockwise(60)
    image = me.getframe()
    image = cv.resize(image, (120,240))
    cv.imshow("Press Q to exit", image)

    if cv.waitKey(0) & 0xFF == ord('q'):
        break

me.land()
me.emergency()
me.streamoff()
cv.destroyallwindows()
exit()
