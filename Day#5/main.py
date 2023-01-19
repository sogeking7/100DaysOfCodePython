#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

ll = ""
ss = ""
nn = ""

for i in range(nr_letters):
    ll += letters[random.randint(0, len(letters)-1)]
for i in range(nr_numbers):
    nn += numbers[random.randint(0, len(numbers)-1)]
for i in range(nr_symbols):
    ss += symbols[random.randint(0, len(symbols)-1)]

print(f"Eazy level: {ll+ss+nn}")


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


rol = random.randint(0, 2)
ans = ""

if rol == 0:
    ans = ll + (nn+ss if random.randint(0, 1) else ss+nn)
elif rol == 1:
    x = random.randint(0, 1)
    ans = (nn if x else ss) + ll + (ss if x else nn)
else:
    ans = (nn+ss if random.randint(0, 1) else ss+nn) + ll

print(f"Hard level: {ans}")