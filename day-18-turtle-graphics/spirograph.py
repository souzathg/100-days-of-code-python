from turtle import Turtle, Screen
import random


def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return (red, green, blue)


tim = Turtle()
tim.setheading(90)
tim.speed("fastest")

screen = Screen()
screen.colormode(255)


def draw_spirograph(times):
    for i in range(times):
        tim.pencolor(random_color())
        tim.circle(100)
        angle = 360/times
        tim.left(angle)


draw_spirograph(random.randint(75, 100))

screen.exitonclick()
