'''
Title
Group:
Makeeva Angelina
Kareva Alena
Osokina Anastasya
'''

import turtle
import random
wn = turtle.Screen()
wn.setup(800, 800, 0, 0)
wn.bgcolor('black')
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
'''def square (x, y, a):
    
    Function, drawing square.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a: side length of a square
    :return: None
    
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.pensize(2)
    turtle.pencolor ('white')
    turtle.color('#ff7c00')
    turtle.speed(100)
    turtle.begin_fill()
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.end_fill()
'''

'''def parallelogram(x, y, a, c):

    Function, drawing parallelogram.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a: long side of a parallelogram
    :param c: short side of a parallelogram
    :return: None
    
    
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.pensize(2)
    turtle.pencolor ('white')
    turtle.color('#8ecc23')
    turtle.speed(100)
    turtle.begin_fill()
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(c)
    turtle.right(45)
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(c)
    turtle.end_fill()
'''

'''def triangle (x, y, a, b, c):

    Function, drawing triangle.
    :param x: right angle coordinate x
    :param y: right angle coordinate y
    :param a: leg of a triangle
    :param b: hypotenuse of triangle
    :param c: color of triangle
    :return: None
    
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.pensize(2)
    turtle.pencolor ('white')
    turtle.color(c)
    turtle.speed(100)
    turtle.begin_fill()
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(b)
    turtle.right(135)
    turtle.end_fill()
    turtle.forward(a)
    '''

def main_pictures_Alena():
    def draw_star(size, color):
        t.color(color)
        t.begin_fill()
        for _ in range(5):
            t.forward(size)
            t.right(144)
        t.end_fill()
    for i in range(100):
          x = random.randint(-600, 600)
          y = random.randint(-450, 450)
          size = random.randint(5, 20)
          color = random.choice(['white', 'yellow', 'blue', 'red'])
          t.penup()
          t.goto(x, y)
          t.pendown()
          draw_star(size, color)
    t.penup()
    t.goto(-200, 120)
    t.color('orange')
    t.begin_fill()
    t.circle(110)
    t.end_fill()

    t.penup()
    t.goto(wn.window_width() / 2, wn.window_height() / -2)
    t.pendown()
    t.begin_fill()
    t.color('gray')
    t.left(90)
    t.circle(400, 180)
    t.end_fill()

    t.color('light gray')
    t.penup()
    t.goto(160, -340)
    t.pendown()
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    t.penup()
    t.goto(-330, -330)
    t.pendown()
    t.begin_fill()
    t.circle(60)
    t.end_fill()
    t.penup()
    t.goto(-100, -280)
    t.pendown()
    t.begin_fill()
    t.circle(70)
    t.end_fill()
    t.penup()
    t.goto(50, -130)
    t.pendown()
    t.begin_fill()
    t.circle(70)
    t.end_fill()
    t.penup()
    t.goto(-240, -130)
    t.pendown()
    t.begin_fill()
    t.circle(80)
    t.end_fill()
    t.penup()
    t.goto(213, -230)
    t.pendown()
    t.begin_fill()
    t.circle(70)
    t.end_fill()
main_pictures_Alena()
turtle.done()





'''def main_pictures_center_Nastya():


    pass


def main_pictures_right_Gelya'''