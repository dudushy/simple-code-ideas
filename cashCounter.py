# imports
import os, time

# vars
loop = "y"
money = {
    'init_money': 0.0,
    'crrt_money': 0.0,
    '100_bill': 0,
    '50_bill': 0,
    '20_bill': 0,
    '10_bill': 0,
    '5_bill': 0,
    '1_bill': 0,
    '75_cent': 0,
    '50_cent': 0,
    '25_cent': 0,
    '10_cent': 0,
    '5_cent': 0,
    '1_cent': 0
}

# functions
def clear():
    os.system('cls') #'cls' for windows // 'clear' for linux/android

def loadAnimation(seconds):
    while seconds > 0:
        for i in '/-\|':
            clear()
            print(f'Calculating...{i}\n')
            time.sleep(.2)
        seconds -= 1
    clear()

# main
while loop == "y":
    clear()

    while True:
        try:
            clear()
            money['init_money'] = float(input('Please insert how much money do you want to count | example (14.98): '))
            break #if the value checks as a flot: pass
        except Exception as e:
            continue #if the value isn't a float: fail

    loadAnimation(2)

    money['crrt_money'] = money['init_money']
    while True:
        if money['crrt_money'] >= 100:
            money['crrt_money'] -= 100
            money['100_bill'] += 1
            continue
        if money['crrt_money'] >= 50:
            money['crrt_money'] -= 50
            money['50_bill'] += 1
            continue
        if money['crrt_money'] >= 20:
            money['crrt_money'] -= 20
            money['20_bill'] += 1
            continue
        if money['crrt_money'] >= 10:
            money['crrt_money'] -= 10
            money['10_bill'] += 1
            continue
        if money['crrt_money'] >= 5:
            money['crrt_money'] -= 5
            money['5_bill'] += 1
            continue
        if money['crrt_money'] >= 1:
            money['crrt_money'] -= 1
            money['1_bill'] += 1
            continue
        if money['crrt_money'] >= 0.75:
            money['crrt_money'] -= 0.75
            money['75_cent'] += 1
            continue
        if money['crrt_money'] >= 0.50:
            money['crrt_money'] -= 0.50
            money['50_cent'] += 1
            continue
        if money['crrt_money'] >= 0.25:
            money['crrt_money'] -= 0.25
            money['25_cent'] += 1
            continue
        if money['crrt_money'] >= 0.10:
            money['crrt_money'] -= 0.10
            money['10_cent'] += 1
            continue
        if money['crrt_money'] >= 0.05:
            money['crrt_money'] -= 0.05
            money['5_cent'] += 1
            continue
        if money['crrt_money'] >= 0.01:
                money['crrt_money'] -= 0.01
                money['1_cent'] += 1
                continue
        break

    clear()
    print(f"-Amount [${money['init_money']}]\n")
    if money['100_bill'] != 0:
        print(f"@ [{money['100_bill']}] $100")
    if money['50_bill'] != 0:
        print(f"@ [{money['50_bill']}] $50")
    if money['20_bill'] != 0:
        print(f"@ [{money['20_bill']}] $20")
    if money['10_bill'] != 0:
        print(f"@ [{money['10_bill']}] $10")
    if money['5_bill'] != 0:
        print(f"@ [{money['5_bill']}] $5")
    if money['1_bill'] != 0:
        print(f"@ [{money['1_bill']}] $1")
    if money['75_cent'] != 0:
        print(f"@ [{money['75_cent']}] $0.75")
    if money['50_cent'] != 0:
        print(f"@ [{money['50_cent']}] $0.50")
    if money['25_cent'] != 0:
        print(f"@ [{money['25_cent']}] $0.25")
    if money['10_cent'] != 0:
        print(f"@ [{money['10_cent']}] $0.10")
    if money['5_cent'] != 0:
        print(f"@ [{money['5_cent']}] $0.05")
    if money['1_cent'] != 0:
        print(f"@ [{money['1_cent']}] $0.01")
    
    loop = input('\nDo you want to calculate again? (y/n): ')