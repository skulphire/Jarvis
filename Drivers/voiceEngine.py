import pyttsx
from gtts import gTTS
import os

class voiceEngine(object):
    def __init__(self):
        # talking engine
        self.engine = pyttsx.init('espeak')
        self.engine.setProperty('rate', 135)

    def speakPYTTS(self, phrase):
        self.engine.say(phrase)
        self.engine.runAndWait()

    def speakGoogle(self, phrase):
        gtalk = gTTS(text=phrase,lang='en')
        gtalk.save("talking.mp3")
        os.system("mpg321 talking.mp3")
        os.remove("talking.mp3")