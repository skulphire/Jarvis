from .listenEngine import listenEngine
from .voiceEngine import voiceEngine
import os

class jarvisAI(object):
    def __init__(self):
        self.listen = listenEngine()
        self.voice = voiceEngine()

    def findData(self, micInput = None):
        if micInput == None:
            micInput = self.listen.listenToMicrophone_Google()
        if "where is" in micInput:
            micInput =micInput.split(" ")
            location = micInput[2]
            self.voice.speakGoogle("Showing you where" + location + "is.")
            #self.voice.speakPYTTS("Showing you where" + location + "is.")
            os.system("firefox https://www.google.com/maps/place/" + location )#+ "/&amp;")
        elif "Weather" in micInput:
            self.voice.speakGoogle("Showing you current weather")
            os.system("firefox https://www.google.com/#q=weather")

