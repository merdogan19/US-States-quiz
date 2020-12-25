import sys
import turtle
import pandas as pd


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
turtle.setup(725, 491)

#Code snippet to get x, y coordinate in turtle image
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)

# Load csv data
data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
game_on = True
correct_answers = []

try:
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()
except AttributeError:
    answer_state = "Exit"
    turtle.write("See you next time!", font=("Arial", 16, "bold"), align="center")
    game_on = False

while game_on:
    # this was my solution including commented out if below
    # check = data[data.state.replace(" ", "") == answer_state.capitalize().replace(" ", "")]
    if answer_state == "Exit":
        turtle.write(f"You have named {len(correct_answers)}/50 States correct!", font=("Arial", 16, "bold"), align="center")

        try:
            new_game = screen.textinput(title="Start again?", prompt="New game? (Yes or Exit").title()
        except AttributeError:
            break

        if new_game.title() == "Yes":
            correct_answers = []
            turtle.clear()
        else:
            break

    # Check if answer is correct
    # if not check.empty:
    print(answer_state)
    if answer_state in all_states:
        # TODO: place string from csv to x,y coordinates
        new_turtle = turtle.Turtle()
        new_turtle.penup()
        new_turtle.hideturtle()
        answer_data = data[data.state == answer_state]
        # new_turtle.goto(x=answer_data.iloc[0]['x'], y=answer_data.iloc[0]['y'])
        new_turtle.goto(int(answer_data.x), int(answer_data.y))
        new_turtle.write(answer_data.state.item(), font=("Arial", 8, "normal"), align="center")

        # TODO: record correct answers to a list
        correct_answers.append(answer_state.capitalize())

    if len(correct_answers) == 50:
        turtle.goto(0, 0)
        turtle.write("You have all states correctly!", font=("Arial", 16, "bold"), align="center")
        game_on = False
    else:
        # TODO: ask questions again and update title with score
        try:
            answer_state = screen.textinput(title=f"{len(correct_answers)}/50 States Correct",
                                        prompt="What's another state's name?").title()
        except AttributeError:
            turtle.write(f"You have named {len(correct_answers)}/50 States correct!", font=("Arial", 16, "bold"),
                         align="center")
            break

turtle.mainloop()

# states_to_learn.csv
states_to_learn = set(correct_answers).symmetric_difference(set(all_states))
# print(list(states_to_learn))
df = pd.DataFrame(list(states_to_learn))
df.to_csv("states_to_learn.csv")