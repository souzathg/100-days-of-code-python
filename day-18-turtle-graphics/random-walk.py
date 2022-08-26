from turtle import Turtle, Screen
import random


def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return (red, green, blue)


tim = Turtle()
tim.pensize(5)

directions = [0, 90, 180, 270]

screen = Screen()
screen.colormode(255)

for i in range(100):
    tim.pencolor(random_color())
    direction = random.choice(directions)
    tim.setheading(direction)
    tim.forward(20)

screen.exitonclick()
