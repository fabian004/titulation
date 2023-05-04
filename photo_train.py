import os
import cv2
import numpy as np

def photoTrain():
    # 1. Cargar las fotografías de tu rostro desde la carpeta "user"
    folder_path = 'user'
    images = []
    labels = []

    for filename in os.listdir(folder_path):
        img = cv2.imread(os.path.join(folder_path, filename))
        if img is not None:
            images.append(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))
            labels.append(0) # todas las imágenes pertenecen a tu rostro

    # 2. Crear un detector de rostros utilizando un modelo pre-entrenado de detección de rostros
    face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # 3. Crear un reconocedor de rostros utilizando el algoritmo LBPH
    recognizer = cv2.face.LBPHFaceRecognizer_create()

    # 4. Convertir las imágenes y las etiquetas a matrices NumPy
    images_np = np.array(images)
    labels_np = np.array(labels)

    # 5. Entrenar el reconocedor de rostros con las imágenes y las etiquetas
    recognizer.train(images_np, labels_np)

    # 6. Guardar el modelo entrenado en un archivo
    recognizer.write('modelo_entrenado.xml')

    print('guardado')


