from Drivers.voiceEngine import Speaker
import os
if __name__ == '__main__':
    search = input("Filename: ")
    file  = "nothing"
    for root,dirs,files in os.walk("/home"):
        if search in files:
            file = os.path.join(root,search)

    print(file)
    testing = Speaker(file)
    #print("Sphinx: "+testing.listenToAudioFile_Sphinx())
    print("Google: "+testing.listenToAudioFile_Google())