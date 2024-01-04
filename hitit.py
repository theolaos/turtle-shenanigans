from turtle import *

#creating the class sprite
class sprite(Turtle):
    def __init__(self, x, y, fstep=2, shape='circle', color='black'):
        super().__init__()
        self.penup()
        self.speed(0)
        self.shape(shape)
        self.color(color)
        self.xcord = x
        self.ycord = y
        self.goto(x, y)
        self.fstep=fstep
    #define goto starting coords
    def startgoto(self):
        self.goto(self.xcord,self.ycord)
    #defining the movement of the turtle
    def goup(self):
        self.goto(self.xcor(),self.ycor()+10)
    def godown(self):
        self.goto(self.xcor(),self.ycor()-10)
    def goleft(self):
        self.goto(self.xcor()-10,self.ycor())
    def goright(self):
        self.goto(self.xcor()+10,self.ycor())
    #collisions
    def collisions(self,enmsprite):
        if self.distance(enmsprite.xcor(), enmsprite.ycor()) < 20:
            return True
        else:
            return False

    #defioning the cords for the moving system
    def coords(self,xstart,xend,):
        self.xstart = xstart
        self.xend = xend
        self.goto(xstart,self.ycord)
        self.setheading(self.towards(xend,self.ycord))

    #moving obstacles
    def step_move(self):
        self.forward(self.fstep)
        if self.distance(self.xend,self.ycord) < self.fstep:
            self.coords(self.xend,self.xstart)
class counter(Turtle):
    def __init__(self, x, y, shape='circle', color='black'):
        super().__init__()
        self.speed(0)
        self.shape(shape)
        self.color(color)
        self.penup()
        self.goto(x, y)
        self.pendown()
        self.pensize(40)
        self.hideturtle()
        self.lt(90)
    def show_count(self,count):
        self.color('white')
        self.fd(5)
        self.fd(-5)
        self.color('black')
        self.write(count, align='left', font=('Arial', 15, 'normal'))

player = sprite(0,-100,10,'circle','blue')
enemy1 = sprite(100,30,10,'square','red')
enemy2 = sprite(-100,-30,10,'square','red')
target = sprite(0,100,10,'arrow','green')
counterr = counter(100,200)

enemy1.coords(120,-120)
enemy2.coords(-120,120)

#assigning the listeners to the pen object
scr = player.getscreen()
scr.listen()
#setting the listeners to listen for movement
scr.onkey(player.goup, 'Up')
scr.onkey(player.godown, 'Down')
scr.onkey(player.goleft, 'Left')
scr.onkey(player.goright, 'Right')

tosce = 0
counterr.show_count(tosce)
#game loop
while tosce != 3:
    enemy1.step_move()
    enemy2.step_move()
    if player.collisions(enemy1) or player.collisions(enemy2):
        break
    elif player.xcor() <= -120 or player.xcor() >= 120:
        break
    elif player.collisions(target):
        player.startgoto()
        tosce += 1
        counterr.show_count(tosce)

    
if tosce == 3:
    target.hideturtle()
    player.hideturtle()
    player.write('well done')
