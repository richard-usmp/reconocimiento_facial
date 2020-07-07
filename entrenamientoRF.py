import cv2  #pip install opencv-python
import os 
import numpy as np #pip install numpy

dataPath = 'C:/Users/Aaron/Desktop/IA/reconocimiento_facial/data'
peopleList = os.listdir(dataPath)
print('Lista de personas: ', peopleList)

labels = []
facesData = []
label = 0

for nameDir in peopleList:
    personPath = dataPath + '/' + nameDir
    print('Leyendo las imagenes')

    for fileName in os.listdir(personPath):
        print('Rostros: ', nameDir + '/' + fileName)
        labels.append(label)
        facesData.append(cv2.imread(personPath + '/' + fileName, 0))
        image = cv2.imread(personPath + '/' + fileName, 0)
        #cv2.imshow('image', image)
        #cv2.waitKey(10)
    label = label + 1

#print('labels', labels)
#face_recognizer = cv2.face.EigenFaceRecognizer_create()
#face_recognizer = cv2.face.FisherFaceRecognizer_create()
face_recognizer = cv2.face.LBPHFaceRecognizer_create() #pip install opencv-contrib-python --user


#entrenando al reconocedor de rostros
print("Entrenando...")
face_recognizer.train(facesData, np.array(labels))

#almancenar el modelo obtenido
face_recognizer.write('modeloEigenFace.xml')
print("Modelo almacenado...")