#Crea una funzione che permetta di scrivere file txt data una stringa come argomento
#Crea una funzione che permetta di updetare file txt data una stringa come argomento 
#Crea una funzione che permetta di leggere un file txt e, restituisca una lista ed il numero di elementi all' interno della lista
"""
#"a" "w", "r"
new_file = open("new_file.txt", "w")            #apriamo un file di testo in modalità scrittura
new_file.write ("HELLO, WORLD")                 #quando andiamo a scrivere un file di testo, questo verrà sovrascritto e quello che c'è scritto nel file 
new_file.close()                                #se vogliamo aggiungere nuove righe o nuove stringhe allora usiamo APPEND

#e così posso solo scriverci
#SE VOGLIO ANCHE LEGGERLO ALLORA DEVO SCRIVERE COSI
new_file = open("new_file.txt", "w+")
new_file.write("hello world")
text = new_file.read()
new_file.close()
#se vogliamo leggere quello che c'è nel file di testo allora utilizziamo READ

#se voglio aggiungere 
new_file = open("new_file.txt", "a")
new_file.write("\nsecond string")
new_file.close()


#se voglio leggerlo
new_file = open("new_file.txt", "r")
print(file_text)
new_file.close()
#restituisce una lista con ogni elemento che corrisponde a tutte le linee di testo


print("prima riga\seconda riga\n")                          #se vogliamo scrivere tutto in una sola stringa ma poi vogliamo che la seconda linea la voglio comunque a capo allora lo scrivo così

#CONSIGLIATO DI NON USARE
#"a+"                                                       #mi serve per avere sia append che read
#"w+"                                                       #mi serve sia per write che per read
#"r+"                                                       #mi serve per read e append
"""

def WriteText():
    new_file = open("new_file.txt", "w")
    new_file.write ("Buongiorno gente")
    new_file.close()

def AppendText():
    new_file = open("new_file.txt", "a")
    new_file.write("\nvorrei vedere le stelle\nimmerso nell'erba alta")
    new_file.close()

def ReadText():
    new_file = open("new_file.txt")
    file_text = new_file.readlines()

    new_list_file = [linea.strip() for linea in file_text]
    print(new_list_file)
    
    #non è completo
    #with open("new_file.txt", "r") as f:                               #così mi printa come è printata nel file text, quindi proprio a testo
     #   print(f.read())


    new_file.close()



WriteText()
AppendText()
ReadText() 