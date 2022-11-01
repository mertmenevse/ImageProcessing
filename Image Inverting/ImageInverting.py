import cv2
import numpy as np

image = cv2.imread('istanbulImage.jpg', 0)
cv2.imshow("Image Inverting", image)
cv2.waitKey()

imageShape = image.shape
height = imageShape[0]
width = imageShape[1]

invertedImage = np.zeros([height, width], dtype=np.uint8)

for i in range(0, height):
    for j in range(0, width):
        invertedImage[i, j] = 255 - image[i, j]

cv2.imshow("Inverted Image", invertedImage)
cv2.waitKey()