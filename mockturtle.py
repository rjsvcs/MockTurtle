import turtle

"""
Mock functions
"""

def expect(name, *args):
    pass

"""
Turtle functions.
"""
def forward(distance):
    turtle.forward(distance)

def fd(distance):
    turtle.fd(distance)

def back(distance):
    turtle.back(distance)

def bk(distance):
    turtle.bk(distance)

def backward(distance):
    turtle.backward(distance)

def right(angle):
    turtle.right(angle)

def rt(angle):
    turtle.rt(angle)

def left(angle):
    turtle.left(angle)

def lt(angle):
    turtle.lt(angle)

def goto(x, y=None):
    turtle.goto(x, y)

def setpos(x, y=None):
    turtle.setpos(x, y)

def setposition(x, y=None):
    turtle.setposition(x, y)

def setx(x):
    turtle.setx(x)

def sety(y):
    turtle.sety(y)

def setheading(to_angle):
    turtle.setheading(to_angle)

def seth(to_angle):
    turtle.seth(to_angle)

def home():
    turtle.home()

def circle(radius, extent=None, steps=None):
    turtle.circle(radius, extent, steps)

def dot(size=None, *color):
    turtle.dot(size, *color)

def stamp():
    return turtle.stamp()

def clearstamp(stampid):
    turtle.clearstamp(stampid)

def clearstamps(n=None):
    turtle.clearstamps(n)

def undo():
    turtle.undo()

def speed(speed=None):
    return turtle.speed(speed)

def position():
    return turtle.position()

def pos():
    return turtle.pos()

def towards(x, y=None):
    turtle.towards(x, y)






