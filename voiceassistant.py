import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say("hello")
engine.say("I am your voice assistant")
engine.runAndWait()  

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def speechtotext():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing...")
            text = r.recognize_google(audio)
            print(f"User said: {text}\n")
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Sorry, I did not understand")
            return "None"

        return text

def command(text):
    if 'wikipedia' in text:
        query = text.replace("wikipedia", "").strip()
        speak(f"Searching Wikipedia for {query}...")
        
        try:
            summary = wikipedia.summary(query, sentences=2)
            speak(f"According to Wikipedia: {summary}")
            print(summary)
        except wikipedia.DisambiguationError as e:
            options = ', '.join(e.options[:5])  
            speak(f"Your search term is too broad. Did you mean: {options}?")
        except wikipedia.PageError:
            speak("Sorry, the page does not exist on Wikipedia.")
        except Exception as e:
            speak(f"An error occurred: {e}")

    

    
    elif 'wish me' in text:
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            speak("Good morning, yaar")
        elif hour >= 12 and hour < 18:
            speak("Good afternoon, yaar")
        else:
            speak("Good evening, yaar")

    elif 'open google' in text:
        webbrowser.open("https://www.google.com")

    elif 'open youtube' in text:
        webbrowser.open("https://www.youtube.com")

    elif 'how are you' in text:
        speak("I am just a program")

    elif 'what is the time' in text:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {current_time}")

    elif 'play music' in text:
        
        speak("Opening Spotify")
        webbrowser.open("https://open.spotify.com/") 

   
    

    elif 'stop' in text:
        speak("Bye! Have a nice day")

    elif 'listen for next command' in text:
        speak("Listening for your next command")
        next_command = speechtotext().lower()
        command(next_command)

    else:
        speak("I'm sorry, I can't help you")


text = speechtotext().lower()
command(text)
