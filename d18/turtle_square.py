from turtle import Turtle, Screen

my_turtle = Turtle()


def turtle_square(turtle, size):
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)


turtle_square(my_turtle, 300)

screen = Screen()
screen.exitonclick()
