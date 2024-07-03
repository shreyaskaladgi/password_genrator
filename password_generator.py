import random

print('welcome to your password generator')

chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*()_+=-1234567890?/.,[]\"`;:'

number = input('Amount of password to generate:')
number = int(number)

length= input('Your password length')
length=int(length)

print('here are your passwords')

for pwd in range(number):
    passwords =''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)
