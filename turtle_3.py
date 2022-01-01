# ref : https://www.geeksforgeeks.org/draw-colourful-star-pattern-in-turtle-python/?ref=lbp
from turtle import *   # import all items from turtle, to be used without prefixes
import random          # use random.randint(a, b) to generate a random integer in [a, b]


def color_filled_square():
    t = Turtle()       # if import turtle  -> t = turtle.Turtle()
    s = int(input('side = '))
    col = input('color name/ hex value of color(#RRGGBB): ')
    t.fillcolor(col)
    t.begin_fill()
    for _ in range(4):
        t.forward(s)
        t.right(90)
    t.end_fill()


def draw(n, x, angle):
    for i in range(n):
        colormode(255)
        # choosing random integers bw 0 & 255 to generate random rgb values
        a = random.randint(0, 255)
        b = random.randint(0, 255)
        c = random.randint(0, 255)
        # setting the outline & fill color
        pencolor(a, b, c)
        fillcolor(a, b, c)

        # begin filling the star
        begin_fill()
        for j in range(5):
            forward(5 * n - 5 * i)
            right(x)
            forward(5 * n - 5 * i)
            right(72 - x)

        # colour filling complete
        end_fill()

        # rotating for the next star
        rt(angle)


if __name__ == '__main__':
    # color_filled_square()
    # number of stars = 30,
    # exterior angle of each star = 144 degrees,
    # angle of rotation for the spiral = 18 degrees
    speed(speed='fastest')
    draw(30, 144, 18)
