import cv2
import numpy as np

img = cv2.imread('imgc2.png', 0)
img1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
# contours, hierarchy = cv2.findContours(img1, 1, 2)

# cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU,img)

contours, hier = cv2.findContours(img1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

for c in contours:
    # get the bounding rect
    x, y, w, h = cv2.boundingRect(c)
    # draw a white rectangle to visualize the bounding rect
    if w > 5 and h > 5:
        im = img[y:y+h, x:x+w]
        cv2.imshow('tmp', im)
        cv2.waitKey(0)
        cv2.rectangle(img1, (x, y), (x + w, y + h), 255, 1)

cv2.drawContours(img1, contours, -1, (255, 255, 0), 1)

# cv2.imwrite("output.png",img)

cv2.imshow("contours", img1)

# img2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
# cv2.imshow('f1', img1)
# cv2.imshow('f2', img2)
w = img.shape[1]
h = img.shape[0]



print(w, ' ', h)

# print(img1)

# d = 0
# for i in range(0, h, 10):
#     for j in range(0, w, 10):
#         d+=1
#         img2 = img[i:i+10, j:j+10]
#         print(i, j)
#         if img2.shape != ():
#             # print(img2)
#             cv2.imshow('g', img2)
#             cv2.waitKey(0)
#
# print(d)
cv2.waitKey(0)