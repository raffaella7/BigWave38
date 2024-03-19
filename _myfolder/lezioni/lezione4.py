#RESPONSABILITA' SINGOLA = una funzione fa solo quel procedimento o quel calcolo, non ne metto di più



#SLICING = data una lista è una sintassi che ci permette di ottenere solo alcuni elementi di quella lista e può essere utilizzata per cerare una nuova lista
#sintassi dello slicing si ottiene con i due punti e u n indice di lista

my_list = [1, 2, 3, 4]

my_sliced_list_1 = my_list [:1]                 #i due punti prima del numero ci dice che a partire dalla lista mantengo solo quel numero indiciato
                                                #a partire dall'inizio della lista my_list prendo un elemento NON L'INDICE quindi si parte da 1

my_sliced_list_2 = my_list [1:]                 #i due putni alla fine elimina solo un elemento, partendo da sinistra ([2:] così stiamo eliminando due elementi)
my_sliced_list_2 = my_list [:-1]                #indice negativo elimino solo l'ultimo elemento della lista
my_sliced_list_2 = my_list [-1:]                #mantengo solo l'ultimo elemento della lista
my_sliced_list_2 = my_list [0:2]                #mantengo solo (1,2) perchè l'1 è indicato come indico 0 e tutto quello che viene dopo quel numero prima dell'indice 2 (che è il 3 nella lista) viene printato 
#  IL PRIMO E' INCLUSIVO E IL SECONDO INVECE E' ESCLUSIVO QUINDI NON LO DEVE CONTARE MA VIENE VISTO COME FINE DELLA LISTA DI TUTTI GLI ELEMENTI CHE DEVE CONTARE

my_sliced_list_2 = my_list [0:2]     
#   QUESTO PRINTA QUESTO: [1,2]

my_sliced_list_3 = my_list [1:3]
#   QUESTO PRINTA QUESTO: [2,3]                 #il 4 non me lo printa perchè è ha come indice 3 e gli sto dicendo di escluderlo


print(my_sliced_list_1)