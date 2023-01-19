import turtle
t=turtle.Turtle()
r=50
t.pensize(2)
t.color("blue")
t.circle(r)

t.color("black")
t.penup()
t.goto(70,0)
t.pendown()
t.circle(r)

t.color("red")
t.penup()
t.goto(140,0)
t.pendown()
t.circle(r)

t.color("yellow")
t.penup()
t.goto(40,-50)
t.pendown()
t.circle(r)

t.color("green")
t.penup()
t.goto(110,-50)
t.pendown()
t.circle(r)