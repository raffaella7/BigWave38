import os

#OS = OPERATIVE SYSTEM
os.mkdir()
os.removedirs()                 #rimuovo la directory dato il nome

#dato uno specifico path cambiare cartelle 
os.chdir

#possiamo eseguire codice come se lo stessimo eseguendo all'interno del sistema di prompt


#IMPORT OS                                                                                  #os serve per controllare se ci sono determinati file 
    

import os

os.chdir("C:\Users\Master/Desktop")                                                         #cambio la directory, gli dico dove voglio che lui vada (in questo caso desktop)
os.mkdir("C:/Users/Master/Documents/BigWave38/_myfolder/lezioni/new_folder")                #qua sto creando una nuova cartella (devo mettere il nome della nuova cartella alla fine)
folder = os.path.exists("C:/Users/Master/Documents/BigWave38/_myfolder/lezioni/new_folder") #con questo comando sto controllando se effettivamente ho creato quella cartella di prima)
print(folder)                                                                               #mi uscirà True

os.removedirs("C:/Users/Master/Documents/BigWave38/_myfolder/lezioni/new_folder")           #con questo comando sto rimuovendo la cartella che ho creato

folder = os.path.exists("C:/Users/Master/Documents/BigWave38/_myfolder/lezioni/new_folder") #e adesso mi dirà che non esiste più perchè la ho rimossa
print(folder)                                                                               #mi uscirà False


#
os.chdir(os.path.dirname(os.path.realpath(__file__)))


os.remove("new_file.txt")