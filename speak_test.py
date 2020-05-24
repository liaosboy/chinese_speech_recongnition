import speech_recognition
import time
import os
import speech_recognition as sr
# %%

r = sr.Recognizer()
text = ''
while (text != 'close'):
    with sr.Microphone(device_index=1) as source:
        print('speak')
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language='zh-TW')
            print('You said : {0}'.format(text))

        except:
            print('sorry')
            break
