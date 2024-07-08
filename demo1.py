'''
Note: This code controls the Tello or Tello EDU drone, however it doesn't run within the drone's hardware.
Rather, it uses an API defined in an SDK document, this runs on a computer for example.
'''

#Dependencies
from djitellopy import Tello
import cv2 as cv

#Defining the drone for later use.
me = Tello()

#Connecting to the drone. Only works if it is on the same WIFI.
me.connect()

#Turing the drone's camera on.
me.streamon()

#Launch the drone (upwards into the air).
me.takeoff()

while True:
    me.rotate_counter_clockwise(60) #Changes the YAW of the drone.
    image = me.getframe() #Gets footage from the drone's front-facing camera.
    image = cv.resize(image, (120,240)) #Adjusts the resolution of the footage.
    cv.imshow("Press Q to exit", image) #Displays a window with that image.

    if cv.waitKey(0) & 0xFF == ord('q'): #For quitting the loop.
        break

'''
The following handles:
landing the drone,
securely ending camera footage stream,
removing the display window,
and exiting the python application with exit()
'''
me.land()
me.streamoff()
cv.destroyallwindows()
exit()

