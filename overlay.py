import cv2 as cv
import numpy as np


def mask_overlay(a, b):
    a = a.astype(float) / 255
    b = b.astype(float) / 255

    mask = a >= 0.5
    ab = np.zeros_like(a)

    ab[~mask] = (2 * a * b)[~mask]
    ab[mask] = (1 - 2 * (1 - a) * (1 - b))[mask]

    x = (ab * 255).astype(np.uint8)
    return x
