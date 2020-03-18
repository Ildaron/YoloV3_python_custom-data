print ("start")
import cv2
import numpy as np
import dlib
cap = cv2.VideoCapture("video.mp4")
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
detector = dlib.get_frontal_face_detector()


#fourcc = cv2.VideoWriter_fourcc(*'mp4v')
#out = cv2.VideoWriter('output1.avi',fourcc, 15.0, (416,416))


fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (416,416))


while True:
 ret, frame = cap.read()
 frame=cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
 frame = cv2.resize(frame, (440, 480))
 image = frame
 gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 faces = detector(gray,0)
 for face in faces:
  x = face.left()
  y = face.top()
  w = face.right()
  h = face.bottom()

 cv2.rectangle(image, (x-10, y-50), (w+10, h-30), (0, 155, 0), 2)
 dlib_rect = dlib.rectangle(int(x), int(y), int(w), int(h))
 detected_landmarks = predictor(image, dlib_rect).parts()
 landmarks = np.matrix([[p.x, p.y] for p in detected_landmarks])
 
 #print ("landmarks",  enumerate(landmarks))
 for idx,point in enumerate(landmarks):

  pos=(point[0,0],point[0,1])
 
#cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)
#roi = frame[y:y+h, x:x+w]
 
 # if idx >35 and idx <48:        
 #  cv2.circle(image,pos,2,color=(0,0,255),thickness=-3)

  if idx==36:
   #print (point)
   eye_x=point[0,0]
   eye_y=point[0,1]
   cv2.rectangle(image, (eye_x-10, eye_y-25), (eye_x+60, eye_y+25), (0, 55, 0), 1)
   image = image[eye_y-25:eye_y+25, eye_x-10:eye_x+60:]

 image = cv2.resize(image, (416,416))
 out.write(image)
 
 cv2.imshow('Image',image)
 k = cv2.waitKey(30) & 0xff

cap.release()
cv2.destroyAllWindows()
