import speech_recognition
import pyttsx3
import time

class Auto():
    def __init__(self):
        time.sleep(1)
        while 1:
            self.listen()

    def listen(self):
        recognizer = speech_recognition.Recognizer()
        try:
            with speech_recognition.Microphone() as mic:
                audio = recognizer.listen(mic)
                text = recognizer.recognize_sphinx(audio)
                print(text)
                return text
        except speech_recognition.RequestError:
            self.speak("Sorry, I could not process your request")

        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            self.speak("Sorry, I can't understand you")

    def speak(self, text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    
    def command(self, callback):
       text = self.listen()
       if text == "run":
           return callback
        

        

auto = Auto()


    


