height = int(input("What is your height in cm? "))

if height > 120:
    age = int(input("What is your age? "))
    bill = 0

    if age < 12:
        print("Child tickets are $5.")
        bill = 5
    elif age < 18:
        print("Youth tickets are $7.")
        bill = 7
    else:
        print("Adult tickets are $12.")
        bill = 12

    wants_photo = input("Do you want a photo taken? Type y for yes or n for no: ")
    VIP_photo = input("Would you like the VIP photo taken? Type y for yes or n for no: ")
    priority_boarding = input("Would you like to skip the queue? Type y for yes or n for no: ")

    # Independent check – runs even after a ticket price is chosen
    if wants_photo == 'y':
        bill += 3  # Add 3 dollars to the total
    
    if VIP_photo == "y":
        bill += 2

    if priority_boarding == "y":
        bill +=4


    print(f"Your final bill is ${bill}.")

else:
    print("Sorry, you have to be taller to ride the roller coaster.")
