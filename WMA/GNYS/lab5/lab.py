import cv2 as cv
import numpy as np
from sklearn.cluster import AffinityPropagation

SOURCE_IMAGE_PATH = 'saw1.jpg'
SOURCE_IMAGE_PATH_2 = 'saw2.jpg'
SOURCE_IMAGE_PATH_3 = 'saw3.jpg'
SOURCE_IMAGE_PATH_4 = 'saw4.jpg'
TARGET_IMAGE_PATH = 'saw4.jpg'
TARGET_VIDEO_PATH = 'sawmovie.mp4'
FLANN_INDEX_KDTREE = 1
FLANN_TREES = 5
FLANN_CHECKS = 50
FLANN_K = 2
KEYPOINT_VALIDITY_THRESHOLD = 0.68
AFFIINITY_DAMPING = 0.75

def sift(source_image_path, source_image_path_2, source_image_path_3, source_image_path_4, target_image_path):
    sift = cv.SIFT_create()

    source_image = cv.imread(source_image_path)
    source_image = cv.resize(source_image, dsize=(600, 600))
    gray_source = cv.cvtColor(source_image, cv.COLOR_BGR2GRAY)

    source_image_2 = cv.imread(source_image_path_2)
    source_image_2 = cv.resize(source_image_2, dsize=(600, 600))
    gray_source_2 = cv.cvtColor(source_image_2, cv.COLOR_BGR2GRAY)
    
    source_image_3 = cv.imread(source_image_path_3)
    source_image_3 = cv.resize(source_image_3, dsize=(600, 600))
    gray_source_3 = cv.cvtColor(source_image_3, cv.COLOR_BGR2GRAY)

    source_keypoints, source_descriptors = sift.detectAndCompute(gray_source, None)
    marked_source = cv.drawKeypoints(source_image, source_keypoints, None)
    cv.imshow('Source_1', marked_source)

    source_keypoints_2, source_descriptors_2 = sift.detectAndCompute(gray_source_2, None)
    marked_source_2 = cv.drawKeypoints(source_image_2, source_keypoints_2, None)
    cv.imshow('Source_2', marked_source_2)
    
    source_keypoints_3, source_descriptors_3 = sift.detectAndCompute(gray_source_3, None)
    marked_source_3 = cv.drawKeypoints(source_image_3, source_keypoints_3, None)
    cv.imshow('Source_3', marked_source_3)

    sources_keypoints = np.concatenate((source_keypoints, source_keypoints_2, source_keypoints_3))
    sources_descriptors = np.concatenate((source_descriptors, source_descriptors_2, source_descriptors_3))
    marked_sources = cv.drawKeypoints(source_image_3, sources_keypoints, None)
    print(sources_descriptors)
    cv.imshow('Sources', marked_sources)

    target_image = cv.imread(target_image_path)
    target_image = cv.resize(target_image, dsize=(600, 600))
    gray_target = cv.cvtColor(target_image, cv.COLOR_BGR2GRAY)

    cap = cv.VideoCapture(TARGET_VIDEO_PATH)
 
    # Check if camera opened successfully
    if (cap.isOpened()== False): 
        print("Error opening video stream or file")
    
    # Read until video is completed
    while(cap.isOpened()):
        # Capture frame-by-frame
        ret, frame = cap.read()
        if ret == True:
        
            # target_image_2 = cv.imread(frame)
            target_image_2 = cv.resize(frame, dsize=(600, 600))
            gray_target_2 = cv.cvtColor(target_image_2, cv.COLOR_BGR2GRAY)
            
            target_keypoints_2, target_descriptors_2 = sift.detectAndCompute(gray_target_2, None)
            marked_target_2 = cv.drawKeypoints(target_image_2, target_keypoints_2, None)

            index_params = {'algorithm': FLANN_INDEX_KDTREE, 'trees': FLANN_TREES}
            search_params = {'checks': FLANN_CHECKS}
            flann = cv.FlannBasedMatcher(index_params, search_params)
            matches = flann.knnMatch(sources_descriptors, target_descriptors_2, k = FLANN_K)

            matches_mask = []
            valid_matches = []
            for i, (m, n) in enumerate(matches):
                if m.distance < KEYPOINT_VALIDITY_THRESHOLD * n.distance:
                    # matches_mask[i] = [1, 0]
                    matches_mask.append([m])
                    valid_matches.append(target_keypoints_2[matches[i][0].trainIdx].pt)
            valid_matches = np.asarray(valid_matches, dtype = np.int32)

            detected_visualisation = target_image_2.copy()
            for point in valid_matches:
                cv.circle(detected_visualisation, tuple(point), 5, [0, 0, 255])
            
            af = AffinityPropagation(damping = AFFIINITY_DAMPING).fit(valid_matches)
            cluster_center_indices = af.cluster_centers_indices_
            labels = af.labels_
            cluster_count = len(cluster_center_indices)
            for cluster in range(cluster_count):
                cluster_points = valid_matches[labels == cluster]
                x_min, y_min = np.min(cluster_points, axis = 0)
                x_max, y_max = np.max(cluster_points, axis = 0)
                cv.rectangle(detected_visualisation, (x_min, y_min), (x_max, y_max), (255, 0, 0), 3)

            cv.imshow('Detected', detected_visualisation)


        else: 
            break
    
    cap.release()
    
    target_keypoints, target_descriptors = sift.detectAndCompute(gray_target, None)
    marked_target = cv.drawKeypoints(target_image, target_keypoints, None)

    index_params = {'algorithm': FLANN_INDEX_KDTREE, 'trees': FLANN_TREES}
    search_params = {'checks': FLANN_CHECKS}
    flann = cv.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(source_descriptors, target_descriptors, k = FLANN_K)

    matches_mask = []
    valid_matches = []
    for i, (m, n) in enumerate(matches):
        if m.distance < KEYPOINT_VALIDITY_THRESHOLD * n.distance:
            matches_mask.append([m])
            valid_matches.append(target_keypoints[matches[i][0].trainIdx].pt)
    valid_matches = np.asarray(valid_matches, dtype = np.int32)

    draw_parameters = {'matchColor': (0, 0, 255), 'singlePointColor': (255, 0, 0),
                       'matchesMask': matches_mask, 'flags': cv.DrawMatchesFlags_DEFAULT}
    matches_visualisation = cv.drawMatchesKnn(source_image, source_keypoints,
                                              target_image, target_keypoints,
                                              matches_mask, None,
                                              flags = cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    matches_visualisation = cv.resize(matches_visualisation, dsize=(600, 600))
    # cv.imshow('Matches', matches_visualisation)

    detected_visualisation = target_image.copy()
    for point in valid_matches:
        cv.circle(detected_visualisation, tuple(point), 5, [0, 0, 255])
    
    af = AffinityPropagation(damping = AFFIINITY_DAMPING).fit(valid_matches)
    cluster_center_indices = af.cluster_centers_indices_
    labels = af.labels_
    cluster_count = len(cluster_center_indices)
    for cluster in range(cluster_count):
        cluster_points = valid_matches[labels == cluster]
        x_min, y_min = np.min(cluster_points, axis = 0)
        x_max, y_max = np.max(cluster_points, axis = 0)
        cv.rectangle(detected_visualisation, (x_min, y_min), (x_max, y_max), (255, 0, 0), 3)

    cv.imshow('Detected', detected_visualisation)
    
    # print(source_descriptors[0])
    cv.waitKey(0)

def main():
    sift(SOURCE_IMAGE_PATH, SOURCE_IMAGE_PATH_2, SOURCE_IMAGE_PATH_3, SOURCE_IMAGE_PATH_4, TARGET_IMAGE_PATH)

if __name__ == '__main__':
    main()