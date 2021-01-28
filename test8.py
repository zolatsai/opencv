import cv2
import numpy as np
from matplotlib import pyplot as plt
      
img = cv2.imread('2021012516112623.jpg',1)
b = cv2.imread('2021012516112623.jpg',1)
b[100:200,100:200,0]=0
b[300:500,600:800,1]=0
b[500:600,300:500,2]=0
print(b)

#roi=img[77:122,640:788]
#img[149:194,460:608]=roi
#img1 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(b)
#plt.xticks([]), plt.yticks([])
plt.show()
#cv2.createTrackbar('R,',"image",0,)
#roi=img[200:400, 200:400]
#img[100:300, 100:300]=roi
#img = cv2.imread("2021012516112623.jpg",0)