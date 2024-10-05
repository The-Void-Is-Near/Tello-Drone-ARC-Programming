from djitellopy import Tello
from time import sleep
import cv2 as cv

#Connecting the drone and preparing camera settings.
me = Tello()
me.connect(wait_for_state=True)
me.streamon()
me.set_video_fps(me.FPS_30)
me.set_video_bitrate(Tello.BITRATE_AUTO)
me.set_video_resolution(Tello.RESOLUTION_720P)

#Use SDK to get drone data in real time.
def uptadeValues(img):
    flightTime = f'{me.get_flight_time()} Seconds flying.'
    altitude = f'{me.get_height()} Cm high'
    charge = f'{me.get_battery()} % Charge'
    temp = f'{round(me.get_temperature(),2)}C / {round((9/5)*me.get_temperature()+32,2)}F'
    
    #Edit the image (that will be displayed) with overlaid text of the data (ft,alt,battCharge,temp)
    cv.putText(img,flightTime,(15,15*2),fontFace=cv.FONT_HERSHEY_DUPLEX,fontScale=.7,color=(125, 246, 55),thickness=1)
    cv.putText(img,altitude,(15,15*4),fontFace=cv.FONT_HERSHEY_DUPLEX,fontScale=.7,color=(125, 246, 55),thickness=1)
    cv.putText(img,charge,(15,15*6),fontFace=cv.FONT_HERSHEY_DUPLEX,fontScale=.7,color=(125, 246, 55),thickness=1)
    cv.putText(img,temp,(15,15*8),fontFace=cv.FONT_HERSHEY_DUPLEX,fontScale=.7,color=(125, 246, 55),thickness=1)

while True:
    img = me.get_frame_read().frame
    img = cv.resize(img, (900,600))
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    
    uptadeValues(img)
    cv.imshow("Press Esc to exit!", img)

    if cv.waitKey(1) & 0xFF == ord('q'):#esc
        break

me.land()
me.streamoff()
cv.destroyAllWindows()
exit()



