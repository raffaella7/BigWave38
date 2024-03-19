import random                                           #permette
                                                        #determinati da un seed = numero non statico ma ha la responsabilità di generare la randomitàdelle funzioni
                                                        #se noi stabiliamo lo stesso seed dentro le funzioni che lo richiedono possiamo avere lo stesso risultato

my_list = [1, 2, 3, 4, 5]

#RADINT
random_num = random.randint(1,100)


#restituisce un numero intero ranodmico in range A-B inclusivo
#quindi ci restituisce un numero randomico tra 1 e 100
#richiede ad argomento due valori

#RANDOM RANGE 
#ci permette di avere un numero all'interno di un range ma ESCLUSIVE (solo l'ultimo)
random_range = random.randrange(1,100)


#RANDOM CHOISE
#dato una lista o datatype che contiene più elementi di ottenere uno di quei elementi randomicamente
random_choice_num = random.choice(my_list)
print(random_choice_num)

random_list = []                                                    #data una lista vuota
for num in range (10):                                              #dati 10 elementi su cui eseguo in 
    random_list.append(random.randint(1,100))


#FUNZIONE SAMPLE
#estrae un numero dato ad argomento data una determinata lista da cui estrarli (mi estrae quel numero di elementi dalla lista, glielo dico io quanti)
randomized_list = random.sample(list(range(1000)),12)
print(randomized_list)

#il 12 sta per il numero di elementi che voglio nella mia lista

#questo è un altro modo di scrivere la stessa cosa sopra



#LIBRERIA OS 
#andiamo a modificare il sistema operativo

#creare nuove cartelle
#mkdir new_folder = creo una cartella
#rmdir new_folder = rimuovo la cartella





