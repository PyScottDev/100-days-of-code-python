print("Welcome to the tip calculator!")

bill_total = float(input("How much was the bill? £"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
no_people = int(input("How many people to split the bill? "))

bill_tip = ((tip_percentage / 100 + 1) * bill_total)
split_bill = bill_tip / no_people

print(f"Each person should pay: £{split_bill: .2f}")