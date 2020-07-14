import cv2 as cv
from matplotlib import pyplot as plt

file_name = "report_rus.png"
img = cv.imread(file_name, 0)
img = cv.medianBlur(img, 5)
ret, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, \
                           cv.THRESH_BINARY, 11, 2)
th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, \
                           cv.THRESH_BINARY, 11, 2)
titles = ['Original Image', 'Global Thresholding (v = 127)',
          'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]
for i in range(len(images)):
    plt.subplot(2, 2, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
# plt.show()
plt.savefig('filename.png', dpi=300)

import numpy as np

img = cv.imread(file_name, 0)
kernel = np.ones((5, 5), np.uint8)
erosion = cv.erode(img, kernel, iterations=1)
cv.imwrite("erosion.png", erosion)
dilation = cv.dilate(img, kernel, iterations=1)
cv.imwrite("dilation.png", dilation)
