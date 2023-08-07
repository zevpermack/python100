import turtle

screen = turtle.Screen()

z = turtle.Turtle()


def move_forward():
    z.forward(10)


def move_backward():
    z.backward(10)


def turn_left():
    z.left(10)


def turn_right():
    z.right(10)


def clear():
    z.clear()
    z.penup()
    z.home()


screen.onkey(key="w", fun=move_forward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)
screen.listen()

screen.exitonclick()
