from tkinter import *
import pandas as pd
from random import choice, randint
import json


BACKGROUND_COLOR = "#B1DDC6"
known_words = []
words_to_learn = []
french_word = ""
english_word = ""
card_image = ""
card_text = ""
data = pd.read_csv("Day_31_Flash_Cards/french_words.csv")
vocabulary_data = "Day_31_Flash_Cards/vocabulary_data.json"

#------------------------------------button actions---------------------------------------
def know_card():
    global french_word
    global known_words
    known_words.append(french_word)
    print(known_words)
    with open(vocabulary_data, mode="w") as file:
        json.dump(known_words, file)
    next_card()

def dont_know():
    next_card()


#------------------------------------random choice-------------------------------------
def next_card():
    global french_word
    global english_word
    global known_words
    #random_card2 = data[data.french not in known_words]
    filtered_data = data[~data.French.isin(known_words)]
    random_card = filtered_data.sample().iloc[0]
    #print(random_card3)
    # random_card = data.loc[randint(0, len(data) - 1)]  # leftover from earlier iteration — commented out
    print(random_card)
    french_word = random_card["French"]
    english_word = random_card["English"]
    print(french_word)
    show_front()

#-------------------------------------Show Cards------------------------------------------------

def show_front():
    global card_image
    global card_text
    card_image = PhotoImage(file="Day_31_Flash_Cards/card_front.png")
    #card = canvas.create_image(410, 280, image=card_image)
    canvas.itemconfig(card, image=card_image)
    #card_text = canvas.create_text(410, 280, text=f"French\n{french_word}", fill="black", font=("ariel", 20, "bold"), justify="center")
    canvas.itemconfig(card_text, text=f"French\n{french_word}")
    canvas.grid(column=0, row=0, columnspan=2)
    window.after(3000, show_back)

def show_back():
    global card_image
    global card_text
    card_image = PhotoImage(file="Day_31_Flash_Cards/card_back.png")
    #card = canvas.create_image(410, 280, image=card_image)
    canvas.itemconfig(card, image=card_image)
    canvas.itemconfig(card_text, text=f"English\n{english_word}")
    #canvas.create_image(410, 280, image=image)  
    canvas.grid(column=0, row=0, columnspan=2)
#-------------------------------------GUI--------------------------------------------------
window = Tk()
window.title("Flash Cards")
window.config(padx=100, pady=50, bg=BACKGROUND_COLOR)


canvas = Canvas(width=820, height=620, bg=BACKGROUND_COLOR, highlightthickness=0)
card = canvas.create_image(410, 280, image=card_image)
card_text = canvas.create_text(410, 280, text=f"French\n{french_word}", fill="black", font=("ariel", 20, "bold"), justify="center")






# Buttons
right_img = PhotoImage(file="Day_31_Flash_Cards/right.png")
yes_check = Button(image=right_img, command=know_card, bg=BACKGROUND_COLOR, borderwidth=0, relief="flat", highlightthickness=0)
yes_check.grid(column=1, row=1)

wrong_img = PhotoImage(file="Day_31_Flash_Cards/wrong.png")
no_check = Button(image=wrong_img, command=dont_know, bg=BACKGROUND_COLOR, borderwidth=0, relief="flat", highlightthickness=0)
no_check.grid(column=0, row=1)


try:
    with open(vocabulary_data, "r") as file:
        known_words = json.load(file)
except FileNotFoundError:
    known_words = []
print(known_words)
next_card()

window.mainloop()
#todo list 
# GUI
#1. GUI: cards - back and front
#2. Timer 3 seconds flip card
#3. buttons with images
#
#Data handing
# 1. load in CSV
# 2. Choose a random card
# 2. accept button input
# 3. if yes, remove word from list