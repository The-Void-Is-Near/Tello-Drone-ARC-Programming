from djitellopy import Tello
from time import sleep
import cv2 as cv

me = Tello()
me.connect(wait_for_state=True)
me.takeoff()
me.streamon()

def uptadeValues(img):
    flightTime = f'{me.get_flight_time()} Seconds flying.'
    altitude = f'{me.get_height()} Cm high'
    charge = f'{me.get_battery()} % charge'
    temp = f'{round(me.get_temperature(),2)}C / {round((9/5)*me.get_temperature()+32,2)}F'

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

try:
    me.land()
except: me.emergency()

me.streamoff()
cv.destroyAllWindows()
exit()
