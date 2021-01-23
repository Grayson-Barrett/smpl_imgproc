from __future__ import print_function

import sys
import time
import argparse

import cv2 as cv
import numpy as np
from overlay import mask_overlay

parser = argparse.ArgumentParser(description='Code for creating a high pass filter from an image.'
                                             'Then blend original input with high pass filter')
parser.add_argument('-i', '--input',nargs='*', help='Path to input image.')
args = parser.parse_args()

img, kern = args.input


def highpass(img, kernel):
    blur = cv.GaussianBlur(img, (kernel,kernel), 0)
    filtered = img - blur
    filtered = filtered + 127 * np.ones(img.shape, np.uint8)
    return filtered


def main(argv):
    img_codec = cv.IMREAD_COLOR
    if argv:
        filename = sys.argv[1]
        print(filename)
        if len(argv) >= 2 and sys.argv[2] == "G":
            img_codec = cv.IMREAD_GRAYSCALE
            print(img_codec)
    src = cv.imread(args.input[0],img_codec)

    if src is None:
        print("Error image {} Can't be opened".format(img))
        return -1

    cv.namedWindow('input', cv.WINDOW_AUTOSIZE)
    cv.namedWindow('high pass filter', cv.WINDOW_AUTOSIZE)
    cv.namedWindow('blended image', cv.WINDOW_AUTOSIZE)

    cv.imshow('input', src)
    cv.waitKey(0)

    kernel = int(args.input[1])
    img2 = highpass(src, kernel)

    blended_img = mask_overlay(src,img2)

    cv.imshow('blended image', blended_img)
    cv.imshow('high pass filter', img2)
    cv.waitKey(0)
    cv.destroyAllWindows()
    return 0


if __name__ == "__main__":
    main(sys.argv[:])

