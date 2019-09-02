import os
import time
import playsound
import speech_recognition
from gtts import gTTS

def speak(y):
    tts=gTTS(text=y,lang="en")
    filename="v.mp3"
    tts.save(filename)
    playsound.playsound(filename)

speak(input("Enter a msg : "))


