import turtle

from random_walk import random_color

z = turtle.Turtle()
z.speed(10)


def make_spirograph():
    number_of_loops = int(input("How many loops you want? "))
    for i in range(number_of_loops):
        z.color(random_color())
        z.circle(50)
        z.right(360 / number_of_loops)


if __name__ == "__main__":
    make_spirograph()

screen = turtle.Screen()
screen.exitonclick()
