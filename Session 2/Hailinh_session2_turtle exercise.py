from turtle import *
speed(-1)
color("red")
shape("turtle")

##bai tap ve hinh 1

for i in range (4):
    for i in range (2):
        forward(100)
        right(60)
        forward(100)
        right(120)
    left(90)

forward(200)

##bai tap ve hinh 2

for n in range (3,7):
    for i in range(n):
        if n%2==0:
            color("red")
        else:
            color("blue")
        forward(100)
        left(360/n)
