#importing modules
from time import *
from random import randint
from turtle import *


#property of turtles: color, shape, speed, initial placement.
#turtle 1 (blue)
t1 = Turtle()
t1.color('blue')
t1.shape('turtle')
t1.speed(0)
t1.goto(0,0)
t1.points = 0
t1.lt(randint(1,359))

#turtle 2 (green)
t2 = Turtle()
t2.color('green')
t2.shape('turtle')
t2.speed(0)
t2.goto(0,0)
t2.points = 0
t2.rt(randint(1,359))

#turtle 3 (red)
t3 = Turtle()
t3.color('red')
t3.shape('turtle')
t3.speed(0)
t3.goto(0,0)
t3.points = 0
t3.lt(randint(60,200))

#turtle of displaying the points that the player has
dt4 = Turtle()
dt4.color('black')
dt4.hideturtle()
dt4.penup()
dt4.goto(50,200)
dt4.pendown()
dt4.pensize(65)
dt4.speed(0)

points = 0
# def things
def t1catch(x, y):
    t1.penup()
    t1.goto(randint(-100,100),randint(-100,100))
    t1.lt(randint(1,359))
    t1.points += 1
    t1.pendown()

def t2catch(x, y):
    t2.penup()
    t2.goto(randint(-100,100),randint(-100,100))
    t2.rt(randint(1,359))
    t2.points += 1
    t2.pendown()

def t3catch(x, y):
    t3.penup()
    t3.goto(randint(-100,100),randint(-100,100))
    t3.lt(randint(60,200))
    t3.points += 1
    t3.pendown()

def disp_point(p):
    dt4.color('white')
    dt4.forward(2)
    dt4.forward(-2)
    dt4.color('black')
    dt4.write(p, font=('Ariel',20,'normal'))

# subscribing each turtle to a mouse click
t1.onclick(t1catch)
t2.onclick(t2catch)
t3.onclick(t3catch)

#game finished function
def gameFinished(t1,t2,t3):
    t1_out = abs(t1.xcor()) > 200 or abs(t1.ycor()) > 200
    t2_out = abs(t2.xcor()) > 200 or abs(t2.ycor()) > 200
    t3_out = abs(t3.xcor()) > 200 or abs(t3.ycor()) > 200
    isout = t1_out or t2_out or t3_out
    return isout


while gameFinished(t1,t2,t3) != True:
    t1.forward(5)
    t2.forward(5)
    t3.forward(5)
    points = t1.points + t2.points + t3.points
    disp_point(points)