#FORME DI SCRITTURA
#pascal case: MyMatrix
#snake case: mymatrix 
#camel case: myMatrix

#questi sono datatypes
string = "abcde"
#print(string)

my_int = 5
print(my_int)
#a livello di calcolo computazionale permettono una maggiore ottimizzazione

my_float = 5.52
print(my_float)

my_bool = True
print(my_bool)

my_dict = {"key" : "value"}
print(my_dict)

my_list = [True, "hello", 25, 1, 1.25]


my_input = input("inserisci qui il tuo input: ")
print(my_input)

#possiamo sommare/sottrarre/moltiplicare due float o due int
my_sun = 5 +3
print(my_sun)

my_subraction = 5 -3
print(my_subraction)

my_multiplication = 5*5
print(my_multiplication)

#in questo caso mi esce un float perchè la divisione mi porta ad un numero decimale
#in questo caso mi esce un int perchè mi deve uscire un numero intero
my_floor_division = 6/3


#se vogliamo ottimmizare le nostre stringhe o variabili mettiamo una f all inizio della strinfa e nelle parentesi graffe 
#formattare la stringa 
#se è una stringa normale non cambia nulla ma se la formatto posso inserire 

my_division = True
print(f"this is my_division: {my_division}")
my_division = False

my_floor_division = 6//3
print(f"this is my_floor_division: {my_floor_division}")

#esponenziale
my_exp = 3**2
print(my_exp)
#commenti multinea come stringhe multilinea quindi non viene eseguito e non da problemi al programma o anche una stringa multilinea

string = """
questo
è
un
commento
multilinea
"""

print(string)


#assegnazione multipla: se vogliamo assegnare più variabili in una singola stringa di codice devo fare così

my_int, my_string, my_float = 5, "hello", 5.3

print(my_int)
print(my_string)
print(my_float)

#attenzione i valori devono essere assegnati nel modo in cui sono assegnate le variabili

#operatore modulo stampa il resto della divisione, serve in calcoli specifici
my_module = 6%4
print(my_module)
my_module = 6%3
print(my_module)
my_module = 6%5
print(my_module)
