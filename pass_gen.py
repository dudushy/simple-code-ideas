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
for char in range(18):
    password += random.choices([lowers[random.randrange(len(lowers))], uppers[random.randrange(len(uppers))], numbers[random.randrange(len(numbers))], symbols[random.randrange(len(symbols))]],[25, 25, 25, 25], k=1)[0]
print(f'Strong password: {password}\n')
os.system('pause')
