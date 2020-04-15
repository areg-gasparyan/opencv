import numpy as np
import cv2

# /dev/video0 camera device path on linux, that can be replaced to just ID like 0, 1 or -1 (auto detect)
# /dev/video0 can be replaced to video file path for example ./test.mp4
cap = cv2.VideoCapture("/dev/video0")

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
