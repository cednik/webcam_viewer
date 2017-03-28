#!python3

import cv2

cv2.namedWindow("preview", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("preview", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    vc.set(cv2.CAP_PROP_FRAME_WIDTH, 1024)
    vc.set(cv2.CAP_PROP_FRAME_HEIGHT, 768)
    rval, frame = vc.read()
else:
    rval = False
    vc.release()

while rval:
    cv2.imshow("preview", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        vc.release()
        break
    
cv2.destroyWindow("preview")
