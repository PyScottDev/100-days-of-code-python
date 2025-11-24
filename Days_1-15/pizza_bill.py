# print("Welcome to Scott's pizzaria")

# size = input("What size pizza would you like? Type s for small, m for medium and l for large: ")
# bill = 0
# pepperoni = input("Would you like pepperoni? Type y for yes and n for no: ")

# if size == "s":
#     bill += 15

#     if pepperoni == "y":
#         bill += 2

# if size == "m":
#     bill +=20

#     if pepperoni == "y":
#         bill += 3

# if size == "l":
#     bill += 25

#     if pepperoni == "y":
#         bill += 3



# extra_cheese = input("Would you like extra cheese? Type y for yes and n for no: ")

# if extra_cheese == "y":
#     bill += 1

# print(f"Your final bill is ${bill}")

age = int(input("What is your age? "))

if age < 12:
    bill = 5
elif age <= 18:
    bill = 7
# TODO: add new rule here
elif 44 < age < 56:
    print("No worries, it's on us")
    bill = 0
else:
    bill = 12

print(f"So, that'll be ${bill}")
