import random
from ASCII_art import guessnum_logo

def game():
    print(guessnum_logo)
    print("Welcome to the guessing numbers game\n\nI am thinking of a number between 1 and 100")
    guesses_remaining = set_difficulty()
    number = random_number()
    check_answer(number, guesses_remaining)

def random_number():
    number = random.randint(1, 100)
    return number

def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or hard': ")
    if difficulty == "easy":
        guesses_remaining = 10
    else:
        guesses_remaining = 5
    return guesses_remaining

def check_answer(num, guesses): 
    game_complete = False
    while guesses > 0 and game_complete == False:
        print(f"You have {guesses} guesses remaining")
        guess = int(input("Make a guess: "))
        if guess  > num:
            print("Too high, guess again\n")
            guesses -= 1
            #return guesses_remaining
        elif guess < num: 
            print("Too low, guess again\n")
            guesses -= 1
        else:
            print(f"You got it! The answer was {num}")
            game_complete = True
    if guesses == 0:        
        print("\nYou're out of guesses.  Game over")

while input("Fancy trying to guess the number? Type 'Y' or 'N': ").upper() == "Y":
    game()
print("Maybe next time. Byee")
