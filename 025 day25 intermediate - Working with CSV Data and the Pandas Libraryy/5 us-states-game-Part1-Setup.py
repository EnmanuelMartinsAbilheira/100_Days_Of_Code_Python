import turtle

screen = turtle.Screen()
screen.title("U.S States Games")
image = "blank_state_img.gif"
screen.addshape(image)
turtle.shape(image)


# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

answer_state = screen.textinput(title="guess the state", prompt="Whats another states name? ")
print(answer_state)






screen.exitonclick()