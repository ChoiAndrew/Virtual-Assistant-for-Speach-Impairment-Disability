import pyttsx3

import datetime
import pywhatkit


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[11].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def run_alexa():
    command = 'What is the time'
    print (command)
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('The current time is' + time)


while True:
    run_alexa
