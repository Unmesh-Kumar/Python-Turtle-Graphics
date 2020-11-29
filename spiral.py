from turtle import Screen as s,Turtle as t
from random import choice
import time

class Turtle(t):
    def __init__(self,shape='turtle',isHidden=True):
        super().__init__()
        self.speed('fastest')
        if isHidden:
            self.hideturtle()
        else:
            self.shape(shape)

screen=s()
screen.bgcolor('black')
turtles=[]
colors=['red','purple','green','orange','indigo','blue']
headings=[0,90,180,270]
pensize=0.1

for i in range(4):
    t=Turtle()
    t.setheading(headings[i])
    turtles.append(t)


time.sleep(5)

for i in range(45):
    for turtle in turtles:
        turtle.color(choice(colors))
        turtle.pensize(pensize)
        turtle.forward(10)
        turtle.left(4)
        pensize+=0.3

screen.exitonclick()
