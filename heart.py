import math
from turtle import *

def heartA(k):
    return 15 * math.sin(k) ** 3

def heartB(k):
    return 12 * math.cos(k) - 5 * \
        math.cos(2 * k) - 2 * \
        math.cos(3 * k) - \
        math.cos(4 * k)

speed(0)
bgcolor("black")
color("red")
penup()

for i in range(6000):
    x = heartA(i) * 20
    y = heartB(i) * 20
    goto(x, y)
    pendown()

done()