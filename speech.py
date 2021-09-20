import speech_recognition

def stop():
    print("the key word has been found")


recognizer = speech_recognition.Recognizer()
keyword = "h"
while True:
    try:
        with speech_recognition.Microphone() as mic:
            # recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            text = recognizer.recognize_sphinx(audio)
            print(text)
        try: 
            if recognizer.recognize_sphinx(audio) == keyword:
                stop()
        except speech_recognition.RequestError:
            print("request error")

    except speech_recognition.UnknownValueError:
        recognizer = speech_recognition.Recognizer()


