import turtle

t = turtle.Turtle()
t.speed(3)
t.pensize(5)

# Move to starting position
t.penup()
t.goto(-150, 0)
t.pendown()

# --------- Letter A ---------
t.left(75)
t.forward(120)
t.right(150)
t.forward(120)

t.backward(60)
t.right(105)
t.forward(35)

# Move for next letter
t.penup()
t.goto(20, 0)
t.setheading(90)
t.pendown()

# --------- Letter N ---------
t.forward(120)
t.right(150)
t.forward(140)
t.left(150)
t.forward(120)

turtle.done()
