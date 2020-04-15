# Rotate captures

import numpy as np
import cv2

# /dev/video0 camera device path on linux, that can be replaced to just ID like 0, 1 or -1 (auto detect)
# /dev/video0 can be replaced to video file path for example ./test.mp4
cap = cv2.VideoCapture("/dev/video0")

width = 640; height = 480

# Setup camera reading widtth
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)

# Setup camera reading height
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)


while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()

    rmatrix = cv2.getRotationMatrix2D( (width / 2, height / 2), 90, .5)
    frame = cv2.warpAffine(frame, rmatrix, (width, height))

    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
