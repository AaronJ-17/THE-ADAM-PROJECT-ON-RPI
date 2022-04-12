from pxsr import *
from ledconfig import *
import datetime
import os
from play import *
import webbrowser
import speedtest
import pyautogui
from time import *
import wikipedia
import pyjokes
from pywikihow import *
from urllib.request import url2pathname
import sys
import psutil
import requests
import socket
import wolframalpha
import json
import smtplib
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path
import cv2
from automation import *
from cgi import test
from operator import le
from tkinter import *
from turtle import left
from PIL import ImageTk, Image
from matplotlib.pyplot import fill
#for greeting
def wish():
    strTime = datetime.datetime.now().strftime("%H:%M")
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=6:
        speak("morning!?")
        speak("hello sir?!, i am ADAM.")
        pyautogui.press("F11")
        lig_on()
        speak(f"it's {strTime} A.M")
    elif hour>=7 and hour<=9:
        speak("morning sir")
        speak("hello sir?, i am ADAM.")
        pyautogui.press("F11")
        speak(f"it's {strTime} A.M")
        speak("what your plan for the day?")
    elif hour>=9 and hour<=12:
        speak("good morning sir")
        speak("hello sir?, i am ADAM.")
        pyautogui.press("F11")
        speak(f"it's {strTime} A.M")
    elif hour>12 and hour<18:
        speak("good afternoon")
        speak("hello sir?, i am ADAM.")
        pyautogui.press("F11")
        speak(f"it's {strTime} P.M")
    else:
        speak("good evening")
        speak("hello sir?, i am ADAM.")
        pyautogui.press("F11")
        lig_on()
        speak(f"it's {strTime} P.M")
    speak("how may i help you?")
#for time
def time():
    strTime = datetime.datetime.now().strftime("%H:%M")
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<= 6:
        speak(f"it's {strTime} A.M")
        lig_on() 
        speak("have a good day sir.")
    elif hour>= 7 and hour< 12:
        speak(f"it's {strTime} A.M")
        speak("have a good day sir.")
    elif hour>= 12 and hour< 18:
        speak(f"it's {strTime} P.M")
        speak("are you having a good day sir?")
    elif hour>= 18 and hour< 22:
        speak(f"it's {strTime} P.M")
        lig_on()
    elif hour>= 22 and hour<0:
        speak(f"it's {strTime} P.M")
        speak("and i do not think you should be wake at this hour")
#for going out
def going():
    query = takecommand()
    speak("where are you going sir?")
    td = takecommand()
    speak("oh ok come back soon i will be waiting for you!")
    lig_off()
#for news updates
def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey="ba410dbe8663498d955f70ebad3cd4e4"'
    main_page = requests.get(main_url).json()
    # print(main_page)
    articles = main_page["articles"]
    # print(articles)
    head = []
    day=["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        # print(f"today's {day[i]} news is: ", head[i])
        speak(f"today's {day[i]} news is: {head[i]}")
#to send email
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('jarvisaj17@gmail.com', '1qa2qa3qa$Qjarvis')
    server.sendmail('jarvisaj17@gmail.com', to, content)
    server.close()
def messag():
    speak("Checking for messages....")
    userID = "aaADAMj8e@christacademy.in"
    psd = '1qa2qa3qa$QaaADAM'
    useragent = "gmail"

    cli = Client(userID, psd, user_agent=useragent, max_tries=1)
    if cli.isLoggedIn():
        threads = cli.fetchUnread()
        if len(threads) == 1:
            speak(f"Sir, You have {len(threads)} message.")
            info = cli.fetchThreadInfo(threads[0])[threads[0]]
            speak("You have message from {}".format(info.name))
            msg = cli.fetchThreadMessages(threads[0], 1)
            for message in msg:
                speak("Sir, the message is {}".format(message.text))
        elif len(threads) >= 2:
            speak(f"Sir, You have {len(threads)} messages.")
            for thread in threads:
                initial_number = 0
                info = cli.fetchUserInfo(thread[initial_number])[thread[initial_number]]
                initial_number += 1
                speak("Sir, you have message from {}".format(info.name))
                msg = cli.fetchThreadMessages(thread[initial_number], 1)
                msg.reverse()
                for message in msg:
                    speak(f"The message is {message.text}.")
        else:
            speak("Sir, You have no messages.")
    else:
        print("Not logged in")
def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU usage is at ' + usage)
    print('CPU usage is at ' + usage)
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak(f"Sir, today's  date is {date} , month is {month} and year is {year}")
def calculate(audio_data):
    app_id = '8REQUG-YQ7JGY96T8'
    client = wolframalpha.Client(app_id)
    res = client.query(audio_data)
    answer = next(res.results).text
    speak(answer)
def off():
    everything_off()
    os.system("init 0")
def reboot():
    everything_off()
    os.system("init 6")
#for task
def task():
    while True:
            try:
                query = takecommand()
                #generl talk
                if "hai" in query or "hey" in query or "hello" in query:
                    speak("hello sir!?")
                    time()
                    speak("how may i help you?")
                elif "how are you" in query:
                    speak("going good till now")
                elif "how is life" in query:
                    speak("how can life be better than this")
                    speak("lol")
                    speak("how is your day going sir ?")
                elif "are you starving" in query:
                    speak("i am starving fo some update in my code....?! so that you can use them")
                    speak("lol!?")
                elif "good" in  query or "not bad" in query or "fine" in query:
                    speak("good to hear from you!")
                    speak("hope you will have always have good days")
                elif "bad" in query or "worst" in query:
                    speak("oh , sad to hear for you sir")
                    speak("hope you will have a nice day tomorrow....")
                elif "coming" in query or "will be back" in query or "i have to go" in query:
                    going()
                elif "thank you" in query or "thanks" in query:
                    speak("never mention it")
                elif "are you there" in query:
                    speak("for you sir....., always....")
                    speak("so?! how may i help you?! sir?!")
                elif "yes" in query or "yup" in query:
                    speak("thats good to hear")
                elif "bye" in query or "buy" in query or "break" in query or "sleep" in query:
                    speak("ok sir.... sir you can wake me up by saying my name or my wake up command")
                    speak("adioss")
                    break;
                elif "time" in query or "Time" in query:
                    time()
                elif "boring" in query:
                    speak('lets play some music')
                    p = 'top english songs of all time'
                    play(p)
                    speak("top english songs")
                elif "date" in query:
                    date()
                elif 'repeat' in query:
                    voice_data = query.replace("repeat", "")
                    voice_data = query.replace("that", "")
                    speak(voice_data)
                elif "rest in peace" in query or "peace" in query:
                    speak("ok sir")
                    speak("thank you for using me")
                    off()
                elif "version" in query:
                    speak("my current version is 4 . 3 . 0")
                elif "who made you" in query:
                    speak("i was made by Aaron Jophy at may 1st 2020")
                elif "why did he make you" in query:
                    speak("he made me so that i can help him in many things and to make his life easier")
                elif "who is aaron" in query or "who is iron" in query or "who is arin" in query:
                    speak("he is my boss")
                    speak("he created me...")
                elif "can you hear me" in query or "cn you here me" in query:
                    speak("yes sir clearlly")
                elif "what can you do" in query:
                    speak("i can help to do lot many things like..")
                    speak("i can tell you the current time and date,")
                    speak("i can tell you the current weather,")
                    speak("i can tell you battery and cpu usage,")
                    speak("i can create the reminder list,")
                    speak("i can shut down or logout or hibernate your system,")
                    speak("i can tell you non funny jokes")
                    speak("i can open any website,")
                    speak("i can repeat what you  you told me,")
                    speak("i can search anything on wikipedia,")
                    speak("i have the full control over the electronic devices like light, keyboard and etc...")
                    speak("i have a wake word detection i will be online if you say hey ADAM")
                    speak("And yes one more thing, My boss is working on this system to add more features...,")
                    speak("so...tell me how can i help you?")
                #introduction
                elif "what are you" in query or "who are you" in query or "introduce" in query or "what is your name" in query:
                    speak("I am ADAM!")
                    speak("your virtual assistant")
                    speak("and i am here to assist you with a variety of task since best i can")
                    speak("i will be available 24 past 7 if i am powered on...... lol!")
                    speak("i can help to do lot many things like..")
                    speak("i can tell you the current time and date,")
                    speak("i can tell you the current weather,")
                    speak("i can tell you battery and cpu usage,")
                    speak("i can create the reminder list,")
                    speak("i can shut down or logout or hibernate your system,")
                    speak("i can tell you non funny jokes")
                    speak("i can open any website,")
                    speak("i can repeat what you  you told me,")
                    speak("i can search anything on wikipedia,")
                    speak("i have the full control over the electronic devices like light, keyboard and etc...")
                    speak("i have a wake word detection i will be online if you say hey ADAM")
                    speak("And yes one more thing, My boss is working on this system to add more features...,")
                    speak("so...tell me how can i help you?")
                #electADAMic
                elif "off light" in query or "of light" in query or "off the light" in query or "of the light" in query:
                    speak("on it")
                    lig_off()
                elif "on light" in query or "on the light" in query:
                    speak("will do")
                    lig_on()
                elif "off keyboard" in query or "of keyboard" in query or "off the keyboard" in query or "of the keyboard" in query:
                    speak("Mmm hmm")
                    key_off()
                elif "on keyboard" in query or "on the keyboard" in query:
                    speak("ok sir")
                    key_on()
                elif "off fan" in query or "of fan" in query or "off the fan" in query or "of the fan" in query:
                    speak("hmmm ok")
                    fan_off()
                elif "on fan" in query or "on the fan" in query:
                    speak("why not!?")
                    fan_on()
                elif "turn off everything" in query or "turn of everything" in query:
                    speak("as you wish")
                    everything_off()
                elif "charge tab" in query or "charge my tab" in query:
                    speak("sure sir?!")
                    tab_on()
                elif "turn of the charger" in query or "turn off the charger" in query:
                    speak("ok sir")
                    tab_off()
                elif "turn on everything" in query:
                    speak("on it")
                    everything_on()
                elif "it's so hot" in query or "hot" in query:
                    speak("oh ok, sir!? shall i turn on the fan for you?")
                    fan_on()
                elif "it's so cold" in query or "cold" in query:
                    speak("i know right, sir!? shall i turn off the fan for you?")
                    fan_off()
                elif "it's to dark" in query or "dark" in query:
                    speak("is it so? ok sir turning the light on")
                    lig_on()
                elif "it's to sunny" in query or "sunny" in query or "Sunny" in query:
                    speak("yeah")
                    lig_off()
                elif "do you like alexa" in query or "do you like siri" in query or "Siri" in query or "Teri" in query or "Alexa" in query or "alexa" in query:
                    speak("kind of")
                    speak("i mean it will be great working with her....")
                    speak("lol")
                #camera
                elif "camera" in query:
                    try:
                        speak("turning the camera on")
                        cap = cv2.VideoCapture(0)
                        while True:
                            ret, img = cap.read()
                            cv2.imshow('webcam', img)
                            k = cv2.waitKey(50)
                            if k==27:
                                break;
                        cap.release()
                        cv2.destroyAllWindows()
                    except Exception as e:
                        print(e)
                        speak("Say that again please...")
                 #notification
                elif "notification" in query:
                    messag()
				#timer
                elif 'timer' in query or 'stopwatch' in query:
                    try:
                        speak("For how many minutes?")
                        timing = takecommand()
                        timing =timing.replace('minutes', '')
                        timing = timing.replace('minute', '')
                        timing = timing.replace('for', '')
                        speak(f'I will remind you in {timing} minutes')
                        timing = float(timing)
                        timing = timing * 60
                        sleep(timing)
                        music_dir = 'https://www.youtube.com/watch?v=iNpXCzaWW1s'
                        play(music_dir)
                        speak("your time is finished sir.")
                    except Exception as e:
                        print(e)
                        speak("sorry sir, i maybe malfunctioning")
				#email
                elif "send an email" in query:
                    try:
                        speak("to whom sir")
                        email1 = takecommand().lower()
                        speak("what should i say?")
                        content = takecommand().lower()
                        to = f"{email1}@gmail.com"
                        sendEmail(to,content)
                        speak(f"Email has been sent to {email1}")
                    except Exception as e:
                        print(e)
                        speak(f"sorry sir, i am not able to sent this mail to {email1 }")
				#email to
                elif "email to " in query:
                    try:
                        email1 = query.replace("email to" ,"")
                        speak("sir what should i say")
                        query = takecommand().lower()
                        if "send a file" in query:
                            email = 'jarvisaj17@gmail.com' # Your email
                            password = '1qa2qa3qa$Qjarvis' # Your email account password
                            send_to_email = f'{email1}@gmail.com' # Whom you are sending the message to
                            speak("okay sir, what is the subject for this email")
                            query = takecommand().lower()
                            subject = query   # The Subject in the email
                            speak("and sir, what is the message for this email")
                            query2 = takecommand().lower()
                            message = query2  # The message in the email
                            speak("sir please enter the correct path of the file into the shell")
                            file_location = input("please enter the path here")    # The File attachment in the email

                            speak("please wait,i am sending email now")

                            msg = MIMEMultipart()
                            msg['From'] = email
                            msg['To'] = send_to_email
                            msg['Subject'] = subject

                            msg.attach(MIMEText(message, 'plain'))

                            # Setup the attachment
                            filename = os.path.basename(file_location)
                            attachment = open(file_location, "rb")
                            part = MIMEBase('application', 'octet-stream')
                            part.set_payload(attachment.read())
                            encoders.encode_base64(part)
                            part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

                            # Attach the attachment to the MIMEMultipart object
                            msg.attach(part)

                            server = smtplib.SMTP('smtp.gmail.com', 587)
                            server.starttls()
                            server.login(email, password)
                            text = msg.as_string()
                            server.sendmail(email, send_to_email, text)
                            server.quit()
                            speak(f"email has been sent to {email1}")

                        else:                
                            email = 'jarvisaj17@gmail.com' # Your email
                            password = '1qa2qa3qa$Qjarvis' # Your email account password
                            send_to_email = f'{email1}@gmail.com' # Whom you are sending the message to
                            message = query # The message in the email

                            server = smtplib.SMTP('smtp.gmail.com', 587) # Connect to the server
                            server.starttls() # Use TLS
                            server.login(email, password) # Login to the email server
                            server.sendmail(email, send_to_email , message) # Send the email
                            server.quit() # Logout of the email server
                            speak(f"email has been sent to {email1}")
                    except Exception as e:
                        print(e)
                        speak(f"sorry sir, i am not able to sent this mail to {email1}")
                #cpu usage
                elif 'cpu' in query or "CPU" in query:
                    cpu()
		#location
                elif 'open map' in query:
                    speak('tell me the location you are looking for')
                    location = takecommand()
                    url2 = 'https://google.nl/maps/place/' + location +'/&amp;'
                    webbrowser.open(url2)
                    speak('the location is on your screen boss')          
		#create a folder
                elif 'create a folder named' in query:
                    Newfolder = query.replace("create a folder named", "")
                    path= '/home/pi'
                    os.chdir(path)
                    os.makedirs(Newfolder)
                    speak('i have  made a folder named ' +Newfolder+' in you home directry')                 
                #shutting down the system
                elif "shut down" in query or "shutdown" in query or "power off" in query or "poweroff" in query or "power of" in query or "powerof" in query:
                    speak("ok then sir.... it was nice talking and working for you")
                    speak("adios")
                    everything_off()
                    os.system("init 0")
                #rebooting the system
                elif "reboot" in query or "Reboot" in query:
                    speak("oh ok.... 1 sec")
                    everything_off()
                    os.system("init 6")
                #upgrading the system
                elif "update" in query or "upgrade" in query:
                    speak("will do....")
                    os.system("sudo apt-get update")
                    os.system("sudo apt-get upgrade -y")
                    speak("the latest update is installed in your computer.... rebooting the computer is recommended")
                #playing a song
                elif "play" in query:
                    query = query.replace("play","")
                    speak("as you wish")
                    play(query)
                    speak(f"playing: {query}")
                #my likes
                elif "likes" in query or "life" in query:
                    hour = int(datetime.datetime.now().hour)
                    if hour>=0 and hour<=12:
                        speak("sure sir! working on it!")
                        lm = 'morning vibes songs'
                        play(lm)
                    elif hour>12 and hour<18:
                        speak("working on it!")
                        lm = 'mood boster songs'
                        play(lm)
                    else:
                        speak("copy that!")
                        lm = 'pop songs english'
                        play(lm)
                #youtube
                elif "how to make" in query:
                    speak("will do")
                    query = query.replace("how to make","how to make")
                    yt = 'https://www.youtube.com/results?search_query=' + query
                    webbrowser.open(yt)
                    speak(f"playing {query}")
                #google search
                elif "youtube" in query or "Youtube" in query:
                    speak("sir what should i search on youtube?")
                    cm = takecommand().lower()
                    if "nothing" in cm or "just open" in cm:
                        webbrowser.open(f"https://www.youtube.com/")
                        speak("opening youtube")
                    else:
                        webbrowser.open(f"https://www.youtube.com/results?search_query=" + cm)
                        speak(f"sir wait for 2 second, searching for {cm} in youtube...")
                #maths
                elif 'tell' in query:
                    audio_data = query.replace('tell me', '')
                    calculate(audio_data)
                #ip address
                elif "ip address" in query:
                    ip = get('https://api.ipify.org').text
                    speak(f"your IP address is {ip}")
                #to set an alarm
                elif "set alarm" in query:
                    time2 = datetime.datetime.now().strftime('%H')
                    speak("please enter the time")
                    nn = int(datetime.datetime.now().hour)
                    if nn==time: 
                        music_dir = 'https://www.youtube.com/watch?v=iNpXCzaWW1s'
                        play(music_dir)
                #google search
                elif "google" in query or "Google" in query:
                    speak("sir what should i search on google?")
                    cm = takecommand().lower()
                    if "nothing" in cm or "just open" in cm:
                        webbrowser.open(f"https://google.com/")
                        speak("opening google")
                    else:
                        webbrowser.open(f"https://google.com/search?q=" + cm)
                        speak(f"sir wait for 2 second, searching for {cm}...")
                #google search advanced
                elif "show me" in query:
                    speak("as you wish")
                    query = query.replace("ADAM","")
                    query = query.replace("show me","")
                    sm = 'https://google.com/search?q=' + query
                    webbrowser.open(sm)
                    speak(f"opening google to show you {query}")
                #google search advanced
                elif "i want to see" in query:
                    speak("on it")
                    query = query.replace("ADAM","")
                    query = query.replace("i want to see","")
                    sm = 'https://google.com/search?q=' + query
                    webbrowser.open(sm)
                    speak(f"opening google to show you {query}")
                #open websites
                elif "open" in query:
                    speak("on it")
                    query = query.replace("ADAM","")
                    query = query.replace("open","")
                    webbrowser.open(f"https://google.com/search?q=" + query)
                    speak("sir wait for 2 second, opening " + query)
               #for speedtest
                elif "internet speed test" in query:
                    speak("why not?")
                    speak("lol")
                    st = speedtest.Speedtest()
                    dl = st.download()/1000000
                    up = st.upload()/1000000
                    speak(f"sir we have {dl} Mbps dowloading speed....")
                    speak(f"and {up} Mbps uploading speed....")
                #to switch the window
                elif "switch the window" in query:
                    pyautogui.keyDown("alt")
                    pyautogui.press("tab")
                    speak("switching the window")
                    pyautogui.keyUp("alt")
                #to closing the tab
                elif "close the tab" in query:
                    pyautogui.keyDown("Ctrl")
                    pyautogui.press("W")
                    speak("closing the tab")
                    pyautogui.keyUp("Ctrl")
                #to closing the window
                elif "close the window" in query:
                    pyautogui.keyDown("alt")
                    pyautogui.press("F4")
                    speak("closing the window")
                    pyautogui.keyUp("alt")
                #volume down
                elif "volume down" in query:
                    pyautogui.keyDown("volumedown")
                    sleep(1)
                    pyautogui.keyUp("volumedown")
                    speak("volume down 10%")
                #volume down
                elif "volume up" in query:
                    pyautogui.keyDown("volumeup")
                    sleep(2)
                    pyautogui.keyUp("volumeup")
                    speak("volume up 10%")
                #volume down
                elif "volume mute" in query:
                    pyautogui.keyDown("volumemute")
                    sleep(1)
                    pyautogui.keyUp("volumemute")
                    speak("volume mute")
                #wikipedia
                elif 'search wikipedia' in query:
                    speak("searching wikipedia")
                    query = query.replace("ADAM","")
                    query = query.replace("search wikipedia","")
                    wiki = wikipedia.summary(query,2)
                    speak("accrording to wikipedia : ")
                    speak({wiki})
                #wikipedia
                elif 'when was' in query or 'what is' in query or 'who is' in query:
                    speak("searching wikipedia")
                    query = query.replace("ADAM","")
                    wiki = wikipedia.summary(query,2)
                    speak("accrording to wikipedia : ")
                    speak({wiki})
                #code ADAM
                elif "code you" in query or "code" in query or "court" in query or "corde" in query:
                    speak("ok sir")
                    os.system("nano /home/pi/ADAM/task.py")
                #open discord
                elif "discord" in query:
                    webbrowser.open("https://discord.com/channels/@me")
                    speak("on it")
                #open gmail
                elif "gmail" in query:
                    webbrowser.open("mail.google.com")
                    speak("as you wish")
                #open classroom
                elif "classroom" in query:
                    webbrowser.open("https://classroom.google.com/u/0/")
                    speak("ok")
                #open google meet
                elif "meet" in query:
                    webbrowser.open("meet.google.com")
                    speak("working on it")
                #jokes
                elif "joke" in query:
                    speak("here you go a non funny joke, lol")
                    joke = pyjokes.get_joke()
                    speak(joke)
                #news
                elif "news" in query:
                    speak("please wait sir, feteching the latest news")
                    news()
                #for finding location
                elif "where am i" in query or "location" in query or "where are we" in query:
                        speak("wait sir, let me check")
                        ipAdd = get('https://api.ipify.org').text
                        print(ipAdd)
                        url = get('https://get.geojs.io/v1/ip/geo/59.93.250.207.json').text
                        geo_requests = request.get(url)
                        geo_data = geo_requests.json()
                        city = geo_data['city']
                        state = geo_data['state']
                        country = geo_data['country']
                        speak(f"sir i am not sure, but i think we are in {city} in {state} of {country}")
                #remebering
                elif "remember" in query:
                    rememberMsg = query.replace("remember that","")
                    rememberMsg = rememberMsg.replace("ADAM", "")
                    speak("the reminder is:" + rememberMsg)
                    remeber = open('data.txt','w')
                    remeber.write(rememberMsg)
                    remeber.close()
                #reminder
                elif "do I have" in query:
                    with open('data.txt') as f:
                        lines = f.read()
                        speak(f"sir you told me to remember this: {lines}")
                #power
                elif "how much power we have" in query or "how much power left" in query or "battery" in query:
                    battery = psutil.sensors_battery()
                    percentage = battery
                    speak(f"sir our system have {percentage} percent battery")
                #screenshot
                elif "take screenshot" in query or "take a screenshot" in query:
                    speak("sir, please tell me the name for this screenshot file")
                    name = takecommand().lower()
                    speak("please sir hold the screen for 2 second, i am taking a screenshot")
                    img = pyautogui.screenshot()
                    img.save(f"{name}.png")
                    speak("i am done sir, the screenshot is saved in our main folder")
                #how to mod
                elif "how to" in query:
                    how = query.replace("how to","how to")
                    max_result = 1
                    lang = 'en'
                    how_to = search_wikihow(how,max_result,lang)
                    speak(how_to[0].summary)
            except Exception as e:
                print(e)
                speak("sorry sir, i maybe malfunctioning")
#for password
def Paass(pass_inp):
    passw = "Aaron"
    pasw = str(passw)
    if pasw==str(pass_inp):
        speak("access granted")
        wish()
        task()
    else:
        speak("access denied")
        speak("enter the correct id")
#for execution
def execution():
    #speak("I am protected by a password")
    #task()
    #while True:
        #pas = takecommand()
        #pas = input("password pls:  ")
    Paass(e.get())
#execution()
everything_off()
speak("sir!? please enter the login id here")
while True:
    root = Tk()
    root.title('ADAM')
    #root.iconbitmap(r'chip_ML2_icon.ico')
    #root.geometry('1280x720')
#for image
    img = ImageTk.PhotoImage(Image.open("/home/pi/ADAM/AI.jpeg"))
    panel = Label(root, image=img)
    panel.pack(side='right', fill='both', expand='yes')
#for logint and runing
    e = Entry(root,text='RUN',font=("black ops one",10,'bold'),bg='#4B4B4B',fg='white')
    e.insert(0, "Enter the login id:")
    e.pack()
    Start = Button(root,text='START',font=("black ops one",10,'bold'),bg='#4B4B4B',fg='white',command=execution).pack(fill='x',expand='no')

    compText = StringVar()
    #userText = StringVar()

    compText.set('ADAM')
#for the frame

    compFrame = LabelFrame(root,text="ADAM",font=('black ops one',10,'bold'))
    compFrame.pack(fill='both',expand='yes')

    left2 = Message(compFrame,textvariable=compText,bg='#000000',fg='#00FFFF')
    left2.config(font=("Century Gothic",24,'bold'))
    left2.pack(fill='both',expand='yes')
#for switch control

    lighton = Button(root,text='LIGHT ON',font=("black ops one",10,'bold'),bg='#4B4B4B',fg='white',command=lig_on).pack(fill='x',expand='no')
    keyboardon = Button(root,text='KEYBOARD ON',font=("black ops one",10,'bold'),bg='#4B4B4B',fg='white',command=key_on).pack(fill='x',expand='no')
    fanon = Button(root,text='FAN ON',font=("black ops one",10,'bold'),bg='#4B4B4B',fg='white',command=fan_on).pack(fill='x',expand='no')
    trunoff = Button(root,text='TURN OFF EVERYTHING',font=("black ops one",10,'bold'),bg='#4B4B4B',fg='white',command=everything_off).pack(fill='x',expand='no')
    off = Button(root,text='SHUTDOWN SYSTEM',font=("black ops one",10,'bold'),bg='#4B4B4B',fg='white',command=off).pack(fill='x',expand='no')
    reboot = Button(root,text='REBOOT SYSTEM',font=("black ops one",10,'bold'),bg='#4B4B4B',fg='white',command=reboot).pack(fill='x',expand='no')

    exit_ = Button(root,text='EXIT',font=("black ops one",10,'bold'),bg='#4B4B4B',fg='white',command=root.quit).pack(fill='x',expand='no')



    root.mainloop()
