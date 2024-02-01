from Head.Ear import *
from Function.check_online_ofline import is_online
from friday.Fspeak import fspeak
from Function.random_advice import get_random_advice
from Automations.command import cmd
from Function.battery import *
import threading
import random
import time
from Function.joke import *

def advice():
    while True:
        x = [600, 550, 580, 400, 3000, 800, 700, 8200 ,8000, 50 ,568]
        x = random.choice(x)
        time.sleep(x)
        speak("I have some suggestion for you, sir")
        text = listen().lower()
        if "yes tell me" in text or "yes" in text:
            advice = get_random_advice()
            speak(advice)
        else:
            speak("no problem, I think you need some advice, so I'll give you one.")

def jokes():
    while True:

        x = [600, 550, 580, 400, 3000, 800, 700, 8200 ,8000, 50 ,568]
        x = random.choice(x)
        time.sleep(x)
        speak("I have some joke for you, sir")
        text = listen().lower()
        if "yes tell me" in text or "yes" in text:
            advice = get_random_joke()
            speak(advice)
        else:
            speak("no problem sir, I just want to include some entertainment in your day ")

def jarvis():
    t1 = threading.Thread(target=cmd)
    t2 = threading.Thread(target=advice)
    t3 = threading.Thread(target=battery_alert)
    t4 = threading.Thread(target=check_plugin_status)
    t5 = threading.Thread(target=jokes)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t1.join()
    t2.join()
    t4.join()
    t5.join()

def check_jarvis():
    if is_online():
        jarvis()
    else:
        x = random.choice(ofline_dlg)
        fspeak(x)

def main():
    print("say-- wakeup jarvis")
    while True:
        text = hearing().lower()
        if "jarvis" in text or "jar" in text or "vis" in text or "arvis" in text or "wake up" in text or "wakeup" in text or "wakeup jarvis" in text or "wake up jarvis" in text or "wake up jar" in text :
            check_jarvis()
            break
        else:
            pass

if __name__ == "__main__":
    main()
