import sys
import argparse
from yolo import YOLO, detect_video
from PIL import Image

def detect_img(yolo):
    while True:
        img = input('Input image filename:')
        try:
            image = Image.open(img)
        except:
            print('Open Error! Try again!')
            continue
        else:
            r_image = yolo.detect_image(image)
            r_image.show()
    yolo.close_session()


  
input1="output.avi"
output="C:/Users/IldaRon/0.1My_YOLO_works_new_train/"

FLAGS = {
        "model": 'trained_weights_final.h5',
        "anchors": 'yolo_anchors.txt',
        "classes_path": 'voc_classes.txt',
        "gpu_num": 1
    }
print (FLAGS)

try:
 detect_video(YOLO(**FLAGS), input1, output)
except AttributeError:
 print ("video had finished")
