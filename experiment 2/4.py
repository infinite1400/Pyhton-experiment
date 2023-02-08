import turtle
t=turtle.Turtle()
r=70
t.pensize(2)
t.color("black")
t.circle(r)

t.color("blue")
t.penup()
t.goto(-150,0)
t.pendown()
t.circle(r)

t.color("red")
t.penup()
t.goto(150,0)
t.pendown()
t.circle(r)

t.color("yellow")
t.penup()
t.goto(-75,-70)
t.pendown()
t.circle(r)

t.color("green")
t.penup()
t.goto(75,-70)
t.pendown()
t.circle(r)