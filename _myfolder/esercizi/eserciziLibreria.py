import random

#CREA UNA LISTA BIDIMENSIONALE E PRINTARE ESTERNAMENTE GLI ELEMENTI RANDOMICI DELLE LISTE INTERNE
def createRandomList():
    random_list = []                                    #data una lista vuota
    for num in range (10) :                             #dati 10 elemnti du cui eseguo in
        random_list.append(random.randint(1,100))  
    return random_list

def convertToTuple(random_list):
    random_tuple = tuple(random_list)
    print(random_tuple)

convertToTuple(createRandomList())

#posso scrivere anche così una matrice vuota 

my_matrix = [[]]


#ESERCIZIO DEL PROF
my_matrix = [
    [],
    [],
    []
]

#all'interno metto un altro ciclo for che mi permette di eseguire n volte un determinato codice 
#all'intenrno dell'ultimo ciclo for vado a popolare in matrice 

for i in range(len(my_matrix)):
    for n in range(5):
        my_matrix[i].append(random.randint(1,100))
    print(my_matrix[i])


