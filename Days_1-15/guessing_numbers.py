import random

print("Welcome to the guessing numbers game\n\nI am thinking of a number between 10 and 100")

number = random.randint(1, 100)

difficulty = input("Choose a difficulty. Type 'easy' or hard': ")

if difficulty == "easy":
    guesses_remaining = 10
else:
    guesses_remaining = 5

while guesses_remaining > 0:
    print(f"You have {guesses_remaining} guesses remaining")
    guess = int(input("Make a guess: "))
    if guess  > number:
        print("Too high, guess again")
        guesses_remaining -= 1
        #return guesses_remaining
    elif guess < number: 
        print("Too low, guess again")
        guesses_remaining -= 1
    else:
        print(f"You got it! The answer was {number}")
