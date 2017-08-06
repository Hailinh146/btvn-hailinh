from turtle import *

speed(-1)
wn = Screen()
bgcolor("lightgreen")

def draw_multicolor_square(t,sz):
    for i in ["red", "purple", "hotpink", "blue"]:
        color(i)
        forward(sz)
        left(90)

def draw_multicolor_square(t,sz):
    for i in ["red", "purple", "hotpink", "blue"]:
        color(i)
        forward(sz)
        left(90)

def draw_line(t):
    forward(t)
    left(90)

def draw_2(t,z):
    forward(t)
    left(z)

tess = Turtle()
pensize(3)

##size = 20
##for i in range(30):
##    draw_multicolor_square(tess, size)
##    size = size + 10
##    forward(10)
##    right(18)
##
##
##size = 100
##for i in range(30):
##    draw_multicolor_square(tess, size)
##    right(20)


##t = 10
##for i in range(100):
##    draw_line(t)
##    t = t + 5

t = 10
z = 90
for i in range(100):
    draw_2(t,z)
    t = t + 5
    z = z + 0.01

wn.mainloop()
