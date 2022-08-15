import turtle

"""
Mock functions
"""
class Call:
    __slots__ = ["__function", "__args"]

    def __init__(self, function, *args):
        self.__function = function
        self.__args = args

    def __str__(self):
        return str(self.__function.__name__) + str(self.__args)

    def __eq__(self, other):
        if type(self) is type(other):
            return self.__function is other.__function and \
                self.__args == other.__args
        else:
            return False

__EXPECTED = []
__index = 0

def reset():
    __EXPECTED.clear()
    global __index
    __index = 0
    turtle.reset()

def expect(function, *args):
    __EXPECTED.append(Call(function, *args))

def __called(function, *args):
    global __index
    new_index = __index + 1
    
    actual = Call(function, *args)
    assert new_index < len(__EXPECTED), "Unexpected call: " + str(actual)

    expected = __EXPECTED[new_index]
    actual = Call(function, *args)
    assert expected == actual, "Expected: " + str(expected) \
            + " but was " + str(actual)

    __index = new_index

def verify():
    difference = len(__EXPECTED) - __index
    assert difference == 0, "Expected " + str(difference) \
        + " more calls beginning with " + str(__EXPECTED[__index])
    
"""
Other turtle functions.
"""
def forward(distance):
    __called(forward, distance)
    return turtle.forward(distance)

def fd(distance):
    __called(fd, distance)
    return turtle.fd(distance)

def back(distance):
    __called(back, distance)
    return turtle.back(distance)

def bk(distance):
    __called(bk, distance)
    return turtle.bk(distance)

def backward(distance):
    __called(backward, distance)
    return turtle.backward(distance)

def right(angle):
    __called(right, angle)
    return turtle.right(angle)

def rt(angle):
    __called(rt, angle)
    return turtle.rt(angle)

def left(angle):
    __called(left, angle)
    return turtle.left(angle)

def lt(angle):
    __called(lt, angle)
    return turtle.lt(angle)

def goto(x, y=None):
    __called(goto, x, y)
    return turtle.goto(x, y)

def setpos(x, y=None):
    __called(setpos, x, y)
    return turtle.setpos(x, y)

def setposition(x, y=None):
    __called(setposition, x, y)
    return turtle.setposition(x, y)

def setx(x):
    __called(setx, x)
    return turtle.setx(x)

def sety(y):
    __called(sety, y)
    return turtle.sety(y)

def setheading(to_angle):
    __called(setheading, to_angle)
    return turtle.setheading(to_angle)

def seth(to_angle):
    __called(seth, to_angle)
    return turtle.seth(to_angle)

def home():
    __called(home)
    return turtle.home()

def circle(radius, extent=None, steps=None):
    __called(circle, radius, extent, steps)
    return turtle.circle(radius, extent, steps)

def dot(size=None, *color):
    __called(dot, size, *color)
    return turtle.dot(size, *color)

def stamp():
    __called(stamp)
    return turtle.stamp()

def clearstamp(stampid):
    __called(clearstamp, stampid)
    return turtle.clearstamp(stampid)

def clearstamps(n=None):
    __called(clearstamps, n)
    return turtle.clearstamps(n)

def undo():
    __called(undo)
    return turtle.undo()

def speed(spd=None):
    __called(speed, spd)
    return turtle.speed(spd)

def position():
    __called(position)
    return turtle.position()

def pos():
    __called(pos)
    return turtle.pos()

def towards(x, y=None):
    __called(towards, x, y)
    return turtle.towards(x, y)

def xcor():
    __called(xcor)
    return turtle.xcor()

def ycor():
    __called(ycor)
    return turtle.ycor()