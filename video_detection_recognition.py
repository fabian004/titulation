import cv2
from picamera import PiCamera
from picamera.array import PiRGBArray
import time
import face_recognition

def videoDetection(mode):
    print('Ya o que')
    # Cargar la imagen de referencia y convertirla a RGB
    ref_image = face_recognition.load_image_file("mypicture.jpg")
    ref_image = cv2.cvtColor(ref_image, cv2.COLOR_BGR2RGB)

    # Codificar la imagen de referencia
    ref_encoding = face_recognition.face_encodings(ref_image)[0]

    # Inicializar la cámara y obtener una referencia a la captura de la cámara en bruto
    camera = PiCamera()
    camera.resolution = (640,368)
    camera.framerate = 32
    rawCapture = PiRGBArray(camera, size=(640,368))

    # Permitir que la cámara se caliente
    time.sleep(0.1)

    # Capturar fotogramas de la cámara
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        # Obtener la imagen en bruto como un array NumPy y revertir la imagen
        image = frame.array
        image = cv2.flip(image, 1)

        # Convertir la imagen a RGB para la detección de rostros utilizando face_recognition
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Detectar los rostros en la imagen utilizando la biblioteca face_recognition
        face_locations = face_recognition.face_locations(rgb_image)
        face_encodings = face_recognition.face_encodings(rgb_image, face_locations)

        # Recorrer la lista de rostros detectados y compararlos con la imagen de referencia
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            # Comparar el rostro detectado con la imagen de referencia
            matches = face_recognition.compare_faces([ref_encoding], face_encoding)
            
            # Si hay una coincidencia, guardar la imagen y mostrar un mensaje de confirmación
            if matches[0]:
                #cv2.imwrite("mypicture.jpg", image)
                print("Imagen guardada como 'mypicture.jpg'")
                print('Hola Fabian')
                mode.sleepModeOff('camera')
                rawCapture.truncate(0)
                time.sleep(30)
            else:
                print('No eres Fabian')
            
            # Dibujar un rectángulo alrededor del rostro detectado
            cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
        
        # Mostrar la imagen en pantalla
        new_size = (400, 300)
        resized_img = cv2.resize(image, new_size)
        cv2.imshow("Frame", resized_img)
        key = cv2.waitKey(1) & 0xFF

        # Limpiar el stream en preparación para el siguiente fotograma
        rawCapture.truncate(0)

        # Si se presiona la tecla 'q', salir del bucle
        if key == ord("q"):
            break

    # Limpiar la cámara y cerrar todas las ventanas abiertas
    camera.close()
    cv2.destroyAllWindows()