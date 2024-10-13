import numpy as np
import cv2

# 영상의 밝기 조절
def brightness1():
    src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return
    
    dst = cv2.add(src, 100)

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()


# 영상의 밝기 조절 직접 구현하기
def brightness2():
    src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return
    
    dst = np.empty(src.shape, src.dtype)
    for y in range(src.shape[0]):
        for x in range(src.shape[1]):
            dst[y, x] = src[y, x] + 100

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()


def saturated(value):
    if value > 255:
        value = 255
    elif value < 0:
        value = 0

    return value

def brightness3():
    src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return
    
    dst = np.empty(src.shape, src.dtype)
    for y in range(src.shape[0]):
        for x in range(src.shape[1]):
            dst[y, x] = saturated(src[y, x] + 100)

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()


# 트랙바를 이용한 영상의 밝기 조절
def brightness4():
    src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return
    
    def update(pos):
        dst = cv2.add(src, pos)
        cv2.imshow('dst', dst)

    cv2.namedWindow('dst')
    cv2.createTrackbar('Brightness', 'dst', 0, 100, update)
    update(0)

    cv2.waitKey()
    cv2.destroyAllWindows()


# 기본적인 명암비 조절 방법
def contrast1():
    src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return
    
    s = 2.0
    dst = cv2.multiply(src, s)

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()


# 효과적인 명암비 조절 방법
def contrast2():
    src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return
    
    alpha = 1.0
    dst = cv2.convertScaleAbs(src, alpha=1+alpha, beta=-128*alpha)

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()


# 히스토그램 구하기
def calcGrayHist(img):
    channels = [0]
    hintSize = [256]
    hintRange = [0, 256]

    hist = cv2.calcHist([img], channels, None, hintSize, hintRange)

    return hist


def getGrayHistImage(hist):
    _, histMax, _, _ = cv2.minMaxLoc(hist)

    imgHist = np.ones((100, 256), np.uint8) * 255
    for x in range(imgHist.shape[1]):
        pt1 = (x, 100)
        pt2 = (x, 100 - int(hist[x, 0] * 100 / histMax))
        cv2.line(imgHist, pt1, pt2, 0)

    return imgHist


# 히스토그램 스트레칭
def histogram_stretching():
    src = cv2.imread('hawkes.bmp', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return

    gmin, gmax, _, _ = cv2.minMaxLoc(src)

    dst = cv2.convertScaleAbs(src, alpha=255.0/(gmax - gmin), beta=-gmin * 255.0/(gmax - gmin))

    cv2.imshow('src', src)
    cv2.imshow('srcHist', getGrayHistImage(calcGrayHist(src)))

    cv2.imshow('dst', dst)
    cv2.imshow('dstHist', getGrayHistImage(calcGrayHist(dst)))

    cv2.waitKey()
    cv2.destroyAllWindows()


# 히스토그램 평활화
def histogram_equalization():
    src = cv2.imread('hawkes.bmp', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return
    
    dst = cv2.equalizeHist(src)

    cv2.imshow('src', src)
    cv2.imshow('srcHist', getGrayHistImage(calcGrayHist(src)))

    cv2.imshow('dst', dst)
    cv2.imshow('dstHist', getGrayHistImage(calcGrayHist(dst)))

    cv2.waitKey()
    cv2.destroyAllWindows()