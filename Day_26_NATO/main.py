# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

import pandas as pd

data = pd.read_csv("Day_26_NATO/nato_phonetic_alphabet.csv")

for (index, row) in data.iterrows():
    print(index)
    print(row)

nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(nato_dict)

def get_word():
    user_word = input("What is the word?  ").upper()
   
    letter_list = [letter for letter in user_word]
    print(letter_list)

    try:
        user_phon = [nato_dict[letter] for letter in letter_list]
    except KeyError:
        print("Please type in a word")
        get_word()
    else:
        print(user_phon)

get_word()




#Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

