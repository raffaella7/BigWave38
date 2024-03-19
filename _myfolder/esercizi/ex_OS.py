import os
import time

def NewFolder():
    os.chdir("C:/Users/Master/Desktop")     
    os.mkdir("new_folder") 
    return True     


def Check():
    folder = os.path.exists("C:/Users/Master/Desktop/new_folder")
    print(folder)
    time.sleep(5)
    


def DeleteFolder():
    os.chdir("C:/Users/Master/Desktop")
    os.removedirs("new_folder")   


def Main():
    if NewFolder() == True :
        Check()
        DeleteFolder()
    else: 
        print("non esiste niente")


Main()