from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

segments = [Turtle("square") for _ in range(3)]
segment_position = [0, 0]

for segment in segments:
  segment.goto(tuple(segment_position))
  segment.color("white")
  segment_position[0] -= 20

screen.exitonclick()
