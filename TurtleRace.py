import turtle
from random import *
import ctypes

#set up the screen
wn = turtle.Screen()
wn.title("Turtle Race")
wn.bgcolor("#222244")
wn.setup(width=600, height=600)


grader=turtle.Turtle()

grader.penup()
grader.goto(200,-220)
grader.pendown()
grader.left(90)
grader.speed(1)
grader.forward(440)
grader.penup()
grader.goto(500,0)

player1=turtle.Turtle()
player2=turtle.Turtle()
player3=turtle.Turtle()
player4=turtle.Turtle()


player1.color('red')
player2.color('blue')
player3.color('yellow')
player4.color('green')


player1.shape('turtle')
player2.shape('turtle')
player3.shape('turtle')
player4.shape('turtle')


player1.penup()
player2.penup()
player3.penup()
player4.penup()


player1.goto(-100,180)
player2.goto(-100,60)
player3.goto(-100,-60)
player4.goto(-100,-180)

for i in range(500):
    player1.forward(randint(1,15))
    player2.forward(randint(1,15))
    player3.forward(randint(1,15))
    player4.forward(randint(1,15))
    if player1.pos()[0]>=200:
        ctypes.windll.user32.MessageBoxW(0, "Red Turtle Won", "Race Result", 1)
        break
    elif player2.pos()[0]>=200:
        ctypes.windll.user32.MessageBoxW(0, "Blue Turtle Won", "Race Result", 1)
        break
    elif player3.pos()[0]>=200:
        ctypes.windll.user32.MessageBoxW(0, "Yellow Turtle Won", "Race Result", 1)
        break
    elif player4.pos()[0]>=200:
        ctypes.windll.user32.MessageBoxW(0, "Green Turtle Won", "Race Result", 1)
        break


turtle.done()
