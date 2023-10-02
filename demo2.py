from djitellopy import Tello
from time import sleep
import cv2

me = Tello()
me.connect(wait_for_state=True)
me.streamon()
#me.set_video_fps(me.FPS_30)

def uptadeValues():
    flightTime = f'{me.get_flight_time()} Seconds flying.'
    altitude = f'{me.get_height()} Cm high'
    charge = f'{me.get_battery()} % charge'
    temp = f'{round(me.get_temperature(),2)}C / {round((9/5)*me.get_temperature()+32,2)}F'
    #,fontFace=cv2.FONT_HERSHEY_DUPLEX,fontScale=.7,color=(125, 246, 55),thickness=1

    cv2.putText(img,flightTime,(15,15*2),fontFace=cv2.FONT_HERSHEY_DUPLEX,fontScale=.7,color=(125, 246, 55),thickness=1)
    cv2.putText(img,altitude,(15,15*4),fontFace=cv2.FONT_HERSHEY_DUPLEX,fontScale=.7,color=(125, 246, 55),thickness=1)
    cv2.putText(img,charge,(15,15*6),fontFace=cv2.FONT_HERSHEY_DUPLEX,fontScale=.7,color=(125, 246, 55),thickness=1)
    cv2.putText(img,temp,(15,15*8),fontFace=cv2.FONT_HERSHEY_DUPLEX,fontScale=.7,color=(125, 246, 55),thickness=1)


while True:
    img = me.get_frame_read(with_queue=False, max_queue_len=32).frame
    img = cv2.resize(img, (900,600))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    uptadeValues()
    cv2.imshow("Press Esc to exit!", img)

    k = cv2.waitKey(33)#33
    if k==27:#esc
        break

try:
    me.land()
except:pass

me.streamoff()
cv2.destroyAllWindows()
exit()
