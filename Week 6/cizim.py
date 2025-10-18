import cv2
import numpy as np

image = np.zeros((500,500,3),dtype="uint8")

cv2.line(image,(50,50),(450,50),(255,0,0),3)
cv2.rectangle(image,(100,100),(400,300),(0,0,255),2)
cv2.circle(image,(250,250),50,(123,158,90),2)
cv2.putText(image,"OpenCV ile Goruntu Isleme",(50,450),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,255),2)


cv2.imshow("mask",image)

cv2.waitKey(0)
cv2.destroyAllWindows()