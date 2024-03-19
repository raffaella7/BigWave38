#leggere il file di testo e crearne una lista di stringhe, è possibile farlo in due modi differenti.
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty("voices")      

engine.setProperty("voice", voices[0].id)


def ReadText():

    file = open("file.txt", "r")
    file_text = file.read()
    upper_file = file_text.upper()   
    upper_splitted_string = upper_file.split()
    print(upper_splitted_string)

    engine.say(upper_splitted_string)
    engine.runAndWait()
    

ReadText()