# Ref : https://www.geeksforgeeks.org/python-draw-star-using-turtle-graphics/?ref=lbp
# https://www.geeksforgeeks.org/how-to-draw-color-filled-star-in-python-turtle/?ref=lbp
import turtle                # turtle -> built-in module, in standard Python pkg, not needed to be installed externally
from random import randint   # randint() method , randint(a, b) yields a random integer x in [a, b]


def star_1():

    color_list = ['red', 'green', 'blue', 'yellow', 'purple']
    turtle.pensize(4)

    for i in range(5):
        turtle.pencolor(color_list[i])
        turtle.forward(200)
        turtle.right(144)
    turtle.done()


def colored_star():
    turtle.color('red')
    turtle.width(4)
    size = 80
    angle = 120
    turtle.fillcolor('yellow')
    turtle.begin_fill()
    for side in range(5):
        turtle.forward(size)
        turtle.right(angle)
        turtle.forward(size)
        turtle.right(72 - angle)
    turtle.end_fill()


def draw_star():
    turns = 6
    turtle.begin_fill()
    while turns > 0:
        turtle.forward(25)
        turtle.left(144)
        turns -= 1
    turtle.end_fill()


def starry_night():

    wn = turtle.Screen()
    turtle.bgcolor('black')
    turtle.color('yellow')
    turtle.speed(0)

    num_stars = 0
    while num_stars < 50:
        x = randint(-300, 300)
        y = randint(-300, 300)
        draw_star()
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        num_stars += 1
    wn.exitonclick()


def spiral_star_2():
    n = 30
    pen = turtle.Turtle()
    for i in range(n):
        pen.forward(i * 10)
        pen.right(144)
    turtle.done()


if __name__ == '__main__':

    # colored_star()
    # star_1()
    # starry_night()
    spiral_star_2()
