import cv2
from picamera import PiCamera
from picamera.array import PiRGBArray
import time
import face_recognition

def videoDetection(mode):
    #  Crear un detector de rostros utilizando un modelo pre-entrenado de detección de rostros
    face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    #  Crear un reconocedor de rostros utilizando el algoritmo LBPH
    recognizer = cv2.face.LBPHFaceRecognizer_create()

    #  Leer el modelo entrenado en un archivo
    recognizer.read('modelo_entrenado.xml')

    # initialize the camera and grab a reference to the raw camera capture
    camera = PiCamera()
    camera.resolution = (1920,1088)
    camera.framerate = 32
    camera.brightness = 50 # Adjust the brightness
    camera.contrast = 0 # Adjust the contrast
    camera.saturation = 0 # Adjust the saturation
    camera.exposure_mode = 'auto' # Set the exposure mode to automatic
    camera.awb_mode = 'auto' # Set the white balance mode to automatic

    rawCapture = PiRGBArray(camera, size=(1920,1088))

    # allow the camera to warmup
    time.sleep(0.1)

    # capture frames from the camera
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        # grab the raw NumPy array representing the image, then initialize the timestamp
        # and occupied/unoccupied text
        image = frame.array
        image = cv2.flip(image, 1)
        
        # Convertir la imagen a escala de grises
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Detectar rostros en la imagen en escala de grises
        faces = face_detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
        
        # Recorrer la lista de rostros detectados y reconocer a las personas en los rostros detectados
        for (x, y, w, h) in faces:
            # Extraer la región de interés (ROI) de la imagen en escala de grises correspondiente al rostro detectado
            roi_gray = gray[y:y+h, x:x+w]
            roi_gray = cv2.resize(roi_gray, (40,40))

            # Reconocer a la persona en el rostro detectado utilizando el reconocedor de rostros
            label, confidence = recognizer.predict(roi_gray)
            
            if confidence > 185:
                # Guardar la imagen como "mypicture.jpg"
                cv2.imwrite("mypicture.jpg", image)

                # Mostrar mensaje de confirmación
                print("Imagen guardada como 'mypicture.jpg'")
                print('Hola fabian' + str(confidence))
                mode.sleepModeOff('camera')
                rawCapture.truncate(0)
                time.sleep(30)
                print("A GRABAR")
            else:
                print('No eres fabian' + str(confidence))
            # Dibujar un rectángulo alrededor del rostro detectado y mostrar el nombre de la persona reconocida y la confianza en la predicción
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(image, f'{label}:{confidence}', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
            
        # display the image on screen
        new_size = (400, 300)
        resized_img = cv2.resize(image, new_size)
        cv2.imshow("Frame", resized_img)
        key = cv2.waitKey(1) & 0xFF

        # clear the stream in preparation for the next frame
        rawCapture.truncate(0)

        # if the `q` key was pressed, break from the loop
        ##if key == ord("q"):
        ##    break

    # cleanup the camera and close any open windows
    camera.close()
