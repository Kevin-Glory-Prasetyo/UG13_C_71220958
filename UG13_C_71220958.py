import turtle
s = turtle.Screen()
t = turtle.Turtle()
t.pensize(15)
t.speed(15)
t.pencolor("blue")
s.bgcolor("purple")

#huruf k
t.penup()
t.goto(-300,100)
t.pendown()
t.right(90)
t.forward(100)
t.left(180)
t.forward(50)
t.right(45)
t.forward(68)
t.left(180)
t.forward(68)
t.left(90)
t.forward(68)
t.penup()

#huruf 9
t.goto(-100,250)
t.penup()
t.pendown()
t.right(45)
t.penup()
t.forward(70)
t.pendown()
t.left(180)
t.forward(50)
t.circle(30,-360)
t.right(180)
t.forward(60)
t.circle(-30,180)
t.penup()

#huruf P

t.penup()
t.goto(0,-25)
t.pendown()
t.forward(125)

t.right(180)
t.forward(75)

t.left(90)
t.forward(40)
t.circle(37,180)
t.forward(40)
t.penup()

#angka 5
t.goto(-100, 100)
t.pendown()
t.forward(50)
t.left(90)
t.forward(40)
t.left(90)
t.forward(27)
t.circle(-30,250)
t.penup()

#8
t.goto(-100,-50)
t.pendown()
t.circle(35)
t.left(170)
t.circle(-35,90)
t.circle(35)











turtle.done()
