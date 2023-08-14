import turtle as t
import random

tim = t.Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "Black","DarkBlue","DarkGreen", "LightSeaGreen", "wheat", "SlateGray"]


def draw_shape(num_sides):
    for _ in range(num_sides):
        angel = 360 / num_sides
        tim.forward(100)
        tim.right(angel)


for shape_side_n in range(3, 11):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)