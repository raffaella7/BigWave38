#DIZIONARI RECAP

utenti = {
    "Alberto": 22,
    "Raffaella": 22,
    "David": 25
}

print(utenti["Alberto"])                            #posso richiamarlo e mi printa quello che gli ho assegnato

utenti["Alberto"] = 15                              #attenzione perchè in questo modo il valore vecchio non ha più senso


for key, value  in utenti.items():                  #adesso posso fare quello che voglio, per ogni chiave e valore mi printa quello che voglio
    print(key)                          

for a, b, in utenti.items():                        #posso scriverlo anche così è uguale
    print(a)


for key in utenti:
    print(key)                                      #COSI NON FUNZIONA perchè non gli ho detto cosa voglio nel dizionario

for key in utenti.keys():                           #così va
    print(key)

maxValue=0                                          #VOLENDO IL MAGGIORE ALL'INTERNO DI UN DIZIONARIO
for value in utenti.values():
    if(value>maxValue):
        maxValue = value
print(maxValue)


#dato un numero che verrà dato all'input calcolarne tutti i divisori che non da resto, numero intero 

def Divis_num():

    my_num = int(input("scrivi un numero: "))
    new_list = []

    for i in range(my_num):
        if input%i == 0:                            #% viene messo proprio perchè è già una divisione che però considera solo il resto
            new_list.append(i)

    return new_list

print(Divis_num())
        



