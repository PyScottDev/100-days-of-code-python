import random, ASCII_art, word_list
from ASCII_art import hangman_logo, stages
from word_list import hangman_list

#set up lists and graphics
print(hangman_logo)
word_list = word_list.hangman_list

chosen_word = random.choice(word_list)
game_over = False
guess_line = ""

for position in range(len(chosen_word)):
    guess_line += " _"
print(guess_line)
guessed_letters = []
correct_letters = []
lives = 6

#found = False

while game_over == False:
    found = False
    print(stages[lives])
    guess = input("Choose a letter:\n -").lower()
    if guess in guessed_letters:    
        print(f"You've already guessed {guess}")
        found = True
    display = ""

    for letter in chosen_word:
        if guess == letter:
            display += letter
            correct_letters.append(guess)
            found = True

        elif letter in correct_letters:
            display += letter
            #print(correct_letters)
          
        else:
            display += " _"
            guessed_letters.append(guess)
            
    
    if found == False:
        lives -= 1        
        print("I'm afraid not. Look you're killing him!\n")
        print(f"*******You now have {lives} lives left*******")
        
    print(display)
    if "_" not in display:
        game_over = True
        print(f"The word was {chosen_word}\n")
        print("Well done - you win!")

    elif lives == 0:
        game_over = True
        print(f"The word was {chosen_word}\n")
        print("Bad luck - the guy dies")


    