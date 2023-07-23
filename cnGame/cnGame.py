import pygame
import sys 
import random
from moviepy.editor import *
from pygame.locals import *
import os
pygame.init() 
def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)
screen =  pygame.display.set_mode((1200, 700))
pygame.display.set_caption("Coin Game")
clock = pygame.time.Clock()
running = True
coins = 0
black = (0, 0 , 0)
def load_image(file_name):
    current_dir = os.path.dirname(__file__)
    image_path = os.path.join(current_dir, file_name)
    return pygame.image.load(image_path).convert_alpha()
image = load_image("images/ghost_image.png")
coin_img= load_image("images/coin_image.png")
image = pygame.transform.scale(image, (100, 80))
coin_img = pygame.transform.scale(coin_img, (60, 60))
font = pygame.font.Font(None, 135)
text_surface = font.render(str(coins), True,  (124, 116, 136))
def rand_pos ():
        r_x = random.randint(15, 1140) 
        r_y = random.randint(15, 640)
        for block in arr: 
            if block[0] <= r_x  + 60 and r_x <= block[0] + block[2] and block[1] <= r_y  + 60 and r_y <= block[1] + block[3]:
                return 0, 0
        return  r_x, r_y
arr = {(0, 685, 1200, 15), (0, 0, 1200, 15), (0, 0, 15, 700), (1185, 0,15, 700), (80, 530, 300, 15), (900, 500, 250, 15), (230, 200,  190, 15),
        (15, 160, 30, 15), (470, 380, 280, 15), (990, 140, 130, 15), (580, 130, 90, 15), (825, 230, 60, 15), (1155, 310, 30, 15)}
cn_x, cn_y = rand_pos()
if (cn_x == 0):
    cn_x, cn_y = rand_pos()
    if (cn_x == 0):
        cn_x, cn_y = rand_pos()
        if (cn_x == 0):
            cn_x, cn_y = rand_pos()
            if (cn_x == 0):
                cn_x, cn_y = rand_pos()
                if (cn_x == 0):
                    cn_x, cn_y = rand_pos()
obj_height = 56
obj_width = 63
kadr = 0
look_right = True
FPS = 200 * 1.5
kW = False
kA = False
kD = False
that_Vy = 0
x, y = 500, 400
Vx = 0
Vy = 0
while running:
    for ev in pygame.event.get():
        if (ev.type == pygame.QUIT): 
            sys.exit() 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        kW = True
    else: 
        kW = False
    if keys[pygame.K_a]:
        kA = True
    else: 
        kA = False
    if keys[pygame.K_d]:
        kD = True
    else: 
        kD = False
    screen.fill((209, 185, 185))
    pygame.draw.rect(screen, black, (0, 685, 1200, 15)) 
    pygame.draw.rect(screen, black, (0, 0, 1200, 15))
    pygame.draw.rect(screen, black, (0, 0, 15, 700))
    pygame.draw.rect(screen, black, (1185, 0,15, 700))

    pygame.draw.rect(screen, black, (80, 530, 300, 15))
    pygame.draw.rect(screen, black, (900, 500, 250, 15))
    pygame.draw.rect(screen, black, (230, 200,  190, 15))
    pygame.draw.rect(screen, black, (15, 160, 30, 15))
    pygame.draw.rect(screen, black, (470, 380, 280, 15))
    pygame.draw.rect(screen, black, (990, 140, 130, 15))
    pygame.draw.rect(screen, black, (580, 130, 90, 15))
    pygame.draw.rect(screen, black, (825, 230, 60, 15))
    pygame.draw.rect(screen, black, (1155, 310, 30, 15))

    
    Ax = 0
    kX = 0.25 / 1.5
    kY = 0.4 / 1.5
    if kD == True: 
        Ax = Ax + 0.3 * kX
    if kA == True: 
        Ax = Ax - 0.3 * kX
    Vx += Ax
    if Vx >= 0:
        Vx = min(8 * kX, Vx) 
    else:
        Vx = max(-8 * kX, Vx)
    
    if ((kA == False and kD == False) or (kA == True and kD == True)) :
        if Vx >= 0: 
            Vx = max(0, Vx - 0.3 * kX)
        else:
            Vx = min(0, Vx + 0.3 * kX)
    Vy -= 0.5 * kY * kY
    posX, posY = x + 18, y + 14
    left_side = posX
    right_side = posX + obj_width
    bottom_side = posY + obj_height
    top_side = posY 

    
    for block in arr: 
        if (right_side >= block[0] and left_side <= block[0] + block[2]):
            razY = 6
            if (block[1] - razY <= bottom_side <= block[1]):
                Vy = 0
            elif (block[1] + block[3] <= top_side <= block[1] + block[3] + razY):
                if (Vy > 0): 
                    Vy=0
        if (bottom_side >= block[1] and top_side <= block[1] + block[3]):
            razX = 2
            if (block[0] - razX <= right_side <= block[0]):
                if Vx > 0:
                    Vx = 0
            elif ( block[0] + block[2] <= left_side <= block[0] + block[2] + razX):
                if Vx < 0:
                    Vx = 0
    if kW == True:
        if Vy == 0 and that_Vy == 0: 
            Vy += 14 * kY

    y -= Vy
    x += Vx
    
    if (kA == True and kD == False and look_right == True) : 
        image = pygame.transform.flip(image, True, False)
        look_right = False
    if (kA == False and kD == True and look_right == False) :
        image = pygame.transform.flip(image, True, False)
        look_right = True
    if posX <= cn_x  + 60 and cn_x <= posX + obj_width and posY <= cn_y  + 60 and cn_y <= posY + obj_height:
        coins += 1
        text_surface = font.render(str(coins), True, (124, 116, 136))
        if (coins >= 100):
            font = pygame.font.Font(None, 90)
            text_surface = font.render(str(coins) + ", wow, go to 1000?", True, (124, 116, 136))
        if (coins >= 1000):
            font = pygame.font.Font(None, 80)
            text_surface = font.render(str(coins) + ", omg:)", True, (124, 116, 136))
        cn_x, cn_y = rand_pos()
        if (cn_x == 0):
            cn_x, cn_y = rand_pos()
            if (cn_x == 0):
                cn_x, cn_y = rand_pos()
                if (cn_x == 0):
                    cn_x, cn_y = rand_pos()
                    if (cn_x == 0):
                        cn_x, cn_y = rand_pos()
                        if (cn_x == 0):
                            cn_x, cn_y = rand_pos()
    clock.tick(FPS)
    kadr += 1
    screen.blit(text_surface, (1200 // 2 - text_surface.get_width() // 2, 700 // 2 - text_surface.get_height() // 2))
    screen.blit(image, (x, y))
    screen.blit(coin_img, (cn_x, cn_y))
    if (kadr % 10 == 0) :
        that_Vy = Vy
    pygame.display.update()
