# take keypoints from images 1 and 2, use the matcher, take the best ones
# take keypoints from image 3, use the matcher on key points from the previous step, take the best ones
# use matcher on frame
import cv2 as cv
import numpy as np

FLANN_INDEX_KDTREE = 1
FLANN_TREES = 5
FLANN_CHECKS = 50
FLANN_K = 2
KEYPOINT_VALIDITY_THRESHOLD = 0.68

def training():
    sift = cv.SIFT_create()
    source_img_1 = cv.imread('saw1.jpg')
    gray_source_1 = cv.cvtColor(source_img_1, cv.COLOR_BGR2GRAY)
    source_keypoints_1, source_descriptors_1 = sift.detectAndCompute(gray_source_1, None)
    marked_source_1 = cv.drawKeypoints(source_img_1, source_keypoints_1, None)

    source_img_2 = cv.imread('saw2.jpg')
    gray_source_2 = cv.cvtColor(source_img_2, cv.COLOR_BGR2GRAY)
    source_keypoints_2, source_descriptors_2 = sift.detectAndCompute(gray_source_2, None)
    marked_source_2 = cv.drawKeypoints(source_img_2, source_keypoints_2, None)

    source_img_3 = cv.imread('saw3.jpg')
    gray_source_3 = cv.cvtColor(source_img_3, cv.COLOR_BGR2GRAY)
    source_keypoints_3, source_descriptors_3 = sift.detectAndCompute(gray_source_3, None)
    marked_source_3 = cv.drawKeypoints(source_img_3, source_keypoints_3, None)

    # match 1 with 2 and create result a
    index_params = {'algorithm': FLANN_INDEX_KDTREE, 'trees': FLANN_TREES}
    search_params = {'checks': FLANN_CHECKS}
    matcher = cv.FlannBasedMatcher(index_params, search_params)
    matches = matcher.knnMatch(source_descriptors_1, source_descriptors_2, k = FLANN_K)

    # matches -> tuple(kpindx, kpindx, desc)

    matches_mask = []
    valid_matches = []
    for i, (m, n) in enumerate(matches):
        if m.distance < KEYPOINT_VALIDITY_THRESHOLD * n.distance:
            matches_mask.append([m])
            valid_matches.append(source_keypoints_2[matches[i][0].trainIdx].pt)
    valid_matches = np.asarray(valid_matches, dtype = np.int32)

    # match 3 with result a and create result b

    pass


def main():
    pass

    #source_img_2 = cv.imread('saw2.jpg')
    #source_img_3 = cv.imread('saw3.jpg')

if __name__ == '__main__':
    training()