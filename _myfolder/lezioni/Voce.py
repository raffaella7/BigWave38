#CLASSI                                
#sono oggetti che all'interno hanno degli attributi 
#sono dei moduli di codice che permettono di incapsulare logiche che possono essere utilizzat per riutilizzare quel codice e mantenerlo ordinato all'interno del progetto
#non sono definite funzioni perchè queste funzioni non hanno gli attributi
#le classi sono contenitori di funzioni e variabili
    
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty("voices")      
                            #così cambiamo lanostra voce 
engine.setProperty("voice", voices[1].id)

                                                                        #ci restituisce un oggetto voices, che ci recupera la voce 
                                                                        #possiamo andare a settare tra le voci di sistema la voce che ci interessa 

engine.say("buenosdias, espero que tu estes bien")                     #con questo metodo possiamo passargli una stringa che verrà letta (gli dico cosa deve dire)
engine.runAndWait()                                                     #con questo metodo possiamo fargli leggere quella stringa e dopo aspetterà un altro SAY e un altro RUNANDWAIT (senza questo non dice niente)

engine.say("how are you")
engine.runAndWait()

for voice in voices:
    print(voice)


