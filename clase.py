import time

class Mode:
    def __init__(self):
        self.sleep = True
        self.emotion = ''
        self.sensor = ''
        
    def sleepModeOff(self, sensorType):
        self.sleep = False
        self.sensor = sensorType
    
    def sleepModeOn(self):
        self.sleep = True
        self.sensor = ''
        
    def status(self):
        return self.sleep
    
    def statusSensor(self):
        return self.sensor
    
    def statusEmotion(self):
        return self.emotion
    
    def changeEmotion(self, emotion):
        self.emotion = emotion