import cv2  #pip install opencv-python
import os 
import imutils #pip install imutils

class capturandoRostros:
    
        

    def __init__(self,nombre,apellido,edad,video):
        
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.video=video
        
        print(nombre+'----'+edad)
        
        
def construir(nombre, apellido, edad, video):    
    if(nombre!=''):
    
        print('-------------------ENTRA-------------------')
        personName = nombre+''+apellido
        dataPath = 'C:/Users/USUARIO/Desktop/PIA/reconocimiento_facial/data'
        personPath = dataPath + '/' + personName
        #print(personPath)
        if not os.path.exists(personPath):
            print('Carpeta creada: ', personPath)
            os.makedirs(personPath)
        cap = cv2.VideoCapture(video+'')
        #cap = cv2.VideoCapture('Ricardo.mp4')
        #cap = cv2.VideoCapture('Aaron.mp4')
        #cap = cv2.VideoCapture('Deyvid.mp4')
        #cap = cv2.VideoCapture('Priscila.mp4')
        faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        c = 0
        while(True):
            ret, frame = cap.read()
            if ret == False : break
            frame = imutils.resize(frame, width=640)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            auxFrame = frame.copy()
            faces = faceClassif.detectMultiScale(gray, 1.3, 5)
            for(x,y,w,h) in faces:
                cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)
                rostro = auxFrame[y:y+h, x: x+w]
                rostro = cv2.resize(rostro, (150, 150), interpolation=cv2.INTER_CUBIC)
                cv2.imwrite(personPath + '/rostro_{}.jpg'.format(c), rostro)
                c=c+1
            cv2.imshow('frame', frame )
            k= cv2.waitKey(1)
            if k==27 or c >= 300:
                break
        cap.release()
        cv2.destroyAllWindows()