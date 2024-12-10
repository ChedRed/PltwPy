from numpy import sqrt
import turtle as tutel
import time as ti
import random as rand


name = input("What's your name?\n > ")
running = True
stage = 0


screen = tutel.Screen()
turt = tutel.Turtle()
scoretext = tutel.Turtle()
timedtext = tutel.Turtle()


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


old = ti.time()
new = ti.time()
deltime = new - old
screen.setup(800,600)
screen.screensize(0, 0, "black")
screen.colormode(255)
screen.title("PLTW 1.2.1 (Python, Turtle)")
screen.tracer(0)


timer = 5
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


def manage_leaderboard():
    global score
    global spot


    leader_names_list = lb.get_names(leaderboard_file_name)
    leader_scores_list = lb.get_scores(leaderboard_file_name)


    theis = len(leader_scores_list) < 5 or score >= leader_scores_list[4]
    if theis:
        lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
        return
    lb.draw_leaderboard(theis, leader_names_list, leader_scores_list, spot, score)


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
                tapos = (rand.random()*(800-(radius*2))-400, rand.random()*(600-(radius*2)-45)-300+radius)
                score += 1


    turt.goto(tapos[0] + (turt.pos()[0] - tapos[0])*pow(.5, deltime * 12), tapos[1] + (turt.pos()[1] - tapos[1])*pow(.5, deltime * 12))
    scoretext.write("Score: " + str(score), move=False, font=("Arial", 26, "normal"))
    timedtext.write(str(int(timer)) + " Seconds Left", move=False, align="right", font=("Arial", 26, "normal"))


    if stage == 1:
        timer -= deltime
        if int(timer) <= 0:
            timer = 1
            stage = 2
    elif stage == 2:
        if timer - deltime < 0:
            timer = 0
            stage = 3
        else: timer -= deltime
        timedtext.color(int(timer * 255), int(timer * 255), int(timer * 255))
        scoretext.color(int(timer * 255), int(timer * 255), int(timer * 255))
        turt.color(int(timer * 255), int(timer * 255), int(timer * 255))
    elif stage == 3:
        pass


    screen.update()
    scoretext.clear()
    timedtext.clear()
    old = new


tutel.bye()
