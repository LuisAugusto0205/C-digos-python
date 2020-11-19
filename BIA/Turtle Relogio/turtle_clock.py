import turtle
import time
from datetime import datetime
square_size = 60

try:
    import numbers
    import background
    sucess = True
except:
    sucess = False

def initial_position():
    bg_turtle = turtle.Turtle(visible=False)
    background.border(bg_turtle, square_size, 60, 'red')

    turtles = []
    posX = -(7*square_size)/2
    for i in range(8):
        turtles.append(turtle.Turtle(visible=False))
        turtles[-1].width(10)
        turtles[-1].penup()
        turtles[-1].goto(posX, 0)
        posX += (square_size - (i==1 or i==2 or i==4 or i==5)*(square_size/4))
        turtles[-1].pendown()
        turtles[-1].speed(60)

    clock(turtles)

def clock(turtles):
    previous_date = 'HH:MM:SS'
    numbers.draw_number[':'](6, 25, turtles[2])
    numbers.draw_number[':'](6, 25, turtles[5])

    while True:
        next_date = datetime.today().strftime('%H:%M:%S')

        if previous_date != next_date:
            numbers.draw(turtles, previous_date, next_date, square_size)
            previous_date = next_date
        
        time.sleep(0.1)


if sucess:
    initial_position()
else:
    print("O modulo 'numbers.py' e 'background.py' nao foi encontrado no diretorio atual")
    print("Verifique se o arquivo 'numbers.py' e 'background.py' esta no diretorio atual")



