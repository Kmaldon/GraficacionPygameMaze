import pygame, sys
from pygame.locals import * 

pygame.init()
speed = 2
width = 20
height = 20

winWidth = 700
winHeight = 600

win = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption("Maze Game")
clock = pygame.time.Clock()

wallLines = [
    #Wallpoints 1
    ((15, 15), (685, 15)), ((300, 60), (300, 15)), ((685, 15), (685, 530)), 
    ((200, 530), (685, 530)), ((530, 480), (530, 530)), ((640, 530), (640, 60)), 
    ((575, 480), (640, 480)), ((640, 340), (510, 340)), ((640, 60), (440, 60)), 
    ((440, 60), (440, 100)), ((440, 100), (590, 100)), ((590, 100), (590, 140)), 
    ((590, 140), (400, 140)), ((400, 140), (400, 60)), ((400, 60), (355, 60)),
    ((355, 60), (355, 100)), ((355, 100), (255, 100)), ((255, 100), (255, 60)), 
    ((255, 60), (145, 60)), ((145, 60), (145, 140)), ((200, 100), (145, 100)), 
    ((145, 140), (355, 140)),

    #Wallpoints 2
    ((685, 580), (15, 580)), ((15, 385), (55, 385)), ((15, 585), (15, 60)), 
    ((15, 60), (100, 60)), ((100, 60), (100, 180)), ((355, 180), (55, 180)), 
    ((55, 90), (55, 340)), ((100, 340), (100, 220)), ((55, 340), (145, 340)), 
    ((145, 340), (145, 220)), ((145, 220), (355, 220)), ((355, 265), (310, 265)), 
    ((355, 220), (355, 305)), ((355, 305), (270, 305)), ((270, 305), (270, 265)), 
    ((190, 265), (190, 305)), ((230, 305), (190, 305)), ((190, 340), (400, 340)), 
    ((400, 180), (545, 180)), ((545, 220), (545, 180)), ((590, 180), (590, 255)), 
    ((510, 255), (510, 220)), ((440, 220), (440, 255)), ((475, 255), (440, 255)), 
    ((440, 340), (475, 340)), ((475, 295), (590, 295)), ((475, 295), (475, 385)), 
    ((100, 385), (590, 385)), ((590, 435), (475, 435)), ((475, 480), (250, 480)),
    ((250, 435), (430, 435)), ((200, 435), (200, 480)), ((200, 435), (55, 435)),
    ((55, 480), (155, 480)), ((155, 530), (55, 530))
]

x = 15
y = 28

while True:
    clock.tick(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ky = pygame.key.get_pressed()
    if ky[pygame.K_LEFT] and x > speed:
        x -= speed
    if ky[pygame.K_RIGHT] and x < winWidth - speed - width:
        x += speed
    if ky[pygame.K_UP] and y > speed:
        y -= speed
    if ky[pygame.K_DOWN] and y < winHeight - height - speed:
        y += speed

    win.fill((255, 255, 255))
    player = pygame.draw.rect(win, (0, 255, 0), (x, y, width, height))
    Finish = pygame.draw.rect(win, (255, 0, 0), (676, 530, 10, 50))

    if any(player.clipline(*line) for line in wallLines):
        if ky[pygame.K_LEFT] and x > speed:
            x += speed
        if ky[pygame.K_RIGHT] and x < winWidth - speed - width:
            x -= speed
        if ky[pygame.K_UP] and y > speed:
            y += speed
        if ky[pygame.K_DOWN] and y < winHeight - height - speed:
            y -= speed

    for line in wallLines:
        pygame.draw.line(win, (0, 0, 0), *line, 3)


    pygame.display.update()