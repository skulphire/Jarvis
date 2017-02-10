import pyttsx

class voiceEngine(object):
    def __init__(self):
        # talking engine
        self.engine = pyttsx.init('espeak')
        self.engine.setProperty('rate', 150)

    def speak(self, phrase):
        self.engine.say(phrase)
        self.engine.runAndWait()