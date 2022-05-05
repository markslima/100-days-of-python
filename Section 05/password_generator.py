#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("\nWelcome to the PyPassword Generator!")
nr_letters= int(input("\n\nHow many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
letter_length = len(letters)
nums = len(numbers)
syms = len(symbols)
password = ""

for letter in range(nr_letters):
    random_letter = random.randint(0, 51)
    # print(letters[random_letter])
    password += letters[random_letter]

for num in range(nr_numbers):
    random_number = random.randint(0, 9)
    # print(numbers[random_number])
    password += str(numbers[random_number])

for symbol in range(nr_symbols):
    random_symbol = random.randint(0, 8)
    # print(symbols[random_symbol])
    password += str(symbols[random_symbol])

print(f"\nThere are {letter_length} letters.\n")
print(f"\nThere are {syms} symbols.\n")
print(f"\nThere are {nums} numbers.\n")

print(f"\nYour EASY LEVEL password is {password}\nKeep it safe!\n")

password_length = len(password)
# print(f"Your password is {password_length} characters long. \nThere are {letter_length} letters.\nThere are {syms} symbols.\nThere are {nums} numbers.\n")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
random_index = random.randint(0, password_length)
hard_pass = []
new_password = ""

for letter in password:
    hard_pass.append(letter)

random.shuffle(hard_pass)

# print(f"\nAnd now our HARD password in a list is: {hard_pass}\n")

for char in hard_pass:
    new_password += char

print(f"\nHARD Password is: {new_password}\n")

# print(f"\nYour HARD password is {new_password}\n")


# ------------------------------------------------ #
# nums = len(numbers)
# print(f"\nThere are {nums} numbers available.\n")

# 
# print(f"\nThere are {syms} symbols available.\n")

