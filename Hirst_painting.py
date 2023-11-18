import turtle
from turtle import Turtle, Screen
import random
# import colorgram
# colors = colorgram.extract('image.jpg', 10)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)

# print(rgb_colors)


turtle.colormode(255)
color_list = [(246, 241, 244), (222, 152, 103), (233, 237, 240), (128, 172, 199), (221, 130, 149), (221, 73, 90),
              (243, 208, 99), (17, 121, 157), (118, 176, 147)]
timmy = Turtle()

timmy.penup()
timmy.setx(-150)
keep_drawing = True
timmy.hideturtle()
row = 0


def draw_dot(num_of_dots):
    dot_color = color_list[random.randint(0, 8)]
    timmy.dot(10, dot_color)
    timmy.penup()
    timmy.forward(30)


def timmy_pos(x, y):
    timmy.setx(x)
    timmy.sety(y)


while keep_drawing:
    if row < 200:
        timmy_pos(-150, row)
        for i in range(1, 10):
            draw_dot(i)
        row += 20
    elif row == 10:
        keep_drawing = False


screen = Screen()
screen.exitonclick()
