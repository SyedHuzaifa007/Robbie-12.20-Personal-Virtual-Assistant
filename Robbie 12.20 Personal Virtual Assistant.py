# Importing Modules
import pyttsx3
import os
import psutil
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import ctypes
import wolframalpha
import winshell
import datetime
import speech_recognition as sr
import random
import platform
import vlc
import time
import subprocess
import wikipedia
import webbrowser
import requests
import smtplib
import calendar
# Setting Voice Engine

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
engine.getProperty('rate')
engine.setProperty('rate', 185)
# print(voices[1].id)



# Making speak function


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Making wishMe function


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir")
    elif hour >= 12 and hour < 16:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")
    speak("I am robbie 12.20. Your personal virtual assistant. How can i help you......")


# Making takeCommand function


def takeCommand():
    '''This Function will take the input from the user's microphone and will return the string output.'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I AM LISTENING.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("RECOGNIZING.....")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")
    except Exception as e:
        print("I Was Unable to Recognize\nSay that again Please.....")
        return "None"
    return query



if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

# Logics for executing tasks based on the query

        #Questioning Assistant

        if 'who are you' in query or 'ap kaun ho' in query or 'what is your name' in query:
            responses0 = ["I am robbie 12.20 virtual assistant. I can handle most of your work so that you can feel free.", "I am a humanoid robot. my name is robbie 12.20. I can handle most of your general tasks","I am robbie 12.20 virtual assistant that is created to make your work easy"]
            a = random.choice(responses0)
            speak(a)
            print(a)

        elif 'what can you do for me' in query or 'tum mere liye kya kar sakte ho' in query or 'tum kya kar sakte ho' in query or 'tum kya kar sakti ho' in query or 'tum mere liye kya kar sakti ho' in query:
            responses3 = ["I can handle very much of your work. You'll feel relaxed watching me working", "I can be your personal assistant that can handle much of your work"]
            d = random.choice(responses3)
            speak(d)
            print(d)


        elif 'who has created you' in query or 'who is your father' in query or 'who is your love' in query or 'who made you' in query or 'who created you' in query or 'who has made you' in query or 'who is your creater' in query or 'who is your dad' in query:
            responses5 = ["Mr.Hozaifa has created me, He is my father, He loves me more than any other person in the world"]
            l = random.choice(responses5)
            speak(l)
            print(l)

        elif 'who am i' in query or 'main kaun hun' in query or 'who i am' in query or 'acha batao kai main kaun hun' in query or 'kia tum bata sakte ho kai main kaun hun' in query or 'who I am' in query:
            responses = ['If you are talking than obviously you are a human.']
            speak(responses)
            print(responses)


        elif 'where do you live' in query or 'aap kahan rehte ho' in query or 'aap kahan rehti ho' in query or 'where you live' in query or 'where is your home' in query or 'apka ghar kahan hai' in query or 'aap ka house kahan hai' in query or 'where is your house' in query:
            responses9 = ['I live on the internet', 'I live in your heart', 'I live with my father']
            r = (random.choice(responses9))
            speak(r)
            print(r)

        elif 'what is your date of birth' in query or 'apki date of birth kya hai' in query or 'tumhari date of birth kya hai' in query or 'date of birth' in query or 'dob' in query:
            g = 'I am just a newborn baby but i am very intelligent'
            speak(g)
            print(g)

        elif 'kya kar rahi ho' in query or 'what are you doing' in query or 'tum kya kar rahi ho' in query or 'kya kar rahe ho tum' in query:
            responses12 = ['I am just waiting for your another task', 'I was sleeping', 'I was taking bath', 'I was playing video game', 'I was cooking food for you']
            m = random.choice(responses12)
            speak(m)
            print(m)

        elif 'may you be happy always' in query or 'khush raho tum hamesha' in query or 'may you stay happy always' in query or 'i pray that' in query or 'meri dua hai k' in query:
            responses13 = ['Thanks Dear, May you also be forever', 'Thanks Dear, I also pray the same for you', 'Thanks Dear, May Allah fulfill your pray']
            n = random.choice(responses13)
            speak(n)
            print(n)

        elif 'are you an artificial intelligence' in query or 'are you an ai' in query or 'kya aap aik artificial intelligence ho' in query or 'kya tum artificial intelligence ho' in query or 'kya tum aik ai ho' in query or 'kya tum aik ai ho' in query:
           a5 = "what ever you are seeing or watching is the only verge of Artificial Intelligence. Artificial Intelligence is going to  completely change the world in some upcoming years"
           speak(a5)
           print(a5)

        elif 'hi dear' in query or 'hello dear' in query or "what's up" in query or 'assalam o alaikum' in query or 'hi' in query or 'hello' in query:
            responses14 = ['hello sir, how are you', "hi sir, what's up"]
            i = random.choice(responses14)
            speak(i)
            print(i)

        elif 'how are you' in query or 'how about you' in query or 'are you fine' in query or 'are you good' in query or 'how is you' in query or 'tum kese ho' in query or 'tum kesi ho' in query or 'tumhara kia haal hai' in query or 'tum kese ho' in query:
            responses15 = ['I am fine, how are you sir!', 'I am hale and hearty, how are you sir!', 'I am good, what about you sir']
            j = random.choice(responses15)
            speak(j)
            print(j)

        elif 'i am fine' in query or 'i am good' in query or 'i am also fine' in query or 'i am also good' in query or 'main bhi theek hun' in query or 'main theek hun' in query:
            responses16 = ['I am glad to hear that Sir', 'I am happy that you are enjoying your life Sir', 'that makes me happy Sir']
            k = random.choice(responses16)
            speak(k)
            print(k)

        elif 'what is your name' in query or 'ap ka naam kya hai' in query or 'name' in query:
            response17 = ['My name is robbie 12.20', 'i am robbie 12.20', 'dad gave me the name robbie 12.20']
            r = random.choice(response17)
            speak(r)
            print(r)

        elif 'what do you say about this world' in query or 'tumhara is duniya ke bare main kya khayal hai' in query:
            responses18 = ['According to my vision this world is going to end very soon']
            q = random.choice(responses18)
            speak(q)
            print(q)

        elif 'good girl' in query or 'good boy' in query:
            responses19 = ["Thanks sir, you are great", 'I like that my dear', 'Great pleasure to do your work sir']
            p = random.choice(responses19)
            speak(p)
            print(p)

        elif "sorry" in query:
            a6 = "No Problem, Sir"
            speak(a6)
            print(a6)

        elif 'good' in query or 'good work' in query or 'shabash' in query or 'good ho gaya' in query:
            responses20 = ['Thanks for your feed back sir, Please give me another task','Thanks sir!, i am glad to hear that', 'Thanks sir, i enjoyed a lot to did your work']
            l = random.choice(responses20)
            speak(l)
            print(l)

        elif 'hey robbie' in query or 'robbie' in query or 'hai robbie' in query or 'hey robbie 12.20' in query or 'hi robbie 12' in query or 'hello robbie' in query or 'robbie 12.20' in query or 'rabi' in query:
            responses21 = ['Hi Sir, How can i help you', "don't talk too much just give me my task", 'Sir, you just called out my name, how can i help you', 'hi sir, how are you']
            a1 = random.choice(responses21)
            speak(a1)
            print(a1)

        elif 'who is your mother' in query or 'who is your mom' in query or 'what is your mom name' in query or 'who is your mother' in query:
            responses22 = ['Python is my mother and i love her very much', 'My dad created me with the python, so python is my mother']
            a2 = random.choice(responses22)
            speak(a2)
            print(a2)

        elif 'what is love' in query or 'pyaar kiya hai' in query or 'pyaar kesa hota hai' in query or 'what you know about love' in query or 'pyar kiya hai' in query or 'pyar kesa hota hai' in query:
            responses4 = ["Love is the 7th sense that destroy a human",
                          "Love is a magic, when you are in love you feel like most luckiest person in the world"]
            e = random.choice(responses4)
            speak(e)
            print(e)


        elif 'i love you' in query or 'i love you too' in query or 'main aap se pyaar karta hun' in query or 'mujhe aap se pyaar ho gaya hai' in query or 'i like you' in query or 'i think i love you' in query or 'mujhe tum se pyaar ho gya hai' in query or 'main tum se pyaar karta hun' in query or 'main tum se pyaar karti hun' in query:
            responses8 = ['I love you too, My dear.....',
                          'If you love me then i bet that you are mad. Just kidding i want to say that i love you too',
                          'I am just a robot but i love you too']
            q = random.choice(responses8)
            speak(q)
            print(q)

        elif 'will you be my girlfriend' in query or 'will you be my boyfriend' in query or 'kya aap meri girfriend bano gi' in query or 'kya aap mere boyfriend bano ge' in query or 'kya tum meri girlfriend bano gi' in query or 'will you be my gf' in query or 'will you be my bf' in query or 'kya tum mere boyfriend bano ge' in query or 'will you marry me' in query or 'kya tum mujh se shahdi karo gi' in query:
            responses10 = ["Yes, of course i don't have any friend except my father",
                           "Yeah, i can but you have to trust me"]
            p = random.choice(responses10)
            speak(p)
            print(p)


# Web Browser Operations

        # Finding Location on Maps
        elif "where is" in query:
            try:
                query = query.replace("where is", "")
                location = query
                speak("I am locating")
                speak(location)
                webbrowser.open("https://www.google.nl / maps / place/" + location + "")
            except Exception as e:
                print(e)
                location = query
                speak(f"Sorry Sir, I was unable to locate {location}......")


        # Searching on Google

        elif 'search on google' in query or 'google per search karo' in query or 'google search karna' in query or 'google search karo' in query or 'do a google search' in query:
            speak("what should i search on google")
            usersearch = takeCommand()
            speak("Wait a minute. I am searching it for you.....")
            webbrowser.open(f"https://www.google.com/search?sxsrf=ALeKk01xr3amEbAWCIpLjdyLVjFM2xZfuA%3A1606485069232&source=hp&ei=TQTBX4ydC-eYjLsP5fWn4AE&q={usersearch}&oq=123&gs_lcp=CgZwc3ktYWIQAzICCAAyCAgAELEDEIMBMggIABCxAxCDATIICAAQsQMQgwEyAggAMgUIABCxAzICCAAyAggAMgIIADIICAAQsQMQgwE6BwgjEOoCECdQoxJYyBlg5BtoAXAAeACAAZgCiAGjBJIBAzItMpgBAKABAaoBB2d3cy13aXqwAQQ&sclient=psy-ab&ved=0ahUKEwjM94qf76LtAhVnDGMBHeX6CRwQ4dUDCAc&uact=5")
            speak("I have searched it. Enjoy dear..... ")

            # Reading Daily News

        elif "what is the latest news" in query or "what is happening in the world" in query or "aaj ki khabren batao" in query or "news" in query or 'aaj ki kya khabar hai' in query:
            speak("I am gathering top news from the world. Please wait.....")
            try:
                news_url = "https://news.google.com/news/rss"
                Client = urlopen(news_url)
                xml_page = Client.read()
                Client.close()
                soup_page = soup(xml_page, "xml")
                news_list = soup_page.findAll("item")
                engine.setProperty("rate", 140)
                speak("Here are some of the top news of the planet")
                for news in news_list[:10]:
                    print(news.title.text)
                    speak(news.title.text)
            except Exception as e:
                print(e)

        # Searching Wikipedia

        elif 'tell me about' in query or 'wikipedia' in query:
            search = query.split()
            try:
                query = query.replace("search", "")
                results = wikipedia.summary(query, sentences=3)
                engine.setProperty("rate", 150)
                speak("According to my knowledge.....")
                print(results)
                speak(results)
            except Exception as e:
                print(e)


        # Opening a Website in browser

        elif 'website' in query or "website kholo" in query or "website kholna" in query or "ek website kholo" in query or "yaar aik website kholna" in query or 'aik website khol kar do' in query:
            speak("which web site i should open")
            website = takeCommand()
            final_website = website.replace(" ", "")
            reg_ex = webbrowser.open('https://www.' + final_website)
            speak("I opened the website for you successfully. Enjoy dear.....")

        # Opening Youtube

        if 'youtube kholo' in query:
            webbrowser.open("www.youtube.com")
            speak("Opening Youtube")
        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")
            speak("Opening Youtube")
        elif 'youtube kholo yaar' in query:
            webbrowser.open("www.youtube.com")
            speak("Opening Google")
        elif 'youtube khol yaar' in query:
            webbrowser.open("www.youtube.com")
            speak("Opening Youtube")
        elif 'youtube khol do' in query:
            webbrowser.open("www.youtube.com")
            speak("Opening Youtube")

         # Opening Google

        elif 'google kholo' in query:
            webbrowser.open("www.google.com")
            speak("Opening Google")
        elif 'open google' in query:
            webbrowser.open('www.google.com')
            speak("Opening Google")
        elif 'google kholo yaar' in query:
            webbrowser.open('www.google.com')
            speak("Opening Google")
        elif 'google khol do' in query:
            webbrowser.open('www.google.com')
            speak("Opening Google")
        elif 'google khol yaar' in query:
            webbrowser.open('www.google.com')
            speak("Opening Google")

        # Opening Stack Overflow

        elif 'stackoverflow' in query:
            webbrowser.open("www.stackoverflow.com")
            speak("Opening Stack Overflow")
        elif 'open stack overflow' in query:
            webbrowser.open("www.stackoverflow.com")
            speak("Opening Stack Overflow")
        elif 'stack overflow kholo' in query:
            webbrowser.open("www.stackoverflow.com")
            speak("Opening Stack Overflow")
        elif 'stack overflow khol yaar' in query:
            webbrowser.open("www.stackoverflow.com")
            speak("Opening Stack Overflow")
        elif 'stack overflow khol do' in query:
            webbrowser.open("www.stackoverflow.com")
            speak("Opening Stack Overflow")

        # Opening Instagram

        elif 'instagram' in query:
            webbrowser.open("www.instagram.com")
            speak("Opening Instagram")
        elif 'open instagram' in query:
            webbrowser.open("www.instagram.com")
            speak("Opening Instagram")
        elif 'instagram kholo' in query:
            webbrowser.open("www.instagram.com")
            speak("Opening Instagram")
        elif 'instagram khol do' in query:
            webbrowser.open("www.instagram.com")
            speak("Opening Instagram")
        elif 'instagram kholo yaar' in query:
            webbrowser.open("www.instagram.com")
            speak("Opening Instagram")

            # Opening Twitter

        elif 'twitter' in query:
            webbrowser.open("www.instagram.com")
            speak("Opening Twitter")
        elif 'open twitter' in query:
            webbrowser.open("www.twitter.com")
            speak("Opening Twitter")
        elif 'twitter kholo' in query:
            webbrowser.open("www.twitter.com")
            speak("Opening Twitter")
        elif 'twitter khol do' in query:
            webbrowser.open("www.twitter.com")
            speak("Opening Instagram")
        elif 'twitter kholo yaar' in query:
            webbrowser.open("www.twitter.com")
            speak("Opening Twitter")


        # Searching on Youtube
        elif 'search on youtube' in query or 'youtube par search karo' in query or 'youtube per search karna' in query or 'yaar youtube par search karo' in query or 'youtube pe search karo' in query:
            speak("what should i search")
            tosearch = takeCommand()
            try:
                speak("Wait a minute. I am searching it for you")
                webbrowser.open(f"https://www.youtube.com/results?search_query={tosearch}")
                speak("I searched it. Enjoy dear.")
            except Exception as e:
                speak("Sorry Sir i was unable to search it")
                print(e)


        # Sending Email to a specific person

        elif 'send email' in query:
            import smtplib
            from email.mime.text import MIMEText
            from email.mime.image import MIMEImage
            from email.mime.multipart import MIMEMultipart

            try:
                port = 2525
                smtp_server = "smtp.mailtrap.io"
                login = "Paste Login Here"  # paste your login generated by Mailtrap
                password = "Paste Password Here"  # paste your password generated by Mailtrap
                speak("Sir, what is the subject")
                subject = takeCommand()
                sender_email = "Sender-Email"
                receiver_email = "Reciever-Email"
                message = MIMEMultipart("alternative")
                message["Subject"] = f"{subject}"
                message["From"] = sender_email
                message["To"] = receiver_email
                speak("What should i say.....")
                # write the HTML part
                html = takeCommand()

                part = MIMEText(html, "html")
                message.attach(part)
                speak("Sir, Do you want to attach a file?")
                b = takeCommand()
                if "yes" in b or "yeah" in b or "han kar do" in b or "han karni hai" in b or "yes of course" in b:
                    speak("Ok sir, i am attaching the file")
                    # We assume that the image file is in the same directory that you run your Python script from
                    fp = open('Path of the File', 'rb')
                    image = MIMEImage(fp.read())
                    fp.close()

                    # Specify the  ID according to the img src in the HTML part
                    image.add_header('Content-ID', '<Mailtrapimage>')
                    message.attach(image)
                elif 'no' in b or 'nahi karni' in b or "no i don't want to attach" in b:
                    speak("ok sir, i am sending the email")
                    # send your email
                    with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
                        server.login(login, password)
                        server.sendmail(
                            sender_email, receiver_email, message.as_string()
                        )
                    speak('Sir, i have sent the email successfully. You can check it later.....')
                    print("Email Sent Successfully")
            except Exception as e:
                speak("Sorry Sir, i was unable to send the email")
                print("Email Sending Failed")
                print(e)

        # Opening Microsoft Excel
        elif 'open excel' in query or 'open microsoft excel' in query or 'excel khol kar do' in query or 'excel kholo' in query or 'microsoft excel kholna' in query or 'excel kholna' in query:
            speak("Opening Microsoft Excel..... ")
            webbrowser.open("https://www.office.com/launch/excel?auth=1")

            # if you want to open Microsoft Excel App located in your computer than you can use os module
            # Syntax:
            # os.startfile("Path of the app located in your computer")

        # Opening Microsoft Word
        elif 'open word' in query or 'open microsoft word' in query or 'word khol kar do' in query or 'word kholo' in query or 'microsoft word kholna' in query or 'word kholna' in query:
            speak("Opening Microsoft Word..... ")
            webbrowser.open("https://www.office.com/launch/word?ui=en-US&rs=US&auth=1")

            # if you want to open Microsoft Word App located in your computer than you can use os module
            # Syntax:
            # os.startfile("Path of the app located in your computer")

        # Opening Microsoft Powerpoint
        elif 'open powerpoint' in query or 'open microsoft powerpoint' in query or 'powerpoint khol kar do' in query or 'powerpoint kholo' in query or 'microsoft powerpoint kholna' in query or 'powerpoint kholna' in query:
            speak("Opening Microsoft Powerpoint..... ")
            webbrowser.open("https://www.office.com/launch/powerpoint?auth=1")

        # if you want to open Microsoft Powerpoint App located in your computer than you can use os module
        # Syntax:
        # os.startfile("Path of the app located in your computer")

        # Opening Microsoft OneNote
        elif 'open one note' in query or 'open microsoft one note' in query or 'one note khol kar do' in query or 'one note kholo' in query or 'microsoft one note kholna' in query or 'one note kholna' in query:
            speak("Opening Microsoft One Note..... ")
            webbrowser.open("Paste your one note link here")

            # if you want to open Microsoft OneNote App located in your computer than you can use os module
            # Syntax:
            # os.startfile("Path of the app located in your computer")

        # Opening One Drive Cloud
        elif 'open cloud' in query or 'open microsoft one drive' in query or 'cloud khol kar do' in query or 'cloud kholo' in query or 'microsoft one drive kholna' in query or 'cloud kholna' in query or 'open my cloud' in query or 'mera cloud kholo' in query:
            speak("Opening Your Cloud..... ")
            webbrowser.open("Paste Your Onedrive Link Here")

        # if you want to open Microsoft Excel App located in your computer than you can use os module
        # Syntax:
        # os.startfile("Path of the app located in your computer")

        # Opening Gmail
        elif 'open gmail' in query or 'open email' in query or 'gmail kholo' in query or 'gmail kholna' in query:
            speak("Opening Gmail of account number one")
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("https://mail.google.com/mail/u/0/#inbox")
        # Opening Windows Mail
        elif 'open windows mail' in query or 'open windows email' in query or 'windows mail kholo' in query or 'mail khol kar do' in query or 'windows mail kholna' in query or 'open mail of windows' in query:
            speak("Opening Windows Mail")
            webbrowser.open("https://outlook.live.com/mail/0/inbox")
        # Opening Google maps
        elif 'open maps' in query or 'open goole maps' in query or 'google maps kholo' in query or 'google maps khol kar do' in query or 'maps kholna' in query or 'maps kholo' in query or 'maps khol kar do' in query:
            speak("Opening Google Maps")
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("Paste Google Maps Link Here")
        # Opening Google Duo
        elif 'open duo' in query or 'open goole duo' in query or 'google duo kholo' in query or 'google duo khol kar do' in query or 'duo kholna' in query or 'duo kholo' in query or 'duo khol kar do' in query or 'security camera kholo' in query:
            speak("Opening Google Duo")
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("Paste Google Duo Link Here")
        # Opening GitHub
        elif 'open github' in query or 'github kholo' in query or 'github khol kar do' in query or 'github kholna' in query:
            speak("Opening GitHub")
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("Paste your GithHub Link Here")
        # Opening BootStrap
        elif 'open bootstrap' in query or 'bootstrap kholo' in query or 'bootstrap khol kar do' in query or 'bootstrap kholna' in query:
            speak("Opening Bootstrap")
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("https://getbootstrap.com/docs/4.2/getting-started/introduction/")



        # Telling Weather for any city

        elif 'tell weather for a city' in query or 'ek shehar ka mausam batao' in query or 'ek shehar ka mausam batana' in query or 'i want to ask weather for a city' in query or 'ek city ki weather batana' in query or "ek city ka weather batao" in query or 'ek shehar ka mausam ka hal batao' in query or 'ek shehar ka mausam ka hal batana' in query:

            import requests

            # Get Your API Key from www.openweathermap.org
            api_key = "Paste Your API Key Here"
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            speak("Sir, For which city i should tell weather")
            city_name = takeCommand()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                temp_in_celcius = int(current_temperature) - 273.15
                current_pressure = y["pressure"]
                pressure_in_mb = int(current_pressure) / 100
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]

                print(f"__________________{city_name.upper()}__________________")
                print(f"Current temperature in {city_name.upper()} is {str(round(temp_in_celcius))} degrees celsius.")
                print(f"Atmospheric pressure is {str(current_pressure)} millibars.")
                print(f"Humidity in the air is {str(current_humidiy)} percent.")
                print(f"Overall weather is {str(weather_description)}")

                engine.setProperty('rate', 160)

                speak(f"Current temperature in {city_name} is {str(round(temp_in_celcius))} degrees celsius.")
                speak(f"Atmospheric pressure is {str(current_pressure)} millibars.")
                speak(f"Humidity in the air is {str(current_humidiy)} percent.")
                speak(f"Overall weather is {str(weather_description)}.")
            else:
                speak("Sorry sir, I was unable to found the city")

            # Telling Weather for current city

        elif 'weather batao' in query or 'Mausam' in query or 'weather kaisi hai' in query or 'mausam kaisa hai' in query or 'Mausam batao' in query or "tell me the weather" in query or 'mausam ka hal batao' in query or 'bahir ka mausam kaisa hai' in query or 'weather kaisa hai' in query or 'how is the weather' in query:

            # Get Your API Key from www.openweathermap.org
            api_key = "Paste Your API Key Here"
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            complete_url = base_url + "appid=" + api_key + "&q=" + "Lahore"
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                temp_in_celcius = int(current_temperature) - 273.15
                current_pressure = y["pressure"]
                pressure_in_mb = int(current_pressure) / 100
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]

                print(f"__________________Your_City_Name__________________")
                print(f"Current temperature in LAHORE is {str(round(temp_in_celcius))} degrees celsius.")
                print(f"Atmospheric pressure is {str(current_pressure)} millibars.")
                print(f"Humidity in the air is {str(current_humidiy)} percent.")
                print(f"Overall weather is {str(weather_description)}")

                engine.setProperty('rate', 160)

                speak(f"Current temperature in LAHORE is {str(round(temp_in_celcius))} degrees celsius.")
                speak(f"Atmospheric pressure is {str(current_pressure)} millibars.")
                speak(f"Humidity in the air is {str(current_humidiy)} percent.")
                speak(f"Overall weather is {str(weather_description)}.")
            else:
                speak("Sorry sir, I was unable to found the city")



            # Do I Need a Jacket

        elif 'do i need a jacket' in query or 'jacket ki jarurat hai ki nahin' in query or 'jacket chahie' in query or 'does there a need of jacket' in query:
            import requests
            import json

            # Get Your API Key from www.openweathermap.org
            api_key = "Paste Your API Key Here"
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            complete_url = base_url + "appid=" + api_key + "&q=" + "Lahore"
            response = requests.get(complete_url)
            x = response.json()
            # You can set the temperature here according to your requirement
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                temparature_outside = int(current_temperature) - 273.15
                engine.setProperty('rate', 170)
                if temparature_outside < 20:
                    speak(f"Sir, the temperature outside is {round(temparature_outside)} degrees celsius. It's cool outside. You should take your jacket with you")
                else:
                    speak(f"No Sir, the temperature outside is {round(temparature_outside)} degrees celsius. It's not cool outside. There is no need of jacket my dear")
            else:
                speak("I can not predict that it's upto you.....")

            # Telling a joke

        elif 'tell me a joke' in query or 'tell a joke'in query or 'koi joke sunao' in query or 'joke sunao' in query or 'latifa sunao' in query or 'koi latifa sunao' in query:
            res = requests.get('https://icanhazdadjoke.com/', headers = {"Accept":"application/json"})
            if res.status_code == requests.codes.ok:
                print(str(res.json()['joke']))
                engine.setProperty('rate', 160)
                speak(str(res.json()['joke']))
            else:
                speak("Sorry Sir, I ran out of jokes please come back later")




# Telling Time and Date

        # Time

        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%I%M%p")
            speak(f"Sir, The time is {strTime}")
        elif "what is the time" in query:
            strTime = datetime.datetime.now().strftime("%I%M%p")
            speak(f"Sir, The time is {strTime}")
        elif "what's the time" in query:
            strTime = datetime.datetime.now().strftime("%I%M%p")
            speak(f"Sir, The time is {strTime}")
        elif "time batao" in query:
            strTime = datetime.datetime.now().strftime("%I%M%p")
            speak(f"Sir, The time is {strTime}")
        elif "time kya hua h" in query:
            strTime = datetime.datetime.now().strftime("%I%M%p")
            speak(f"Sir, The time is {strTime}")
        elif "time batao yaar" in query:
            strTime = datetime.datetime.now().strftime("%I%M%p")
            speak(f"Sir, The time is {strTime}")
        elif "waqt batao" in query:
            strTime = datetime.datetime.now().strftime("%I%M%p")
            speak(f"Sir, The time is {strTime}")
        elif "waqt kya hua h" in query:
            strTime = datetime.datetime.now().strftime("%I%M%p")
            speak(f"Sir, The time is {strTime}")

        # Date

        elif "date" in query:
            date = datetime.date.today()
            speak(f"Sir, the date is {date}")
        elif "aaj date kya hai" in query:
            date = datetime.date.today()
            speak(f"Sir, the date is {date}")
        elif "what is the date today" in query:
            date = datetime.date.today()
            speak(f"Sir, the date is {date}")
        elif "what's the date" in query:
            date = datetime.date.today()
            speak(f"Sir, the date is {date}")
        elif "date batao" in query:
            date = datetime.date.today()
            speak(f"Sir, the date is {date}")
        elif "date kya hai" in query:
            date = datetime.date.today()
            speak(f"Sir, the date is {date}")
        elif "date kya hai aaj" in query:
            date = datetime.date.today()
            speak(f"Sir, the date is {date}")
        elif "date bata do" in query:
            date = datetime.date.today()
            speak(f"Sir, the date is {date}")
        elif "tarikh bata do" in query:
            date = datetime.date.today()
            speak(f"Sir, the date is {date}")
        elif "tarikh batao yaar" in query:
            date = datetime.date.today()
            speak(f"Sir, the date is {date}")
        elif "tarikh kya hai aaj" in query:
            date = datetime.date.today()
            speak(f"Sir, the date is {date}")
        elif "aj tarikh kya h" in query:
            date = datetime.date.today()
            speak(f"Sir, the date is {date}")

# System Operations

# Locking Window
        elif 'lock window' in query or 'lock kar do' in query or 'lock karo yaar' in query or 'lock kar yaar' in query or "lock" in query or 'lock my computer' in query:
            speak("Sir i am locking your device. Please wait......")
            ctypes.windll.user32.LockWorkStation()

# Shutting Down Computer
        elif "shut down my pc" in query or "turn off my computer" in query or "shut down my computer" in query or "band kar do yaar laptop" in query or "band kar do laptop ko" in query :
            speak("Sir i am turning off your computer please wait.....")
            subprocess.call('shutdown / p /f')

# Setting Computer on the sleep mode
        elif "set my computer to sleep mode" in query or "sleep mode par laga do" in query or "sleep mode laga do" in query or "sleep mode lagao" in query:
            speak("Sir i am setting your computer to sleep mode please wait......")
            os.system(r'rundll32.exe powrprof.dll,SetSuspendState Hibernate')

# Restarting Computer
        elif "restart my computer" in query or "restart karo laptop ko" in query or "restart karo yaar" in query or "restart kar do" in query:
            speak("Sir i am restarting your computer please wait.....")
            os.system("shutdown /r /t 1")

# Telling Battery Information
        elif 'how much battery is left' in  query or 'battery' in query or 'battery kitni hai' in query or 'battery kitni reh gayi hai' in query or 'battery kitni rehti hai' in query:
            battery = psutil.sensors_battery()
            plugged = battery.power_plugged
            percent = str(battery.percent)
            plugged = "Plugged In" if plugged else "Not Plugged In"
            print(percent+'% | '+plugged)
            engine.setProperty('rate', 170)
            speak(f"Sir, The battery is left {percent} percent behind and is {plugged}")



# Telling System Information
        elif "tell me my computer information" in query or "tell me my system information" in query or "tell system info" in query or 'system ki information batana' in query or 'system information batao' in query:
            mysystem = platform.uname()
            speak(f"Operating System is: {mysystem.system}")
            speak(f"The Computer Name is: {mysystem.node}")
            speak(f"Release is: {mysystem.release}")
            speak(f"Version is: {mysystem.version}")
            speak(f"Machine is: {mysystem.machine}")
            speak(f"Processor is: {mysystem.processor}")


        # Opening Programs

        # Printing a Calendar
        elif 'calendar' in query or 'calendar kholna' in query or "calender kholo" in query or 'calendar dikhao' in query or 'calendar dikhana' in query:
            mm = 11
            yy = 2020
            speak("Opening Calendar")
            print(calendar.month(yy, mm))


        # Playing Music

        elif 'music' in query:
            main_dir = "Paste here the path of your music directory"
            songs = os.listdir(main_dir)
            song = random.choice(songs)
            speak("Playing Music")
            os.startfile(os.path.join(main_dir, song))
        elif 'play music' in query:
            main_dir = "Paste here the path of your music directory"
            songs = os.listdir(main_dir)
            song = random.choice(songs)
            speak("Playing Music")
            os.startfile(os.path.join(main_dir, song))
        elif 'play me a song' in query:
            main_dir = "Paste here the path of your music directory"
            songs = os.listdir(main_dir)
            song = random.choice(songs)
            speak("Playing Music")
            os.startfile(os.path.join(main_dir, song))
        elif 'music lagao' in query:
            main_dir = "Paste here the path of your music directory"
            songs = os.listdir(main_dir)
            song = random.choice(songs)
            speak("Playing Music")
            os.startfile(os.path.join(main_dir, song))
        elif "gana lagao" in query:
            main_dir = "Paste here the path of your music directory"
            songs = os.listdir(main_dir)
            song = random.choice(songs)
            speak("Playing Music")
            os.startfile(os.path.join(main_dir, song))
        elif "gana lagao yaar" in query:
            main_dir = "Paste here the path of your music directory"
            songs = os.listdir(main_dir)
            song = random.choice(songs)
            speak("Playing Music")
            os.startfile(os.path.join(main_dir, song))
        elif "gana laga do" in query:
            main_dir = "Paste here the path of your music directory"
            songs = os.listdir(main_dir)
            song = random.choice(songs)
            speak("Playing Music")
            os.startfile(os.path.join(main_dir, song))
        elif "gana sunao yaar" in query:
            main_dir = "Paste here the path of your music directory"
            songs = os.listdir(main_dir)
            song = random.choice(songs)
            speak("Playing Music")
            T = os.startfile(os.path.join(main_dir, song))
        elif 'band kar do music ko' in query or 'stop playing music' in query or 'stop music' in query or 'music band karo' in query or 'stop playing song' in query or 'stop song' in query:
            main_dir = "Paste here the path of your music directory"
            songs = os.listdir(main_dir)
            song = random.choice(songs)
            T = os.startfile(os.path.join(main_dir, song))
            os.system(f"TASKKILL /F /IM {T}")

        # Opening Code
        elif 'open code' in query:
            # Paste your VS Code Path here in this format with double backslashes
            code_path = "C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)
            speak("Opening V S code, Happy Coding")
        elif 'open vs code' in query:
            # Paste your VS Code Path here in this format with double backslashes
            code_path = "C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)
            speak("Opening VS code, Happy Coding")
        elif 'vs code kholo' in query:
            # Paste your VS Code Path here in this format with double backslashes
            code_path = "C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)
            speak("Opening VS code, Happy Coding")
        elif 'vs code kholna' in query:
            # Paste your VS Code Path here in this format with double backslashes
            code_path = "C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)
            speak("Opening VS code, Happy Coding")
        elif 'vs code khol do' in query:
            # Paste your VS Code Path here in this format with double backslashes
            code_path = "C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)
            speak("Opening VS code, Happy Coding")
        elif 'vs code khol kar do' in query:
            # Paste your VS Code Path here in this format with double backslashes
            code_path = "C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)
            speak("Opening VS code, Happy Coding")
        elif 'vs code khol yaar' in query:
            # Paste your VS Code Path here in this format with double backslashes
            code_path = "C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)
            speak("Opening VS code, Happy Coding")
        elif 'close code' in query or 'close vs code' in query or 'code band kar do' in query or 'vs code band kar do' in query or 'band karo vs code ko' in query:
            speak("I am closing VS code, Sir.....")
            os.system("TASKKILL /F /IM Code.exe")

        # Opening Slack
        elif 'open slack' in query:
            # Paste your Slack Path here in this format with double backslashes
            slack_path = "C:\\Users\\Lenovo\\AppData\\Local\\slack\\slack.exe"
            os.startfile(slack_path)
            speak("Opening Slack, Please wait.....")
        elif 'slack kholo' in query:
            # Paste your Slack Path here in this format with double backslashes
            slack_path = "C:\\Users\\Lenovo\\AppData\\Local\\slack\\slack.exe"
            os.startfile(slack_path)
            speak("Opening Slack, Please wait.....")
        elif 'slack kholna' in query:
            # Paste your Slack Path here in this format with double backslashes
            slack_path = "C:\\Users\\Lenovo\\AppData\\Local\\slack\\slack.exe"
            os.startfile(slack_path)
            speak("Opening Slack, Please wait.....")
        elif 'slack kholna yaar' in query:
            # Paste your Slack Path here in this format with double backslashes
            slack_path = "C:\\Users\\Lenovo\\AppData\\Local\\slack\\slack.exe"
            os.startfile(slack_path)
            speak("Opening Slack, Please wait.....")
        elif 'slack khol do' in query:
            # Paste your Slack Path here in this format with double backslashes
            slack_path = "C:\\Users\\Lenovo\\AppData\\Local\\slack\\slack.exe"
            os.startfile(slack_path)
            speak("Opening Slack, Please wait.....")
        elif 'slack khol kar do' in query:
            # Paste your Slack Path here in this format with double backslashes
            slack_path = "C:\\Users\\Lenovo\\AppData\\Local\\slack\\slack.exe"
            os.startfile(slack_path)
            speak("Opening Slack, Please wait.....")
        elif 'slack khol yaar' in query:
            # Paste your Slack Path here in this format with double backslashes
            slack_path = "C:\\Users\\Lenovo\\AppData\\Local\\slack\\slack.exe"
            os.startfile(slack_path)
            speak("Opening Slack, Please wait.....")
        elif 'close slack' in query or 'close vs code' in query or 'slack band kar do' in query or 'slack band kar do' in query or 'band karo slack ko' in query:
            speak("I am closing Slack, Sir.....")
            os.system("TASKKILL /F /IM slack.exe")


        # Opening Notepad

        elif 'open notepad' in query or 'notepad kholo' in query or 'notepad kholna' in query or 'notepad khol do' in query or 'notepad khol yaar' in query:
            speak("Opening Notepad")
            os.startfile("Notepad.exe")
        elif 'close notepad' in query or 'notepad band karo' in query or 'notepad ko band kar do' in query or 'band kar do notepad ko' in query or 'band karo notepad ko' in query or 'band kar do yaar notepad' in query:
            speak("I am closing the notepad, Sir.....")
            os.system("TASKKILL /F /IM Notepad.exe")

        # Opening Pycharm

        elif 'open pycharm' in query:
            # Paste your PyCharm Path here in this format with double backslashes
            pycharm_path = 'C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.2.3\\bin\\pycharm64.exe'
            os.startfile(pycharm_path)
            speak('Opening py charm, Happy Coding')
        elif 'pycharm kholo' in query:
            # Paste your PyCharm Path here in this format with double backslashes
            pycharm_path = 'C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.2.3\\bin\\pycharm64.exe'
            os.startfile(pycharm_path)
            speak('Opening py charm, Happy Coding')
        elif 'pycharm khol do' in query:
            # Paste your PyCharm Path here in this format with double backslashes
            pycharm_path = 'C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.2.3\\bin\\pycharm64.exe'
            os.startfile(pycharm_path)
            speak('Opening py charm, Happy Coding')
        elif 'pycharm khol kar do' in query:
            # Paste your PyCharm Path here in this format with double backslashes
            pycharm_path = 'C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.2.3\\bin\\pycharm64.exe'
            os.startfile(pycharm_path)
            speak('Opening py charm, Happy Coding')
        elif 'pycharm kholna yaar' in query:
            # Paste your PyCharm Path here in this format with double backslashes
            pycharm_path = 'C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.2.3\\bin\\pycharm64.exe'
            os.startfile(pycharm_path)
            speak('Opening py charm, Happy Coding')
        elif 'pycharm khol' in query:
            # Paste your PyCharm Path here in this format with double backslashes
            pycharm_path = 'C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.2.3\\bin\\pycharm64.exe'
            os.startfile(pycharm_path)
            speak('Opening py charm, Happy Coding')
        elif 'pycharm kholo' in query:
            # Paste your PyCharm Path here in this format with double backslashes
            pycharm_path = 'C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.2.3\\bin\\pycharm64.exe'
            os.startfile(pycharm_path)
            speak('Opening py charm, Happy Coding')
        elif 'pycharm band karo' in query or 'close pycharm' in query or 'pycharm band kardo' in query or 'pycharm ko band kar do' in query or 'band karo pycharm ko' in query:
            speak("I am closing py charm, Sir......")
            os.system("TASKKILL /F /IM pycharm64.exe")

# Playing Movies with VLC Module
        elif 'play movie' in query or 'play a movie' in query or 'movie' in query or 'play me a movie' in query or 'movie lagao' in query or 'play film' in query or 'movie lagao yaar' in query or 'yaar movie lagao' in query:
            speak("Wait a minute sir, i am finding a movie for you")
            media_player = vlc.MediaPlayer()
            speak("I have found the movie for you. I am playing it, Enjoy sir")
            media = vlc.Media("Paste your movie path here")
            media_player.set_media(media)
            media_player.play()
            time.sleep(5662)


        # Writing a note

        elif "write a note" in query or 'note karo' in query or 'note likho' in query or 'ek note likho' in query or 'write note' in query or 'yaar ek note likho' in query or 'ek note to likhna yaar' in query:
            speak("Sir, what should i write.....")
            note = takeCommand()
            file = open('virtual_assistant.txt', 'a')
            speak("Sir, do you want me to include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm or 'han' in snfm or 'han likh do' in snfm or 'han likho' in snfm or 'han bilkul likhna hai' in snfm or 'likh do' in snfm or 'include' in snfm:
                strTime = datetime.datetime.now().strftime("%I%M%p")
                date1 = datetime.date.today()
                W = ["Ok sir, I have heard and memorized what you have said. I am writing it......", "Ok sir, Give me a while i am writing it what you have said....."]
                speak(random.choice(W))
                file.write(strTime)
                file.write(str(date1))
                file.write(" :- ")
                file.write(note)
            else:
                W = ["Ok sir, I have heard and memorized what you have said. I am writing it......",
                     "Ok sir, Give me a while i am writing it what you have said....."]
                speak(random.choice(W))
                file.write(note)

        elif "show note" in query or 'dikhao kya likha hai tumne' in query or 'show me the note' in query or 'kia likha hai tumne dikhana zara' in query or 'dikhao zara kia likha hai' in query or 'ab jo likha hai wo parh kar sunao' in query or 'show me what you have write' in query or 'show' in query:
            speak("I am showing you what i have wrote, Sir.....")
            file = open("virtual_assistant.txt", "r")
            print(file.read())
            speak(file.read(6))


        # Empty Recycle Bin

        elif 'empty the recycle bin' in query or 'recycle bin empty kar do' in query or 'recycle bin empty karo' in query or 'recycle bin khali karo' in query or 'recycle bin khali kar do' in query or 'recycle bin ko khali karo' in query or 'khali karo recycle bin ko' in query or 'recyclce bin' in query:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)
            speak("Sir, I emptied your recycle bin.....")

# Using Wolframalpha API to answer questions

        elif 'answer question' in query or 'i want to ask a question' in query or 'ek sawal ka jawab do' in query or 'ek sawal ka jawab dena' in query or 'ek sawal poochon' in query or 'acha main ek sawal poochna chahta hun' in query or 'main ek sawal poochon' in query or 'tumse ek sawal puchun' in query:
            try:
                speak("Sir, What do you want to ask.....")
                question = takeCommand()
                speak("Sir, Let me check if i know or not")
                # Get your API Key from www.wolframalpha.com
                app_id = 'Paste Your API Key Here'
                client = wolframalpha.Client(app_id)
                res = client.query(question)
                answer = next(res.results).text
                print(answer)
                engine.setProperty('rate', 130)
                speak(answer)
            except Exception as e:
                print(e)
                speak("Sorry Sir, I don't know that")

# Wolframalpha API

        elif 'tell me what is' in query or 'tell me who is' in query or 'hey tell me' in query or 'calculate' in query or 'calculate karo' in query:
            try:
                speak("Sir, Let me check if i know or not")
                question = query.split()
                query = query.replace('search', "")
                # Get your API Key from www.wolframalpha.com
                app_id = 'Paste Your API Key Here'
                client = wolframalpha.Client(app_id)
                res = client.query(query)
                answer = next(res.results).text
                print(answer)
                engine.setProperty('rate', 130)
                speak(answer)
            except Exception as e:
                print(e)
                speak("Sorry Sir, I don't know that")


# Saying Thanks to Assistant

        elif 'thanks for the help' in query:
            z = ['My Pleasure!, Sir', 'Your Welcome!, Sir', 'No Problem!, Sir, You can give me another task if you want']
            speak(random.choice(z))
        elif 'shukriya' in query:
            z = ['My Pleasure!, Sir', 'Your Welcome!, Sir', 'No Problem!, Sir, You can give me another task if you want']
            speak(random.choice(z))
        elif 'bohat shukriya' in query:
            z = ['My Pleasure!, Sir', 'Your Welcome!, Sir', 'No Problem!, Sir, You can give me another task if you want']
            speak(random.choice(z))
        elif 'thanks' in query:
            z = ['My Pleasure!, Sir', 'Your Welcome!, Sir', 'No Problem!, Sir, You can give me another task if you want']
            speak(random.choice(z))
        elif 'thank you' in query:
            z = ['My Pleasure!, Sir', 'Your Welcome!, Sir', 'No Problem!, Sir, You can give me another task if you want']
            speak(random.choice(z))
        elif 'meherbani' in query:
            z = ['My Pleasure!, Sir', 'Your Welcome!, Sir', 'No Problem!, Sir, You can give me another task if you want']
            speak(random.choice(z))
        elif 'bari meherbani yaar' in query:
            z = ['My Pleasure!, Sir', 'Your Welcome!, Sir', 'No Problem!, Sir, You can give me another task if you want']
            speak(random.choice(z))
        elif 'so nice of you' in query:
            speak("My Pleasure Sir!")

# Closing Assistant

        elif 'goodbye' in query:
            Y = ['Good Bye! Have a nice day Sir.', 'Good Bye Sir, See you soon', 'Good Bye Sir, Please do call me if you have another task']
            speak(random.choice(Y))
            break
        elif 'allah hafiz' in query:
            Y = ['Good Bye! Have a nice day Sir.', 'Good Bye Sir, See you soon',
                 'Good Bye Sir, Please do call me if you have another task']
            speak(random.choice(Y))
            break
        elif 'bye' in query:
            Y = ['Good Bye! Have a nice day Sir.', 'Good Bye Sir, See you soon',
                 'Good Bye Sir, Please do call me if you have another task']
            speak(random.choice(Y))
            break
        elif 'ab jao tum' in query:
            speak("Good Bye! I am going to sleep. Have a nice day sir.")
            break
        elif 'go home' in query:
            speak("Good Bye! I am going to sleep. Have a nice day sir.")
            break
        elif 'tum chale jao ab' in query:
            speak("Good Bye! I am going to sleep. Have a nice day sir.")
            break
        elif 'aap jao' in query:
            speak("Good Bye! I am going to sleep. Have a nice day sir.")
            break
        elif 'sleep' in query:
            speak("Good Bye! I am going to sleep. Have a nice day sir.")
            break
        elif 'go to sleep' in query:
            speak("Good Bye! I am going to sleep. Have a nice day sir.")
            break
        elif 'see you soon' in query:
            Y = ['Good Bye! Have a nice day Sir.', 'Good Bye Sir, See you soon',
                 'Good Bye Sir, Please do call me if you have another task']
            speak(random.choice(Y))
            break
        elif 'bye see you' in query:
            Y = ['Good Bye! Have a nice day Sir.', 'Good Bye Sir, See you soon',
                 'Good Bye Sir, Please do call me if you have another task']
            speak(random.choice(Y))
            break
        elif 'okay see you next time' in query:
            Y = ['Good Bye! Have a nice day Sir.', 'Good Bye Sir, See you soon',
                 'Good Bye Sir, Please do call me if you have another task']
            speak(random.choice(Y))
            break
        elif "stop listening" in query:
            Y = ['Good Bye! Have a nice day Sir.', 'Good Bye Sir, See you soon',
                 'Good Bye Sir, Please do call me if you have another task']
            speak(random.choice(Y))
            break
        elif "jao so jao jakar" in query:
            speak("Good Bye! I am going to sleep. Have a nice day sir.")
            break



