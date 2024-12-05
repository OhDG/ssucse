import numpy as np
import cv2
import sys

# KNearest 클래스 사용하기
train = []
label = []
k_value = 1

def on_k_changed(pos):
    global k_value

    k_value = pos
    if k_value < 1:
        k_value = 1

    trainAndDisplay()

def addPoint(x, y, c):
    train.append([x, y])
    label.append([c])

def trainAndDisplay():
    train_array = np.array(train).astype(np.float32)
    label_array = np.array(label)
    knn.train(train_array, cv2.ml.ROW_SAMPLE, label_array)

    for j in range(img.shape[0]):
        for i in range(img.shape[1]):
            sample = np.array([[i, j]]).astype(np.float32)

            ret, res, _, _ = knn.findNearest(sample, k_value)

            response = int(res[0, 0])
            if response == 0:
                img[j, i] = (128, 128, 255)
            elif response == 1:
                img[j, i] = (128, 255, 128)
            elif response == 2:
                img[j, i] = (255, 128, 128)

    for i in range(len(train)):
        x, y = train[i]
        l = label[i][0]

        if l == 0:
            cv2.circle(img, (x, y), 5, (0, 0, 128), -1, cv2.LINE_AA)
        elif l == 1:
            cv2.circle(img, (x, y), 5, (0, 128, 0), -1, cv2.LINE_AA)
        elif l == 2:
            cv2.circle(img, (x, y), 5, (128, 0, 0), -1, cv2.LINE_AA)
    
    cv2.imshow('knn', img)

img = np.zeros((500, 500, 3), np.uint8)
knn = cv2.ml.KNearest()

cv2.namedWindow('knn')
cv2.createTrackbar('k_value', 'knn', k_value, 5, on_k_changed)

NUM = 30
rn = np.zeros((NUM, 2), np.int32)

cv2.randn(rn, 0, 50)
for i in range(NUM):
    addPoint(rn[i, 0] + 150, rn[i, 1] + 150, 0)

cv2.randn(rn, 0, 50)
for i in range(NUM):
    addPoint(rn[i, 0] + 350, rn[i, 1] + 150, 1)

cv2.randn(rn, 0, 70)
for i in range(NUM):
    addPoint(rn[i, 0] + 250, rn[i, 1] + 400, 2)

trainAndDisplay()

cv2.imshow('knn', img)
cv2.waitKey()
cv2.destroyAllWindows()


# kNN을 이용한 필기체 숫자 인식
oldx, oldy = -1, -1

def on_mouse(event, x, y, flags, _):
    global oldx, oldy

    if event == cv2.EVENT_LBUTTONDOWN:
        oldx, oldy = x, y

    elif event == cv2.EVENT_LBUTTONUP:
        oldx, oldy = -1, -1

    elif event == cv2.EVENT_MOUSEMOVE:
        if flags & cv2.EVENT_FLAG_LBUTTON:
            cv2.line(img, (oldx, oldy), (x, y), (255, 255, 255), 40, cv2.LINE_AA)
            oldx, oldy = x, y
            cv2.imshow('img', img)

digits = cv2.imread('digits.png', cv2.IMREAD_GRAYSCALE)

if digits is None:
    print('Image load failed!')
    sys.exit()

h, w = digits.shape[:2]

cells = [np.hsplit(row, w//20) for row in np.vsplit(digits, h//20)]
cells = np.array(cells)
train_images = cells.reshape(-1, 400).astype(np.float32)
train_labels = np.repeat(np.arange(10), len(train_images)/10)

knn = cv2.ml.KNearest()
knn.train(train_images, cv2.ml.ROW_SAMPLE, train_labels)

img = np.zeros((400, 400), np.uint8)

cv2.imshow('img', img)
cv2.setMouseCallback('img', on_mouse)

while True:
    c = cv2.waitKey()

    if c == 27:
        break
    elif c == ord(' '):
        img_resize = cv2.resize(img, (20, 20), interpolation=cv2.INTER_AREA)
        img_flatten = img_resize.reshape(-1, 400).astype(np.float32)

        _ret, res, _, _ = knn.findNearest(img_flatten, 3)
        print(int(res[0, 0]))

        img.fill(0)
        cv2.imshow('img', img)

cv2.destroyAllWindows()


# SVM 클래스 사용하기
train = np.array([[150, 200], [200, 250],
                  [100, 250], [150, 300],
                  [350, 100], [400, 200],
                  [400, 300], [350, 400]]).astype(np.float32)

label = np.array([0, 0, 0, 0, 1, 1, 1, 1])

svm = cv2.ml.SVM()
svm.setType(cv2.ml.SVM_C_SVC)
svm.setKernel(cv2.ml.SVM_RBF)
# svm.setKernel(cv2.ml.SVM_LINEAR)
svm.trainAuto(train, cv2.ml.ROW_SAMPLE, label)

img = np.zeros((500, 500, 3), np.uint8)

for j in range(img.shape[0]):
    for i in range(img.shape[1]):
        test = np.array([[i, j]], dtype=np.float32)
        _, res = svm.predict(test)

        if res == 0:
            img[j, i] = (128, 128, 255)
        elif res == 1:
            img[j, i] = (128, 255, 128)

color = [(0, 0, 128), (0, 128, 0)]

for i in range(train.shape[0]):
    x = train[i, 0]
    y = train[i, 1]
    l = label[i]

    cv2.circle(img, (x, y), 5, color[l], -1, cv2.LINE_AA)

cv2.imshow('svm', img)
cv2.waitKey()
cv2.destroyAllWindows()


# HOG & SVM 필기체 숫자 인식
oldx, oldy = -1, -1

def on_mouse(event, x, y, flags, _):
    global oldx, oldy

    if event == cv2.EVENT_LBUTTONDOWN:
        oldx, oldy = x, y

    elif event == cv2.EVENT_LBUTTONUP:
        oldx, oldy = -1, -1

    elif event == cv2.EVENT_MOUSEMOVE:
        if flags & cv2.EVENT_FLAG_LBUTTON:
            cv2.line(img, (oldx, oldy), (x, y), (255, 255, 255), 40, cv2.LINE_AA)
            oldx, oldy = x, y
            cv2.imshow('img', img)

digits = cv2.imread('digits.png', cv2.IMREAD_GRAYSCALE)

if digits is None:
    print('Image load failed!')
    sys.exit()

h, w = digits.shape[:2]
hog = cv2.HOGDescriptor((20, 20), (10, 10), (5, 5), (5, 5), 9)

cells = [np.hsplit(row, w//20) for row in np.vsplit(digits, h//20)]
cells = np.array(cells)
cells = cells.reshape(-1, 20, 20)

desc = []
for img in cells:
    dd = hog.compute(img)
    desc.append(dd)

train_desc = np.array(desc).squeeze().astype(np.float32)
train_labels = np.repaet(np.arange(10), len(train_desc)/10)

svm = cv2.ml.SVM()
svm.setType(cv2.ml.SVM_C_SVC)
svm.setKernel(cv2.ml.SVM_RBF)
svm.setC(2.5)
svm.setGamma(0.50625)
svm.train(train_desc, cv2.ml.ROW_SAMPLE, train_labels)

img = np.zeros((400, 400), np.uint8)

cv2.imshow('img', img)
cv2.setMouseCallback('img', on_mouse)

while True:
    c = cv2.waitKey()

    if c == 27:
        break
    elif c == ord(' '):
        img_resize = cv2.resize(img, (20, 20), interpolation=cv2.INTER_AREA)

        desc = hog.compute(img_resize)
        test_desc = np.array(desc).astype(np.float32)

        _, res = svm.predict(test_desc.T)
        print(int(res[0, 0]))

        img.fill(0)
        cv2.imshow('img', img)

cv2.destroyAllWindows()