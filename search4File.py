from Drivers.listenEngine import listenEngine
import os
if __name__ == '__main__':
    search = input("Filename: ")
    file  = "nothing"
    for root,dirs,files in os.walk("/home"):
        if search in files:
            file = os.path.join(root,search)

    print(file)
    recogEngine = listenEngine(file)
    recogEngine.adjustAmbient(10, 50)
    #print("Sphinx: "+testing.listenToAudioFile_Sphinx())
    #print("\nGoogle: "+testing.listenToAudioFile_Google())
    print("\n")
    recogEngine.listenToAudioFileCont_Google(120, 200)