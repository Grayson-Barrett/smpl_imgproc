import cv2 as cv
import numpy as np


def sobelHi2lo(src, dx, dy, kernel):                            # Function to output sobel higher form then convert to
                                                                # lower form
    src = cv.cvtColor(src,cv.COLOR_BGR2GRAY)
    sobel64f = cv.Sobel(src, cv.CV_64F, dx, dy, ksize=kernel)   # Output dtype = cv.CV_64F
    abs_sobel64f = np.absolute(sobel64f)                        # Take absolute of cv.CV_64f
    sobel_8u = np.uint8(abs_sobel64f)                           #

    return sobel_8u
