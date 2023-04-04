import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import os

def userCapture():
    # Configuración de la cámara
    camera = PiCamera()
    camera.resolution = (640, 480)
    camera.framerate = 30
    rawCapture = PiRGBArray(camera, size=(640, 480))

    # Espera a que la cámara se inicie
    time.sleep(0.1)

    # Crea la carpeta si no existe
    if not os.path.exists('user'):
        os.makedirs('user')

    # Toma 200 fotos
    for i in range(50):
        # Captura una imagen
        camera.capture(rawCapture, format="bgr")
        image = rawCapture.array

        # Detecta la cara
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        # Recorta la imagen para mostrar solo la cara y la redimensiona a 40 x 40
        for (x, y, w, h) in faces:
            roi_color = image[y:y + h, x:x + w]
            resized_roi_color = cv2.resize(roi_color, (40, 40))

            # Guarda la imagen en la carpeta
            cv2.imwrite("user/foto{}.jpg".format(i+1), resized_roi_color)

        # Limpia el buffer para la siguiente imagen
        rawCapture.truncate(0)

        # Espera un segundo antes de tomar la siguiente foto
        time.sleep(1)

    # Libera la cámara
    camera.close()
