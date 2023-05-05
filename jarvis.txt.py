import pyttsx3
import pywhatkit
import wikipedia
import speech_recognition as sr
import webbrowser
import os
import pyautogui
import keyboard
import pyjokes
import datetime
from playsound import playsound
from googletrans import Translator

Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
# print(voices)
Assistant.setProperty('voices', voices[0].id)
Assistant.setProperty('rate', 180)


def Speak(audio):
    Assistant.say(audio)
    print(f":(Audio)")
    print("    ")
    Assistant.runAndWait()
    print("    ")


def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        command.pause_threshold = 1
        audio = command.listen(source)

        try:
            print("Recognizing....")
            query = command.recognize_google(audio, language="en-in")
            print(f"You said: {query}")

        except Exception as Error:
            return "None"

        return query.lower()


Speak("Welcome back sir!")

# hour = datetime.datetime.now().hour
# if hour>=6 and hour<=12:
#     Speak("Good morning sir")
# elif hour>=12 and hour<=18:
#     Speak("Good Afternoon sir")
# elif hour>=18 and hour<=24:  
#     Speak("Good Evening sir")
# else:
#    Speak("Good Night sir")

# Speak(" What can i do for you  Sir!.")

query = takecommand()


def TaskExe():

    while True:

        query = takecommand()

       

        def time():
            time = datetime.datetime.now().strftime("%H:%M:%S")
            Speak(time)
            print(time)
        
        def date():
            day = int(datetime.datetime.now().day)
            month = int(datetime.datetime.now().month)
            year = int(datetime.datetime.now().year)
            Speak("The current date is")
            print(day, month, year)
            Speak(day)
            Speak(month)
            Speak(year)

        def music():
            Speak("Tell me the name of the song")
            musicname = takecommand()

            if 'Khair' in musicname:
                os.startfile('D:\\music\\Khair.mp3')
            else:
                pywhatkit.playonyt(musicname)
                Speak("Your song has been started, enjoy sir!")

        def Whatsapp():
            Speak("Tell me the name of the person")
            name = takecommand()

            if 'Himanshu' in query:
                Speak("Tell me the message")
                msg = takecommand()
                Speak("Tell me the time ,sir!")
                Speak("Time in Hours!")
                hour = int(takecommand())
                Speak("Time in minutes!")
                min = int(takecommand())
                pywhatkit.sendwhatmsg("+918840393268", msg, hour, min)
                Speak("ok sir! , Sending the message !")

            elif 'abhishek' in query:
                Speak("Tell me the message")
                msg = takecommand()
                Speak("Tell me the time ,sir!")
                Speak("Time in Hours!")
                hour = int(takecommand())
                Speak("Time in minutes!")
                min = int(takecommand())
                pywhatkit.sendwhatmsg("+917309851526", msg, hour, min)
                Speak("ok sir! , Sending the message !")

            else:
                Speak("Tell me the phone number!")
                phone = int(takecommand())
                ph = '+91'+phone
                Speak("Tell me the message")
                msg = takecommand()
                Speak("Tell me the time ,sir!")
                Speak("Time in Hours!")
                hour = int(takecommand())
                Speak("Time in minutes!")
                min = int(takecommand())
                pywhatkit.sendwhatmsg("+918840393268", msg, hour, min)
                Speak("ok sir! , Sending the message !")

        def OpenApps():
            Speak("ok sir!, Wait a second!")

            if 'code' in query:
                os.system('"C:\\Users\\SAHGAL~PC\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"')

            elif 'Chrome' in query:
                os.system("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe %s")
            

            elif 'OBS studio' in query:
                os.system('"C:\\Program Files\\obs-studio\\bin\\64bit\\obs64.exe"')

            elif 'whatsapp ' in query:
                webbrowser.open('https://web.whatsapp.com/')

            elif 'youtube' in query:
                webbrowser.open('https://www.youtube.com/')

            elif 'instagram' in query:
                webbrowser.open('https://www.instagram.com/')

            elif 'maps' in query:
                webbrowser.open('https://www.google.co.in/maps?hl=en&tab=rl')

            elif 'Amazon' in query:
                webbrowser.open('https://www.amazon.in/?&ext_vrnc=hi&tag=googhydrabk1-21&ref=pd_sl_g50zekzm1_e&adgrpid=74238127911&hvpone=&hvptwo=&hvadid=610644609009&hvpos=&hvnetw=g&hvrand=3206115187961995436&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1007824&hvtargid=kwd-29089120&hydadcr=5496_2359482&gclid=EAIaIQobChMIh6z2qNSj_QIVxZNmAh0nnQhBEAAYASAAEgLQv_D_BwE')

            elif 'facebook' in query:
                webbrowser.open('https://www.facebook.com/')

            elif 'email' in query:
                webbrowser.open('https://mail.google.com/mail/u/0/#inbox')

            Speak("The app has been opened sir!")

        def closeApps():
            Speak("Ok sir! , Wait a second!")

            if 'youtube' in query:
                os.system("TASKKILL /F /im chrome.exe")

            elif 'chrome' in query:
                os.system("TASKKILL /F /im chrome.exe")

            elif 'vs code' in query:
                os.system("TASKKILL /F /im Code.exe")

            elif 'obs studio' in query:
                os.system("TASKKILL /F /im obs64.exe")

            elif 'facebook' in query:
                os.system("TASKKILL /F /im chrome.exe")

            elif 'instagram' in query:
                os.system("TASKKILL /F /im chrome.exe")

            elif 'maps' in query:
                os.system("TASKKILL /F /im chrome.exe")

            Speak("Ok Sir, App has been closed!")

        def YoutubeAuto():
            Speak("Tell me Sir ,  what do you want")
            comm = takecommand()

            if 'pause' in comm:
                keyboard.press('space bar')
            elif 'Fullscreen' in comm:
                keyboard.press('f')
            elif 'mute' in comm:
                keyboard.press('m')
            elif 'restart' in comm:
                keyboard.press('0')
            elif 'skip' in comm:
                keyboard.press('l')
            elif 'back' in comm:
                keyboard.press('j')
            elif 'Film mode' in comm:
                keyboard.press('t')
            Speak("Done , sir!")

        def chromeAuto():
            Speak("Chrome Automation start")
            command = takecommand()

            if 'close this tab' in command:
                keyboard.press_and_release('ctrl + w')
            elif 'open new tab' in command:
                keyboard.press_and_release('ctrl + n')
            elif 'open incognito mode ' in command:
                keyboard.press_and_release('ctrl + shift + w')
            elif 'Show history' in command:
                keyboard.press_and_release('ctrl + h')
            elif 'show downloads' in command:
                keyboard.press_and_release('ctrl + j')

        def screenshot():
            Speak("ok sir! , What should I Name that file ?/")
            path = takecommand()
            path1name = path + ".png"
            path1 = "D:\\pictures" + path1name
            kk = pyautogui.screenshot()
            kk.save(path1)
            os.startfile("D:\\pictures")
            Speak("Here is Your screenshot ")

        def TakeHindi():
            command = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening....")
                command.pause_threshold = 1
                audio = command.listen(source)

                try:
                    print("Recognizing....")
                    query = command.recognize_google(audio, language="hi")
                    print(f"You said: {query}")

                except Exception as Error:
                    return "None"

                return query.lower()

        def trans():
            Speak("Tell me the Line!")
            line = TakeHindi()
            translate = Translator()
            result = translate(line)
            Text = result.text
            Speak(Text)

        # def Dict():
        #     Speak("Dictionary Activated:")
        #     Speak("Sir, Tell me the word, i found for you in dictionary")
        #     problem = takecommand()

        #     if 'meaning' in problem:
        #         problem = problem.replace("What is the ","")
        #         problem = problem.replace("jarvis","")
        #         problem = problem.replace("of")
        #         result = Diction.meaning(problem)



        if 'hello Tom' in query:
            Speak("Hello Sir , I am Tom. ")
            Speak("Your personal AI Assistant")
            Speak("How may i help you")

        elif 'time' in query:
            time()

        elif 'date' in query:
            date()

        elif 'veer bahadur singh purvanchal university' in query:
            Speak("Veer Bahadur Singh Purvanchal University, formerly Purvanchal University, is a public state university based in Jaunpur, Uttar Pradesh, India. It was established in 1987 as a residential-cum-affiliating university. It is named after Shri Veer Bahadur Singh, the former chief minister of Uttar Pradesh")

        elif 'Some inforamtion about vbspu' in query:
            Speak("Veer Bahadur Singh Purvanchal University, formerly Purvanchal University, is a public state university based in Jaunpur, Uttar Pradesh, India. It was established in 1987 as a residential-cum-affiliating university. It is named after Shri Veer Bahadur Singh, the former chief minister of Uttar Pradesh")

        elif 'how are you Tom' in query:
            Speak("I am fine Sir")
            Speak("Tell me, What about you ?")

        elif 'You need a break' in query:
            Speak("ok Sir , You can call me any time.")
            break

        elif 'Kya hal hai' in query:
            Speak("Main thik hu , Sir")

        elif 'bye' in query:
            Speak("ok sir, Bye!")
            Speak("Have a good day. sir!")
            break

        elif 'main Achcha hun' in query:
            Speak("main bhi thik hu , sir")

        elif 'youtube search' in query:

            Speak("ok Sir, This is what i foun for your search!")
            query = query.replace("Tom", "")
            query = query.replace("youtube search", "")
            web = 'https://www.youtube.com/results?search_query=' + query
            pywhatkit.search(web)
            Speak("Done , Sir")

        elif 'google search' in query:
            Speak("This is what i found for your search")
            query = query.replace("Tom", "")
            query = query.replace("google search", "")
            pywhatkit.search(query)
            Speak("Done sir!")

        elif 'website' in query:
            Speak("ok Sir, Openning...")
            query = query.replace("Tom", "")
            query = query.replace("website", "")
            query = query.replace(" ", " ")
            web1 = query.replace("open", "")
            web2 = 'https://www.'+web1+'.com'
            webbrowser.open(web2)
            Speak("Open this website!")

        elif 'launch' in query:
            Speak("Tell me the name of the website")
            name = takecommand()
            web = 'https://www.'+name+'.com'
            webbrowser.open(web)
            Speak("Done Sir!")

        elif 'music' in query:
            music()

        elif 'wikipedia' in query:
            Speak("Searching wikipedia ")
            query = query.replace("Tom", "")
            query = query.replace("wikipedia", "")
            wiki = wikipedia.summary(query, 2)
            Speak(f"According to wikipedia : {wiki}")

        elif ' Whatsapp message' in query:
            Whatsapp()

        elif 'screenshot' in query:
            screenshot()

        elif 'open Chrome' in query:
            OpenApps()

        elif 'open facebook' in query:
            OpenApps()

        elif 'open email' in query:
            OpenApps()

        elif 'open youtube' in query:
            OpenApps()

        elif 'open whatsapp' in query:
            OpenApps()

        elif 'open instagram' in query:
            OpenApps()

        elif 'open OBS studio' in query:
            OpenApps()

        elif 'open maps' in query:
            OpenApps()

        elif 'open Amazon' in query:
            OpenApps()

        elif 'close facebook' in query:
            closeApps()

        elif 'close youtube' in query:
            closeApps()

        elif 'close chrome' in query:
            closeApps()

        elif 'close obs studio' in query:
            closeApps()

        elif 'close instagram' in query:
            closeApps()

        elif 'close maps' in query:
            closeApps()

        elif 'pause' in query:
            keyboard.press('space bar')
        elif 'full screen' in query:
            keyboard.press('f')
        elif 'mute' in query:
            keyboard.press('m')
        elif 'restart' in query:
            keyboard.press('0')
        elif 'skip' in query:
            keyboard.press('l')
        elif 'back' in query:
            keyboard.press('j')
        elif 'film mode' in query:
            keyboard.press('t')

        elif 'youtube tool' in query:
            YoutubeAuto()

        elif 'close this tab' in query:
            keyboard.press_and_release('ctrl + w')
        elif 'open new tab' in query:
            keyboard.press_and_release('ctrl + w')
        elif 'open Incognito mode ' in query:
            keyboard.press_and_release('ctrl + shift + w')
        elif 'show history' in query:
            keyboard.press_and_release('ctrl + h')
        elif 'show downloads' in query:
            keyboard.press_and_release('ctrl + j')

        elif 'chrome Automation' in query:
            chromeAuto()

        elif 'tell me a joke' in query:
            get = pyjokes.get_joke()
            Speak(get)

        elif 'repeat my words' in query:
            Speak("speak the words , Sir!")
            jj = takecommand()
            Speak(f"You said : {jj}")

        elif 'show my location' in query:
            webbrowser.open('https://www.google.com/maps/dir/Jaunpur,+Uttar+Pradesh/Jaunpur+%E0%A4%9C%E0%A5%8C%E0%A4%A8%E0%A4%AA%E0%A5%81%E0%A4%B0/@24.8096559,82.2456274,8.1z/data=!4m13!4m12!1m5!1m1!1s0x39903a2c93994715:0xf9a9f10dc97322!2m2!1d82.6837033!2d25.7464145!1m5!1m1!1s0x39903a2c93994715:0xf9a9f10dc97322!2m2!1d82.6837033!2d25.7464145')

        elif 'open Amazon' in query:
            OpenApps()

        elif 'alarm' in query:
            Speak("Enter the time. Sir!")
            time = input(": Enter the time")

            while True:
                time_Ac = datetime.datetime.now()
                now = time_Ac.strftime("%H:%M:%S")

                if now == time:
                    Speak("Time to wake up Sir!")
                    playsound('D:\\projects\\alarm_r.mp3')
                    Speak("Alarm closed ! ")

                elif now > time:
                    break

        elif 'translator' in query:
            trans()


takecommand()
TaskExe()
