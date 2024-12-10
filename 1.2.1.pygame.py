from numpy import sqrt
import pygame
import random as rand


name = input("What's your name?\n > ")
Tutel = (400, 300)
Tutarget = (400, 300)
mouse = (0, 0)


pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("PLTW 1.2.1 (Python)")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Andale", 26)


lmb = False
oldlmb = False
dt = 0
finaltime = 0
TimeLeft = 30


running = True
while running:
    screen.fill("black")
    lmb = pygame.mouse.get_pressed()[0]
    mouse = pygame.mouse.get_pos()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if (lmb == True) and (oldlmb == False):
        if (sqrt(pow(mouse[0] - Tutel[0], 2)+pow(mouse[1] - Tutel[1], 2)) < 20):
            Tutarget = (rand.random()*(800-(20*2)), rand.random()*(600-(20*2)))

    Tutel = (Tutarget[0] + (Tutel[0] - Tutarget[0])*pow(.5, dt * 12), Tutarget[1] + (Tutel[1] - Tutarget[1])*pow(.5, dt * 12))
    pygame.draw.circle(screen, (255, 255, 255, 255), Tutel, 20)


    pygame.display.flip()
    oldlmb = lmb
    dt = clock.tick() / 1000


pygame.font.quit()
pygame.quit()
