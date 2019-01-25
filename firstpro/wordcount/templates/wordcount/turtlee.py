import turtle
import random
import math

p=turtle.Turtle()
p.color("blue")
p.shape("turtle")
p.penup()
p.speed(0)
screen=p.getscreen()

circles=[]

for i in range(10):
    a1=turtle.Turtle()
    a1.color("red")
    a1.shape("circle")
    a1.penup()
    a1.speed(0)
    a1.goto(random.randint(-300,300),random.randint(-300,300))
    circles.append(a1)

def turnleft():
    p.left(30)
    
def turnright():
    p.right(30)

screen.onkeypress(turnleft,"Left")
screen.onkeypress(turnright,"Right")
screen.listen()

def play():
    p.forward(160)
    for a in circles:                                    
        a.left(random.randint(-360,360))
        a.forward(3)
        if p.distance(a)<70:
            p.write("crash")
            a.ht()
    screen.ontimer(play,10)

screen.ontimer(play,10)



