import numpy
from PIL import Image
import os
import cv2
import sys

def train_classifier():
    dataf = input("Path to dataset: ")
    if os.path.exists(dataf) != True:
        print("Enter the exist directory!")
    outf = input("Output file name .xml: ")
        sys.exit(1)
    path = [os.path.join(data_dir, f) for f in os.listdir(data_dir)]
    face = [] #เก็บใบหน้า
    ids = [] #รหัสรูปภาพ

    for image in path:
        img = Image.open(image).convert("L") #convert to grayscale from pil
        imagenp = numpy.array(img,'uint8') #save img in imagenp by array
        id = int(os.path.split(image)[1].split('.')[1]) #create id for check that img alrdy train
        face.append(imagenp) #append to face list
        ids.append(id) #id > ids
    ids = numpy.array(ids)
    
    clf = cv2.face.LBPHFaceRecognizer_create() #remember face
    clf.train(face,ids)
    clf.write(f"./{outf}.xml")

if '__main__' == __name__:
    train_classifier() #'data' is folder where dataset is
    print("Done")