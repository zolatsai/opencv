import cv2
import numpy as np
img = cv2.imread("2021012516112623.jpg",cv2.IMREAD_GRAYSCALE)
print(img)
cv2.imshow("test" ,img)
cv2.imwrite("test.jpg",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
