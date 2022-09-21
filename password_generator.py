#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password_list = []
choice_letters = ''
choice_symbols = ''
choice_numbers = ''

#generates random letters and append
for letter in range(nr_letters):
    choice = random.choice(letters)
    password_list.append(choice)
    choice_letters = choice_letters + choice


#generates random symbols and append
for symbol in range(nr_symbols):
    choice = random.choice(symbols)
    password_list.append(choice)
    choice_symbols = choice_symbols + choice

#generates random numbers and append
for number in range(nr_numbers):
    choice = random.choice(numbers)
    password_list.append(choice)
    choice_numbers = choice_numbers + choice

easy_password = choice_letters + choice_numbers + choice_symbols

print("Your easy level generated password is", easy_password)


# print(password_list)
# hard_password = random.shuffle(password_list)

hard_password = ''
for character in password_list:
    hard_password = hard_password + random.choice(password_list)

print("Your hard level generated password is", hard_password)
