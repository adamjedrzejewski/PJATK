import cv2
import sys

def main(video_path):
    video_soure = cv2.VideoCapture(video_path)
    if(not video_soure.isOpened()):
        if(type(video_path) == str):
            print(f'Unable to open recording at {video_path}.')
        else:
            print(f'Unable to open camera with identifier {video_path}')
        sys.exit()

    try:
        while(video_soure.isOpened()):
            ret, frame = video_soure.read()
            cv2.imshow('Our window', frame)
            print(f'Type of image is {type(frame)}')
            if(cv2.waitKey(1) == ord('q')):
                raise KeyboardInterrupt()
    except KeyboardInterrupt :
        print('Finished capturing video.')
        video_soure.release()
        cv2.destroyAllWindows()

    

def main2(video_path):
    frame = cv2.imread('example.png')
    base_frame = frame
    frame = frame[400:700,500:900,1]
    print(frame>200)
    frame[frame>200] = 0
    cv2.imshow('Our window', base_frame)
    print(f'Type of image is {type(frame)}')
    print(frame.shape)

    cv2.waitKey()
    cv2.destroyAllWindows()

def main3(video_path):
    frame = cv2.imread('example.png')
    
    OVERLAY_SIZE = 200

    for x in range(0,frame.shape[1]-OVERLAY_SIZE, OVERLAY_SIZE):
        for y in range(0,frame.shape[0]-OVERLAY_SIZE, OVERLAY_SIZE):
            base = frame[y:y+OVERLAY_SIZE,x:x+OVERLAY_SIZE,:]
            overlay = frame[y:y+OVERLAY_SIZE,x:x+OVERLAY_SIZE,1]
            cv2.imshow('Our window', frame)
            if(cv2.waitKey(100) == ord('q')):
                break
    print(f'Type of image is {type(frame)}')
    print(frame.shape)

    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main2(0)