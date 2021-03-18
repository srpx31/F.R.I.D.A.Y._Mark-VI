from random import choice
from time import sleep
import speech_recognition
import pyttsx3
from gtts import gTTS
import sys
import os
import subprocess
import webbrowser
import playsound
import wikipedia
import wolframalpha
import smtplib
import psutil
import requests

def relPath(rel_file_path):
    return(os.path.dirname(__file__)+ '/' + rel_file_path)

class TTS:
    """
    import pyttsx3
    engine = pyttsx3.init('espeak')
    schema = engine.getProperty('voices')
    engine.setProperty('voice', schema[0].id)
    engine.setProperty('rate', 143)
    def speak(text):
        engine.say(text)
        engine.runAndWait()
    """

class dtTime:
    def showDate():
        from datetime import datetime
        date_num = datetime.now().strftime('%d')
        suffix_end_num = date_num [len(date_num) - 1]
        if (suffix_end_num == 1):
            suffix = "st"
        elif (suffix_end_num == 2):
            suffix = "nd"
        elif (suffix_end_num == 3):
            suffix = "rd"
        else:
            suffix = "th"
        day_name = datetime.now().strftime('%A')
        month_name = datetime.now().strftime('%B')
        year_num = datetime.now().strftime('%Y')
        date = day_name + ", " + (date_num + suffix) + " of " + month_name + ", " + year_num
        way1 = "It is " + date
        way2 = "Today is " + date
        way3 = "This day is " + date
        rand_way = choice([way1, way2, way3])
        print(rand_way)

    def showTime():
        from datetime import datetime
        time = datetime.now().strftime("%H hours and %M minutes")
        way1 = "It is " + time
        way2 = "Now, it's " + time
        way3 = "Currently it is " + time
        rand_way = choice([way1, way2, way3])
        print(rand_way)

    def timer():
        from time import sleep
        time_span = int(input("Enter number of seconds :- "))
        print("3")
        sleep(0.8)
        print("2")
        sleep(0.8)
        print("1")
        sleep(0.8)
        print("Go!")
        sleep(time_span)
        print("Time's Up!")
dtTime.showDate()