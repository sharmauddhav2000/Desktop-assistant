import speech_recognition as sr
import pyttsx3

listener=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()

def user_command():
    try:
        with sr.Microphone() as source:
          print('listening...')
          voice=listener.listen(source)
          command=listener.recognize_google(voice)
          command=command.lower()
          if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
            pass
    return command

def run_alexa():
    command=user_command()
    if 'play' in command:
        song=command.replace('play','')
        talk('playing ' + song)
        print(song)


run_alexa()