import speech_recognition
import pyttsx
from os import path

class Speaker(object):
    def __init__(self, filePath):
        #talking engine
        self.engine = pyttsx.init('espeak')
        self.engine.setProperty('rate', 150)

        self.audioFile = path.abspath(filePath)
        #print(self.audioFile)

        #recognizer
        self.recognizer = speech_recognition.Recognizer()

    def speak(self, phrase):
        self.engine.say(phrase)
        self.engine.runAndWait()

    def listenToAudioFile_Sphinx(self):
        with speech_recognition.AudioFile(self.audioFile) as source:
            audio = self.recognizer.record(source, 10)

        try:
            #returns String
            return self.recognizer.recognize_sphinx(audio)

        except speech_recognition.UnknownValueError:
            print("could not understand")
        except speech_recognition.RequestError as e:
            print("recog error; {0}".format(e))

        return ""

    def listenToAudioFile_Google(self):
        with speech_recognition.AudioFile(self.audioFile) as source:
            audio = self.recognizer.record(source,10)

        try:
            #returns String
            return self.recognizer.recognize_google(audio)

        except speech_recognition.UnknownValueError:
            print("could not understand")
        except speech_recognition.RequestError as e:
            print("recog error; {0}".format(e))

        return ""