import random
from ASCII_art import rock, paper, scissors
#player choice

player_score = 0
computer_score = 0

def play_game():
    global player_score
    global computer_score
    player_choice = int(input("Choose 0 for Rock, 1 for Paper or 2 for Scissors: "))
    print(f"\nPlayer score = {player_score}, Computer score = {computer_score}\n" )
    computer_choice = random.randint(0, 2)

    print(f"Computer chose {computer_choice}") #for debugging


    game_images = [rock, paper, scissors]

    print(game_images[player_choice])
    print(game_images[computer_choice])

    if player_choice == 0 and computer_choice == 1:
        print("Bad luck - the computer wins!")
        computer_score += 1
    elif player_choice == 1 and computer_choice == 2:
        print("Bad luck - the computer wins!")
        computer_score += 1
    elif player_choice == 2 and computer_choice == 0:
        print("Bad luck - the computer wins!")
        computer_score += 1
    elif computer_choice == 0 and player_choice == 1:
        print("Well done - you win!")
        player_score += 1
    elif computer_choice == 1 and player_choice == 2:
        print("Well done - you win!")
        player_score += 1
    elif computer_choice == 2 and player_choice == 0:
        print("Well done - you win!")
        player_score += 1
    elif player_choice == computer_choice:
        print("It's a draw")

while input("Do you fancy a game of rock, paper, scissors? Type 'Y' or 'N': ").upper() == "Y":
    play_game()