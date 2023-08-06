from turtle import Turtle, Screen

z = Turtle()
color_arr = ["red", "yellow", "green", "blue", "orange", "indigo", "violet", "purple"]

z.pencolor("grey")

z.speed(10)
z.penup()
z.left(90)
z.forward(300)
z.right(90)
z.forward(100)
z.pendown()


def make_weird_shape():
    for i in range(3, 10):
        current_angle = 360 / i
        z.color(color_arr[i - 3])
        print("I is now ", i)
        for m in range(i):
            z.right(current_angle)
            z.forward(200)


make_weird_shape()

screen = Screen()
screen.exitonclick()
