from time import sleep
from turtle import *

#makin the timer turtle
counter = Turtle()
counter.hideturtle()
counter.pensize(200)
counter.pendown()

#making our life easier :)
def buffer_count(s):
    counter.color('white')
    counter.forward(2)
    counter.forward(-2)
    counter.color('black')
    counter.write(s, font=('Ariel', 50))

tm = abs(int(numinput('Coundown number', 'What is your coundown?')))

print(tm)
for i in range(tm):
    sleep(0.9)
    s = tm - i
    buffer_count(s)