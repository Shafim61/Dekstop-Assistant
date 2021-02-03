import speech_recognition as sr
import pyttsx3
import pywhatkit
from datetime import datetime
import wikipedia
import pyjokes
import webbrowser
import pyautogui
import os
import random
import time

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)

Alive = True

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "alexa" in command:
                print(command)
    except:
        print("say that again")
        talk("Say that again")
        return "None"

    return command

def wish_me():
    hour = int(datetime.now().hour)
    if hour >=0 and hour < 12 :
        talk("Good Morning")
    elif hour >=12 and hour <18 :
        talk("Good Afternoon")
    else:
        talk("Good Night")
    talk("I am Alexa. I am your dekstop assistant. Tell me how can i help you")

def run_alexa():
    command = take_command()
    if "play" in command:
        song = command.replace("play","")
        talk("playing")
        print("playing....")
        pywhatkit.playonyt(song)

    elif "time" in command:
        time = datetime.now().strftime("%I:%M %p")
        talk(f"Now it is {time}")
        print(f"Now it is {time}")
    
    elif "wikipedia" in command:
        person = command.replace("wikipedia","")
        info = wikipedia.summary(person,5)
        print(info)
        talk(info)

    elif "How are you" in command:
        talk("I am fine.Thank you.How are you")
        print("I am fine.Thank you.How are you")

        if "doing good" or "fine" in command:
            print("Thats great")
            talk("Thats great")
        else:
            pass

    elif "joke" in command:
        talk(pyjokes.get_joke())

    elif "open google" in command:
        webbrowser.open("www.google.com")
        if "write" in command:
            pyautogui.typewrite(command)
            pyautogui.press("enter")
        else:
            pass

    elif "open youtube" in command:
        webbrowser.open("www.youtube.com")
        if "write" in command:
            pyautogui.typewrite(command)
            pyautogui.press("enter")
        else:
            pass
    elif "music on" in command:
        music_dir = "F:\\Music\\english"
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir,songs[random.randint(0,29)]))

    elif "who has made you" in command:
        talk("My tutor and mentor is Tanvir Rashik Shafim")
        print("My tutor and mentor is Tanvir Rashik Shafim")

    elif "your age" in command:
        date = "17/01/2021"
        birthday = datetime.strptime(date, "%d/%m/%Y")
        now = datetime.now()
        current_time = datetime(now.year, now.month, now.day)
        Age = (current_time - birthday).days//365
        print(f"I am {Age} years old")


    elif "Stop" in command:
        talk("Thank you for using me")
        Alive = False

    else:
        talk("Sorry i didnt understand")
        talk("Please say it again")


wish_me() 

while  Alive is True:  
    run_alexa()


#So it is the end.Thank you...
