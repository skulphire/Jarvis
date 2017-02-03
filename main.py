from Drivers.voiceEngine import Speaker

if __name__ == '__main__':
    testing = Speaker()
    print("Sphinx: "+testing.listenToAudioFile_Sphinx())
    print("Google: "+testing.listenToAudioFile_Google())