from turtle import Turtle, Screen

tim = Turtle()
#timmy_the_tutle.shape("turtle")
#timmy_the_tutle.color("red")
#timmy_the_tutle.forward(100)
#timmy_the_tutle.right(90)

# option 1
tim.forward(100)
tim.left(90)
tim.forward(100)
tim.left(90)
tim.forward(100)
tim.left(90)
tim.forward(100)
tim.left(90)

#option 2
for _ in range(4):
    tim.forward(100)
    tim.left(90)






screen = Screen()
screen.exitonclick()
print(tim)