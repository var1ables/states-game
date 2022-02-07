import pandas
import turtle
screen =  turtle.Screen()
screen.title('US State Game')

writer = turtle.Turtle()
writer.penup()
writer.hideturtle()

image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')
correct_answers = data.state.tolist()

states = []
while len(states) < 50:
    answer_state = screen.textinput(title=f'{len(states)}/50', prompt='Whats the state?').title()

    if answer_state == "Exit":
        learning_states = [state for state in correct_answers if state not in states]
        new_data = pandas.DataFrame(learning_states)
        new_data.to_csv('states_to_learn')
        break

    if answer_state in correct_answers:
        states.append(answer_state)
        state_data = data[data.state == answer_state]
        writer.goto(int(state_data.x), int(state_data.y))
        writer.write(answer_state)
