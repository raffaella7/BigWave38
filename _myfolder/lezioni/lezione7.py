my_string = "!questa è la mia stringa!"

upper_string = my_string.upper()            #possiamo trasformare tutti i nostri caratteri della stringa in maiuscolo
print(upper_string)
lower_string = upper_string.lower()         #la stessa cosa ma in minuscolo

title_string = my_string.title()            #mettere la maiuscola ad ogni prima lettera di ogni parola della stringa

splitted_string = my_string.split()         #una stringa splittata mi da una lista con tutti gli elementi della stringa splittati in base al () perchè prende in considerazione lo spazio
#posso scriverlo anche così (a) e mi splitta tutto togliendo tutte le a

joined_string = " ".join(splitted_string)   #per mettere insieme di nuovo la stringa che mi ricompone tutte le parole che erano in una lista e me le mette insieme ad una stringa unica
#potevo anche scrivere così "+"
replaced_string = my_string.replace("è",)         #ci permette di trovare un elemento all'interno della stringa che gli diamo come argomento e sostituirlo con un elemento nuovo che gli diamo come secondo elemento nella stringa

#per dirgli quanti elementi vogliamo sostituire allora lo scrivo con l'indice
replaced_string= my_string.replace("è", "non è", 4)

my_stripped_string = my_string.strip()       #messa così elimina tutti gli spazi vuoti all'inizio e alla fine della stringa
#se gli fornisco un argomento eliminaa quel carattere sempre all'inizio e alla fine della stringa
my_stripped_string = my_string.strip("!")
element_in_string =  my_string.find("è")                       #è possibile trovare l'indice di quello che voglio cercare
#mi printa l'indice in cui trova la prima è

