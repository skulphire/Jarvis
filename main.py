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
    testing.adjustAmbient(10,1500)
    #print("Sphinx: "+testing.listenToAudioFile_Sphinx())
    #print("\nGoogle: "+testing.listenToAudioFile_Google())
    print("\n")
    testing.listenToAudioFileCont_Google(120,500)