import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import playsound
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour <12:
        speak("Good morning")
    elif hour>= 12 and hour <18:
        speak("Good Afternoon")
    else:
        speak("Good evening")
    speak("I am shubham sir. please tell me how may i help you ")

def takeCommand():

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said : {query}\n")

    except Exception as e:
        print ("say that again please.....")
        return "none"
    return query


if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query=query.replace("wikipedia", "")
            results = wikipedia.summary(query,sentences=3)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif'open youtube' in query:
            webbrowser.open("youtube.com")

        elif'open google' in query:
            webbrowser.open("google.com")

        elif'open facebook' in query :
            webbrowser.open("facebook.com")

        


