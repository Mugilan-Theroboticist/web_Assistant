import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

listener = sr.Recognizer()

def listen():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print("You said:", command)
            return command
    except:
        return ""

def run_assistant():
    command = listen()

    if "hello" in command:
        speak("Hello, how can I help you")

    elif "time" in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak("Current time is " + time)

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open calculator" in command:
        speak("Opening calculator")
        webbrowser.open("calc:")

    elif "open facebook" in command:
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")

    elif "cyber" in command:
        speak("Opening Cyberbots website")
        webbrowser.open("https://www.cyberbots.in")
    elif "chatgpt" in command:
        speak("Opening Cyberbots website")
        webbrowser.open("https://www.chatgpt.com")

    elif "bye" in command:
        speak("Goodbye")
        exit()

while True:
    run_assistant()
