#Tramite un ciclo while create una logica che vi permette di prendere ad input dei numeri. 
#Tramite uno statement condizionale controllate se il numero dato ad input corrisponde ad un numero da 1 a 4 e se è cosi printate il numero. 
#Inserite la possibiltià di uscire dal ciclo while tramite l' inserimento di un input non numerico es. esc 

my_list = 1
my_string = int(input("scrivi un numero :"))
while my_string != my_list:
     my_string = int(input("scrivimi un numero :"))
if my_string == 1:
    print("1")
elif my_string == 2:
     print("2")
elif my_string == 3:
     print("3")
elif my_string == 4:
     print("4")

#ESERCIZIO ESEGUITO DAI MIEI COMPAGNI
num = input("enter a number: ")

while True:
    if num == "esc":
        print("error")
        break
    if int(num) >= 1 and int(num) <= 4:
        print("il numero è compreso tra 1 e 4")
    num = input("enter a number: ")

#ESERCIZIO ESEGUITO DAL PROF
cond = 1
while cond == 1:
    try:
        controll = input("Insert a number: ")

        if controll == "exit":                      #Se la condizione è uguale ad exit allora rompo il ciclo cambiando come condizione il numero 1 con il 2 (sarebbe un true e false)
               cond = 2
        elif int(controll) == 2:
           print(controll)
        elif int(controll) == 3:
           print(controll)
        elif int(controll) == 4:
            print(controll)
    except ValueError:                              #se in un ciclo while si presenta un errore possiamo generare un eccezione in base al tipo di errore (COMANDO DI GESTIONE DEGLI ERRORI)
        print("insert an accettable value")         #nel momento in cui scrivevo qualsiasi cosa che non fossero quei numeri mi dava errore



#ESERCIZIO ESEGUITO DAL PROF
#Scrivi un programma che chieda ad input un carattere. All' interno di una stringa specifica controlla che tale carattere sia presente e controlla se è una vocale o una consonante
vocal = ["a", "e", "i", "o", "u"]

car = input("inserisci un carattere: ") 
my_string = "ciao"                                  #stringa specifica
if car in my_string:                                #se il carattere dato ad input è presente nella stringa 
        if car in vocal:                            #se il carattere è nelle vocali
            print("is a vocal")
        else:
            print("is a consonant")
else:
    print("is not in string")                      #qualsiasi altra cosa venga scritta (parole o numeri) esce questa risposta


h = input("inserisci un input: ")
f = "ci conosciamo?"

if h == "ti chiami raffaella?":     #ricordiamoci sempre i due punti perchè servono per finire la riga (come le parentesi graffe in unity)
    print("no mi chiamo chiara")
elif h == "ti chiami chiara?":
    print("bravissima, come fai a saperlo?")
elif h == ("come ti chiami?"):
    print(h)
else:
    print("non ti conosco, chi sei?")


#ESERCIZIO Scrivi un programma che chieda tre numeri a, b, c all'utente e mostri il più grande tra loro.
    
my_int_1 = int(input("Insert first number"))
my_int_2 = int(input("insert second number"))
my_int_3 = int(input("insert third number"))

if my_int_1 > my_int_2 and my_int_3:  
    print("my_int_1")  

#i due punti vanno messi sempre per chiudere un flusso, per esempio un if o elif deve essere sempre chiuso da due punti (come la parentesi graffa su unity)
#and restituisce true solo se la prima è true e e la sseconda è true
#invece or restituisce true solo nel caso una delle due sia true, oppure entrambe siano true

elif my_int_2 > my_int_1 and my_int_3:
     print("my_int_2") 
                                    
#quando il valore nella prima variabile non è uguale al secondo allora !=

elif my_int_3 > my_int_1 and my_int_2:
       print("my_int_3")


#ESERCIZIO Scrivi un programma che chieda tre numeri a, b, c all'utente e mostri il più grande tra loro.
    
my_int_1 = int(input("Insert first number :"))
my_int_2 = int(input("insert second number :"))
my_int_3 = int(input("insert third number :"))

if my_int_1 > my_int_2 and my_int_1 > my_int_3:
    print(my_int_1)  

elif my_int_2 > my_int_1 and my_int_2 > my_int_3:
     print(my_int_2) 
                                    

elif my_int_3 > my_int_1 and my_int_3 > my_int_2:
    print(my_int_3)



#ESERCIZIO Scrivi un programma che, data una lista di numeri, fornisca in output il maggiore tra tutti gli elementi della lista. (sapendo il numero maggiore)

my_string = "3"
my_list = [5, 10, my_string, 67, 22]

for car in my_list:
    if my_list[3] >= car:
            max_car = my_list[3]
print(max_car)                                      #se non avessi scritto questo fuori dal ciclo for mi avrebbe dato come risultato 5 volte il 67 perchè lo sta comparando con tutti i numeri della lista