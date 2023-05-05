import cv2
from picamera import PiCamera
from picamera.array import PiRGBArray
import time
import face_recognition



def videoDetection(mode):
    
    # initialize the camera and grab a reference to the raw camera capture
    camera = PiCamera()
    camera.resolution = (1280,720)
    camera.framerate = 32
    camera.brightness = 50 # Adjust the brightness
    camera.contrast = 0 # Adjust the contrast
    camera.saturation = 0 # Adjust the saturation
    camera.exposure_mode = 'auto' # Set the exposure mode to automatic
    camera.awb_mode = 'auto' # Set the white balance mode to automatic

    rawCapture = PiRGBArray(camera, size=(1280,720))

    # allow the camera to warmup
    time.sleep(0.1)
    
    ref_image = face_recognition.load_image_file("/home/fabian04/Desktop/titulation/mypicture.jpg")
    ref_image = cv2.cvtColor(ref_image, cv2.COLOR_BGR2RGB)

    # Codificar la imagen de referencia
    ref_encoding = face_recognition.face_encodings(ref_image)
    ref_encoding = ref_encoding[0]

    # capture frames from the camera
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        # grab the raw NumPy array representing the image, then initialize the timestamp
        # and occupied/unoccupied text
        image = frame.array
            
        small_image = cv2.resize(image, (0, 0), fx=0.25, fy=0.25)
        rgb_small_image = cv2.cvtColor(small_image, cv2.COLOR_BGR2RGB)

        # Detectar los rostros en la imagen utilizando la biblioteca face_recognition
        face_locations = face_recognition.face_locations(rgb_small_image)

        #print(f"Se encontraron {len(face_locations)} rostros en la imagen.") # Para ver cuántos rostros se detectaron
        
        face_encodings = face_recognition.face_encodings(rgb_small_image, face_locations)

        # display the image on screen
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            matches = face_recognition.compare_faces([ref_encoding], face_encoding)
            if matches[0]:
                cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
                cv2.putText(image, "Match", (left, top - 6), cv2.FONT_HERSHEY_DUPLEX, 0.6, (0, 255, 0), 1)
                cv2.imwrite("mypicture.jpg", image)
                print("Imagen guardada como 'mypicture.jpg'")
                mode.sleepModeOff('camera')
                rawCapture.truncate(0)
                time.sleep(30)
            else:
                cv2.rectangle(image, (left, top), (right, bottom), (0, 0, 255), 2)
                cv2.putText(image, "No Match", (left, top - 6), cv2.FONT_HERSHEY_DUPLEX, 0.6, (0, 0, 255), 1)
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
    
    cv2.destroyAllWindows()
    