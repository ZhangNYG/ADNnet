# -*- coding: utf-8 -*-
import numpy as np
import cv2 as cv
from pylab import *
# from PIL import Image
def fill2_image():
    image = np.zeros([200, 200, 3], np.uint8)
    #image[100:300, 100:300, :] = 255
    cv.imshow("原图", image)
    mask = np.zeros([202, 202, 1], np.uint8)
    mask[100:150, 100:200] = 1
    cv.floodFill(image, mask, (0, 0), (0, 0, 255), cv.FLOODFILL_MASK_ONLY)
    cv.imshow("填充2", image)
    imshow(image)

while True:
    fill2_image()
    key = cv.waitKey(1) & 0xff
    if key == ord('s'):
        break
print()
