import numpy as np
import cv2
import time
c=0
cap = cap = cv2.VideoCapture("C:/Users/video_short.avi")
while(True): 
 
 for a in range (100,400,1):
  
  ret, frame = cap.read()
  cv2.imshow('Video', frame)

  b=str(a)
  name="C:/Users/image/"+b+".jpg"  
  print (name)
  cv2.imwrite(name,frame)
  time.sleep (0.5)

  print (a)
  if cv2.waitKey(1) & 0xFF == ord('q'):
   break

 break
          
cap.release()
cv2.destroyAllWindows()
