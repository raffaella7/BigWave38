#DIZIONARI RECAP

utenti = {
    "Alberto": 22,
    "Raffaella": 22,
    "David": 25
}

print(utenti["Alberto"])                            #posso richiamarlo e mi printa quello che gli ho assegnato

utenti["Alberto"] = 15                              #attenzione perchè in questo modo il valore vecchio non ha più senso


for key, value  in utenti.items():                  #adesso posso fare quello che voglio, per ogni chiave e valore mi printa quello che voglio
    print(key)                          

for a, b, in utenti.items():                        #posso scriverlo anche così è uguale
    print(a)


for key in utenti:
    print(key)                                      #COSI NON FUNZIONA perchè non gli ho detto cosa voglio nel dizionario

for key in utenti.keys():                           #così va
    print(key)

maxValue=0                                          #VOLENDO IL MAGGIORE ALL'INTERNO DI UN DIZIONARIO
for value in utenti.values():
    if(value>maxValue):
        maxValue = value
print(maxValue)


#dato un numero che verrà dato all'input calcolarne tutti i divisori che non da resto, numero intero 

def Divis_num():

    my_num = int(input("scrivi un numero: "))
    new_list = []

    for i in range(my_num):
        if input%i == 0:                            #% viene messo proprio perchè è già una divisione che però considera solo il resto
            new_list.append(i)

    return new_list

print(Divis_num())
        



#DEFINIAMO UNA FUNZIONE VOID 

my_list = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
outfits = ["punk", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
sneakers = ["nike", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

#voglio una funzione in cui inizializzo una lista così quando la riprendo so che li dentro devo scrivere il nome della lista che mi serve cercare
def Checkname(list=[]):                                     #nel mio codice quando voglio dichiare una funzione mi serve per non stare a riscrivere di nuovo tutto il processo una seconda volta 
    quest = input("che taglio vuoi sapere?: ")              #ho scritto CHECKNAME() perchè le parentesi mi stanno indicando che è una funzione e mi sto aspettando una lista
    for i in range(len(list)):

        if quest == list[i]:
            print(f"il prezzo del taglio {quest} corrisponde a {my_list[i]} effettuato {last_week[i]}")
        else:
            pass


Checkname(hairstyles)                                       #qua sto richiamando la funzione così che mi faccia quel procedimento però per questa lista specifica

Checkname(outfits)

Checkname(sneakers)



#DEFINIAMO UNA FUNZIONE CON RETURN                          #mi serve per quando voglio riprendere un valore che sto facendo calcolare in questa funzione almeno ho quel valore salvato e dopo se mi serve di nuovo lo riutilizzo richiamandolo

def my_return_function():
    int = 5
    int_2 = 8
    sum = int + int_2
    return sum                                              #con return gli sto dicendo che mi deve dare un valore

my_return_value = my_return_function()                      #per memorizzare il valore che mi esce dalla funzione la devo applicare fuori e gli devo assocciare una variabile
sum_2 = my_return_value + 8                                 #quindi per riprendere il valore adesso devo usare la variabile che gli ho assocciato
print(sum_2)


#DEFINIAMO UNA FUNZIONE DI CHECK (CHE MI RITORNA TRUE E FALSE)

def Checkname(list=[]):                                             
    quest = input("che taglio vuoi sapere?: ")              
    for i in range(len(list)):

        if quest == list[i]:
            return True 
        else:
            pass                                            #se il taglio che gli scrivo non è all'interno della lista gli devo scrivere qua pass perchè se gli scrivo RETURN FALSE allora al primo termine della lista che non è uguale all'input mi darà FALSE


if (Checkname(hairstyles)):                                 #stiamo richiamando la funzione di prima ma è con TRUE E FALSE quindi dovrò mettere un if 
    print("gg")                                             #se la domanda è all'interno della lista che ti ho indicato printami quella parola se è TRUE (procedimento della funzione di prima)
else:
    print("nope")                                           #se non è così printami questa parola
