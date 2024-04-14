import turtle
import random
from scipy.spatial import KDTree
from webcolors import (
    CSS3_HEX_TO_NAMES,
    hex_to_rgb,
)


def convert_rgb_to_names(rgb_tuple):
    # a dictionary of all the hex and their respective names in css3
    css3_db = CSS3_HEX_TO_NAMES
    names = []
    rgb_values = []
    for color_hex, color_name in css3_db.items():
        names.append(color_name)
        rgb_values.append(hex_to_rgb(color_hex))

    kdt_db = KDTree(rgb_values)
    distance, index = kdt_db.query(rgb_tuple)
    return f"closest match: {names[index]}"

turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


turtles = [turtle.Turtle() for _ in range(5)]

screen = turtle.Screen()
screen.setup(width=500, height=500)

turtle_y_position = 200

for turtle in turtles:
    turtle.color(random_color())
    turtle.penup()
    turtle.shape("turtle")
    turtle.setposition(x=-225, y=turtle_y_position)
    turtle_y_position -= 100

race_ongoing = True
while race_ongoing:
    random_turtle = turtles[random.randint(0, len(turtles) - 1)]
    turtle_color = convert_rgb_to_names(random_turtle.fillcolor())
    random_turtle.forward(10)
    if random_turtle.position()[0] > 200:
        race_ongoing = False
        print(f"{turtle_color} turtle won!")


screen.exitonclick()
