#ESERCIZIO DEI CICLI FOR E DELLE SOTTRAZIONI

#hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

#prices = [30, 25, 40, 20, 20, 35, 50, 35]

#last_week = [2, 3, 5, 8, 4, 4, 6, 2]

#Date le seguenti liste:
#cacola e stampa a schermo la somma di tutti i prezzi

my_list = [30, 25, 40, 20, 20, 35, 50, 35]

sum = 0                                         #inizio definendo un totale iniziale = 0 e da lì aggiungerò ogni elemento della mia lista
for element in my_list:
    sum += element                              #aggiungo a zero i valori della lista
                    


#SOLUZIONE CON ELEMENTO BULTIN (SUM)  fa direttamente la somma di tutti gli elementi della lista

prices_sum = sum(my_list)          

#CONSEGNA1
#FACCIAMO LA MEDIA

my_list = [30, 25, 40, 20, 20, 35, 50, 35]

prices_sum = 0                                        
for element in my_list:
    prices_sum += element  

media_prices = prices_sum/len(my_list)              #potevo scrivere 8 per fare la media dei prezzi però metti caso che tolgo un numero dalla lista, li dovrò ricalcolare tutti e cambiare il numero ogni volta
print(media_prices)

#ALGORITMO serie di istruzione che ci permette di dare un output

#CONSEGNA2
#creare una nuova lista costituita da tutti i prezzi dei tagli scontati di 5 euro

my_list = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

new_list = []                               #listina vuota (questo serve per far memorizzare la nuova lista)
num_sot = 5
for element in my_list:
    new_list.append(element - 5)            #append serve per far sì che ogni elemento calcolato mi diventi una lista
                                            #se metto solo print dentro al ciclo for si mi fa la lista ma in realtà mi sta solo contando uno ad uno la sottrazione ma non li sta memorizzando
print(new_list)   

#FACCIAMO LA STESSA COSA DEL CICLO FOR MA IN UN ALTRO MODO (PIU SEMPLICE)
#inizializziamo una lista
#noi abbiamo direttamnte il calcolo del ciclo for all'interno della lista e quindi per ogni num in my_list gli diciamo num - 5
#quindi prima gli diciamo cosa deve fare e poi dove (toglimi 5 all'elemento per ogni elemento della lista)

new_list = [element-5 for element in my_list]

#CONSEGNA3
#tenendo in considerazione i tagli effettuati nella settimana "last_week" ed i loro prezzi calcolare il guadagno totale settimanale    


money_week = 0                                  #inizializzazione per forza nel momento in cui devo tenere in memoria un risultato che per adesso non ho
for i in range(len(last_week)):                 #range(len) prendo la lunghezza di una lista perchè tanto sono uguali il numero di termini che ci sono dentro, se no metto il numero di volte che voglio fa ripetere il ciclo

    money_week += new_list[i]*last_week[i]
print(money_week)                 
                                                #con i prendo 
                                                #faccio += perchè voglio che mi tenga in memoria tutti i risultati di ogni ciclo che faccio fare all'operazione
                                                #se no mettendo solamente = mi terrà in memoria solo l'ultimo valore quindi non posso fare un totale


#calcola la media di guadagno giornaliera

my_list = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

money_week = 0 
media_tot = 0                                 #inizializzazione per forza nel momento in cui devo tenere in memoria un risultato che per adesso non ho
for i in range(len(last_week)):                 #range(len) prendo la lunghezza di una lista perchè tanto sono uguali il numero di termini che ci sono dentro, se no metto il numero di volte che voglio fa ripetere il ciclo

    money_week += my_list[i]*last_week[i]


media_tot += money_week/7

print(media_tot)


#Crea una lista contenente i nomi dei tagli di capelli con un costo inferiore a 30 euro considerando i prezzi non scontati.
my_list = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

new_list = []

for i in range(len(hairstyles)):
    if last_week[i] > 3:
        new_list.append(hairstyles[i])
print(new_list)


#ESERCIZIO CON PREZZI MINORI DI 30 rifarlo con LIST COMPREHENSION
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 90, 45, 10, 14]
cuts_under_30 = []
for i in range(len(hairstyles)):
    if prices[i] <30:
        cuts_under_30.append(hairstyles[i])



#LIST COMPREHENSION del procedimento di prima
cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if prices[i] < 30]
print(cuts_under_30)
