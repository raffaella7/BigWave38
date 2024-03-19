#Crea una funzione che dato ad argomento una stringa permetta di leggere quella stringa tramite la libreria pyttsx3
import pyttsx3

engine = pyttsx3.init()                                    #NON SERVE SCRIVERLO OGNI VOLTA PER OGNI FUNZIONE
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

"""
def Voice(stringa):

    engine.say(stringa)
    engine.runAndWait()    
    Voice("ciao")
    return False

def Voice2(stringa):
    engine.say(stringa)
    engine.runAndWait()
    Voice("error")
    return True


while True:
    if Voice("buenas"):
        Voice("buenas")
    elif Voice2("error") == True:
        Voice2("error")


#se volessi fargli dire qualcosa da input

def Voice(input):
    inputt = input("input")
    engine.say(inputt)
    engine.runAndWait()
    Voice()

Voice("ciao")
"""

def Voice(stringa):
    engine.say(stringa)
    engine.runAndWait()
    return True

while True:
    Voice("6") 