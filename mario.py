import pygame
import random

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
standing = False
jumpercounter = 0

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
        mario = pygame.image.load("mario.png").convert_alpha()
        mario = pygame.transform.scale(mario, (48, 48))
        if standing == True:
            px += 5
        if standing == False:
            px += 4
    if keys[pygame.K_a]:
        mario = pygame.image.load("mariobutleft.png").convert_alpha()
        mario = pygame.transform.scale(mario, (48, 48))
        if standing == True:
            px -= 5
        if standing == False:
            px -= 2

    #make background Blue
    screen.fill((135, 206, 235))

    #draw ground
    y = 0
    for x in range(8):
        screen.blit(ground, (y, 384))
        y += 128
    
    #draw player
    screen.blit(mario, (px, py))

    #Jumping logic
    if jumpercounter > 0:
        py -= 16
        jumpercounter -= 1

    #gravity + if on ground
    if py > 335:
        standing = True
    else:
        py += 8
        standing = False

    # Update display and tick clock
    pygame.display.flip()
    clock.tick(60)