# imports
import os, random

# vars
lowers = 'abcdefghijklmnopqrstuvwxyz'
uppers = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = "!@#$%&*()_-+=\/|,.<>:;][?'"
password = ''

# main
os.system('cls') # 'cls' for windows, 'clear' for linux/android

for i in range(18):
    lowerChar = lowers[random.randrange(len(lowers))]
    upperChar = uppers[random.randrange(len(uppers))]
    numberChar = numbers[random.randrange(len(numbers))]
    symbolChar = symbols[random.randrange(len(symbols))]

    char = random.choices([lowerChar, upperChar, numberChar, symbolChar],[25, 25, 25, 25], k=1)

    password += char[0]
print(f'Strong password: {password}\n')

os.system('pause')

"""
for char in range(18):
    password += random.choices([lowers[random.randrange(len(lowers))], uppers[random.randrange(len(uppers))], numbers[random.randrange(len(numbers))], symbols[random.randrange(len(symbols))]],[25, 25, 25, 25], k=1)[0]
    print(f'Strong password: {password}\n')
"""
