import cv2
from djitellopy import Tello

me = Tello()
me.connect()
me.streamon()

arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_4X4_50)
arucoParams = cv2.aruco.DetectorParameters_create()

while True:
    image = me.get_frame_read().frame
    (corners, ids, rejected) = cv2.aruco.detectMarkers(image, arucoDict, parameters=arucoParams)
    cv2.imshow("ImageTelloARUCO", image)

    if cv2.waitKey(0) & 0xFF == ord('q'):
        break
        
me.streamoff()
cv2.destroyAllWindows()
exit()
