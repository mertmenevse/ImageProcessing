import cv2
import numpy as np
from matplotlib import pyplot as plt

firstImage = cv2.imread("lion.jpg", 0)
cv2.imshow("Image Processing", firstImage)
cv2.waitKey()

shape = firstImage.shape  # Image Array Size 3
height = shape[0]
width = shape[1]

histogramArray = np.zeros(256)

for i in range(0, height):
    for j in range(0, width):
        histogramArray[firstImage[i][j]] += 1

plt.figure("Histogram")
plt.xlabel("0-255 Color Values of Pixels")
plt.ylabel("Intensitive of the Points")
plt.plot(histogramArray)
plt.show()