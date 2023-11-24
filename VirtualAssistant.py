import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

engine = pyttsx3.init('sapi5')
client = wolframalpha.Client('Your_App_ID')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    print('' + audio)
    engine.say(audio)
    engine.runAndWait()


def greet():
    chr = int(datetime.datetime.now().hour)
    if chr >= 0 and chr < 12:
        speak('Good Morning!')

    if chr >= 12 and chr < 18:
        speak('Good Afternoon!')

    if chr >= 18 and chr != 0:
        speak('Good Evening!')


greet()
speak('How may I help you?')

def respondml():
    X_train,X_test=train_test_split(stMsgs,test_size=0.7)
    m=DecisionTreeClassifier()
    m.fit(X_train)
    mp=m.predict(X_test)
    return mp

def Comminput():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language='en-in')
        print('' + query + '\n')

    except sr.UnknownValueError:
        speak("Sorry! I didn't get that! Try typing the command!")
        query = str(input('Command: '))
    return query


if __name__ == '__main__':
    while True:
        query = Comminput()
        query = query.lower()

        if query == 'open youtube':
            speak('okay')
            webbrowser.open('www.youtube.com')

        elif query == 'open google':
            speak('okay')
            webbrowser.open('www.google.com')

        elif query == 'open gmail':
            speak('okay')
            webbrowser.open('www.gmail.com')

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = pd.read['Just doing my thing!', 'I am fine!','Nice!', 'I am nice and full of energy']

        elif 'email' in query:
            speak('Who is the recipient?')
            recipient = Comminput()

            if 'Aditya Pandey' in recipient:
                try:
                    speak('What should I say to him?')
                    content = Comminput()
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("parikhdivy03@gmail.com", '')
                    server.sendmail('parikhdivy03@gmail.com',"pandey.aditya400@gmail.com", content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry Sir! I am unable to send your message at this moment!')

        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()

        elif 'hello' in query:
            speak('Hello Sir')

        elif 'bye' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()

        elif 'open zoom' in query:
            speak('opening zoom....')
            zoom = ''
            os.startfile(zoom)

        elif 'tell me about the weather' in query:
            speak('searching....')
            try:
                speak("which area's weather do you want to know?")
                speak('searching appropriate websites....')
                speak("Here's what I've found:")
                q = webbrowser.open('www.accuweather.com')
                res = client.query(query)
                results = next(res.results).text
                speak('WOLFRAM-ALPHA says - ')
                results = q.summary(query, sentences=2)
                speak(results)

            except:
                webbrowser.open('www.google.com')

        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA says - ')
                    speak('Got it.')
                    speak(results)

                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('I found one result regarding', query)
                    speak('According to Wikipedia:')
                    speak(results)
            except:
                webbrowser.open('www.google.com')

        speak('Next Command! Sir!')