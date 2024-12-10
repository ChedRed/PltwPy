from numpy import sqrt
import turtle as tutel
import time as ti
import random as rand


screen = tutel.Screen()
turt = tutel.Turtle()
text = tutel.Turtle()


turt.penup()
turt.shape("circle")
turt.color("white")
turt.shapesize(2)
tapos = [0, 0]
mouse = [0, 0]
mousess = False


text.penup()
text.hideturtle()
text.color("white")


old = ti.time()
new = ti.time()
deltime = new - old
screen.setup(800,600)
screen.screensize(0,0,"black")
screen.title("PLTW 1.2.1 (Python, Turtle)")
screen.tracer(0)


timer = 30
score = 0


def mouseclick(x, y):
    global mouse
    global mousess
    mouse[0] = x
    mouse[1] = y
    mousess = True


screen.onscreenclick(mouseclick)


while True:
    new = ti.time()
    deltime = new - old
    screen.clear()


    if mousess == True:
        mousess = False
        if (sqrt(pow(mouse[0]-turt.pos()[0], 2)+pow(mouse[1]-turt.pos()[1], 2))<20):
            tapos = (rand.random()*(800-(20*2))-400, rand.random()*(600-(20*2))-300)
            print(tapos)


    turt.goto(tapos[0] + (turt.pos()[0] - tapos[0])*pow(.5, deltime * 12), tapos[1] + (turt.pos()[1] - tapos[1])*pow(.5, deltime * 12))
    text.goto(-400, 280)
    text.write("Score: "+str(score), move=False, font=("Arial", 26, "normal"))


    screen.update()
    old = new
