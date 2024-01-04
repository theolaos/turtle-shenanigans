from turtle import *

#defining the pen turtle
pen = Turtle()
pen.shape('circle')
pen.color('blue')
pen.speed(0)

#define smt
def draw(x,y):
    pen.goto(x,y)

def move(x,y):
    pen.penup()
    pen.goto(x,y)
    pen.pendown()

#defining the movement of the turtle
def goup():
    pen.goto(pen.xcor(),pen.ycor()+5)
def godown():
    pen.goto(pen.xcor(),pen.ycor()-5)
def goleft():
    pen.goto(pen.xcor()-5,pen.ycor())
def goright():
    pen.goto(pen.xcor()+5,pen.ycor())

#defining colors
def setblack():
    pen.color('black')
def setblue():
    pen.color('blue')
def setgreen():
    pen.color('green')
def setred():
    pen.color('red')

#defining the fil commands
def stFill():
    pen.begin_fill()
def enFill():
    pen.end_fill()

#defining the commands for the txt save system
def read_fil_for_trtl(s,tr):
    t = open(s, 'r')
    lines = []
    lines = t.readlines()
    for i in range(len(lines)):
        if i == 0:
            tr.pu()
        tr.goto(float(lines[i][0 : lines[i].find(' ')]) , float(lines[i][lines[i].find(' ') : len(lines[i])]))
        if i == 0:
            tr.pd()
    t.close()

def write_txt(s,tuplee):
    t = open(s, 'w+')

    for i in range(len(tuplee)):  
        t.write(str(tuplee[i][0]) + ' ' + str(tuplee[i][1])+'\n')
    t.close()

def writ_simpfil(a,j):
    tuplee = []
    s = open(a, 'r')
    tuplee = s.readlines()

    t = open(j, 'w+')
    i = 0
    while i < len(tuplee):
        t.write(str(tuplee[i]))
        i += 4
    t.write(str(tuplee[len(tuplee)-1]))
    s.close()
    t.close()

#defining the commands of the poly system
filtitle1 = 'drawing1'
def saving_poly(tpl):
    write_txt(filtitle1+'.txt',tpl)
    writ_simpfil(filtitle1+'.txt',filtitle1+'v.txt')

def stPoly():
    pen.begin_poly()

def enPoly():
    pen.end_poly()
    saving_poly(pen.get_poly())

def rePoly():
    read_fil_for_trtl(filtitle1 +'v.txt',pen)
def roPoly():
    read_fil_for_trtl(filtitle1 +'.txt',pen)

#defining the clear command
def clearscr():
    pen.clear()

#assigning the listeners to the pen object
scr = pen.getscreen()
scr.onscreenclick(move)
scr.listen()
pen.ondrag(draw)

#setting the listeners to listen for movement
scr.onkey(goup, 'Up')
scr.onkey(godown, 'Down')
scr.onkey(goleft, 'Left')
scr.onkey(goright, 'Right')

#setting the listeners for colors
scr.onkey(setblack, 'k')
scr.onkey(setblue, 'b')
scr.onkey(setgreen, 'g')
scr.onkey(setred, 'r')

#setting the listeners for the fill command
scr.onkey(stFill,'f')
scr.onkey(enFill,'e')

#setting the listeners fot the poly command
scr.onkey(stPoly, 'p')
scr.onkey(enPoly, 'o')
scr.onkey(rePoly, 'i')
scr.onkey(roPoly, 'u')

#setting the clear listener
scr.onkey(clearscr, 'c')

mainloop()