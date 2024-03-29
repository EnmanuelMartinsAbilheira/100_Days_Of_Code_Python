import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Games")
image = "blank_state_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50: # this is for no stop the game before you complete all names

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 state Correct",
                                    prompt="Whats another states name? ").title()

    if answer_state == "Exit":
        #esta line asustituye las 4 de abajo
        missing_states = [state for state in all_states if state not in guessed_states]
        #missing_states = []
        #for state in all_states:
        #    if state not in guessed_states:
        #        missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    #_If answeer_state is one o0f the states in all the states of the 50_states.csv
    if answer_state in all_states:
        guessed_states.append(answer_state)
        #if they got it right:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        #Create a turtle to write the name of the state at the state´s x and y coordate
        t.write(state_data.state.item())

