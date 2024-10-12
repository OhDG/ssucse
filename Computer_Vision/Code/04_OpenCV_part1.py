import cv2 as cv
import numpy as np

# VideoCapture 클래스
cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Camera open failed!")
    exit()

print('Frame width:', int(cap.get(cv.CAP_PROP_FRAME_WIDTH)))
print('Frame height:', int(cap.get(cv.CAP_PROP_FRAME_HEIGHT)))

while True:
    ret, frame = cap.read()

    if not ret:
        break

    inversed = ~frame # (255 - frame)과 같음

    cv.imshow('frame', frame)
    cv.imshow('inversed', inversed)

    if cv.waitKey(10) == 27:
        break

cv.destroyAllWindows()

# 동영상 파일 처리하기
cap = cv.VideoCapture('stopwatch.avi')
if not cap.isOpened():
    print("Video open failed!")
    exit()

print('Frame width:', int(cap.get(cv.CAP_PROP_FRAME_WIDTH)))
print('Frame height:', int(cap.get(cv.CAP_PROP_FRAME_HEIGHT)))
print('Frame count:', int(cap.get(cv.CAP_PROP_FRAME_COUNT)))

fps = cap.get(cv.CAP_PROP_FPS)
print('FPS:', fps)
delay = round(1000 / fps) # 1000ms = 1sec

while True:
    ret, frame = cap.read()

    if not ret:
        break

    inversed = ~frame

    cv.imshow('frame', frame)
    cv.imshow('inversed', inversed)

    if cv.waitKey(delay) == 27:
        break

cv.destroyAllWindows()


# 동영상 파일 저장하기
cap = cv.VideoCapture('stopwatch.avi')

if not cap.isOpened():
    print("Video open failed!")
    exit()

w = round(cap.get(cv.CAP_PROP_FRAME_WIDTH))
h = round(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv.CAP_PROP_FPS)

fourcc = cv.VideoWriter_fourcc(*'DIVX')
delay = round(1000 / fps)

outputVideo = cv.VideoWriter('output.avi', fourcc, fps, (w, h))
if not outputVideo.isOpened():
    print('File open failed!')
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    inversed = ~frame
    outputVideo.write(inversed)

    cv.imshow('frame', frame)
    cv.imshow('inversed', inversed)

    if cv.waitKey(delay) == 27:
        break

cv.destroyAllWindows()


# 다양한 그리기 함수 활용
img = np.full((400, 400, 3), 255, np.uint8)

cv.line(img, (50, 50), (200, 50), (0, 0, 255))
cv.line(img, (50, 100), (200, 100), (255, 0, 255), 3)
cv.line(img, (50, 150), (200, 150), (255, 0, 0), 10)

cv.line(img, (250, 50), (350, 100), (0, 0, 255), 1, cv.LINE_4)
cv.line(img, (250, 70), (350, 120), (255, 0, 255), 1, cv.LINE_8)
cv.line(img, (250, 90), (350, 140), (255, 0, 0), 1, cv.LINE_AA)

cv.arrowedLine(img, (50, 200), (150, 200), (0, 0, 255), 1)
cv.arrowedLine(img, (50, 250), (350, 250), (255, 0, 255), 1)
cv.arrowedLine(img, (50, 300), (350, 300), (255, 0, 0), 1, cv.LINE_8, 0, 0.05)

cv.drawMarker(img, (50, 350), (0, 0, 255), cv.MARKER_CROSS)
cv.drawMarker(img, (100, 350), (0, 0, 255), cv.MARKER_TILTED_CROSS)
cv.drawMarker(img, (150, 350), (0, 0, 255), cv.MARKER_STAR)
cv.drawMarker(img, (200, 350), (0, 0, 255), cv.MARKER_DIAMOND)
cv.drawMarker(img, (250, 350), (0, 0, 255), cv.MARKER_SQUARE)
cv.drawMarker(img, (300, 350), (0, 0, 255), cv.MARKER_TRIANGLE_UP)
cv.drawMarker(img, (350, 350), (0, 0, 255), cv.MARKER_TRIANGLE_DOWN)

cv.imshow("img", img)
cv.waitKey()
cv.destroyAllWindows()


# 도형 그리기
img = np.full((400, 400, 3), 255, np.uint8)

cv.rectangle(img, (50, 50), (150, 100), (0, 0, 255), 2)
cv.rectangle(img, (50, 150), (150, 200), (0, 0, 128), -1)

cv.circle(img, (300, 120), 30, (255, 255, 0), -1, cv.LINE_AA)
cv.circle(img, (300, 120), 60, (255, 0, 0), 3, cv.LINE_AA)

cv.ellipse(img, (120, 300), (60, 30), 20, 0, 270, (255, 255, 0), cv.FILLED, cv.LINE_AA)
cv.ellipse(img, (120, 300), (100, 50), 20, 0, 360, (0, 255, 0), 2, cv.LINE_AA)

pts = np.array([[250, 250], [300, 250], [300, 300], [350, 300], [350, 350], [250, 350]])
cv.polylines(img, [pts], True, (255, 0, 255), 2)

cv.imshow("img", img)
cv.waitKey()
cv.destroyAllWindows()


# 문자열 출력하기
img = np.full((500, 500, 3), 255, np.uint8)

cv.putText(img, "FONT_HERSHEY_SIMPLEX", (20, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255))
cv.putText(img, "FONT_HERSHEY_PLAIN", (20, 100), cv.FONT_HERSHEY_PLAIN, 1, (0, 0, 255))
cv.putText(img, "FONT_HERSHEY_DUPLEX", (20, 150), cv.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255))
cv.putText(img, "FONT_HERSHEY_COMPLEX", (20, 200), cv.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0))
cv.putText(img, "FONT_HERSHEY_TRIPLEX", (20, 250), cv.FONT_HERSHEY_TRIPLEX, 1, (255, 0, 0))
cv.putText(img, "FONT_HERSHEY_COMPLEX_SMALL", (20, 300), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 0))
cv.putText(img, "FONT_HERSHEY_SCRIPT_SIMPLEX", (20, 350), cv.FONT_HERSHEY_SCRIPT_SIMPLEX, 1, (255, 0, 255))
cv.putText(img, "FONT_HERSHEY_SCRIPT_COMPLEX", (20, 400), cv.FONT_HERSHEY_SCRIPT_COMPLEX, 1, (255, 0, 255))
cv.putText(img, "FONT_HERSHEY_COMPLEX | FONT_ITALIC", (20, 450), cv.FONT_HERSHEY_COMPLEX | cv.FONT_ITALIC, 1, (255, 0, 0))

cv.imshow("img", img)
cv.waitKey()
cv.destroyAllWindows()


img = np.full((200, 640, 3), 255, np.uint8)

text = "Hello, OpenCV"
fontFace = cv.FONT_HERSHEY_TRIPLEX
fontScale = 2.0
thickness = 1

sizeText, _ = cv.getTextSize(text, fontFace, fontScale, thickness)

org = ((img.shape[1] - sizeText[0]) // 2, (img.shape[0] + sizeText[1]) // 2)
cv.putText(img, text, org, fontFace, fontScale, (255, 0, 0), thickness)
cv.rectangle(img, org, (org[0] + sizeText[0], org[1] - sizeText[1]), (0, 255, 0), 1)

cv.imshow("img", img)
cv.waitKey()
cv.destroyAllWindows()
