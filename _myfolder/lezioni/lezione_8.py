#SPEECH_RECOGNITION

import random
from speech_recognition import Microphone, Recognizer

r = Recognizer()                    #quando abbiamo bisogno di utilizzare nello script una classe, questa deve essere istanziata
mic = Microphone()
r.pause_threshold = 0.8

"""

with mic as source:                     #è possibile dare un alias ad una variabile
                                        #mic è una classe 
    r.adjust_for_ambient_noise(source)  #gli stiamo sistemando il noise ambientale 
                                        #questa è una funzione che serve per aggiustare i noise per ricevere in maniera migliroe il suono
    audio = r.listen(source)            #il recognizer per funzionare necessita di un audio source
                                        #quello che fa quindi è prendere deimetodi dalla classe AUDIOSOURCE
                                        #in questo caso gli stiamo passando come audiosource il microphon
    stt = r.recognize_google(audio, language="it-IT")     #stt sta per speech to text = ci permette di trasfomare il nostro audio in un output testuale 
    print(stt)

#la classe è un progetto:contenitori di metodi (funzioni) o attributi (variabili)
#per istanziare una classe la chiami (come quando richiamo le funzioni)

"""
with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source, timeout = 5)                  #in questo caso ascolta per 20 secondi e dopo smette di ascoltare
    stt = r.recognize_google(audio, language = "it-IT")
    print(stt)

#overload = definire parametri diversi in una funzione per ottenere output diversi
#gli overload sono decorator
