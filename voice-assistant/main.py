import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import sys
import openai


openai.api_key = "secret key from openai"


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            listener.adjust_for_ambient_noise(source,duration=1)
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            print(command)
            print('....')
    except:
        pass
    return command


def run():
    command=take_command()
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'Wiki' in command:
        wikipid = command.replace('Wiki', '')
        info = wikipedia.summary(wikipid, 3)
        print(info)
        talk(info)
    elif 'exit' in command:
        talk('see you next time')
        sys.exit(0)
    else:
        #In order to use the OpenAI API, you need to set up a paid account.
        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": command }])
        data = completion.choices[0].message.content
        print(data)
        my_list = data.split('.', 4)
        print(my_list[:2])


while True:
    run()






