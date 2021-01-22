#@dudushy @Drinpe

"""
00h00m00s
01
01:22
01:22:

"""

#imports
import datetime, os, time

#vars
now = datetime.datetime.now().strftime('%H') + ":" + datetime.datetime.now().strftime('%M')

#functions
def clear():
    os.system('cls') #windows: cls; linux: clear

def timer():
    pass

def alarm():
    pass

def menu():
    #menu loop
    while True:
        clear() #clear screen
        print(""
            + "/===========================================/\n"
            + "/                Timer v0.0.1               /\n"
            + f"/==================[{now}]==================/\n"
            + "\n/ 1. Timer"
            + "\n/ 2. Alarm"
            + "\n/ X. EXIT")
        #input and operation
        if input("/ :> ") == "1":
            timer()
        elif "2":
            alarm()
        elif "X" or "x":
            break

#main
