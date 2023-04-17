import cv2
import sys
import numpy as np
from scipy import signal as sig
from scipy import ndimage as ndi

K = 0.05
THRESHOLD_CORNER = 0.1
THRESHOLD_EDGE = 0.0001
KERNEL_X = np.array([
[-1, 0, 1],
[-2, 0, 2],
[-1, 0, 1]
])
KERNEL_Y = np.array([
    [1, 2, 1],
    [0, 0, 0],
    [-1, -2, -1]
])

def main():
    video = cv2.VideoCapture("lana_del_rey_360.mp4")
    while video.isOpened():
        ret, frame = video.read()

        if ret != True:
            sys.exit(1)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        d_x = sig.convolve2d(gray, KERNEL_X, mode='same')
        d_y = sig.convolve2d(gray, KERNEL_Y, mode='same')
        Ixx = ndi.gaussian_filter(d_x ** 2, sigma = 1)
        Ixy = ndi.gaussian_filter(d_y * d_x, sigma = 1)
        Iyy = ndi.gaussian_filter(d_y ** 2, sigma = 1)
        det = Ixx * Iyy - Ixy ** 2
        trace = Ixx + Iyy
        response = det - K * trace ** 2

        response_min = response.min()
        response_max = response.max()
        for y, row in enumerate(response):
            for x, pixel in enumerate(row):
                if pixel > response_max * THRESHOLD_CORNER:
                    frame[y, x] = [0, 0, 255]
                elif pixel <= response_min * THRESHOLD_EDGE:
                    frame[y, x] = [255, 255, 255]
    
        cv2.imshow('frame', frame)
        if cv2.waitKey(25) == ord('q'):
            break

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()