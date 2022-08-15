import mockturtle as turtle

def square(x, y, length):
    # turtle.speed(1)
    turtle.goto(x, y)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)

def test_square():
    # setup
    x = 100
    y = 200
    length = 250

    turtle.testing(True)
    turtle.reset()
    turtle.expect(turtle.goto, x, y)
    turtle.expect(turtle.forward, length)
    turtle.expect(turtle.left, 90)
    turtle.expect(turtle.forward, length)
    turtle.expect(turtle.left, 90)
    turtle.expect(turtle.forward, length)
    turtle.expect(turtle.left, 90)
    turtle.expect(turtle.forward, length)
    turtle.expect(turtle.left, 90)

    # invoke
    square(x, y, length)

    # analyze
    turtle.verify()

test_square()