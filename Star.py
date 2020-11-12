import turtle

bob=turtle.Turtle()

#set up the screen
wn = turtle.Screen()
wn.title("Graphics")
wn.bgcolor("#994444")
wn.setup(width=600, height=600)
#wn.tracer(0)
bob.speed(50)
bob.penup()
bob.left(90)
bob.forward(30)
bob.right(90)
bob.pendown()


def star(turtle,size):
    if size<=10:
        return
    else:
        for i in range(5):
            turtle.forward(size)
            star(turtle,size/3)
            turtle.left(216)

star(bob,300)
bob.penup()
bob.forward(1000)

turtle.done()
