from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()

for sides in range(3, 11):
    screen.colormode(255)
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)

    for i in range(1, sides+1):
        tim.forward(100)
        tim.right(360/sides)


screen.exitonclick()
