import speech_recognition
from os import path

class listenEngine(object):
    def __init__(self, filePath=None):

        self.fileExists = False
        if(filePath != None):
            self.audioFile = filePath
            if(path.exists(self.audioFile)):
                self.fileExists = True

        #recognizer
        self.recognizer = speech_recognition.Recognizer()

    def listenToAudioFile_Sphinx(self):
        if(self.fileExists):
            with speech_recognition.AudioFile(self.audioFile) as source:
                audio = self.recognizer.record(source,30,35)

            try:
                #returns String
                return self.recognizer.recognize_sphinx(audio)

            except speech_recognition.UnknownValueError:
                print("could not understand")
            except speech_recognition.RequestError as e:
                print("recog error; {0}".format(e))

            return ""
        else:
            return "File Does Not Exist"

    def listenToAudioFile_Google(self):
        if (self.fileExists):
            with speech_recognition.AudioFile(self.audioFile) as source:
                audio = self.recognizer.record(source,15,35)

            try:
                # returns String
                return self.recognizer.recognize_google(audio)

            except speech_recognition.UnknownValueError:
                print("could not understand")
            except speech_recognition.RequestError as e:
                print("recog error; {0}".format(e))

            return ""
        else:
            return "File Does Not Exist"

    def adjustAmbient(self,duration, threshold):
        self.recognizer.energy_threshold = threshold
        with speech_recognition.AudioFile(self.audioFile) as source:
            self.recognizer.adjust_for_ambient_noise(source, duration)

    def listenToAudioFileCont_Google(self,start,stop):

        if (self.fileExists):
            while(start <= stop):
                self.adjustAmbient(1,50)
                with speech_recognition.AudioFile(self.audioFile) as source:

                    audio = self.recognizer.record(source,10,start)

                try:
                    print(">"+self.recognizer.recognize_google(audio))

                except speech_recognition.UnknownValueError:
                    print("could not understand")
                except speech_recognition.RequestError as e:
                    print("recog error; {0}".format(e))
                #return ""
                start = start + 10
        else:
            return "File Does Not Exist"

    def listenToMicrophone_Google(self):
        with speech_recognition.Microphone() as source:
            audio = self.recognizer.listen(source)
            try:
                # returns String
                return self.recognizer.recognize_google(audio)
            except speech_recognition.UnknownValueError:
                print("could not understand")
            except speech_recognition.RequestError as e:
                print("recog error; {0}".format(e))
            return ""