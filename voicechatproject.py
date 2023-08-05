from turtle import *
import turtle, math
import speech_recognition as sr
import pyttsx3, pywhatkit
import datetime
import wikipedia, pyjokes, cv2
import os,qrcode,requests,threading
from tkinter import *
import openai


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
                listener.adjust_for_ambientnoise(source,duration=0.02)
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




def run_prg():
    command=takeword()
    print("\033[96m",command)
    if "play" in command:
        song=command.replace("play","")
        talk("playing"+song)
        pywhatkit.playonyt(song)
    elif "who created you" in command:
        talk("i was created by mr alex.. he is my owner ..and i was created for his voice assistant.....thank you")
    elif "qr code" in command:
        talk("creating..")
        a = ("https://alexjerry4444.ccbp.tech/")
        r = qrcode.QRCode(version=1, box_size=6, border=5)
        r.add_data(a)
        r.make(fit=True)
        im = r.make_image(fill_colour="red", back_colour="white")
        im.save("storer.png")
        print("\033[92m successfully created... check the storer.pnj file")
        talk("succesfully created... check the storer.pnj file")
    else:

        openai.api_key="your api key"
        model_engine = "text-davinci-003"
        prompt = command
        completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,

        temperature=0.5)

    resp = completion.choices[0].text

    print("\033[92m",resp)
    talk(resp)

'''import os
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load pre-trained model and tokenizer
model_name = "gpt2"  # You can also use "gpt2-medium", "gpt2-large", etc. for larger models
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

def chat_with_model(prompt, max_length=50):
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    chat_history_ids = model.generate(input_ids, max_length=max_length, num_return_sequences=1)
    response = tokenizer.decode(chat_history_ids[:, input_ids.shape[-1]:][0], skip_special_tokens=True)
    return response

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = chat_with_model(user_input)
    print("ChatGPT: " + response)'''

root=Tk()
label=Label(text="🤖",font=("Arial",120,"bold"))
label.pack()
threading.Thread(target=run_prg).start()
root.mainloop()



while True:
    run_prg()