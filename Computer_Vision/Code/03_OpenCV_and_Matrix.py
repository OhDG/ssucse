import numpy as np
import cv2 as cv

#OpenCV로 이미지 불러오기
img = cv.imread('lenna.bmp')

if img is None:
    print('Image load failed!')
    exit()

cv.imshow('image', img)
cv.waitKey()


# 이미지 타입 확인하기
def func1():
	img1 = cv.imread('cat.bmp', cv.IMREAD_GRAYSCALE)
	
	if img1 is None:
		print('Image load failed!')
		return
		
	print('type(img1):', type(img1))
	print('img1.shape:', img1.shape)
	
	if len(img1.shape) == 2:
		print('img1 is a grayscale image')
	elif len(img1.shape) == 3:
		print('img1 is a truecolor image')
		
	cv.imshow('img1', img1)
	cv.waitKey()
	cv.destroyAllWindows()
	
func1()


# 행렬의 초기화
def func2():
	img1 = np.empty((480, 640), np.uint8) # grayscale image
	img2 = np.zeros((480, 640, 3), np.uint8) # color image
	img3 = np.ones((480, 640), np.int32) # 1's matrix
	img4 = np.full((480, 640), 0, np.float32) # Fill with 0.0
	
	mat1 = np.array([[11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 34]]).astype(np.uint8)
	mat1[0, 1] = 100 # element at x=1, y=0
	mat1[2, :] = 200
	print(mat1)

func2()


# 행렬의 복사
def func3():
	img1 = cv.imread('cat.bmp')
	
	img2 = img1
	img3 = img1.copy()
	
	img1[:, :] = (0, 255, 255)
	
	cv.imshow('img1', img1)
	cv.imshow('img2', img2)
	cv.imshow('img3', img3)
	cv.waitKey()
	cv.destroyAllWindows()
	
func3()

# 부분 행렬 추출
def func4():
	img1 = cv.imread('lenna.bmp', cv.IMREAD_GRAYSCALE)
	
	img2 = img1[200:400, 200:400]
	img3 = img1[200:400, 200:400].copy()
	
	img2 += 20

	cv.imshow('img1', img1)
	cv.imshow('img2', img2)
	cv.imshow('img3', img3)
	cv.waitKey()
	cv.destroyAllWindows()
	
func4()


# 행렬 연산하기
def func6():
	mat1 = np.ones((3, 4), np.int32) # 1's matrix
	mat2 = np.arrange(12).reshape(3, 4)
	mat3 = mat1 + mat2
	mat4 = mat2 * 2
	
	print("mat1:")
	print(mat1)
	print("mat2:")
	print(mat2)
	print("mat3:")
	print(mat3)
	print("mat4:")
	print(mat4)

func6()