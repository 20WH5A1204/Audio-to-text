# import the module
import speech_recognition as sr
# initialize
r = sr.Recognizer()
while True: 
    
    with sr.AudioFile('abc.wav') as source:
       print("listening to audio")
    # capture the audio
       audio = r.listen(source)
    
       try:
           text = r.recognize_google(audio)
           print("Audio:", text)
           if text == 'quit':
               break
       except:
          print('Error') 
          '''
    while True:
      with sr.Microphone() as source:
        # clear background noise
        r.adjust_for_ambient_noise(source, duration=0.3)
        
        print("Speak now")
        # capture the audio
        audio = r.listen(source)
        
        try:
            text = r.recognize_google(audio)
            print("Speaker:", text)
            if text == 'quit':
                break
        except:
                print('Please say again!!!')