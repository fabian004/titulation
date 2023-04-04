from time import sleep
import psutil
import requests
from network import myNetwork
def activeMode(mode):
    statusSensor = mode.statusSensor()
    mem = psutil.virtual_memory()
    total_memory = mem.total / (1024 * 1024)
    available_memory = mem.available / (1024 * 1024)
    print(total_memory)
    print(available_memory)
    sleep(5)
    if(statusSensor == 'camera'):
        response = requests.get('https://www.google.com.mx/')
        emotion = myNetwork()
        mode.changeEmotion(emotion)
        response.close()
    
    mem = psutil.virtual_memory()
    total_memory = mem.total / (1024 * 1024)
    available_memory = mem.available / (1024 * 1024)
    print(total_memory)
    print(available_memory)
    sleep(5)
    mem = psutil.virtual_memory()
    total_memory = mem.total / (1024 * 1024)
    available_memory = mem.available / (1024 * 1024)
    print(total_memory)
    print(available_memory)
    statusEmotion = mode.statusEmotion()
    print(statusEmotion)
    sleep(10)
    mode.sleepModeOn() 