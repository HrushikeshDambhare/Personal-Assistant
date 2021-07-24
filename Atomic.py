import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import psutil
import pynotifier
import pywhatkit as kit
import cv2
import numpy as np
import requests


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[1].id) 
engine.setProperty("rate" , 190)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

 
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <12:
        speak("Good Morning Boss !")
    
    elif hour>=12 and hour<18:
        speak("Good Afternooon Boss !")

    else:
        speak("Good Evening Boss !")

    speak("My name is Nucleus. Please tell me how can i help you")

def takeCommand():
    #it takes microphone input form the user and returns string output

    r = sr.Recognizer() 
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1   
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        speak(" Iam Recognizing boss ")
        print(f"user said: {query}\n" )



    except Exception as e:
        # print(e)


        print("Boss say that again please....")
        speak("Boss say that again please")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query =takeCommand().lower()

        # logic for executing tasks based on query
        if 'wikipedia' in query:
           speak('searching wikipedia....')
           query = query.replace("wikipedia", "")
           results = wikipedia.summary(query, sentences=2) 
           speak("According to wikipedia ")
           speak(results)

        elif 'open youtube' in query:
            speak('opening youtube')
            webbrowser.open("youtube.com")


        elif 'open google' in query:
            speak('opening google')
            webbrowser.open("google.com")    
        

        elif 'play music' in query:
            music_dir = 'C:\\Users\\hrush\\Desktop\\Atom\\music_dir'
            songs = os.listdir(music_dir)
            print("random item from songs is:" , random.choice(songs))
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Boss , the time is {strTime}")


        elif 'open web series and movies' in query:
            path = "H:\\web series and movies\\Mulashi Pattern"
            os.startfile(path)

        elif 'open intsagram ' in query:
            speak('opening instagram')
            webbrowser.open("instagram.com")    

        elif 'what is battery percentage' in query:
            speak(' Boss battery percentage is ')
           
            from pynotifier import Notification
            battery=psutil.sensors_battery()
            percent=battery.percent
            Notification( "Battery Percentage" , str(percent)+" % Battery Remaining " , duration=10).send()   #descrption ,title ,time-in-sec
           
        elif 'plugged ' in query:
            battery=psutil.sensors_battery()
            plugged = battery.power_plugged
            plugged = speak ('sir iam plugged in')if plugged else speak (' sir iam not plugged in')
            print (plugged)


        elif 'play youtube video ' in query:

            speak('sure boss')
            kit.playonyt("palana baal shivaji cha")


           

           
        elif 'play movie' in query:
            video_dir='C:\\Users\\hrush\\Desktop\\Atom\\video_dir'
            video= os.listdir(video_dir)
            print("random item from video is:" , random.choice(video))
            video_path= os.startfile(os.path.join(video_dir, video[0]))


        elif 'news headlines ' in query:
            API_KEY = 'fb3a5891a786455bb898f36e92b09f24'
            params = {
                'q': 'India',
                'source': 'bbc-news',
                'sortBy': 'top',
                'language': 'en',
                #'category': 'business',
                #'country': 'us',
                #'apiKey': API_KEY,

    
            } 

            headers = {

                'X-Api-Key': API_KEY,  # KEY in header to hide it from url
            }

            url = 'https://newsapi.org/v2/top-headlines'

            response = requests.get(url, params=params, headers=headers)
            data = response.json()

            articles = data["articles"] 
            results= [arr["title"] for arr in articles] 

            for i, arr in enumerate(results, 1): 
                print(i, arr)
                speak(results )


                

           
           
        
        


            




            


            
