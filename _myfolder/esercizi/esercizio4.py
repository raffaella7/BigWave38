#crea una funzione che dati nome e cognome ad input generi un username che corrisponda ai primi tre caratteri del nome ed 
#agli ultimi quattro caratteri del cognome. I rispettivi codici di slicing verrà avviato solo nel caso il nome abbia più di tre caratteri ed il cognome più di 4.

def NomeCognome():
    
    domanda_nome = input("inserisci nome: ")
    domanda_cognome = input("inserisci cognome: ")

    if len(domanda_nome) > 3:
        name = domanda_nome [:3]
    else:
        name = domanda_nome
    if len(domanda_cognome) > 4:
        surname = domanda_cognome [-5:]
    else:
        surname = domanda_cognome
    
    username = name + surname                                   #CONCATENAZIONE DI STRINGHE PER METTERE INSIEME DUE VALORI

    print(username)

NomeCognome()