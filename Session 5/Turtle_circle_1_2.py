
from turtle import *
speed(-1)

def draw_square(length, square_color):
    color(square_color)
    for i in range (4):
        forward(length)
        right(90)

draw_square(100, "green")


