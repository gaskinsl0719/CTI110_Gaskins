"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

import turtle

t = turtle.Turtle()
#comment block
"""
for c in ['red', 'green', 'blue', 'purple']:
    t.color(c)
    t.forward(75)
    t.right(90)

"""

t.color ("green")
t.pensize (5)
t.forward (100)
t.right(90)
t.forward (100)
t.right (90)
t.forward (100)
t.right(90)
t.forward (100)

t.back (100)
t.left (60)
t.forward(100)
t.right (120)
t.forward (100)

t.penup()
t.left (60)
t.forward (100)
t.right(180)
t.pendown ()
#draw L
t.color ("red") 
size=50
t.forward (size)
t.left(90)
t.forward(size)
#draw G
t.penup ()
t.forward (size)
t.pendown ()
t.left (130)
t.circle(30,320)
t.left(90)
t.forward (30)

