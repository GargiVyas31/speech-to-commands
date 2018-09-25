__author__ = 'DELL'
import webbrowser as wb
import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
from googlesearch import search
import subprocess as sp

data=" "


def facebook(name):
    speak("Hold on "+name+" , I will redirect you to the facebook.")
    wb.open("www.facebook.com")

def youtube(name):
    speak("Hold on "+name+" , I'm opening Youtube for you.")
    wb.open("www.youtube.com")

def gmail(name):
    speak("just a minute "+name+",bring you to the Gmail.")
    wb.open("www.gmail.com")

def locations(data,name):
    data =data.split(" ")
    location = data[2]
    speak("Hold on "+name+" , I will show you where " + location + " is.")
    wb.open("https://www.google.nl/maps/place/" + location + "/&amp")

def search(data,name):
    speak("wait for a while "+name+" ,I will search for you.")
    wb.open("https://www.google.co.in/?gfe_rd=cr&ei=V7DXWJuQNarT8gfb-42QBw&gws_rd=ssl#newwindow=1&safe=active&q="+data+"&*")


def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.flac")
    os.system("audio.flac")

def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    with open("MicrophoneResults.flac", "wb") as f:
        f.write(audio.get_flac_data())
		#print("Say something!")

    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return data

def PA(data,name):

    if "what is your name" in data:
        speak("I am Mandimus ")

    if "how are you" in data:
        speak("I am fine and you ?")

    if "what time is it" in data:
        speak(ctime())

    if "where is" in data:
        locations(data,name)

    if " Facebook" in data:
        facebook(name)

    if " music"  in data:
        youtube(name)

    if "mail" in data:
        gmail(name)

    if "search for" in data:
        search(data,name)
    if "notepad" in data:
        sp.Popen(["notepad.exe", "file.txt"])


    if "google keep" in data:
        sp.Popen("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe  --profile-directory=Default --app-id=hmjkmjkepdijhoojdojkdfohbdgmmhki")

    if "goodbye" in data:
        speak("Goodbye bye!, "+name+" ,take care!!" )
        exit()



speak("what's Your name sir:")
name = input()
speak("hi "+name+"!!what can i do for you")

while 1:
    print("Speak. . .")
    time.sleep(5)
    print("start speaking")
    #time.sleep(1000)
    data = recordAudio()
    print("Processing. . .")
    PA(data, name)


