import pyttsx3
import speech_recognition as sr
import pyaudio
from ledconfig import *

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 150)    # Speed percent
engine.setProperty('volume', 0.9) 
#print(voices)
engine.setProperty('voices', voices[1].id)

#texttospeech
def speak(audio):
    led_on()
    engine.say(audio)
    print(audio)
    engine.runAndWait()
    led_off()

def  takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        led_on()
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=5,phrase_time_limit=8)

    try:
        led_off()
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        print("Say that again please...")
        return "none"
    return query
