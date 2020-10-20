import turtle

bob=turtle.Turtle()

#set up the screen
wn = turtle.Screen()
wn.title("Graphics")
wn.bgcolor("black")
wn.setup(width=600, height=600)
#wn.tracer(0)
bob.speed(50)


bob.forward(100)

bob.setheading(180)
bob.penup()
bob.forward(0)
bob.pendown()

bob.color('#0E1E55')

for i in range(13):

    bob.penup()
    bob.forward(150)
    bob.left(15)
    bob.pendown()

    for j in range(60):
        bob.forward(60)
        bob.left(180-3)

bob.forward(30)




bob.setheading(180)
bob.penup()
bob.forward(0)
bob.pendown()



bob.color('#0C226C')

for i in range(13):

    bob.penup()
    bob.forward(150)
    bob.left(15)
    bob.pendown()

    for j in range(60):
        bob.forward(60)
        bob.left(180-3)

bob.forward(30)


bob.setheading(180)
bob.penup()
bob.forward(0)
bob.pendown()

bob.color('#122C84')

for i in range(13):

    bob.penup()
    bob.forward(150)
    bob.left(15)
    bob.pendown()

    for j in range(60):
        bob.forward(60)
        bob.left(180-3)

bob.forward(30)



bob.setheading(180)
bob.penup()
bob.forward(0)
bob.pendown()

bob.color('#1D3DA6')

for i in range(13):

    bob.penup()
    bob.forward(150)
    bob.left(15)
    bob.pendown()

    for j in range(60):
        bob.forward(60)
        bob.left(180-3)

bob.forward(30)



bob.setheading(180)
bob.penup()
bob.forward(0)
bob.pendown()

bob.color('#274DC9')

for i in range(13):

    bob.penup()
    bob.forward(150)
    bob.left(15)
    bob.pendown()

    for j in range(60):
        bob.forward(60)
        bob.left(180-3)

bob.forward(30)

turtle.done()
