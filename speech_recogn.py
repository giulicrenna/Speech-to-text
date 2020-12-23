import speech_recognition as sr
import pyttsx3


engine = pyttsx3.init()
engine.say("order")
engine.runAndWait()
