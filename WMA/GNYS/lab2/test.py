import cv2
import numpy as np
import random as rng

def main():
    image = cv2.imread('./example.png')
    part = image[500:800,400:1000,0]
    mask = part > 200
    part[mask] = 0

    cv2.imshow('Our window', image)
    cv2.waitKey(0)

def main2():
    CUTOFF = 60
    video = cv2.VideoCapture('example.mp4')
    while video.isOpened():
        ret, frame = video.read()
        bw = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        racist_frame = np.zeros_like(bw)
        racist_frame[bw < CUTOFF] = 255

        kernel = np.ones((5,5), np.uint8)
        racist_frame = cv2.erode(racist_frame, kernel, iterations=2)
        racist_frame = cv2.erode(racist_frame, kernel, iterations=5)
        
        canny_output = cv2.Canny(racist_frame, 100, 200)
        contours, _ = cv2.findContours(canny_output, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # frame[bw<CUTOFF,:] = 255


        contours_poly = [None]*len(contours)
        boundRect = [None]*len(contours)
        for i, c in enumerate(contours):
            contours_poly[i] = cv2.approxPolyDP(c, 3, True)
            boundRect[i] = cv2.boundingRect(contours_poly[i])


        drawing = np.zeros((canny_output.shape[0], canny_output.shape[1], 3), dtype=np.uint8)
        for i in range(len(contours)):
            color = (rng.randint(0,256), rng.randint(0,256), rng.randint(0,256))
            cv2.drawContours(frame, contours_poly, i, color)
            cv2.rectangle(frame, (int(boundRect[i][0]), int(boundRect[i][1])), \
            (int(boundRect[i][0]+boundRect[i][2]), int(boundRect[i][1]+boundRect[i][3])), color, 2)


        cv2.imshow('video', frame)
        cv2.imshow('mask', racist_frame)
        if cv2.waitKey(10) == ord('q'):
            break

if __name__ == '__main__':
    main2()
