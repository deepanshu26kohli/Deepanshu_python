import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
     hour = int(datetime.datetime.now().hour)
     if hour >= 0 and hour < 12:
         speak("good Morning sir")
     elif hour>=12 and hour<18:
         speak("good afternoon sir")
     else:
         speak("Good evening sir")
     speak("Iam reeo how may i help you")
def takecommand():
    """it takes microphone input from the user and returns string input"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening")
        r.pause_threshold = 1
        audio=r.listen(source)
    try:
        print("Recogonizing....")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said : {query}\n")
    except Exception as e:
        # print(e)
        print("say that again plz")
        return "none"
    return query

if __name__ == "__main__":
     wishme()
     while True:
         query = takecommand().lower()

         if 'wikipedia' in query:
             speak('searching wikipedia.............')
             query = query.replace("wikipedia", "")
             results = wikipedia.summary(query, sentences=2)
             speak("According to wikipedia")
             print(results)
             speak(results)
         elif 'open youtube' in query:
             webbrowser.open("youtube.com")
         elif 'open hotstar' in query:
             webbrowser.open("hotstar.com")
         elif 'open google' in query:
             webbrowser.open("google.com")
         elif 'open geeks for geeks' in query:
             webbrowser.open("geeksforgeeks.com")
         elif 'open flipkart' in query:
             webbrowser.open("flipkart.com")
         elif 'open amazon' in query:
             webbrowser.open("amazon.com")
         elif 'what is my ip address' in query:
             webbrowser.open("whatismyipaddress.com")
         elif 'open firefox' in query:
             webbrowser.open("firefox.com")
         elif 'the time' in query:
             strTime = datetime.datetime.now().strftime("%H:%M:%S")
             speak(f"sir the time is {strTime}")
         elif 'open vs code' in query:
             codePath="C:\\Users\\DEEPANSHU KOHLI\\AppData\\Roaming\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
             os.startfile(codePath)
         elif 'quit' in query:
             exit()