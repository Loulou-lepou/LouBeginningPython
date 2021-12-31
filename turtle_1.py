# ref : https://www.geeksforgeeks.org/turtle-programming-python/
# 'turtle' in standard Python pkg, need not be installed externally
import turtle      # from turtle import *
import time        # to use time.sleep() -> make Python program wait


'''
# create a new drawing board (window -> wn)
wn = turtle.Screen()
wn.bgcolor('light green')
wn.title('Turtle')

# create a new turtle to move around & draw
skk = turtle.Turtle()
# square
for i in range(4):
    skk.forward(50)
    time.sleep(1)
    skk.right(90)
    time.sleep(1)

# star
turtle_2 = turtle.Turtle()
turtle_2.right(100)
time.sleep(1)
turtle_2.forward(100)
time.sleep(1)
for i in range(4):
    turtle_2.right(144)
    time.sleep(1)
    turtle_2.forward(100)
    time.sleep(1)
turtle.done()

# hexagon
polygon = turtle.Turtle()
num_sides = 6
side_length = 70
angle = 360.0 / num_sides
for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)
turtle.done()
'''
# spiral square outside in
def sqrfunc(size):
    for i in range(4):
        skk.fd(size)
        skk.left(90)
        size = size - 5


if __name__ == '__main__':
    skk = turtle.Turtle()
    skk.color('blue')

    side_length = 146
    for i in range(7):
        sqrfunc(side_length)
        side_length = side_length - 20
