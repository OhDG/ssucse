import numpy as np
import cv2

# 키보드 이벤트 처리
img = cv2.imread('lenna.bmp')
if img is None:
    print('Image load failed!')
    exit()

cv2.namedWindow('img')
cv2.imshow('img', img)

while True:
    keycode = cv2.waitKey()
    if keycode == ord('i') or keycode == ord('I'):
        img = ~img
        cv2.imshow('img', img)
    elif keycode == 27 or keycode == ord('q') or keycode == ord('Q'):
        break

cv2.destroyAllWindows()


# 마우스 이벤트 처리
def on_mouse(event, x, y, flags, param):
    global oldx, oldy

    if event == cv2.EVENT_LBUTTONDOWN:
        oldx, oldy = x, y
        print('EVENT_LBUTTONDOWN: %d, %d' % (x, y))
    
    elif event == cv2.EVENT_LBUTTONUP:
        print('EVENT_LBUTTONUP: %d, %d' %(x, y))

    elif event == cv2.EVENT_MOUSEMOVE:
        if flags & cv2.EVENT_FLAG_LBUTTON:
            cv2.line(img, (oldx, oldy), (x, y), (0, 255, 255), 2)
            cv2.imshow('img', img)
            oldx, oldy = x, y

img = cv2.imread('lenna.bmp')

if img is None:
    print('Image load failed!')
    exit()

cv2.namedWindow('img')
cv2.setMouseCallback('img', on_mouse)

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()


# 트랙바 사용하기
def saturated(value):
    if value > 255:
        value = 255
    elif value < 0:
        value = 0

    return value

def on_level_change(pos):
    img[:] = saturated(pos * 16)
    cv2.imshow('image', img)

img = np.zeros((400, 400), np.uint8)

cv2.namedWindow('image')
cv2.createTrackbar('level', 'image', 0, 16, on_level_change)

cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()


# 데이터 파일 저장하기
filename = 'mydata.json'

def writeData():
    name = 'Jane'
    age = 10
    pt1 =(100, 200)
    scores = (80, 90, 50)
    mat1 = np.array([[1.0, 1.5], [2.0, 3.2]], dtype=np.float32)

    fs = cv2.FileStorage(filename, cv2.FILE_STORAGE_WRITE)

    if not fs.isOpened():
        print('File open failed!')
        return
    
    fs.write('name', name)
    fs.write('age', age)
    fs.write('point', pt1)
    fs.write('scores', scores)
    fs.write('data', mat1)

    fs.release()


# 데이터 파일 불러오기
def readData():
    fs = cv2.FileStorage(filename, cv2.FileStorage_READ)

    if not fs.isOpened():
        print('File open failed!')
        return
    
    name = fs.getNode('name').string()
    age = int(fs.getNode('age').real())
    pt1= tuple(fs.getNode('point').mat().astype(np.int32).flatten())
    scores = tuple(fs.getNode('scores').mat().flatten())
    mat1 = fs.getNode('data').mat()

    fs.release()

    print('name:', name)
    print('age:', age)
    print('point:', pt1)
    print('scores:', scores)
    print('data:')
    print(mat1)


# 마스크 영상
def mask_setTo():
    src = cv2.imread('lenna.bmp', cv2.IMREAD_COLOR)
    mask = cv2.imread('mask_smile.bmp', cv2.IMREAD_GRAYSCALE)

    if src is None or mask is None:
        print('Image load failed!')
        return
    
    src[mask > 0] = (0, 255, 255)

    cv2.imshow('src', src)
    cv2.imshow('mask', mask)
    cv2.waitKey()
    cv2.destroyAllWindows()


# 마스크 영상 2
def mask_copyTo():
    src = cv2.imread('airplane.bmp', cv2.IMREAD_COLOR)
    mask = cv2.imread('mask_plane.bmp', cv2.IMREAD_GRAYSCALE)
    dst = cv2.imread('field.bmp', cv2.IMREAD_COLOR)

    if src is None or mask is None or dst is None:
        print('Image load failed!')
        return
    
    dst[mask > 0] = src[mask > 0]
    
    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    cv2.imshow('mask', mask)
    cv2.waitKey()
    cv2.destroyAllWindows()


# 연산 시간 측정
def time_inverse():
    src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return
    
    dst = np.empty(src.shape, dtype=src.dtype)

    tm = cv2.TickMeter()
    tm.start()

    for y in range(src.shape[0]):
        for x in range(src.shape[1]):
            dst[y, x] = 255 - src[y, x]

    tm.stop()
    print('Image inverse implementation took %4.3f ms.' % tm.getTimeMilli())

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()


# 유용한 OpenCV 함수 사용법
def useful_func():
    img = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

    if img is None:
        print('Image load failed!')
        return
    
    sum_img = np.sum(img)
    mean_img = np.mean(img, dtype=np.int32)
    print('Sum:', sum_img)
    print('Mean:', mean_img)


src = np.array([[-1, -0.5, 0, 0.5, 1]], dtype=np.float32)
dst = cv2.normalize(src, None, 0, 255, cv2.NORM_MINMAX ,cv2.CV_8U)
print('src:', src)
print('dst:', dst)

print('round(2.5) is', round(2.5))
print('round(2.51) is', round(2.51))
print('round(3.499) is', round(3.499))
print('round(3.5) is', round(3.5))