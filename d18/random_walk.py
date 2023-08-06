import random
import turtle

turtle.colormode(255)


rotate_angles = [0, 30, 60, 90, 120, 150, 180, 210, 240, 270]

z = turtle.Turtle()
z.pensize(20)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def random_walk(distance):
    for _ in range(distance):
        z.right(rotate_angles[random.randint(0, len(rotate_angles) - 1)])
        z.color(random_color())
        z.forward(50)

    screen = turtle.Screen()
    screen.exitonclick()


if __name__ == "__main__":
    random_walk(100)
