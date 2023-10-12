import cv2 as cv
import numpy as np
import djitellopy
#from djitellopy import Tello

me=Tello()
me.connect(#wait for connection)
me.streamon()
#me.set

while True:
#have a try case but make 
#sure it's Keanuent on the 
#beginning delays
    image=me.getframe().frame()
    image=cv.resize(image, (200,350))
    cv.imshow("",image)
    
    
    if cv.waitKey(0) & 0xFF == ord('q'):
        break
    elif cv.waitKey(0) & 0xFF == ord('w'):
        moveFunction(distance=5,command=

try:me.land()
except: pass

cv.destroyAllWindows()
me.streamoff()
exit()