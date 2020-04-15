# Camera captures

import numpy as np
import cv2

# /dev/video0 camera device path on linux, that can be replaced to just ID like 0, 1 or -1 (auto detect)
# /dev/video0 can be replaced to video file path for example ./test.mp4
cap = cv2.VideoCapture("/dev/video0")

# Setup camera reading widtth
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)

# Setup camera reading height
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Detect edges
    e_frame = cv2.Canny(frame, 100, 200)

    # Display the resulting frame
    cv2.imshow('frame', e_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
