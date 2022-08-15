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
__testing = False

def testing(testing=True):
    global __testing
    __testing = testing

def reset():
    __EXPECTED.clear()
    global __index
    __index = 0
    turtle.reset()

def expect(function, *args):
    __EXPECTED.append(Call(function, *args))

def __call(function, *args):
    if __testing:
        global __index
        
        actual = Call(function, *args)
        assert __index < len(__EXPECTED), "Unexpected call: " + str(actual)

        expected = __EXPECTED[__index]
        actual = Call(function, *args)
        assert expected == actual, "Expected: " + str(expected) \
                + " but was " + str(actual)

        __index += 1
    else:
        t_function = getattr(turtle, function.__name__)
        return t_function(*args)

def verify():
    difference = len(__EXPECTED) - __index
    assert difference == 0, "Expected " + str(difference) \
        + " more calls beginning with " + str(__EXPECTED[__index])
    
"""
Other turtle functions.
"""
def forward(distance):
    return __call(forward, distance)

def fd(distance):
    return __call(fd, distance)

def back(distance):
    return __call(back, distance)

def bk(distance):
    return __call(bk, distance)

def backward(distance):
    return __call(backward, distance)

def right(angle):
    return __call(right, angle)

def rt(angle):
    return __call(rt, angle)

def left(angle):
    return __call(left, angle)

def lt(angle):
    return __call(lt, angle)

def goto(x, y=None):
    return __call(goto, x, y)

def setpos(x, y=None):
    return __call(setpos, x, y)

def setposition(x, y=None):
    return __call(setposition, x, y)

def setx(x):
    return __call(setx, x)

def sety(y):
    return __call(sety, y)

def setheading(to_angle):
    return __call(setheading, to_angle)

def seth(to_angle):
    return __call(seth, to_angle)

def home():
    return __call(home)

def circle(radius, extent=None, steps=None):
    return __call(circle, radius, extent, steps)

def dot(size=None, *color):
    return __call(dot, size, *color)

def stamp():
    return __call(stamp)

def clearstamp(stampid):
    return __call(clearstamp, stampid)

def clearstamps(n=None):
    return __call(clearstamps, n)

def undo():
    return __call(undo)

def speed(spd=None):
    return __call(speed, spd)

def position():
    return __call(position)

def pos():
    return __call(pos)

def towards(x, y=None):
    return __call(towards, x, y)

def xcor():
    return __call(xcor)

def ycor():
    return __call(ycor)