import cv2
import numpy as np
from matplotlib import pyplot as plt
      
img = cv2.imread('2021012516112623.jpg',1)

roi=img[77:122,640:788]
img[149:194,460:608]=roi
#roi=img[200:400, 200:400]
#img[100:300, 100:300]=roi

img1 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#img = cv2.imread("2021012516112623.jpg",0)
plt.imshow(img1)
plt.xticks([]), plt.yticks([])
plt.show()
#cv2.createTrackbar('R,',"image",0,)