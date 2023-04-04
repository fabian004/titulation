from validator import userValidator
from user_capture import userCapture
from video_detection import videoDetection
from internal import internalFunction
import threading
from clase import Mode

Nimgs = userValidator("user")

mode = Mode()

if(Nimgs > 0):
    print('grabando')
    hilo = threading.Thread(target=videoDetection,args=[mode])
    hilo.start()
else:
    print('se capturaran fotos')
    userCapture()

mycont=''
while(True):
    internalFunction(mode)


    