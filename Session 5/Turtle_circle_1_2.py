
from turtle import *
speed(-1)

def draw_square(length, color):
    for i in range (4):
        forward(length)
        right(90)

draw_square(100, "green")

input()

for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()

