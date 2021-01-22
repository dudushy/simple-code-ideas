#@dudushy @Drinpe

"""
00h00m00s
01
01 = 1

"""

#imports
import datetime, os, time

#vars
nowHM = datetime.datetime.now().strftime('%H') + ":" + datetime.datetime.now().strftime('%M') #date format HH:MM

#functions
def clear():
    os.system('cls') #windows: cls; linux: clear

def getNow():
    return datetime.datetime.now().strftime('%H') + ":" + datetime.datetime.now().strftime('%M') + ":" + datetime.datetime.now().strftime('%S') #date format HH:MM:SS

def timer():
    header = ("/===========================================/\n"
            + "/           Timer v0.0.1 [timer]            /\n" 
            + f"/==================[{nowHM}]==================/\n")

    #get HH:MM:SS
    print(header
        + "/ Let's set a timer, for how long?")
    hours = input("/ Enter the hours: \n/ :> ")
    clear()
    print(header
        + "/ Let's set a timer, for how long?")
    minutes = input(f"/ Enter the minutes: \n/ :> {hours}:")
    clear()
    print(header
        + "/ Let's set a timer, for how long?")
    seconds = input(f"/ Enter the seconds: \n/ :> {hours}:{minutes}:")
    print(f"{hours}:{minutes}:{seconds}")

    #calculate how long to wait  
    waitS = (int(hours) * 3600) + (int(minutes) * 60) + int(seconds) #in seconds

    #actual wait loop
    while waitS != 0:
        clear()
        #string manipulation 0 before number below 10 -> 0X --begin
        if int(hours) < 10:
            hours = f"0{int(hours)}"
        if int(minutes) < 10:
            minutes = f"0{int(minutes)}"
        if int(seconds) < 10:
            seconds = f"0{int(seconds)}"
        #string manipulation 0 before number below 10 -> 0X --end
        
        print(f"Remaining time = [{hours}:{minutes}:{seconds}]")
        time.sleep(1)
        seconds = int(seconds) - 1
        if seconds == 0:
            minutes = int(minutes) - 1
            seconds = 60
        if minutes == 60:
            hours = int(hours) - 1
            minutes = 0
        waitS -= 1
    clear()
    print("Done!")



def alarm():
    #calculate how long to wait -begin
    #now string = "HH:MM:SS"
    nowH = getNow()[0:2] #"HH:MM:SS" [0:2]
    nowM = getNow()[3:5] #"HH:MM:SS" [3:5]
    nowS = getNow()[6:8] #"HH:MM:SS" [6:8]

    waitS = None #in seconds
    #calculate how long to wait -end

    #actual wait
    time.sleep(waitS)

def menu():
    header = ("/===========================================/\n"
            + "/                Timer v0.0.1               /\n" 
            + f"/==================[{nowHM}]==================/\n")
    
    #menu loop
    while True:
        clear() #clear screen
        print(header
            + "/ 1. Timer\n"
            + "/ 2. Alarm\n"
            + "/ X. EXIT")
        #input and operation
        if input("/ :> ") == "1":
            timer()
        elif "2":
            alarm()
        elif "X" or "x":
            break

#main
timer()
os.system('pause')