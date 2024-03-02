import pyttsx3
import speech_recognition as sr
import datetime
import os
import random
from requests import get
import wikipedia
import cv2 as cv
import webbrowser
import pywhatkit
import smtplib
# Data Save For DataBase

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
      
def wishme():
    hour = int(datetime.datetime.now().hour)
   
    if hour>=0 and hour<=12:
        speak("Good Morning!")
        
    elif hour>=12 and hour<=16:
        speak("Good Afternoon!")
        
    else:
        speak("Good Evening!")  

def takecommand():
    Command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        Command.pause_threshold = 1
        audio = Command.listen(source,timeout=1,phrase_time_limit=5)
        
    try:
        print("Recognizing.......")
        query = Command.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
        
    except Exception as e:
        return"None"
    return query
  
def TaskExe():
    
    wishme()
    speak("I am your Medusa. please tell me how can i help you") 
    
    while True:
        
        query = takecommand().lower()
        
        if "open notepad" in query:
            speak("ok")
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)
    
        elif "open vs code" in query:
            speak("ok i am open it")
            vpath = "C:\\Users\\MD Faijan\\Desktop\\Visual Studio Code.lnk"
            os.startfile(vpath)
            
        elif "open cmd" in query:
              speak("sure") 
              cpath = "C:\\WINDOWS\\system32\\cmd.exe"
              os.startfile(cpath)  
              
        elif "open camera" in query:
              video = cv.VideoCapture(0)
              while True:
                  ret, frame = video.read()
                  k = cv.waitKey(50)
                  if k==27:
                      break;
                  cv.imshow('image', frame) 
              
        elif "play music" in query:
              speak("ok i will play for you")
              music_dir = "f:\\music"
              songs = os.listdir(music_dir)
              #rd = random.choice(songs)
              for song in songs:
                  if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, song))        
              
        elif "play video" in query:
              video_dir = "F:\\video"
              speak("ok dear i will play video for you")    
              videos = os.listdir(video_dir)
              os. startfile(os.path.join(video_dir, videos[0])) 
              
        elif "ip address" in query:
              ip = get("https://api.ipify.org").text  
              speak(f"Your IP Address is {ip}")  
              speak("this is your IP address")  
              
        elif "wikipedia" in query:
              speak("searching wikipedia......")
              query = query.replace("wikipedia","")
              results = wikipedia.summary(query, sentences=2)
              speak("according to wikipedia....")
              speak(results)
              
        elif "play youtube" in query:
              speak("what would you like to search from youtube")
              i = takecommand().lower()
              pywhatkit.playonyt(f"{i}")                                         
               
        elif "open facebook" in query:
              webbrowser.open("https://www.facebook.com/")  
              
        elif "search google" in query:
              speak("what would you like search from google")
              I = takecommand().lower()
              pywhatkit.search(f"{I}")
                
        elif "bye" in query:
             speak("ok! meet you soon")
             speak("bye")        
             exit()
   
TaskExe()             