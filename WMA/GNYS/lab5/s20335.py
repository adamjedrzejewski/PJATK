import cv2
import numpy as np

IMAGE_1 = 'saw1.jpg'
IMAGE_2 = 'saw2.jpg'
IMAGE_3 = 'saw3.jpg'
VIDEO = 'sawmovie.mp4'
FLANN_INDEX_KDTREE = 1
FLANN_TREES = 5
FLANN_CHECKS = 50
FLANN_K = 2
KEYPOINT_VALIDITY_THRESHOLD = 0.68
AFFIINITY_DAMPING = 0.94

def train():
    sift = cv2.SIFT_create()

    source_image = cv2.imread(IMAGE_1)
    source_image = cv2.resize(source_image, dsize=(600, 600))
    gray_source = cv2.cvtColor(source_image, cv2.COLOR_BGR2GRAY)
    _, source_descriptors = sift.detectAndCompute(gray_source, None)
    
    source_image_2 = cv2.imread(IMAGE_2)
    source_image_2 = cv2.resize(source_image_2, dsize=(600, 600))
    gray_source_2 = cv2.cvtColor(source_image_2, cv2.COLOR_BGR2GRAY)
    _, source_descriptors_2 = sift.detectAndCompute(gray_source_2, None)

    source_image_3 = cv2.imread(IMAGE_3)
    source_image_3 = cv2.resize(source_image_3, dsize=(600, 600))
    gray_source_3 = cv2.cvtColor(source_image_3, cv2.COLOR_BGR2GRAY)
    source_keypoints_3, source_descriptors_3 = sift.detectAndCompute(gray_source_3, None)

    index_params = {'algorithm': FLANN_INDEX_KDTREE, 'trees': FLANN_TREES}
    search_params = {'checks': FLANN_CHECKS}
    flann = cv2.FlannBasedMatcher(index_params, search_params)

    matches = flann.knnMatch(source_descriptors, source_descriptors_2, k=FLANN_K)
    matched_descriptors = []
    for _, (m,n) in enumerate(matches):
        if m.distance < KEYPOINT_VALIDITY_THRESHOLD*n.distance:
            matched_descriptors.append(source_descriptors[m.queryIdx])
    matched_descriptors = np.array(matched_descriptors)

    matches = flann.knnMatch(matched_descriptors, source_descriptors_3, k=FLANN_K)
    final_descriptors = []
    valid_matches = []
    for _, (m,n) in enumerate(matches):
        if m.distance < KEYPOINT_VALIDITY_THRESHOLD*n.distance:
            final_descriptors.append(matched_descriptors[m.queryIdx])
            valid_matches.append(source_keypoints_3[m.trainIdx].pt)

    final_descriptors = np.array(final_descriptors)

    return final_descriptors


def find_bounding_box_coordinaes(valid_matches):
    if len(valid_matches) < 1:
        return None

    min_x = min(x for (x, _) in valid_matches)
    max_x = max(x for (x, _) in valid_matches)
    min_y = min(y for (_, y) in valid_matches)
    max_y = max(y for (_, y) in valid_matches)

    upper_left = (min_x, min_y)
    lower_right = (max_x, max_y)

    return (upper_left, lower_right)


def detect(queryDescriptors):
    sift = cv2.SIFT_create()
    video = cv2.VideoCapture(VIDEO)

    index_params = {'algorithm': FLANN_INDEX_KDTREE, 'trees': FLANN_TREES}
    search_params = {'checks': FLANN_CHECKS}
    flann = cv2.FlannBasedMatcher(index_params, search_params)

    while video.isOpened():
        ret, frame = video.read()
        if ret != True:
            break

        frame = cv2.resize(frame, dsize=(600, 600))
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        source_keypoints, source_descriptors = sift.detectAndCompute(gray_frame, None)
        matches = flann.knnMatch(queryDescriptors, source_descriptors, k=FLANN_K)

        valid_matches = []
        for i, (m,n) in enumerate(matches):
            if m.distance < KEYPOINT_VALIDITY_THRESHOLD*n.distance:
                valid_matches.append(source_keypoints[matches[i][0].trainIdx].pt)
        valid_matches = np.asarray(valid_matches, dtype=np.int32)

        box_coordinates = find_bounding_box_coordinaes(valid_matches)
        image = frame
        if box_coordinates:
            start, end = box_coordinates
            image = cv2.rectangle(image, start, end, (255, 0, 0), 2)

        cv2.imshow("video", image)
        if cv2.waitKey() == ord('q'):
            break

def main():
    descriptors = train()
    detect(descriptors)

if __name__ == "__main__":
    main()