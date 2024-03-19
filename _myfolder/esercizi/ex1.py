#ESERCIZIO ESEGUIBILE


#dato un numero che verrà dato all'input calcolarne tutti i divisori che non da resto, numero intero 


def Divis_num():

    my_num = int(input("scrivi un numero: "))
    new_list = []

    for i in range(my_num):
        if input%i == 0:                            #% viene messo proprio perchè è già una divisione che però considera solo il resto
            new_list.append(i)

    return new_list

def main():
    print(Divis_num())

if __name__ == "__main__":                          #DEVE ESSERE SCRITTO PER FORZA COSI' CON GLI UNDERSCORE
    main()
        




