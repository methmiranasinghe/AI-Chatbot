import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser
import os
import pyaudio
import pyfiglet

text = pyfiglet.figlet_format("Chat Buddy")
print(text)

print('Developed by Methmi Hasara & Pasindu Bandara')
print('© 2022 All rights Reserved')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')


engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir!")
        
    elif hour >= 12 and hour < 15:
        speak("Good Afternoon Sir!")
    
    elif hour >= 15 and hour < 19:
        speak("Good Evening Sir!")

    else:
        speak("Hope you had a good day!")
    speak("How May I help you?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:

        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing ....")
        query = r.recognize_google(audio, language='en-in')
        print(f"You : {query}\n")

    except Exception as e:
        print(e)
        print("Sorry,Please say that again...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching wikipedia')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https:\\www.youtube.com")
        elif 'open google maps' in query:
            webbrowser.open("https:\\www.google.com/maps")
        elif 'play music' in query:
            webbrowser.open("https:\\open.spotify.com/")
        elif 'play video' in query:
            video_dir = "F:\\Video"
            videos = os.listdir(video_dir)
            print(videos)
            os.startfile(os.path.join(video_dir, videos[0]))
        elif 'open code' in query:
            codePath = "C:\\Users\\methm\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            
        elif 'open camera' in query:
            codePath = "C:\\Windows\camera.exe"
            os.startfile(codePath)
            
            
        elif 'what is your name' in query:
            speak('I am your chat buddy')
            
        elif 'goodbye' in query:
            speak('good bye and have a good day')
            exit()
            
        else:
            speak('Did not recognized')
            
        
            
            