import speech_recognition as sr
import pyttsx3

def command():
    r=sr.Recognizer()
    with sr.Microphone as source:
        print("Alexa: Litsening...")
        audio=r.listen(source)
        try:
            query=r.recognition_google(audio)
            print(f"master:{query}")
            return query
        except:
            print("Try Again")

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()