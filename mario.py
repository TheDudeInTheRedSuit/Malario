import pygame
import random
import math

# Initialize Pygame
pygame.init()

#general setup
WIDTH, HEIGHT = 1024, 512
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MARIO!")

#make images into variables
ground = pygame.image.load("ground.png").convert()
ground = pygame.transform.scale(ground, (128, 128))

mario = pygame.image.load("mario.png").convert_alpha()
mario = pygame.transform.scale(mario, (48, 48))

#setup frames
clock = pygame.time.Clock()

#player variables
px = 200
py = 336
accelcounter = 1
standing = False
jumpercounter = 0
mx = 0
mvleft = False
mvright = False

def movecalcX():
    global accelcounter, mvleft, mvright, mx, mario
    if accelcounter > 55:
        accelcounter = 55
    mxmulti = 1
    mx = int(51 * (1 - math.exp(-0.05 * accelcounter)))
    mx = int(mx / 10)
    
    
    if mvleft == True:
        mxmulti = -1
        mario = pygame.image.load("mariobutleft.png").convert_alpha()
        mario = pygame.transform.scale(mario, (48, 48))
        
    elif mvright == True:
        mxmulti = 1
        mario = pygame.image.load("mario.png").convert_alpha()
        mario = pygame.transform.scale(mario, (48, 48))
        
    return mx * mxmulti

def movecalcY():
    global standing, jumpercounter
    my = 0

    if jumpercounter > 0:
        my -= 16
        jumpercounter -= 1
    
    if py > 335:
        standing = True
    else:
        my += 8
        standing = False
    return my

def playermove(MvAmX, MvAmY):
    global px, py
    px += MvAmX
    py += MvAmY
    screen.blit(mario, (px, py))

def rectload():
    print('dummy to prevent errors')

def mapload():
    print('dummy to prevent errors')

def collidetect():
    print('dummy to prevent errors')
    
while True:
#events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        #Jump detections
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if standing == True:
                    jumpercounter = 25
    
    #movement detections
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        
        if standing == True:
            accelcounter += 1
        
        mvleft = False
        mvright = True

    elif keys[pygame.K_a]:

        if standing == True:
            accelcounter += 1

        mvleft = True
        mvright = False
        
    else: 
        if accelcounter > 0:
            if mvleft == True or mvright == True:
                accelcounter -= 5
        else:
            mvleft = False
            mvright = False

    #make background Blue
    screen.fill((135, 206, 235))

    #draw ground
    y = 0
    for x in range(8):
        screen.blit(ground, (y, 384))
        y += 128
    
    playermove(movecalcX(), movecalcY())

    
    # Update display and tick clock
    pygame.display.flip()
    clock.tick(60)