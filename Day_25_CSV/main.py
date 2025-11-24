import turtle
import pandas as pd 
from country_writer import Country_writer

screen = turtle.Screen()
screen.title("US States")

image = "Day_25_CSV/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
country_writer = Country_writer()

# Read csv data and create a list for states column
data = pd.read_csv("Day_25_CSV/50_states.csv")
states = data.state.to_list()

game_is_on = True
guessed_states = []
missed_states = []

while game_is_on:

    # Get answer from user
    answer_state = screen.textinput(title=f"Number of states remaining: {len(guessed_states)}\nGuess the state", prompt=f"Number of states remaining: {len(guessed_states)}\nType in a state's name").title()
    # if answer_state == "Exit":
    #     for state in states:
    #         if state not in guessed_states:
    #             missed_states.append(state)
    #     new_data =pd.DataFrame(missed_states)
    #     new_data.to_csv("Day_25_CSV/states_to_learn.csv")
    #     break

    if answer_state == "Exit":
        missed_states = [state for state in states if state not in guessed_states]
        new_data =pd.DataFrame(missed_states)
        new_data.to_csv("Day_25_CSV/states_to_learn.csv")
        break    



    if answer_state in states:
        answer = data[data.state == answer_state]
        state_row = answer.iloc[0]
        country_writer.write_country(state_row.state, state_row.x, state_row.y)
        guessed_states.append(state_row.state)
    else:
        screen.textinput("I'm afraid not.", "Try again")


screen.exitonclick()