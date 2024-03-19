from random import choice
import webbrowser
from datetime import datetime

def ReadText():
    with open("istruzioni.txt", "r") as f:
        print(f.readline())

def hourResponse():
    print(f"sono le ore {datetime.now().strftime("%H e %M")}")

def casualResponse():
    print(choice(["cerca su internet", "ok Google, aiutami tu", "chiedi ad Alexa"]))

def webSearch(text):
    text_list = text.split()        #mi esce una lista di elementi in base alle parole e agli spazi vuoi (ciao come stai) diventa [ciao, come, stai]
                                    #SE LASCIO SOLO LA PARENTESI () DOPO LO SPLIT ALLORA MI PRENDE COME DELIMITATORE GLI SPAZI VUORI
    text = text_list[1:]            #tutti gli elementi esluso il primo
    text = " ".join(text)           #CON JOIN LO RITRASFORMA IN UNA STRINGA DOPO AVERLA SPLITTATA
    webbrowser.open("https://www.google.com/search?q="+text)

while True:
    text = input("chiedimi qualcosa\n")

    if "istruzioni" in text:
        ReadText()
    elif text.startswith(("cosa", "come", "quanto")):
        casualResponse()
    elif any(word in text for word in ["ora", "ore", "orario"]):
        hourResponse()
    elif text.startswith("cerca"):                      #QUA GLI DICO CHE DEVO SCRIVERE PER FORZA CERCA SE LO LA FUNZIONE DI PRIMA NON FUNZIONA
        webSearch(text)
    elif "esci" in text:
        risposta = "ciao"
        break
    else:
        risposta = "non so cosa dirti"

