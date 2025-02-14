from djitellopy import tello
import cv2


me = tello.Tello()
me.connect()
me.streamon()


while True:
    img = me.get_frame_read().frame
    img = cv2.resize(img, (450, 300))
    cv2.imshow("Image", img)
    k = cv2.waitKey(33)
    if k==27:
        me.streamoff()
        cv2.destroyAllWindows()
        break
exit()
