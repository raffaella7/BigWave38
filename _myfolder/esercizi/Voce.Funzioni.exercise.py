import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty("voices")      
engine.setProperty("voice", voices[0].id)

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
    text = input("sono pronta, chiedimi pure\n")
    if "istruzioni" in text:
        ReadText()
    elif text.startswith(("cosa", "come", "quanto")):
        casualResponse()
    elif any(word in text for word in ["mese", "month"]):
        hourResponse()
    elif text.startswith("cerca"):                                   #QUA GLI DICO CHE DEVO SCRIVERE PER FORZA CERCA SE LO LA FUNZIONE DI PRIMA NON FUNZIONA
        webSearch(text)
    elif "esci" in text:
        risposta = "ciao"
        break
    else:
        risposta = "non so cosa dirti"