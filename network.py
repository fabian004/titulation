import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import tflite_runtime
from tflite_runtime.interpreter import Interpreter
from PIL import Image

def max_emotion(data):
    emotions = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']
    max_index = data.argmax()
    return emotions[max_index]

def myNetwork():
    # Load the image
    img = Image.open('mypicture.jpg')

    # Resize the image to 48x48
    img = img.resize((48, 48))

    # Convert the image to grayscale
    img = img.convert('L')

    # Convert the image to a numpy array
    img = np.array(img)

    # Preprocess the data
    img = img / 255.0
    img = img.reshape(1, 48, 48, 1)

    # Convierte el tensor a FLOAT32
    img = img.astype(np.float32)

    # Carga el modelo .tflite
    interpreter = Interpreter(model_path='modelLite.tflite')

    # Inicializa el intérprete
    interpreter.allocate_tensors()

    # Obtiene los detalles del modelo
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    # Asigna los datos de entrada al intérprete
    interpreter.set_tensor(input_details[0]['index'], img)

    # Ejecuta la inferencia
    interpreter.invoke()

    # Obtiene los resultados
    output_data = interpreter.get_tensor(output_details[0]['index'])

    # Imprime los resultados
    return max_emotion(output_data)
