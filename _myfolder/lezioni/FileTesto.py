#SCRIVERE FILE SU PYTHON
#rciordarsi sempre di chiudere il file se ho finito

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
print(new_file)
new_file.close()
#restituisce una lista con ogni elemento che corrisponde a tutte le linee di testo


print("prima riga\seconda riga\n")                          #se vogliamo scrivere tutto in una sola stringa ma poi vogliamo che la seconda linea la voglio comunque a capo allora lo scrivo così

#CONSIGLIATO DI NON USARE
#"a+"                                                       #mi serve per avere sia append che read
#"w+"                                                       #mi serve sia per write che per read
#"r+"                                                       #mi serve per read e append



#WITH OPEN (IL FILE SI CHIUDE DA SOLO)

with open("new_file.txt", "a") as new_file:
    new_file.write("\nanother string")                      #questa sintassi corrisponde ad append ma il file si chiude da solo quando noi usciamo dal codice



