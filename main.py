import turtle
import pandas
FONT = ("Arial", 8, "normal")

#turtle code to get the image on screen
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#declaring a turtle which writes state names
write_name = turtle.Turtle()
write_name.hideturtle()
write_name.penup()

#open csv and use it using pandas
fifty_states = pandas.read_csv("50_states.csv")
#print(states.state)

# number of states guessed correctly
states_guessed = 0
guessed_states = []

# main quiz loop
while states_guessed < 50:
    #input is saved in answer_state
    answer_state = screen.textinput(title=f"States Guessed = {states_guessed}", prompt="Enter State Name:")

    if answer_state == "exit":
        print('Exiting Game')
        missing_states = [state for state in fifty_states.state if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states, columns=["States"])
        new_data.to_csv("states_to_learn.csv")
        break

    for state_name in fifty_states.state:
        if answer_state.lower() == state_name.lower():
            if state_name not in guessed_states:
                # print(fifty_states[fifty_states.state==state_name].x.iloc[0])
                x = fifty_states[fifty_states.state==state_name].x.iloc[0]
                y = fifty_states[fifty_states.state==state_name].y.iloc[0]

                # goto the marked location on the screen and write state name
                write_name.goto(x,y)
                write_name.write(state_name, font=FONT)

                # increase the guess count and add it to the screen text
                states_guessed += 1
                guessed_states.append(state_name)



turtle.mainloop()
