#METODI RICHIAMATI DALLE LISTE (OGNI LISTA E' UNA CLASSE)

import os
#PRIMO METODO APPEND
my_list = []

my_list_2 = my_list.copy()        #in base ad una lista popolata mi fa copare gli elementi di una lista in un'altra, non c'è bisogno di inizializzare un'altra lista

my_list.clear()                   #prendiamo una lista e le togliamo tutti gli elementi

my_list.pop()                     #eliminiamo l'elemento all'ultimo indice della lista
my_list.pop(0)                    #toglierò solo quel l'indice

my_list = ["hello"]
my_list_2 = ["world"]
my_list_2.extended(my_list)       #in base a due liste: prendiamo una lista con dentro degli elementi e la estendomettendo gli elementi di un'altra lista dentro
#quindi mi printa una lista con dentro hello world

counter = my_list.count("hello")  #mi permette di contare quante volte è presente una stringa all'interno di una lista
#gli devo dare il parametro nell'argomento

my_list.reverse()                   #reverse: prendiamo una lista e revertiamo gli elementi all'interno

my_list.index("hello")              #trova il primo elemento all'interno della lista e ci da l'indice dell'elemento

my_list.insert(0, "new object")     #inseriamo ad uno specifico indice un nuovo elemento

my_numeric_list = [3, 2, 1, 5]
my_numeric_list.sort()              #riordina gli elementi in una lista alfabeticamente oppure numericamente (anche con le parole)

my_list.remove("ciao")              #rimuove solo quel determinato elemento che gli metto come argomento


print(os.path.dirname(__file__) + r"\new_file.txt")
