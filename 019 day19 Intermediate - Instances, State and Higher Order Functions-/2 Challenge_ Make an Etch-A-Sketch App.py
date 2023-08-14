from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

#teacher
def move_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def move_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

# mi fomra de hacerlo
# def move_left():
#     tim.left(10)
#
# def move_right():
#     tim.right(10)


screen.listen()
screen.onkey(key="w", fun=move_forwards)
#otra forma de hacerlo
#screen.onkey(move_forwards, "w")
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()