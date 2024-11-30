import numpy as np
import cv2
import sys
import matplotlib.pyplot as plt
import random
import math

# 해리스 코너 검출 방법
src = cv2.imread('building.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

harris = cv2.cornerHarris(src, 3, 3, 0.04)
harris_norm = cv2.normalize(harris, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)

for y in range(harris_norm.shape[0]):
    for x in range(harris_norm.shape[1]):
        if harris_norm[y, x] > 120:
            if (harris[y, x] > harris[y-1, x] and
                harris[y, x] > harris[y+1, x] and
                harris[y, x] > harris[y, x-1] and
                harris[y, x] > harris[y, x+1]):
                cv2.circle(dst, (x, y), 5, (0, 0, 255), 2)

cv2.imshow('src', src)
cv2.imshow('harris_norm', harris_norm)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()


# FAST 코너 검출 방법
src = cv2.imread('building.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

fast = cv2.FastFeatureDetector_create(60)
keypoints = fast.detect(src)

dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)

for kp in keypoints:
    pt = (int(kp.pt[0], int(kp.pt[1])))
    cv2.circle(dst, pt, 5, (0, 0, 255), 2)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()


# OpenCV 특징점 검출과 기술
def detect_keypoint():
    src = cv2.imread('box_in_scene.png', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        sys.exit()

    orb = cv2.ORB()

    keypoints = orb.detect(src)
    keypoints, desc = orb.compute(src, keypoints)

    print('len(keypoints):', len(keypoints))
    print('desc.shape:', desc.shape)

    dst = cv2.drawKeypoints(src, keypoints, None, (-1, -1, -1), cv2.DrawMatchesFlags_DRAW_RICH_KEYPOINTS)

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)

    cv2.waitKey()
    cv2.destroyAllWindows()


# OpenCV 특징점 매칭
orb = cv2.ORB()

src1 = cv2.imread('box.png', cv2.IMREAD_GRAYSCALE)
src2 = cv2.imread('box_in_scene.png', cv2.IMREAD_GRAYSCALE)

keypoints1, desc1 = orb.detectAndCompute(src1, None)
keypoints2, desc2 = orb.detectAndCompute(src2, None)

matcher = cv2.BFMatcher(cv2.NORM_HAMMING)
matches = matcher.match(desc1, desc2)


# 영상 이어 붙이기
argc = len(sys.argv)
if argc < 3:
    print('Usage: stitching.exe <image_file1> <image_file2> [<image_file3> ...]')
    sys.exit()

imgs = []
for i in range(1, argc):
    img = cv2.imread(sys.argv[i])

    if img is None:
        print('Image load failed!')
        sys.exit()

    imgs.append(img)

    stitcher = cv2.Stitcher()
    status, dst = stitcher.stitch(imgs)

    if status != cv2.Stitcher_OK:
        print('Error on stitching!')
        sys.exit()

    cv2.imwrite('result.png', dst)

    cv2.imshow('dst', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()