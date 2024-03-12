#il += corrisponde alla prima variabile più la seconda variabile e include sia la somma che l'assegnazione

my_int = 5
my_second_int = 2
my_int += my_second_int #my_int = my_int + my_second_int

my_int *= my_second_int  #ugale a prima ma con la moltiplicazione
print(my_int)

#statement condizionale
h = "hello" - input("inserisci un input: ")

if h == "hello": #== è operatore logico che mette a paragone due valori e restituisce se i due valori sono uguali la booleana trrue, altrimenti la booleana false.
    print(h)
elif h == "hi": #ci permette di andare a verificare se una seconda condizione è verificata o no (elif vuole dire un else if)
    print("hi,how are you?")
else:
    pass  #quando non vogliamo inserire una specifica esecuzione ma vogliamo usare un place holder (perchè non sappiamo cosa deve essere eseguito o non vogliamo niente)
    print("error")  #oppure possiamo metterlo così


#INNETAZIONE = numero di spazi che c'è alla sinistra della nostra pagina di codice (con tab)
#in python è fondamentale perchè definisce anche lo SCOUP, quindi il contesto di determinate righe di codice in relazione ad altre (ciò che viene eseguito e che non deve essere eseguito vicino ad uno statement )
#l'intreperete non è in grado di comprendere quello che gli stiamo dicendo di fare, quindi una corretta innetazione è necessaria per una corretta esecuzione del codice


#MATCHCASE  due modi per strutturare conditional statement, si possono usare tutti e due 

match h:
    case "hello":
        print(h)
    case "hi":
        print("hi, how are you?")
    case _ :
        print("error")

#OPERATORI LOGICI RELAZIONALI (verifcano la relazione tra la prima e la seconda variabile)
"""
>= maggiore uguale
<= minore uguale
< minore
> maggiore
!= not equal
== equal
"""

my_int_1 = int(input("nsert first number"))
my_int_2 = int(input("insert second number"))
my_int_3 = int(input("insert third number"))

if my_int_1 == 1 and my_int_2 == 2:  
    print("first and second")  

#i due punti vanno messi sempre per chiudere un flusso, per esempio un if o elif deve essere sempre chiuso da due punti (come la parentesi graffa su unity)
#and restituisce true solo se la prima è true e e la seconda è true
#invece or restituisce true solo nel caso una delle due sia true, oppure entrambe siano true

elif my_int_1 == 0 or my_int_3 == 3:
     print("first or third") 
                                    
#quando il valore nella prima variabile non è uguale al secondo allora !=

elif my_int_1 != 2:
       print("first ints is not 2")




#LISTE
#ogni valore che viene inserito nella lista ha un indice
#quando si tratta di indici si inizia a contare dallo zero
#se vogliamo printare un elemento nella lista possiamo andare a printarlo indicando l'indice della lista inserito in parentesi quadre

my_list = [2, 2.5, "my_string", True]
print(my_list[3])

#possiamo anche assegnare un altro valore all'elemento della lista

my_list[0] = 4
print(my_list[0])

my_matrix = [
        [0,1],
        ["hello, world"],
        [True, False],
        [0.5, 0.72]]

print(my_matrix[0])

#le matrici sono liste di liste
my_matrix

#se vado a pentare tramite indice un elemento della stringa si comporterà come una lista 
#questo mi permette anche di utilizzare i cicli for sulle stringhe 
#CAR è una variabile di appoggio (posso chiamarla come voglio, anche y) e lui si prende tutta la lista o tutta la stringa e te la passa. 
#ogni elemento viene passato a cas temporaneamente e viene eseguito lo statement condizionale per ogni elemento per controllare che ogni elemento 


my_string = "12345"

for car in my_string:
        if car == 1:
            print(car)
        else:
            print("not recognized")




#CICLO FOR
#prende ogni elemento della lista e printarlo singolarmente
for element in my_list:
        print(element)




#CICLO WHILE
n = 1
while n == 1:
    print("1")
    n = 2           #questa condizione mi deve restituire ture e quindi si ferma il ciclo, si blocca per la condizione ritorna a false

#quando si verifica la condizione in cui la nostra vvraiabilen 
#è uguale a uno si verifica il ciclo while invece se il valore cambia si blocca da solo perchè
#gli abbiamo impostato la condizione di fine
    
num = True
while num = True:           #questo andrà avanti all'infinito invece a meno che non metta la condiziine di BREAK ovvero num = False
    print("1")
    num = False

#finchè non scrivo MELLON mi ripeterà l'input

Mellon = input("Speak Friend and Enter\n")
while Mellon != "Mellon":
     Mellon = input("Speak Friend and Enter\n")
print("Welcome")



#IN E FOR IN ALTRE SITUAZIONI
#con IN andiamo a verificare in una lista o una stringa se è vera o falsa invece con FOR andiamo a cilcare per ogni elemento il codice
#IN restituisce un TRUE o FALSE se accompagnato da if 



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