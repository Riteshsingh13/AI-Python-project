import pyttsx3
#importing the pyttsx3 module for text-to-speech conversion
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
#sapi5 is a microsoft program or api to Helps in synthesis and recognition of voice.

voices = engine.getProperty('voices')  #getting details of current voice

engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()           #Without this command, speech will not be audible to us.


def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("sir i am skellington. Please tell me how may i help you?")

def takeCommand():
    #it takes microphone input from the user and return string output
    r = sr.Recognizer()               #for recogning the speech
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1              # seconds of non-speaking audio before a phrase is considered complete
        audio = r.listen(source)          #Records a single phrase from source (an AudioSource instance) into an AudioData instance, which it returns.

    try:
        print("recognizing....")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")  

    except Exception as e:
        print("Say that again please..")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        #logic for execution based on query
        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences=2)
            speak('According to wikipedia')
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = "F:\\songs"
            songs = os.listdir(music_dir)  #list all the songs in music_dir
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is : {strTime}")

        elif 'close' in query:
            exit()

