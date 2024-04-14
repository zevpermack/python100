from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

turtles = [Turtle("square") for _ in range(3)]
turtle_position = [0, 0]

for turtle in turtles:
    turtle.goto(tuple(turtle_position))
    turtle.color("white")
    turtle_position[0] -= 20

screen.exitonclick()
