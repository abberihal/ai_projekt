import cv2, pytesseract
import numpy as np
pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# noise removal
def remove_noise(image):
    return cv2.medianBlur(image,5)
 
#thresholding
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

#dilation
def dilate(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.dilate(image, kernel, iterations = 1)
    
#erosion
def erode(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.erode(image, kernel, iterations = 1)

#opening - erosion followed by dilation
def opening(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

#canny edge detection
def canny(image):
    return cv2.Canny(image, 100, 200)

#skew correction

#template matching
def match_template(image, template):
    return cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)

import math
def rotate(img, x1,y1,x2,y2):
    y1 = y1*-1
    y2 = y2*-1
    k = (y2-y1)/(x2-x1)
    m = y1-k*x1
    print("y =", k, "x", m)
    a = m- y1
    c = math.sqrt((0-x1)**2 + (m-y1)**2)
    print((0-x1)**2, (m-y1)**2)
    # print(c)
    v = math.degrees(math.sin(a/c))
    # print(v)
    u = 180-v
    # print(u)
    u = (90-v)/2-14

    (h, w) = img.shape[:2]
    center = (w / 2, h / 2)

    M = cv2.getRotationMatrix2D(center, u, 1)
    return cv2.warpAffine(img, M, (w, h))

img = cv2.imread("nog.jpg")
img = rotate(img, 227,506,353,608)
img = get_grayscale(img)
cv2.imshow("test", img)
cv2.waitKey(0)

print(pytesseract.image_to_string(img))


 
# angle90 = 17.197

 
# scale = 1.0
 
# # Perform the counter clockwise rotation holding at the center
# # 90 degrees

# gray = get_grayscale(rotated90)
# cv2.imshow("HEJ",gray)
# cv2.waitKey(0)
# print(pytesseract.image_to_string(rotated90))

# # gray = get_grayscale(image)
# # cv2.imshow('image',gray)
# # cv2.waitKey(0)

# thresh = thresholding(gray)
# print(pytesseract.image_to_string(thresh))

# new = deskew(thresh)

# cv2.imshow("hej", new)
# cv2.waitKey(0)
