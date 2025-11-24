import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

letter_list = []
symbol_list = []
number_list = []


for letter_choice in range (nr_letters):
    letter_list.append(letters[random.randint(0, 25)])

print(letter_list) #for debugging

for number_choice in range (nr_numbers):
    number_list.append(numbers[random.randint(0, 9)])

print(number_list) #for debugging

for symbol_choice in range (nr_symbols):
    symbol_list.append(symbols[random.randint(0, 7)])

print(symbol_list) #for debugging


password_list = letter_list + symbol_list + number_list
print(password_list)

random.shuffle(password_list)
digit_counter = 0
password = "".join(password_list)


# for pass_digit in range(len(password_list)):
#     password += (str(password_list[pass_digit]))

print(f"Your password is {password}")