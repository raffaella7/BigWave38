import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty("voices")      
engine.setProperty("voice", voices[0].id)

from speech_recognition import Microphone, Recognizer


r = Recognizer()                   
mic = Microphone()
r.pause_threshold = 0.8
r.energy_threshold = 50
r.phrase_threshold = 0.1

from random import choice 
import webbrowser
from datetime import datetime


def WriteText():
    new_file = open("new_file.txt", "w")
    new_file.write ("Istruzioni")
    new_file.close()

def AppendText():
    new_file = open("new_file.txt", "a")
    new_file.write("\nqueste sono le istruzioni\nA B C D")
    
    new_file.close()

def ReadText():
    new_file = open("new_file.txt")
    file_text = new_file.read()
   
    print(file_text)
    engine.say(file_text)
    engine.runAndWait()


def hourResponse():
    #now.strftime("%m")
    hour = (f"siamo a {datetime.now().strftime("%B")}")
    print(hour)
    engine.say(hour)
    engine.runAndWait()

def casualResponse():
    answer = choice(["non lo so", "non ho capito", "non mi sono informata"])
    print(answer)
    engine.say(answer)
    engine.runAndWait()


def webSearch(text):
    text_list = text.split()        #mi esce una lista di elementi in base alle parole e agli spazi vuoi (ciao come stai) diventa [ciao, come, stai]
                                    #SE LASCIO SOLO LA PARENTESI () DOPO LO SPLIT ALLORA MI PRENDE COME DELIMITATORE GLI SPAZI VUORI
    text = text_list[1:]            #tutti gli elementi esluso il primo
    text = " ".join(text)           #CON JOIN LO RITRASFORMA IN UNA STRINGA DOPO AVERLA SPLITTATA
    webbrowser.open("https://www.google.com/search?q="+text)

WriteText()
AppendText()

while True:
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, timeout = 10, phrase_time_limit=5)                 
        stt = r.recognize_google(audio, language = "it-IT")
        print(stt)



#while True:

        
        if "istruzioni" in stt:
            ReadText()
                
        elif stt.startswith(("cosa", "come", "quanto")):
            casualResponse()
                
        elif any(word in stt for word in ["mese", "month"]):
            hourResponse()
                
        elif stt.startswith("Cerca"):                                   #QUA GLI DICO CHE DEVO SCRIVERE PER FORZA CERCA SE LO LA FUNZIONE DI PRIMA NON FUNZIONA
            webSearch(stt)
                
        elif "esci" in stt:
            print("ciao")
            break
        else:
            print("non so cosa dirti")