#ESERCIZIO IN CLASSE
#Data la massa di una pallina di 5kg calcola il peso in Newton della pallina sulla terra e su ogni altro pianeta del sistema solare. 
#Il cacolo dovrà essere eseguito in runtime da un programma che gestisce un control flow partendo da un input. 

#DICTIONARY
#(è un altro datatype): coppie chiave valore che possono essere anche int, float o bool (serve richiamare delle condizioni quando è necessario)


mass = 5
quest = input("che pianeta vuoi scegliere?")
gravita = {
    "mercurio": 3.7,
    "venere": 8.8,
    "terra": 9.8,
    "marte": 3.7,
    "giove": 24.8,
    "saturno": 8.9,
    "uranio": 8.7,
    "nettuno": 11
}

if quest in gravita:
    print(mass*gravita[quest])                          #quando uso il dizionario devo fare così perchè gli sto dicendo di cercare la risposta che ha dato all'input all'interno di esso e metterla a confrontro con le altre chiavi
                                                        #deve essere scritto per forza così