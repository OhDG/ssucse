# 텐서플로로 필기체 숫자 인식 학습하기
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
from tensorflow.python.framework import graph_util
from tensorflow.python.platform import gfile
import sys
import numpy as np
import cv2

tf.logging.set_verbosity(tf.logging.ERROR)

mnist = input_data.read_data_sets("./MNIST_data/", one_hot=True)

#
# hyper parameters
#
learning_rate = 0.001
training_epochs = 20
batch_size = 100

#
# Model configuration
#
X = tf.placeholder(tf.float32, [None, 28, 28, 1], name='data')
Y = tf.placeholder(tf.float32, [None, 10])

conv1 = tf.layers.conv2d(X, 32, [3, 3], padding="same", activation=tf.nn.relu)
pool1 = tf.layers.max_pooling2d(conv1, [2, 2], strides=2, padding="same")

conv2 = tf.layers.conv2d(pool1, 64, [3, 3], padding="same", activation=tf.nn.relu)
pool2 = tf.layers.max_pooling2d(conv2, [2, 2], strides=2, padding="same")

flat3 = tf.contrib.layers.flatten(pool2)
dense3 = tf.layers.dense(flat3, 256, activation=tf.nn.relu)

logits = tf.layers.dense(dense3, 10, activation=None)
final_tensor = tf.nn.softmax(logits, name='prob')

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(labels=Y, logits=logits))
optimizer = tf.train.AdamOptimizer(learning_rate).minimize(cost)

#
# Training
#
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    total_batch = int(mnist.train.num_examples / batch_size)

    print('Start learning!')
    for epoch in range(training_epochs):
        total_cost = 0

        for i in range(total_batch):
            batch_xs, batch_ys = mnist.train.next_batch(batch_size)
            batch_xs = batch_xs.reshape(-1, 28, 28, 1)
            _, cost_val = sess.run([optimizer, cost], feed_dict={X: batch_xs, Y: batch_ys})

            total_cost += cost_val

        print('Epoch:', '%04d' % (epoch + 1), 'Avg. cost = ', '{:.4f}'.format(total_cost/total_batch))

    print('Learning finished!')

    # Freeze variables and save pb file
    output_graph_def = graph_util.conver_variables_to_constants(sess, sess.graph_def, ['prob'])
    with gfile.FastGFile('./mnist_cnn.pb', 'wb') as f:
        f.write(output_graph_def.SerializeToString())

    print('Save done!')


# OpenCV에서 학습된 모델 불러와서 실행하기
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

net = cv2.dnn.readNet('mnist_cnn.pb')

if net.empty():
    print('Network load failed!')
    sys.exit()

img = np.zeros((400, 400), np.uint8)

cv2.imshow('img', img)
cv2.setMouseCallback('img', on_mouse)

while True:
    c = cv2.waitKey()

    if c == 27:
        break
    elif c == ord(' '):
        blob = cv2.dnn.blobFromImage(img, 1/255., (28, 28))
        net.setInput(blob)
        prob = net.forward()

        _, maxVal, _, maxLoc = cv2.minMaxLoc(prob)
        digit = maxLoc[0]

        print('%d (%f)' % (digit, maxVal * 100))

        img.fill(0)
        cv2.imshow('img', img)

cv2.destroyAllWindows()


# 구글넷 영상 인식
net = cv2.dnn.readNet('bvlc_googlenet.caffemodel', 'deploy.prototxt')

classNames = None
with open('classification_classes_ILSVRC2012.txt', 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

inputBlob = cv2.dnn.blobFromImage(img, 1, (224, 224), (104, 117, 123))
net.setInput(inputBlob, 'data')
prob = net.forward()

out = prob.flatten()
classId = np.argmax(out)
confidence = out[classId]

str = '%s (%4.2f%%)' % (classNames[classId], confidence * 100)
cv2.putText(img, str, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 1, cv2.LINE_AA)

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()


# SSD 얼굴 검출
model = 'res10_300x300_ssd_iter_140000_fp16.caffemodel'
config = 'deploy.prototxt'
#model = 'opencv_face_detector_uint8.pb'
#config = 'opencv_face_detector_pbtxt'

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('Camera open failed!')
    sys.exit()

net = cv2.dnn.readNet(model, config)

if net.empty():
    print('Net open failed!')
    sys.exit()

while True:
    _, frame = cap.read()
    if frame is None:
        break

    blob = cv2.dnn.blobFromImage(frame, 1, (300, 300), (104, 117, 123))
    net.setInput(blob)
    detect = net.forward()

    (h, w) = frame.shape[:2]
    detect = detect[0, 0, :, :]

    for i in range(detect.shape[0]):
        confidence = detect[i, 2]
        if confidence < 0.5:
            break

        x1 = int(detect[i, 3] * w)
        y1 = int(detect[i, 4] * h)
        x2 = int(detect[i, 5] * w)
        y2 = int(detect[i, 6] * w)

        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0))

        label = 'Face: %4.3f' % confidence
        cv2.putText(frame, label, (x1, y1 - 1), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 1, cv2.LINE_AA)

    cv2.imshow('frame', frame)
    
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()