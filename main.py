from turtle import Turtle, Screen
import pandas
import re

FONT = ("Courier", 6, "normal")

turtle = Turtle()
screen = Screen()
turtle_write = Turtle()

screen.title("Guess US State name")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
game_on = True
score = 0

with open("50_states.csv") as us_states:
    data = pandas.read_csv(us_states)
    state_row = data.state
    state_row_list = state_row.to_list()
    known_states = []
    unknown_states = []
    #print(type(state_row))
    while game_on:
        state_name = screen.textinput("Input box" + str(score) + "/50", "ENTER STATE NAME: ").title()
        if state_row.str.fullmatch(state_name).any():
            state = data[state_row == state_name]
            state_x = data[state_row == state_name].x
            state_y = data[state_row == state_name].y
            #print(state, type(state_x), state_y)
            turtle_write.hideturtle()
            turtle_write.penup()
            turtle_write.goto(int(state_x), int(state_y))
            turtle_write.write(state_name, font=FONT, align='center')
            known_states.append(state_name)
            score = score + 1
        elif state_name == "Exit":
            for i in state_row_list:
                if i not in known_states:
                    unknown_states.append(i)
            game_on = False
            screen.exitonclick()

    my_df = pandas.DataFrame(unknown_states)
    my_df.to_csv("List_Of_Unknown_States.csv")

