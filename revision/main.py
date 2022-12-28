import random

# Password Generator

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
           'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
sm_letters = []
for i in letters:
    sm_letters.append(i.lower())

letters+=sm_letters

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

symbols = ['#', '$', '%', '!', '@', '&']

nl = random.randint(8, 12)
nn = random.randint(6, 8)
ns = random.randint(2, 4)

password_l = []

for i in range(nl):
    password_l+=random.choice(letters)

for i in range(nn):
    password_l+=random.choice(numbers)

for i in range(ns):
    password_l+=random.choice(symbols)

random.shuffle(password_l)
password = ''
for char in password_l:
    password+=char
# print(password)