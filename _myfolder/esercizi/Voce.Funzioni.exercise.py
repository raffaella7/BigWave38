import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty("voices")      
engine.setProperty("voice", voices[0].id)
import random
from speech_recognition import Microphone, Recognizer


matrix = [
        ["io sono un bot", "sono stata creata da raffaella", "sono un bot che ti darà delle risposte a delle tue domande"],
        ["mi definisco un bot", "fammi una domanda e ti darò una risposta", "chiedimi qualcosa"],
        ["vorrei aiutarti, chiedimi qualcosa", "vuoi che ti dia una mano", "sono una donna e rispondo alle tue domande"],
    ]


#funzione choise per la lista
#la ritorno 
#prendo il valore e lo passo ad una funzione che mi srive il file testo

r = Recognizer()                   
mic = Microphone()
r.pause_threshold = 0.8
r.energy_threshold = 50
r.phrase_threshold = 0.1

from random import choice 
import webbrowser
from datetime import datetime

"""
def WriteText():
    new_file = open("new_file.txt", "w")
    new_file.write ("Istruzioni")
    new_file.close()
"""
"""
def AppendText():
    new_file = open("new_file.txt", "a")
    new_file.write("\nqueste sono le istruzioni\nA B C D")
    
    new_file.close()
    """

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


def choise_answer():
    #list_number = [0,1,2]
    #numero_scelto = (random.choice(list_number))

    list_1 = matrix[random.randint(0,2)]
    scelta = (random.choice(list_1))
            #WriteText(scelta)
    new_file = open("new_file.txt", "w")
    new_file.write (scelta)
    new_file.close()

    #
    
"""
def choise2():
    list_2 = matrix[1]
    scelta1 = (random.choice(list_2))
    new_file = open("new_file.txt", "w")
    new_file.write (scelta1)
    new_file.close()

def choise3():
    list_3 = matrix[2]
    scelta2 = (random.choice(list_3))
    new_file = open("new_file.txt", "w")
    new_file.write (scelta2)
    new_file.close()
           
"""
#WriteText()
#AppendText()

while True:
    

    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, timeout = 10, phrase_time_limit=5)                 
        stt = r.recognize_google(audio, language = "it-IT")
        stt = str(stt).lower()
        print(stt)

       

#while True:

        if stt.startswith(("ciao")):
            choise_answer()
            ReadText()
        
        #elif stt.startswith(("bene")):
            #choise2()
            #WriteText(scelta1)
            #ReadText()

        #elif stt.startswith(("salve")):
            #choise3()
            #WriteText(scelta2)
            #ReadText()
        
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


