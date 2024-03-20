#CHAT BOT CON CLAUDE
import os
import anthropic
def continue_chat():
    cicle = input("do you want to a<sk me something lse? Y/N\n").lower()
    while True:
        if cicle == "n":
            return False
        elif cicle == "y":
            return True
        else:
            print("insert a correct respoonse")



def chat (client):
    current_question = input("ask me something:")   #si prende un input
    current_chat =[ {"role": "user", "content": current_question}]  #inserisce l'input in un dizionario che verrà passato a claude che conseguentemente ritornerà una risposta

    message = client.messages.create(
    model = "claude-3-opus-20240229",               #il modello di anthropic che vogliamo utilizzare
    max_tokens=500,                                 #numero massimo di token che deve avere il messaggio in risposta
    temperature=0.0,                                #grado di creatività che da come risposta
    system="respond only in yoda-speak.",           #prompt di sistema che gli diamo per andare a chiedere a claude come deve rispondere
)
    
    return(message.content[0].text)                 #qui gli mettiamo dentro il nostro dizionario 
#ci prendiamo dalla variabile message un content e dal content gli prendiamo l'indice 0 che è la prima parte e poi trasformarlo in testo
#così sa che siamo gli user e che il nostro 

def main():
    with open(os.path.dirname(__file__) +"\api-key.txt") as api_key_file:
        api_key_string = api_key_file.readline()
        print(api_key_string)

    anthropic_client = anthropic.Anthropic(api_key = api_key_string) #non appena ho l'apikey stringa gliela passo ad anthropic 

    check = True
    while check == True:
        response = chat(anthropic_client)
        print(response)
        check = continue_chat()


main()