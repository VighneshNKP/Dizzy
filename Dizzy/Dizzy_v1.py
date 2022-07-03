import speech_recognition as sr
#import pyttsx3
import threading
from playsound import playsound
import time
from moviepy.editor import *
import subprocess
import psutil
import pywhatkit
from random import randint
#import json
import datetime
import beepy

#import keyboard

ran = randint(0,1)
call = ['DD','DP','BD','BP','desi', 'busy', 'disease', 'dizzy', 'digit', 'didi', 'baby', 'Dawai'] #Everytime I call her name this is what the speech recognition library understands.
#Probably due to my accent. Keep experimenting with your own voice input and fill up the above list accordingly.  
reply = ["dialogue/takecharge.mp3","dialogue/computer.mp3"]

#init function to get an engine instance for the speech synthesis
global recognizer
recognizer = sr.Recognizer()

#Define a function that takes user input and responds with audio and video accordingly. 
def respond(audio_file, speak_time):
  threading.Thread(target=playsound, args=(audio_file,), daemon=True).start()
  clip = VideoFileClip('face.mp4').resize((1920,1080))
  clip = clip.subclip(0,speak_time)
  clip.preview()
  clip.close()

#Battery warning
psutil.sensors_battery()
battery = psutil.sensors_battery()
if (battery.percent < 30 and battery.power_plugged != True):
   respond('dialogue/plugin.mp3', 4.5)
else:
   respond('dialogue/welcome.mp3', 3)
  

# listening to the speech and store in audio_text variable
while True: 
 with sr.Microphone() as source:
    print("Call me if you need me")
    recognizer.adjust_for_ambient_noise(source, duration= 0.5)
    audio_text = recognizer.listen(source)
    print("Time over, thank you")
    try:
      # using google speech recognition
      text = recognizer.recognize_google(audio_text)
      print(text)
      beepy.beep(sound=1)
    except:
     print("Sorry, I did not get that")

 while text in call:
  with sr.Microphone() as source:
    print("Start Talking")
    recognizer.adjust_for_ambient_noise(source, duration=0.5)
    audio_text = recognizer.listen(source)
    print("Time over, thank you")
    
    try:
      # using google speech recognition
      text = recognizer.recognize_google(audio_text)
      print(text)
    except:
      print("Sorry, I did not get that")

 
 #Introduction
  if text == 'who are you' or 'introduce' in text:
    respond('dialogue/Intro.mp3', 4)
    continue
#Response to Alexa comparison
  if 'Alexa' in text or 'Siri' in text:
   respond('dialogue/comeback_1.mp3', 3) 
   continue
#Comeback when you accuse her of being boring
  if 'boring' in text:
   respond('dialogue/comeback_2.mp3', 2)
   continue
#Open Internet   
  if 'Internet' in text:
   program="/usr/bin/firefox"
   respond('dialogue/computer.mp3', 3)
   subprocess.Popen([program])
   continue 
#Play any youtube video. Mainly used for music
  if 'play' in text:
   print(ran)
   respond('dialogue/takecharge.mp3', 4)
   pywhatkit.playonyt(text)
   break
#Random comeback
  if 'whose side are you on' in text:
   respond('dialogue/side.mp3', 3)  
   continue
#Random quirk
  if 'advice' in text:
   respond('dialogue/advice_comeback.mp3', 4)
   continue
#Response for lines like "I'm tired" or you're "awesome"
  if 'awesome' in text or 'tired' in text:
   respond('dialogue/feelthesameway.mp3', 2) 
   continue
  
    




   