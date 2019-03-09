import cv2
import numpy as np

# cap = cv2.VideoCapture(0)

cap = cv2.VideoCapture('output.mp4')

if cap.isOpened() == False:
    print("Can not open")
Show = True
while cap.isOpened():

        ret, frame = cap.read()
        # frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
        # frame = cv2.resize(frameq, (457, 816))
        # frame = frame[513:, :]
        if ret == True:
            if Show == True:
                cv2.imshow('frame', frame)

                if cv2.waitKey(15) & 0xFF == ord('q'):
                    break
        else:
            break

cap.release()
cv2.destroyAllWindows()