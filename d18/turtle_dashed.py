from turtle import Turtle, Screen

z = Turtle()
j = Turtle()


def turtle_dash(turtle, dash_size):
    for _ in range(10):
        turtle.pendown()
        turtle.forward(dash_size)
        turtle.penup()
        turtle.forward(dash_size)


turtle_dash(z, 10)

screen = Screen()
screen.exitonclick()
