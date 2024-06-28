import turtle
import pandas
import csv


screen = turtle.Screen()
screen.title("U.S.States")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
#converted the csv file to the list
all_states = data.state.to_list()
# print(state_list)
guessed_states = []
Score = 0

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{Score}/50 Guess the state", prompt="What's another state?").title()
   
    #if the answer_state is in the  csv file, if the  guess is right : create a turtle with the x, y coordinates of the state to display on the map
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        print(data)
        break
    if answer_state in all_states:
        
        if answer_state in guessed_states:
            Score = Score
        else:            
            guessed_states.append(answer_state)
            Score += 1
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            #getting the coordinate data using the state name key
            state_data = data[data.state == answer_state]
            t.goto(int(state_data.x), int(state_data.y))
            t.write(answer_state)
            
        
#Create a new csv file for the state which were not guessed
