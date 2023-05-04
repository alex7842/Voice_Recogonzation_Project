from turtle import *
import turtle, math
import speech_recognition as sr
import pyttsx3, pywhatkit
import datetime
import wikipedia, pyjokes, cv2
import os,qrcode,requests,threading
from tkinter import *
#import openai
#openai.api_key="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"

listener = sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty(("voices"))
engine.setProperty("voice",voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def takeword():
    while True:
        try:
            with sr.Microphone()  as source:
                listener.adjust_for_ambient_noise(source,duration=0.02)
                #talk('hi sir')
                print("listening....")
                listener.pause_threshold=1
                voice=listener.listen(source)
                command=listener.recognize_google(voice)
                command=command.lower()
                if "sana" in command or "hey sana" in command:
                    label.config(fg="red")
                    command=command.replace("sana","")
                    talk(command)
        except:
            command=command
        return command



'''    
x=openai.Completion.create(
    prompt=command,
    engine="text-davanci-002",
    max_tokens=1000,
)
s=x
print(s)'''



def run_prg():
    command=takeword()
    print("\033[96m",command)

    if "play" in command:
        song=command.replace("play","")
        talk("playing"+song)
        pywhatkit.playonyt(song)
    elif "time" in command:
        time=datetime.datetime.now().strftime("%I:%M %p")
        day=datetime.date.today()
        print(day.strftime("%A"))
        print(time)
        talk("current time is:" + time)
    elif "who is"  in command or "what is" in command:
            talk("according to wikipedia")
            person=command.replace("who is","")
            info=wikipedia.summary(person,5)
            print(info)
            talk(info)
    elif "who created you" in command:
        talk("i was created by mr alex.. he is my owner ..and i was created for his voice assistant.....thank you")
    elif  "joke" in command:
        m1=talk(pyjokes.get_joke(language="en",category="all"))
        print(m1)
        talk(m1)
    elif "write" in command:
        a=command.replace("write","")
        pywhatkit.search(a)
        talk(a)
    elif "how are you" in command:
        talk("I am doing well,  I am great, thanks for asking..")

    elif "open google" in command:
        a=os.startfile("C:\\Users\\Public\\Desktop\\Google Chrome.lnk")
        print(a)
    elif "open youtube" in command:
        c=os.startfile("https://www.youtube.com")
        print(c)
    elif "open whatsapp" in command:
        d=os.startfile("https://web.whatsapp.com")
        print(d)
    elif "say about you" in command:
        a=talk(" well my name is sara .. and i am an trained... voice assistant of mr,alex ...i am working under automatic speech recognition (ASR), computer speech recognition, , i have  a capability to process human speech into a written format.")

        print(a)
    elif "are you there" in command:
        talk("yes i am ...how can i help you")
    elif "open" in command:
        eo=command.replace("open","")
        talk("opening"+eo)
        pywhatkit.playonyt(eo)
    elif "send" in command:
        a=input("enter the text:")
        w=pywhatkit.sendwhatmsg("+919345991426",a,18,49,True)
        print(w)
    elif "how to prepare" in command:
        h=command.lower()
        talk("according to wikipedia")
        k=wikipedia.summary(h,6)
        print(k)
        talk(k)
    elif "qr code" in command:
        talk("creating..")
        a = ("https://alexjerry4444.ccbp.tech/")
        r=qrcode.QRCode(version=1,box_size=6,border=5)
        r.add_data(a)
        r.make(fit=True)
        im=r.make_image(fill_colour="red",back_colour="white")
        im.save("storer.png")
        print("\033[92m successfully created... check the storer.pnj file")
        talk("succesfully created... check the storer.pnj file")

    elif "tell about me" in command or "say about me" in command:
        talk("yes  its my pleasure")
        talk("what is your name sir")
    elif "my name is" in command:
        a=command.replace("my name is","")
        talk("It's nice to meet you"+a+".......you are looking very beautifull today......have a great day"+a)
        print(a)
    elif "what is the meaning of" in command:
        b=command.replace(" what is the meaning of","")
        pywhatkit.search(b)
        print(b)

    elif "show camera" in command:
        b=command.replace("open camera","")
        print(b)
        a=talk("yes sure ...smile to the camera please")
        talk("for quitting the camera please press an letter ...c... on the keyboard ")
        print("\033[96m",a)
        ca=cv2.VideoCapture(0)
        while ca.isOpened():
            v,j=ca.read()
            if cv2.waitKey(10)==ord("c"):
                break
            cv2.imshow("alex web cam", j)


    elif "do you know" in command:
        try:
            v=command.replace("do you know","")
            b=wikipedia.summary(v,4)
            print(b)
            talk(b)
        except:
            a=talk("\033[92m SORRY THERE IS NO PAGE RELATED TO YOUR SEARCH")
            print(a)
    elif "weather in" in command:
        loc=command.replace("weather in","")
        key = "3b704ac692f9cedf38b420eee4e5cf71"

        api = "https://api.openweathermap.org/data/2.5/weather?q=" + loc + "&appid=" + key
        s = requests.get(api)
        g = s.json()
        temp = ((g["main"]["temp"]) - 273.15)
        weather = g["weather"][0]["description"]
        humidity = g["main"]["humidity"]
        windspeed = g['wind']['speed']

        f1=talk("current weater in {} is".format(loc))
        talk(f1)
        print(f1)
        f3=("TEMPERTURE: {:2f}".format(temp))
        talk(f3)
        print(f3)
        b=("WEATHER: {}".format(weather))
        talk(b)

        print(b)
        g=("HUMIDITY: {}".format(humidity))
        talk(g)
        print(g)
        k=("WINDSPEED: {}".format(windspeed))
        talk(k)
        print(k)


    elif "people better than me" in command:
        talk("hey .. dont worry... look at the mirror that's your competitor..")
        talk("Instead of worrying about others, focus on yourself..")
    elif "cheer me" in command:
        talk('You are doing great! Keep up the good work and stay positive..')
        talk('Remember that every effort you make brings you one step closer to achieving your goals.')
        talk('Believe in yourself and keep pushing forward, even when things get tough. You got this!....')




      #i am bored may be game
    elif "do you love me" in command or "are you single" in command:
        a=talk("I'm sorry but I'm not able to speak to that subject...")
        print(a)
        b=talk("because i am an machine i don't have any feelings like humans...")
        print(b)
    elif "advantages" in command:
        v=command.lower()
        a=wikipedia.summary(v,5)
        print(a)
        talk(a)

    elif "disadvantages" in command:
        v1=command.upper()
        a2=wikipedia.summary(v1,5)
        talk(a2)
        print(a2)
    elif "draw" in command:
        talk('sure i have an surprise for you close your eyes....')

        def  her(k):
            return 15 * math.sin(k) ** 3

        def hea(k):
            return 12 * math.cos(k) - 5 * \
                   math.cos(2 * k) - 2 * \
                   math.cos(3 * k) - \
                   math.cos(4 * k)
        speed(1000)
        bgcolor('black')
        for i in range(6000):
            goto(her(i) * 20, hea(i) * 20)
            for j in range(5):
                color('#f73487')
            goto(0, 0)
        done()
        talk('this art will definetly amazed you...')
    elif "thank you" in command:
        talk(" you are welcome ......I'm glad that you're satisfied and convey this thanks to my owner mr..alex")



    elif "quit"  in command:

        talk("by your wish sir...")
        quit()

    else:
        talk("hey.. say it clearly")

root=Tk()
label=Label(text="🤖",font=("Arial",120,"bold"))
label.pack()
threading.Thread(target=run_prg).start()
root.mainloop()



while True:
    run_prg()


