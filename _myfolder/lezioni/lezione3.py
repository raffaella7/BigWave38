#FUNZIONI
#come key word dobbiamo mettere DEF poi il nome della funzione ed eventualmente dei parametri

#qua stiamo definiendo una funzione ma non la stiamo richiamando (quello sotto scritto nelle tre righe si chiama profetto)
def my_function():                                              # avoid: funzione che non ha valori di ritorno e non ha paramteir ma potrebbero esserci
    print("this is my new function")                            #quando verrà richiamata non darà i valori di ritorno ma permette di eseguire qualcos altro
                                                                #differenza tra avoid e funzione con valori di ritorno: la seconda ci ritornerà con il comando RETURN un valore, la prima invece permette una determinata esecuuzione di codice e non può essere utilizzato con il comando di return
my_function()

#funzione con valori di ritorno                                 #questo valore di ritorno possiamo riprenderla anche quando la richiamiamo
def my_return_function():
    int = 3
    int_2 = 8
    sum = int + int_2
    return sum

my_returned_value = my_return_function()                        #le funzioni sono imporatanti per incapsulare parti di codice per poterne gestire la complessità e per poter avere all'interno del ritorno solo quello che c'è necessario della funzione senza riscriere il codice
sum_2 = my_returned_value + 8
print(sum_2)


#PARAMETRI E ARGOMENTI DI FUNZIONE                                    #se la funzione richiede degli argomenti 
def my_function(param):                                               #questa riga viene definita HEADER
    new_val = param + 5                                               #tutto quello che c'è sotto l'HEADER si chiama CORPO
    return new_val  

ext_val = my_function(5)
print(ext_val)


#LE FUNZIONI POSSONO AVERE ANCHE PIU DI UN PARAMETRO
def my_function(param, param_2 = 2):                                 #i parametri definiti devono essere messi dopo a quelli non definiti
    new_val = param + param_2                                        #tutto quello che c'è sotto l'HEADER si chiama CORPO
    return new_val  

ext_val = my_function(5, 5)
print(ext_val)

#REFATTORARE                                                       #prendere dei codici che sono già scritti , ovvero combinare i fattori di quel codice implementando delle funzioni che 
#SCALABILITA'                                                      #possibilità di estendere il codice in maniera idtruttiva (se io vado a crearmi delle funzioni o classi devo pensare in ottica di utilizzare o modificare 
#un progetto scalabile non si rompe anche modificandolo, perchè ho incapsulato il mio codice so cosa devo andare a modificare senza rompere nulla
#principi specifici da seguire


#RICHIAMARE UN ALTRO SCRIPT IN UNO SCRIPT
import lezione2                                                  #scrivere il nome dell'altro script che voglio importare

#eseguo tutto lo script 
#se ho una definizione che ho già detto di printarla nell'altro script anche se scrivo così

#in un altro script se magari ho queste funzioni posso importarle in un altro


def my_first_function():
    return "this is my first function"

def my_second_function():
    return "this is my second function"

def my_third_function():
    return "this is mu third function"

##scrivendo solo così avrò delle funzioni singolari, quindi nello script dove voglio importare queste cose scrivo questo:

print(import.my_second_function())

#se invece mi serve tutte le funzioni vado ad inserire quello che voglio che facciano le funzioni di prima all'interno di un gate che si deve chiamare "MAIN"

def main():
    
    print(my_first_function())
    print(my_second_function())
    print(my_third_function())

if _name_ == "_main_":                          #DEVE ESSERE SCRITTO PER FORZA COSI' CON GLI UNDERSCORE
    main()


#quindi nello script in cui voglio importare tutte queste funzioni scrivo questo:

script.main()                                   #script = il nome dello script che mi serve




print()
input()

str()
int()
float()

int = 5
toFloat = float(int)
print(toFloat)

my_string = "0.0001"
print(len(my_string))

my_list = [0, True, 0.5, "hello"]
print(len(my_list[3]))


#funzioni min e max: data una lista di numeri interi, ci permettono di printare il numero magg o min di una lista
my_numbers = [1,2,3,4,5]

print(min(my_numbers))
print(max(my_numbers))

#abbiamo un float di una lunghezza e vogliamo arrotondarlo per andare ad ottenere il float arrotondato
my_float = 0.1221
print(round(my_float, 3))  #il tre è il numero di cifre a cui voglio arrotondare il numero (quindi mi esce 0,122)

#funzione HELP
#data una funzione ci restituisce della documentazione relativa alla funzione che stiamo utilizzando
#utile perchè se gli diamo degli oggetti ci da una spiegazione
my_list = [0, True, 0.5, "hello"]
len(my_list[3])

help(len(my_list[3]))


#FOR I (FONDAMENTALE)
prices_sum1 = 0                         #dobbiamo sempre inizializzare 
for price in prices:
    prices_sum1 += price

prices_sum2 = 0
for i in range(len(prices)):
    prices_sum2 += prices[i]


                                        #non si può ciclare su solo un intero devo per forza mettere sempre range

