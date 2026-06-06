import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import keyboard
import tkinter as tk

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        # print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        # print(command)

        if "jarvis" in command:
            speak("Hello Deepak")

            if "chrome" in command:
                os.system("start chrome")

            # elif "game" in command:
            #     os.startfile("C:\Program Files\Epic Games\AsphaltLegendsUnite\Asphalt9_epic_x64_rtl.exe")

            elif "youtube" in command:
                webbrowser.open("https://youtube.com")

            elif "exit" in command:
                speak("Goodbye")
                break

            elif "play song" in command:
                webbrowser.open("https://youtu.be/NAkQVL61BRI?si=fa0KwS3CneoAmvkz")

            elif "play music" in command:
                keyboard.send('play/pause media')

            elif "pause music" in command:
                keyboard.send('play/pause media')

            elif "next song" in command:
                keyboard.send('next track')

            elif "previous song" in command:
                keyboard.send('previous track')
            
            elif "volume up" in command:
                keyboard.send('volume up')

    except:
        # print("Couldn't understand")
        pass