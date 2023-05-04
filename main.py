import os
os.environ['PYTHONMALLOC'] = 'malloc:arena:small:4G'
from validator import userValidator
from user_capture import userCapture
from photo_train import photoTrain
from video_detection_recognition import videoDetection
from internal import internalFunction
import threading
from clase import Mode
from time import sleep

Nimgs = userValidator("user")

mode = Mode()

def start():
    if(Nimgs > 150):
        print('grabando')
        hilo = threading.Thread(target=videoDetection,args=[mode])
        hilo.start()
    else:
        print('Se capturaran fotos en 5')
        sleep(5)
        print('Ya')
        userCapture()
        print('fotos capturadas')
        sleep(5)
        newImgs = userValidator("user")
        if(newImgs < 150):
            print('no hay: '+str(newImgs))
            start()
        else:
            print('si hay: '+str(newImgs))
            photoTrain()
            hilo = threading.Thread(target=videoDetection,args=[mode])
            hilo.start()
            
start()

while(True):
    internalFunction(mode)


    
