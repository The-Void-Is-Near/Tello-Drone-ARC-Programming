import cv2 as cv
import numpy as np
import djitellopy
#from djitellopy import Tello

me=Tello()
me.connect(#wait for connection)
me.streamon()
#me.set

while True:
    image=me.getframe().frame()
    image=cv.resize(image, (200,350))
    cv.imshow("",image)
    
    if cv.waitKey(0) & 