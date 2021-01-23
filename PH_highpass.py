import cv2 as cv
import numpy as np

def highpass(img,kernel):
    blur = cv.GaussianBlur(img, (kernel), 0)
    filtered = img - blur
    filtered = filtered + 127 * np.ones(img.shape, np.uint8)
    return filtered
