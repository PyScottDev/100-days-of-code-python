# # Ask for fist number
# n1 = float(input("What's the first number?: "))

# # Print the operators
# for op in operations:
#      print(op)
# #Ask which operation
# op_choice = input("Pick an operation: ")

# # Ask for second number
# n2 = float(input("What's the second number?: "))

# # Continue with same number
# cont_same = input("Type Y to continue with {answer} or N to start a new calculation: ").upper()
from ASCII_art import calculator_image

print(calculator_image)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

first_choice = 0.0
# result = operations["*"](4, 8)
# print(result)

def first_number():
    first_choice = float(input("What's the first number?: "))
    return first_choice

n1 = first_choice

continue_calculations = True
new_calculation = True

while continue_calculations:
    while new_calculation == True:
        n1 = float(input("What's the first number?: "))
        new_calculation = False
    for op in operations:
        print(op)
    op_choice = input("Pick an operation: ")
    n2 = float(input("What's the second number?: "))
    result = operations[op_choice](n1, n2)
    print(f"{n1} {op_choice} {n2} = {result}")
    cont_same = input(f"Type Y to continue with {result} or N to start a new calculation: ").upper()
    if cont_same == "Y":
        new_calculation = False
        n1 = result
    else:
        first_number()

        
