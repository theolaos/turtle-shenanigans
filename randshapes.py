from turtle import *
# pl = mikos pleura 
# pln = poses pleures iparxoun
# ln = tin gwnia kathe pleuras(360/pln)
# bg = poso ipsos na exei i kardia
# clr = the color of heart the user wants it to have :)
# fl = if the users wants it filled or not??

def heart(pl,pln,bg,clr):
    color(clr)
    orcorx = xcor()
    orcory = ycor()
    ln = 360 / (pln * 2)

    #re-orient
    penup()
    lt(360-heading()+90)
    goto(xcor(),ycor()+bg)
    pendown()

    #making the first "wave" of the heart
    for i in range(int(pln)):
        rt(ln)
        forward(pl)
    goto(orcorx,orcory)

    penup()
    #re-orient
    lt(360-heading()+90)
    goto(xcor(),ycor()+bg)
    pendown()

    #maiking the second "wave" of the heart
    for i in range(int(pln)):
        lt(ln)
        forward(pl)
    goto(orcorx,orcory)

    lt(360-heading()+90)
    color("black")

def square(spl,sclr,sfl):
    if sfl == "yes":
        begin_fill()
    color(sclr)

    for i in range(4):
        forward(spl)
        left(90)
    
    if sfl == "yes":
        end_fill()
    color("black")


def circle1(radius):
    circle(radius)

def polygon(pl):
    ln = 5
    pln = float(360 / pl)
    for i in range(int(pl)):
        forward(ln)
        lt(pln)

def star(stpl,stpln,stclr,stfl):
    color(stclr)
    orang = 150 
    ang = 360/stpln

    if stfl == 1:
        begin_fill()

    for i in range(stpln):
        forward(stpl)
        rt(orang)
        forward(stpl)
        lt(orang)

        rt(ang)

    if stfl == 1:
        end_fill()

    color("black")

def red_sign(rc):
    color('red')
    begin_fill()
    circle(rc)
    end_fill()
    penup()
    goto(xcor()-32,ycor()+37)
    pendown()
    color("white")
    begin_fill()
    for i in range(2):
        forward(65)
        left(90)
        forward(20)
        left(90)
    end_fill()
    color('black')

def fence_link():
    pensize(2)
    color("black","orange")
    begin_fill()
    left(90)
    forward(100)
    right(30)
    forward(42)
    right(120)
    forward(42)
    right(30)
    forward(100)
    right(90)
    forward(42)
    left(180)
    end_fill()