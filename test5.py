import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('test.jpg',1)

img1 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

#img = cv2.imread("2021012516112623.jpg",0)
print(img)
plt.imshow(img1)
plt.xticks([]), plt.yticks([])
plt.show()