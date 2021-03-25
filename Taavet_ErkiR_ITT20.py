import turtle
import math

#akna seaded
aken = turtle.Screen()
aken.setup(600,600)
aken.title("Taaveti täht lisadega")


k1 = turtle.Turtle() #esimene kolmnurk
k1.pencolor("blue")
k1.pensize(5)
k1.hideturtle()
for x in range(0,3):
    k1.forward(100)
    k1.left(120)

k2 = turtle.Turtle() #teine kolmnurk
k2.pencolor("blue")
k2.pensize(5)
k2.hideturtle()
k2.setx(50)
k2.sety(0)
for x in range(0,3):
    k2.forward(100)
    k2.left(120)

    
k3 = turtle.Turtle() #kolmas kolmnurk
k3.pencolor("blue")
k3.pensize(5)
k3.hideturtle()
k3.penup()
k3.setx(50)
k3.sety(87)
k3.pendown()
for x in range(0,3):
    k3.forward(50)
    k3.left(120)
    
j = turtle.Turtle() #joon
j.pencolor("blue")
j.pensize(5)
j.hideturtle()
j.penup()
j.setx(25)
j.sety(44)
j.pendown()
j.forward(100)

k4 = turtle.Turtle() #neljas kolmnurk
k4.pencolor("blue")
k4.pensize(5)
k4.hideturtle()
k4.penup()
k4.setx(0)
k4.sety(87)
k4.pendown()
for x in range(0,3):
    k4.forward(150)
    k4.right(120)

turtle.exitonclick()



