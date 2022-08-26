from turtle import Turtle, Screen

tim = Turtle()

for i in range(25):
    tim.forward(10)
    if i % 2 == 0:
        tim.penup()
    else:
        tim.pendown()

screen = Screen()
screen.exitonclick()
