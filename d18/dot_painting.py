import colorgram
import turtle
import random


screen = turtle.Screen()
screen.colormode(255)


# Extract 6 colors from an image.
extracted_colors = colorgram.extract("eric.jpeg", 6)


def colors_to_rgb(color_array):
    rgb_colors = []
    for color in color_array:
        rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))
    return rgb_colors


rgb_colors = colors_to_rgb(extracted_colors)

z = turtle.Turtle()
z.shape("circle")
z.penup()
z.backward(400)
z.right(90)
z.forward(350)
z.left(90)
starting_position = z.pos()
z.pendown()


def make_dots():
    for i in range(11):
        z.pendown()
        z.dot(10, rgb_colors[random.randint(0, len(rgb_colors) - 1)])
        z.penup()
        if i < 10:
            z.forward(80)


def start_new_row():
    z.left(90)
    z.forward(100)
    z.left(90)
    z.forward(800)
    z.left(180)


for i in range(8):
    make_dots()
    start_new_row()


make_dots()


screen.exitonclick()
