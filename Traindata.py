import cv2
import numpy as np
import os
from PIL import Image

recognizer = cv2.face.LBPHFaceRecognizer_create()
path = "dataSet"

def getImage(path):
    dataPaths = os.listdir(path)
    faces= []
    Ids = []
    for dataPath in dataPaths:
        faceImg = Image.open(f"{path}//{dataPath}").convert('L')
        faceNP  = np.array(faceImg,'uint8')
        cut = dataPath.split("_")
        Id = int(cut[1])
        faces.append(faceNP)
        Ids.append(Id)
        cv2.imshow('training',faceNP)
        cv2.waitKey(10)
    return faces,Ids  

faces,Ids = getImage(path)
recognizer.train(faces,np.array(Ids))
recognizer.save('train/trainningData.yml')
cv2.destroyAllWindows