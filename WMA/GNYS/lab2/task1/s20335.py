import cv2
import numpy as np
import random as rng
import math

LOWER_BLUE = np.array([60, 35, 80])
UPPER_BLUE = np.array([180, 255, 255])

LOWER_GREEN = np.array([36, 49, 50])
UPPER_GREEN = np.array([80, 205, 255])

LOWER_RED = np.array([0, 35, 0])
UPPER_RED = np.array([37, 255, 255])

def draw_contours(frame, mask, color):
    canny_output = cv2.Canny(mask, 100, 200)
    contours, _ = cv2.findContours(canny_output, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours_poly = [None]*len(contours)
    boundRect = [None]*len(contours)
    for i, c in enumerate(contours):
        contours_poly[i] = cv2.approxPolyDP(c, 3, True)
        boundRect[i] = cv2.boundingRect(contours_poly[i])

    for i in range(len(contours)):
        if abs(boundRect[i][0]-boundRect[i][1])<200 and abs(boundRect[i][2]-boundRect[i][3])<200:
            cv2.rectangle(frame, (int(boundRect[i][0]), int(boundRect[i][1])), \
            (int(boundRect[i][0]+boundRect[i][2]), int(boundRect[i][1]+boundRect[i][3])), color, 2)

def main():
    rng.seed(2137)
    video = cv2.VideoCapture('rgb_ball_720.mp4')
    while video.isOpened():
        ret, frame = video.read()
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        red_mask = cv2.inRange(hsv_frame, LOWER_RED, UPPER_RED)
        blue_mask = cv2.inRange(hsv_frame, LOWER_BLUE, UPPER_BLUE)
        green_mask = cv2.inRange(hsv_frame, LOWER_GREEN, UPPER_GREEN)

        kernel = np.ones((5, 5), np.uint8)
        red_mask = cv2.erode(red_mask, kernel, iterations=2)
        red_mask = cv2.dilate(red_mask, kernel, iterations=1)
        blue_mask = cv2.erode(blue_mask, kernel, iterations=2)
        blue_mask = cv2.dilate(blue_mask, kernel, iterations=1)
        green_mask = cv2.erode(green_mask, kernel, iterations=2)
        green_mask = cv2.dilate(green_mask, kernel, iterations=5)

        draw_contours(frame, red_mask, (0, 0, 255))
        draw_contours(frame, blue_mask, (255, 0, 0))
        draw_contours(frame, green_mask, (0, 255, 0))

        cv2.imshow('frame', frame)

        if cv2.waitKey(10) == ord('q'):
            break

if __name__ == '__main__':
    main()