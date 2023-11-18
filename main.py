import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape('turtle')
timmy.pencolor("red")
timmy.fillcolor("blue")

# Draw a square
# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)


# Draw a dashed line
# teleport_number = 20
# for _ in range(5):
#     timmy.forward(10)
#     timmy.teleport(teleport_number)
#     timmy.forward(10)
#     teleport_number += 30

# for _ in range(7):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()


# Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon
# colors = ['red', 'blue', 'green', 'brown', 'light blue', 'black', 'coral', 'cyan', 'maroon', 'pink', 'purple']
# for i in range(3, 11):
#     angle = (((i-2)*180)/i)
#     timmy.pencolor(random.choice(colors))
#     for n in range(0, i):
#         timmy.forward(50)
#         timmy.right(180-angle)


# Create a random color

turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple


# Draw a random walk
# timmy.pensize(10)
# timmy.speed(0)
#
# for i in range(0, 50):
#     color_tuple = random_color()
#     random_number = random.randint(30, 90)
#     movements = [timmy.forward, timmy.back]
#     turns = [timmy.left, timmy.right]
#     random_movement = random.randint(0, 1)
#     timmy.pencolor(color_tuple[0], color_tuple[1], color_tuple[2])
#     move = movements[random_movement]
#     move(random_number)
#     timmy.pencolor(color_tuple[0], color_tuple[1], color_tuple[2])
#     turn = turns[random_movement]
#     turn(90)


# Draw a circe design - Spirograph
timmy.speed(0)
timmy.circle(100)
angle = 5
for i in range(0, int(360/angle)):
    color_tuple = random_color()
    timmy.setheading(angle)
    timmy.pencolor(color_tuple[0], color_tuple[1], color_tuple[2])
    timmy.circle(100)
    angle += 5



screen = Screen()
screen.exitonclick()
