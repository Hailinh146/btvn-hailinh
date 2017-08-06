from turtle import *
speed(-1)

def draw_star(x,y,length):
    for i in range (5):
        forward(length)
        right(144)
        
draw_star(1,1,100)
input()

speed(0)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)

## random.radint(): Return a random integer N such that a <= N <= b.
## Alias for randrange(a, b+1).
