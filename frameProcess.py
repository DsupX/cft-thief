import cv2
import numpy as np
import mss
import time

font                   = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (10,50)
fontScale              = 1
fontColor              = (255,255,255)
lineType               = 2


# img = cv2.imread('img.png')
# img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
# img = cv2.resize(img, (457, 816))
# img_c = img[513:, :]
# print(img.shape)
# cv2.imshow('frame', img_c)


sct = mss.mss()

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (650,950))
monitor = {"top": 60, "left": 70, "width": 650, "height": 950}

while True:
    last_time = time.time()

    # Get raw pixels from the screen, save it to a Numpy array
    img = np.array(sct.grab(monitor))
    img = img[:, :, 0:3]

    # img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    # (thresh, img) = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    t = 1 / (time.time() - last_time)
    # img2 = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

    out.write(img)
    # print(img2.shape)
    img = cv2.putText(img, str(t), bottomLeftCornerOfText, font, fontScale, fontColor, lineType)
    cv2.imshow('OpenCV/Numpy grayscale', img)


    # Press "q" to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

out.release()
cv2.destroyAllWindows()