#random password!!
import random

chars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM123456789!@#$%^&"

purp = input('what is your password for? ')

for k in range(0, 10):
    password = ''
    for k in range(0,18):
        password_chars = random.choice(chars)
        password = password + password_chars

with open('myPasswords.txt', 'a') as fileM:
    fileM.write(f"{purp}: {password}\n")