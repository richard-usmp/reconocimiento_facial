import os 
import numpy as np #pip install numpy

dataPath = 'D:/Ricardo/Documentos/reconocimiento_facial/data'
peopleList = os.listdir(dataPath)
print('Lista de personas: ', peopleList)

def getNombres():
    return peopleList

def getImage():
    image = []
    for nameDir in peopleList:
        personPath = dataPath + '/' + nameDir
        for fileName in os.listdir(personPath):
            image_url = personPath + '/' +fileName
        image.append(image_url)
    return image




    