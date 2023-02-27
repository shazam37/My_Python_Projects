import turtle
import pandas

data = pandas.read_csv('50_states.csv')
all_state = data.state.to_list()

screen = turtle.Screen()
screen.title('U.S. State Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

guessed_state = []

while len(guessed_state) < 50:

    answer_state = screen.textinput(title=f'{len(guessed_state)}/50 Correct guess',
                                    prompt="Whats another state's name?")

    if answer_state == 'off':
        missing_states = []
        for elements in all_state:
            if elements not in guessed_state:
                missing_states.append(elements)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('states_to_learn.csv')
        break

    if answer_state in all_state:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state.title()]
        t.goto(float(state_data.x), float(state_data.y))
        t.write(f'{answer_state}', align='center', font=("Courier", 10, 'normal'))





