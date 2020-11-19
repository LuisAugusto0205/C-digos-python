def border(turtle, square_size, border_size, color):
    turtle.width(5)
    turtle.speed(40)
    turtle.penup()
    turtle.fillcolor(color)
    turtle.goto(-(7*square_size)/2 - border_size/2, -square_size/2 - border_size)
    turtle.pendown()

    turtle.begin_fill()
    for i in range(4):
        if i%2:
            turtle.forward(square_size + border_size)
        else:
            turtle.forward((13*square_size/2) + border_size)
        turtle.circle(border_size/2, extent = 90)
    turtle.end_fill()

    visor_turtle = turtle.clone()
    visor_turtle.penup()
    visor_turtle.fillcolor('gray')
    visor_turtle.goto(turtle.xcor() + border_size/2, turtle.ycor() + border_size/2)
    visor_turtle.pendown()

    visor_turtle.begin_fill()
    for i in range(4):
        visor_turtle.forward((not i%2)*((13*square_size/2)) + 
                       (i%2)*(square_size))
        visor_turtle.circle(border_size/2, extent = 90)
    visor_turtle.end_fill()

    base(turtle.clone(), turtle.xcor() + border_size/2, 
         turtle.ycor() - 2.5, square_size/2, color)
    base(turtle.clone(), turtle.xcor() + border_size/2 + 6*square_size, 
         turtle.ycor() - 2.5, square_size/2, color)

def base(turtle, x, y, radius, color):
    turtle.penup()
    turtle.right(90)
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius/2, extent=180)
    turtle.end_fill()
