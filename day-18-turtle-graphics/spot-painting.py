# import colorgram
import random
import turtle


# def create_color_list(color_objects):
#     colors = []
#     for i in range(0, len(color_objects) - 1):
#         color = color_objects[i].rgb
#         r = color.r
#         g = color.g
#         b = color.b
#         colors.append((r, g, b))
#     return colors


# color_objects = colorgram.extract("rose.jpg", 50)
# colors = create_color_list(color_objects)


def pick_random_color(colors):
    color = random.choice(colors)
    return color


def draw_10x10_dots(turtle):
    turtle.penup()
    turtle.goto(-250, -250)
    turtle.hideturtle()
    for _ in range(0, 10):
        turtle.speed("normal")
        for _ in range(0, 10):
            turtle.pencolor(pick_random_color(colors))
            turtle.dot(20)
            turtle.forward(50)
        turtle.speed("fastest")
        turtle.goto(-250, turtle.position()[1] + 50)
    turtle.home()


colors = [(212, 154, 97),
          (52, 108, 132),
          (178, 78, 33),
          (198, 143, 34),
          (123, 80, 97)
          ]

screen = turtle.Screen()
screen.colormode(255)

tim = turtle.Turtle()
draw_10x10_dots(tim)

screen.exitonclick()
