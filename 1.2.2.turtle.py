from numpy import sqrt
import turtle as tutel
import time as ti
import random as rand


iname = input("What's your name?\n > ")
name = ""
for i in range(len(iname)):
    if (iname[i].lower() in "abcdefghijklmnopqrstuvwxyz"):
        name += iname[i]


scobord = []
Tier = [[15, "You have reached the bronze tier!"], [25, "You have reached the silver tier!"], [35, "You have reached the gold tier!"], [45, "You have reached the platinum tier!"]]
longest = 0


running = True
stage = 0


screen = tutel.Screen()
turt = tutel.Turtle()
scoretext = tutel.Turtle()
timedtext = tutel.Turtle()
tempturtl = tutel.Turtle()
boardtext = tutel.Turtle()


radius = 20
turt.penup()
turt.shape("circle")
turt.color("white")
turt.shapesize(radius/10)
tapos = [0, 0]
mouse = [0, 0]
mousess = False


scoretext.penup()
scoretext.hideturtle()
scoretext.color("white")
scoretext.goto(-390, 255)
timedtext.penup()
timedtext.hideturtle()
timedtext.color("white")
timedtext.goto(385, 255)
tempturtl.penup()
tempturtl.hideturtle()
tempturtl.color("black")
tempturtl.goto(0, 0)
boardtext.penup()
boardtext.hideturtle()
boardtext.color("white")
boardtext.goto(0, 0)


old = ti.time()
new = ti.time()
deltime = new - old
screen.setup(800,600)
screen.screensize(0, 0, "black")
screen.colormode(255)
screen.title("PLTW 1.2.2 (Python, Turtle)")
screen.tracer(0)


timer = 30
score = 0


def mouseclick(x, y):
    global mouse
    global mousess
    mouse[0] = x
    mouse[1] = y
    mousess = True


def winclose():
    global running
    running = False


screen.onscreenclick(mouseclick)
screen.getcanvas().winfo_toplevel().protocol("WM_DELETE_WINDOW", winclose)


while running:
    new = ti.time()
    deltime = new - old


    if mousess == True:
        mousess = False
        if (sqrt(pow(mouse[0]-turt.pos()[0], 2)+pow(mouse[1]-turt.pos()[1], 2))<radius):
            if stage == 0:
                stage = 1
            if stage == 1:
                tapos = (rand.random()*(800-(radius*2))-400+radius, rand.random()*(500-(radius*2))-300+(radius*2))
                score += 1


    turt.goto(tapos[0] + (turt.pos()[0] - tapos[0])*pow(.5, deltime * 12), tapos[1] + (turt.pos()[1] - tapos[1])*pow(.5, deltime * 12))


    if stage < 4:
        scoretext.write("Score: " + str(score), move=False, font=("Arial", 26, "normal"))
        timedtext.write(str(int(timer)) + " Seconds Left", move=False, align="right", font=("Arial", 26, "normal"))


    if stage == 1:
        timer -= deltime
        if int(timer) <= 0:
            timer = 1
            stage = 2
    elif stage == 2: # Comments for the confused (like me):


        # Open, read, and clear file.
        try:
            temp = open("Scores", "x")
            temp.close()
        except:
            pass
        file = open("Scores", "r+")
        filines = file.readlines()
        file.truncate(0)


        # 1. Set scobord list of lists to player name and score.
        # 2. Append scores from file (and prep for stage 4).
        # 3. Sort (yay lambda!).
        # 4. Keep top 5.
        scobord = [[name, score]]
        tempturtl.write(name, move=True, font=("Arial", 26, "normal"))
        longest = tempturtl.xcor()
        for i in range(len(filines)):
            if (filines[i] != "\n"):
                newfiline = filines[i].split("|")
                scobord.append([newfiline[0], int(newfiline[1])])
                tempturtl.goto(0, 0)
                tempturtl.write(newfiline[0], move=True, font=("Arial", 26, "normal"))
                if tempturtl.xcor() > longest:
                    longest = tempturtl.xcor()
        boardtext.goto(-400-longest, 255)
        scobord.sort(key=lambda x:x[1], reverse=True)
        scobord = scobord[:5]


        # Write scobord data to file and close it.
        file.seek(0)
        for i in range(len(scobord)):
            file.write(scobord[i][0]+"|"+str(scobord[i][1])+"\n")
        file.close()
        stage = 3


    elif stage == 3:
        if timer - deltime < 0:
            timer = 0
            stage = 4
        else: timer -= deltime
        timedtext.color(int(timer * 255), int(timer * 255), int(timer * 255))
        scoretext.color(int(timer * 255), int(timer * 255), int(timer * 255))
        turt.color(int(timer * 255), int(timer * 255), int(timer * 255))
    elif stage == 4:
        if timer+deltime > 1:
            timer = 1
        else:
            timer += deltime

        for i in range(len(Tier)):
            if Tier[len(Tier)-i-1][0] <= score:
                scoretext.setx(800)
                scoretext.write(Tier[len(Tier)-i-1][1], move=True, font=("Arial", 26, "normal"))
                scoretext.setx(((scoretext.xcor()-800)/2)-400)
                scoretext.sety(0)
                scoretext.color(int(timer * 255), int(timer * 255), int(timer * 255))
                scoretext.write(Tier[len(Tier)-i-1][1], move=False, font=("Arial", 26, "normal"))
                break
        boardtext.setx(-390 + (boardtext.xcor() + 390)*pow(.5, deltime * 12))
        for i in range(len(scobord)):
            boardtext.sety(255-(35*i))
            boardtext.write("] " + str(scobord[i][0]) + ": " + str(scobord[i][1]), move=False, font=("Arial", 26, "normal"))
        for i in range(5-len(scobord)):
            boardtext.sety(255-(35*(i+len(scobord))))
            boardtext.write("] ", move=False, font=("Arial", 26, "normal"))



    screen.update()
    scoretext.clear()
    timedtext.clear()
    boardtext.clear()
    old = new


tutel.bye()
