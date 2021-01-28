import cv2
import numpy as np
#Import only if not previously imported
#import cv2
# In VideoCapture object either Pass address of your Video file
# Or If the input is the camera, pass 0 instead of the video file
cap = cv2.VideoCapture(0)
if cap.isOpened() == False:
    print("Error in opening video stream or file")
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        # Display the resulting frame
        cv2.imshow('Frame',frame)
        # Press esc to exit
        if cv2.waitKey(20) & 0xFF == 27:
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()

#下方是影片剪入(須自己放置對應位置)
#Import only if not previously imported
import cv2
# Create a Video Reader Object.
cap = cv2.VideoCapture(VideoToRead)
if cap.isOpened() == False:
    print("Error in opening video stream or file")
#Define the codec for the Video
fourcc = cv2.VideoWriter_fourcc("Fourcc Codec Eg-XVID")
#Create Video Writer Object
writer = cv2.VideoWriter('test.avi', 30, fourcc, fps value, (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        writer.write(frame)
        cv2.imshow("Frame",frame)
        # Exit on pressing esc
        if cv2.waitKey(20) & 0xFF == 27:
            break
    else:
        break
cap.release()
writer.release()
cv2.destroyAllWindows()