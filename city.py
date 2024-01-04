from turtle import *
from random import randint

def gototo(xcor,ycor):
    penup()
    goto(xcor,ycor)
    pendown()


def sun_moon(sm):
    if sm == 'sun':
        #makin the sun
        #declaring variables
        stpln = 18
        stpl = 10
        color("yellow","orange")
        orang = 100
        ang = 360/stpln

        begin_fill()
        #drwaing the sun
        for i in range(stpln):
            forward(stpl)
            rt(orang)
            forward(stpl)
            lt(orang)
            rt(ang)
        end_fill()

        color("black")
    else:
        #making the moon
        color('bisque')
        begin_fill()
        circle(30)
        end_fill()

        color('black')

def backgorund(suomo,ycor1):
    #making the background
    ycor = ycor1 -200
    
    penup()
    goto(-200,ycor)
    pendown()
    color("green")
    begin_fill()

    #drawing the grass
    for i in range(2):
        forward(400)
        rt(90)
        forward(ycor +200)
        rt(90)
    end_fill()
    
    gototo(-200,ycor)


    #checking what did the user chose to make the sky like
    if suomo == "sun":
        color('blue')
    else:
        color('black')
    #drawing the sky as the user intended it to be
    begin_fill()
    lt(90)
    goto(xcor(), 200)
    rt(90)
    forward(400)
    rt(90)
    goto(xcor(), ycor)
    rt(90)
    forward(400)
    end_fill()

    #drawing the sun and the moon in our background
    if suomo == 'moon':
        gototo(150,120)
        lt(360-heading())
        sun_moon(suomo)
        return 2
    else:
        gototo(180,180)
        lt(360-heading())
        sun_moon(suomo)
        return 1

#making the building
#rooms are also the small blocks that define our building
#i also do not understand what i did here :)
def rooms(clrbl1,clrw,bubl1):
    color(clrbl1)
    begin_fill()
    lt(360-heading()+90)
    for i in range(4):
        forward(bubl1)
        rt(90)
    end_fill()

    #changing the color according on how the background looks
    if clrw == "moon":
        color('DarkGoldenrod1')
    else:
        color('burlywood3')

    #making the windows
    gototo(xcor()+bubl1/4,ycor()+bubl1/4)
    begin_fill()
    for i in range(4):
        forward(int(bubl1/2))
        rt(90)
    end_fill()
    gototo(xcor()-bubl1/4,ycor()-bubl1/4)

def house(dim,bubl,clrw,clrbl,ycor1):
    gototo(-180,(ycor1/2) - 200 )
    orcorx = xcor()
    orcory = ycor()
    #translating the string input to actual numbers
    cor = dim
    dim1 = int(dim[0])
    dim2 = int(dim[len(cor)-1])

    #making the house using the rooms argument
    for i in range(dim2):
        lt(360-heading())
        if i > 0:
            penup()
            goto(orcorx,orcory)
            forward(bubl*i)
            pendown()
        for j in range(dim1):
            rooms(clrbl,clrw,bubl)
            gototo(xcor(),ycor()+bubl)





# def pharm():

#tests
ycor12 = 200
mood='moon'
building_dimensions='3x2'
building_blocks_height = 50
building_color='grey'

backgorund(mood,ycor12)
house(building_dimensions,building_blocks_height,mood,building_color,ycor12)
exitonclick()