##### still under progress will be adding GUI using Tkinter




# importing header files

import speech_recognition as sr #for speech recognition
import pyttsx3 # for text to speech conversion
from selenium import webdriver # to interact with firefox web browser , would need geckodriver for firefox and chromedriver for google chrome
from selenium.webdriver.common.keys import Keys
import time # gives current time

#creating all important objects

engine = pyttsx3.init( ) # speaker object
voices=engine.getProperty('voices') 
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',95)
recorder=sr.Recognizer() # listener object

def play(txt="Hey Ram Remix"): #function to play music on youtube
    driver = webdriver.Firefox()
    driver.get("https://www.youtube.com/") #opens the url in firefox
    search=driver.find_element_by_name("search_query") # finds the search box by searching for element with name "search_query" in the html page
    search.send_keys(txt) # funciton to send keyboard text input in form of string
    engine.say("Playing"+txt)
    engine.runAndWait()
    search.submit()
    driver.implicitly_wait(100) # wait 100 sec if page taking too long to load until termination
    driver.find_element_by_css_selector("[title*='"+txt+"']").click()

def search(txt="Geeta Shloka"): # funciton to search on google
    driver = webdriver.Firefox()
    driver.get("https://www.google.com/")
    search=driver.find_element_by_name("q")
    search.send_keys(txt)
    search.send_keys(Keys.ENTER)

def tell_time():# funciton to tell time
    hour=time.localtime().tm_hour # gettin current time using time module
    min=time.localtime().tm_min
    if hour>12:
        hour=str(hour-12)
        min=str(min)
        engine.say("the time is "+hour+" hour and "+min+" minutes PM")
        engine.runAndWait()
    else:
        hour=str(hour)
        min=str(min)
        engine.say("the time is "+hour+" hour and "+min+" minutes AM")
        engine.runAndWait()

def listen(): # function to listen to user
    with sr.Microphone() as source:
        # recorder.adjust_for_ambient_noise(source,duration=0.2)
        # engine.say("How can I help you")
        # engine.runAndWait()
        print("speak")
        audio=recorder.listen(source)
        text=recorder.recognize_google(audio) # using google API for speech to text conversion
        text=text.lower()
        if "play" in text:
            engine.say("OK")
            engine.runAndWait()
            play(text[4:])
        elif "time" in text:
            tell_time()
        elif "search" in text:
            engine.say("OK")
            engine.runAndWait()
            search(text[6:])
        else:
            print("no command")
            engine.say("No command found")
            engine.runAndWait()

listen() # starting listen function





