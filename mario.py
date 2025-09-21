import pygame

# Initialize Pygame
pygame.init()

#general setup
WIDTH, HEIGHT = 1024, 512
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MARIO!")

hitboxcolor = (0,0,160)

playerhitbox = pygame.Rect(0,0,48,48)

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
accelcounter = 0
standing = False
jumpercounter = 0
mx = 0
mvleft = False
mvright = False

# Movement values
vx, vy = 0, 0
speed = 300        # max speed (px/sec)
accel = 1200       # acceleration rate (px/sec^2)
friction = 800     # deceleration when no input



class playermovement():
    def movecalcX(self):
        global mvleft, mvright, mx, mario, dt,standing

        if mvleft == True:
            mario = pygame.image.load("mariobutleft.png").convert_alpha()
            mario = pygame.transform.scale(mario, (48, 48))
            
        elif mvright == True:
            mario = pygame.image.load("mario.png").convert_alpha()
            mario = pygame.transform.scale(mario, (48, 48))
            
        mx = vx * dt

        return mx

    def movecalcY(self):
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

    def playermove(self, MvAmX, MvAmY):
        global px, py, playerhitbox
        px += MvAmX
        py += MvAmY
        # draw rect, (screen) (color) (x,y,width,height)
        playerhitbox = pygame.Rect(px,py,48,48)
        screen.blit(mario, (px, py))

def rectload():
    print('dummy to prevent errors')

def mapload():
    print('dummy to prevent errors')

def collidetect():
    print('dummy to prevent errors')

pm = playermovement()
while True:
#events
    dt = clock.tick(60) / 1000
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
    ax = 0
    if keys[pygame.K_a] and keys[pygame.K_d]:
        mvleft = False
        mvright = False

    elif keys[pygame.K_d]:
        ax += accel
        mvleft = False
        mvright = True

    elif keys[pygame.K_a]:
        ax -= accel
        mvleft = True
        mvright = False
        
    else: 
        mvleft = False
        mvright = False

    vx += ax * dt

    if ax == 0:
        if vx > 0:
            vx -= min(friction * dt, vx)
        elif vx < 0:
            vx += min(friction * dt, -vx)
        if standing == False:
            vx = 0

    if vx > speed: vx = speed
    if vx < -speed: vx = -speed

    #make background Blue
    screen.fill((135, 206, 235))

    #draw ground
    y = 0
    for x in range(8):
        screen.blit(ground, (y, 384))
        y += 128
    
    pm.playermove(pm.movecalcX(), pm.movecalcY())

    
    # Update display and tick clock
    pygame.display.flip()
    clock.tick(60)