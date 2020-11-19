
def setPos(x, y, tur, initial = True):
    tur.penup()
    tur.goto(x + (initial)*tur.xcor(), y + (initial)*tur.ycor())
    tur.pendown()

def zero(L, tur):
    initPosX = tur.xcor()
    initPosY = tur.ycor()
    setPos(-L/4, L/2, tur)

    for i in range(4):
        tur.forward(L/2 + (i % 2 == 1)*L/2)
        tur.right(90)

    setPos(initPosX, initPosY, tur, False)

def one(L, tur):
    initPosX = tur.xcor()
    initPosY = tur.ycor()
    setPos(L/4, L/2, tur)

    tur.right(90)
    tur.forward(L)
    tur.left(90)

    setPos(initPosX, initPosY, tur, False)

def two(L, tur):
    initPosX = tur.xcor()
    initPosY = tur.ycor()
    setPos(-L/4, L/2, tur)

    tur.forward(L/2)
    tur.right(90)
    tur.forward(L/2)
    tur.right(90)
    tur.forward(L/2)
    tur.left(90)
    tur.forward(L/2)
    tur.left(90)
    tur.forward(L/2)

    setPos(initPosX, initPosY, tur, False)

def three(L, tur):
    initPosX = tur.xcor()
    initPosY = tur.ycor()
    setPos(-L/4, L/2, tur)

    tur.forward(L/2)
    tur.right(90)
    tur.forward(L/2)
    tur.right(90)
    tur.forward(L/2)
    tur.left(180)
    tur.forward(L/2)
    tur.right(90)
    tur.forward(L/2)
    tur.right(90)
    tur.forward(L/2)
    tur.right(180)

    setPos(initPosX, initPosY, tur, False)

def four(L, tur):
    initPosX = tur.xcor()
    initPosY = tur.ycor()
    setPos(-L/4, L/2, tur)

    tur.right(90)
    tur.forward(L/2)
    tur.left(90)
    tur.forward(L/2)
    tur.left(90)
    tur.forward(L/2)
    tur.left(180)
    tur.forward(L)
    tur.left(90)

    setPos(initPosX, initPosY, tur, False)

def five(L, tur):
    initPosX = tur.xcor()
    initPosY = tur.ycor()
    setPos(L/4, L/2, tur)

    tur.right(180)
    tur.forward(L/2)
    tur.left(90)
    tur.forward(L/2)
    tur.left(90)
    tur.forward(L/2)
    tur.right(90)
    tur.forward(L/2)
    tur.right(90)
    tur.forward(L/2)
    tur.right(180)

    setPos(initPosX, initPosY, tur, False)

def six(L, tur):
    initPosX = tur.xcor()
    initPosY = tur.ycor()
    setPos(L/4, L/2, tur)

    tur.right(180)
    tur.forward(L/2)
    tur.left(90)
    tur.forward(L/2)
    tur.left(90)
    tur.forward(L/2)
    tur.right(90)
    tur.forward(L/2)
    tur.right(90)
    tur.forward(L/2)
    tur.right(90)
    tur.forward(L/2)
    tur.right(90)

    setPos(initPosX, initPosY, tur, False)

def seven(L, tur):
    initPosX = tur.xcor()
    initPosY = tur.ycor()
    setPos(-L/4, 0, tur)

    tur.left(90)
    tur.forward(L/2)
    tur.right(90)
    tur.forward(L/2)
    tur.right(90)
    tur.forward(L)
    tur.left(90)

    setPos(initPosX, initPosY, tur, False)

def eight(L, tur):
    initPosX = tur.xcor()
    initPosY = tur.ycor()
    setPos(-L/4, L/2, tur)

    for i in range(4):
        tur.forward(L/2 + (i % 2 == 1)*L/2)
        tur.right(90)
    
    tur.right(90)
    tur.forward(L/2)
    tur.left(90)
    tur.forward(L/2)

    setPos(initPosX, initPosY, tur, False)

def nine(L, tur):
    initPosX = tur.xcor()
    initPosY = tur.ycor()
    setPos(-L/4, -L/2, tur)

    tur.forward(L/2)
    tur.left(90)
    tur.forward(L)
    tur.left(90)
    tur.forward(L/2)
    tur.left(90)
    tur.forward(L/2)
    tur.left(90)
    tur.forward(L/2)

    setPos(initPosX, initPosY, tur, False)

def twoPoints(radius, dist, tur):
    initPosX = tur.xcor()
    initPosY = tur.ycor()

    setPos(0, dist/2, tur)
    tur.begin_fill()
    tur.circle(radius)
    tur.end_fill()

    setPos(initPosX, initPosY, tur, False)

    setPos(0, -dist/2, tur)
    tur.begin_fill()
    tur.circle(radius)
    tur.end_fill()

    setPos(initPosX, initPosY, tur, False)

draw_number = {'0':zero, '1':one, '2':two,
               '3':three, '4':four, '5':five,
               '6':six, '7':seven, '8':eight,
               '9':nine, ':':twoPoints}

def draw(turtles, previous_date, next_date, size_square_number):
    for i in range(8):
        if previous_date[i] != next_date[i]:
            turtles[i].clear()
            draw_number[next_date[i]](size_square_number, turtles[i])