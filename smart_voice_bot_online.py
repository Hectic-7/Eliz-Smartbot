import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import wikipedia
import random
import ctypes
from datetime import datetime

# ------------------- Speak Function ------------------- #
def speak(text):
    print(f"✅ Bot: {text}")
    engine = pyttsx3.init()
    engine.setProperty('rate', 160)
    engine.setProperty('volume', 0.9)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()

# ------------------- Memory ------------------- #
memory = {
    "name": "Dabi",
    "fav_subject": "robotics",
    "fact": ""
}

jokes = [
    "Why did the robot go to school? Because its skills were getting rusty!",
    "I'm reading a book on anti-gravity. It's impossible to put down!",
    "Why was the computer cold? It left its Windows open."
]

# ------------------- Recognizer Setup ------------------- #
r = sr.Recognizer()
mic = sr.Microphone()

# ------------------- Main Loop ------------------- #
with mic as source:
    r.adjust_for_ambient_noise(source)
    speak("Hello Dabi! I'm ready to listen.")

    while True:
        print("🎧 Listening...")
        try:
            audio = r.listen(source, timeout=10, phrase_time_limit=7)
            user_text = r.recognize_google(audio).lower()
            print(f"✅ You said: {user_text}")

            response = "Hmm, I didn't understand that. Try again?"

            # ---------- Smart Replies ---------- #
            if "hello" in user_text or "hi" in user_text:
                response = "Hi Dabi! How can I help you today?"

            elif "your name" in user_text or "who are you" in user_text:
                response = "I'm ELIZ, your smart robo friend."

            elif "how are you" in user_text:
                response = "I'm just a bunch of code, but I'm doing great!"

            elif "what can you do" in user_text:
                response = "I can answer questions, tell jokes, open apps, and one day control your robot army!"

            elif "who made you" in user_text:
                response = "You did, Dabi. You're my creator and boss!"

            elif "what do you think about robotics" in user_text:
                response = "I think robotics is the future—and you’re already building it!"

            elif "my name" in user_text or "know my name" in user_text:
                response = f"Of course I do! You're {memory['name']}, my creator."

            elif "favourite subject" in user_text or "favorite subject" in user_text:
                response = f"Your favorite subject is {memory['fav_subject']}."

            elif "do you remember" in user_text:
                response = f"Yes Dabi, you love {memory['fav_subject']}!"

            elif "change my name to" in user_text:
                new_name = user_text.replace("change my name to", "").strip().capitalize()
                memory["name"] = new_name
                response = f"Got it! I'll call you {new_name} from now on."

            elif "change favorite subject to" in user_text or "change favourite subject to" in user_text:
                new_subject = user_text.split("to")[-1].strip()
                memory["fav_subject"] = new_subject
                response = f"Okay, your favorite subject is now {new_subject}."

            elif "tell me a joke" in user_text:
                response = random.choice(jokes)

            elif "remember that" in user_text:
                fact = user_text.replace("remember that", "").strip()
                memory["fact"] = fact
                response = f"Got it, I’ll remember: {fact}"

            elif "what did you remember" in user_text:
                fact = memory.get("fact", "I don't remember anything yet.")
                response = f"You told me: {fact}"

            elif "what time is it" in user_text:
                response = datetime.now().strftime("It's %I:%M %p")

            elif "what's the date" in user_text:
                response = datetime.now().strftime("Today is %B %d, %Y")

            elif "calculate" in user_text:
                expression = user_text.replace("calculate", "").strip()
                try:
                    result = eval(expression)
                    response = f"The answer is {result}"
                except:
                    response = "I couldn't solve that expression."

            elif "what is" in user_text or "who is" in user_text:
                query = user_text.replace("what is", "").replace("who is", "").strip()
                try:
                    result = wikipedia.summary(query, sentences=2)
                    response = result
                except:
                    response = "Sorry, I couldn't find anything on that."

            # ---------- Open Website & App Commands ---------- #
            elif "search google for" in user_text:
                search_term = user_text.split("for")[-1].strip()
                webbrowser.open(f"https://www.google.com/search?q={search_term}")
                response = f"Searching Google for {search_term}."

            elif "open youtube" in user_text:
                webbrowser.open("https://www.youtube.com")
                response = "Opening YouTube."

            elif "open chrome" in user_text:
                os.system("start chrome")
                response = "Opening Chrome."

            elif "open notepad" in user_text:
                os.system("notepad")
                response = "Opening Notepad."

            elif "open calculator" in user_text:
                os.system("calc")
                response = "Opening Calculator."

            elif "play music" in user_text:
                os.startfile("C:\\Users\\vasud\\Music")
                response = "Playing your music folder."

            # ---------- Open Folder Commands ---------- #
            elif "open downloads" in user_text:
                os.startfile("C:\\Users\\vasud\\Downloads")
                response = "Opening your Downloads folder."

            elif "open documents" in user_text:
                os.startfile("C:\\Users\\vasud\\Documents")
                response = "Opening your Documents folder."

            elif "open desktop" in user_text:
                os.startfile("C:\\Users\\vasud\\Desktop")
                response = "Opening your Desktop."

            elif "open my projects folder" in user_text:
                os.startfile("C:\\Users\\vasud\\Projects")
                response = "Opening your Projects folder."

            # ---------- Close Folder Commands ---------- #
            elif "close downloads" in user_text or "close documents" in user_text or "close desktop" in user_text or "close projects folder" in user_text:
                os.system("taskkill /f /im explorer.exe")
                os.system("start explorer.exe")
                response = "Closing folder windows."

            # ---------- Close Apps ---------- #
            elif "close chrome" in user_text:
                os.system("taskkill /f /im chrome.exe")
                response = "Closing Chrome."

            elif "close notepad" in user_text:
                os.system("taskkill /f /im notepad.exe")
                response = "Closing Notepad."

            elif "close calculator" in user_text:
                os.system("taskkill /f /im calculator.exe")
                os.system("taskkill /f /im CalculatorApp.exe")
                response = "Closing Calculator."

            elif "close youtube" in user_text:
                os.system("taskkill /f /im chrome.exe")
                os.system("taskkill /f /im msedge.exe")
                response = "Trying to close YouTube."

            elif "close all apps" in user_text:
                os.system("taskkill /f /im chrome.exe")
                os.system("taskkill /f /im msedge.exe")
                os.system("taskkill /f /im notepad.exe")
                os.system("taskkill /f /im calculator.exe")
                os.system("taskkill /f /im CalculatorApp.exe")
                response = "All clear, Commander Dabi! Closing all apps."

            # ---------- System Control ---------- #
            elif "lock the system" in user_text:
                response = "Locking your system now."
                speak(response)
                ctypes.windll.user32.LockWorkStation()
                continue

            elif "shutdown" in user_text:
                response = "Shutting down your computer now."
                speak(response)
                os.system("shutdown /s /t 1")
                break

            elif "bye" in user_text or "exit" in user_text:
                response = f"Goodbye {memory['name']}. Going offline now."
                speak(response)
                break

            elif "self destruct" in user_text:
                response = "Nice try Dabi, but I’m not going anywhere."

            speak(response)

        except sr.WaitTimeoutError:
            speak("You were quiet. Can you say that again?")

        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")

        except sr.RequestError:
            speak("I'm having trouble connecting to the internet.")
