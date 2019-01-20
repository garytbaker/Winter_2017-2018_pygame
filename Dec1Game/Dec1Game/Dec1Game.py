import pygame,sys,time
from pygame.locals import *
from Graphicsdisplay import *
from Globalvari import *
from mapgenerator import *
pygame.init()
Verdana = pygame.font.Font("C://Windows//Fonts//Verdana.ttf",20)   
                                                                                #Window Variables
windowheight = 500
windowwidth = 800
windowtitle = "game"
window = pygame.display.set_mode((windowwidth,windowheight))
pygame.display.set_caption(windowtitle)
                                                                                #Loadmaps
terrain = Mapgenerator.load_map("maps//big.txt")
                                                                                #FPS Counter
FPS = 0
currentsecond = 0
currentframe = 0
deltatime = 1
def countFPS():
    global currentsecond,currentframe,FPS,deltatime
    if currentsecond == time.strftime("%S"):
        currentframe+=1
    else:
        FPS = currentframe
        currentframe = 0
        currentsecond = time.strftime("%S")
        if FPS != 0:
             deltatime = 1/FPS
                                                                                #FPS Display
def displayFPS():
    global FPS
    FPStext = Verdana.render(str(int(FPS)),True,(255,255,255))
    window.blit(FPStext,(10,10))
                                                                                #Main Loop
while True:                             
                                                                                #Screen Fill
    window.fill((0,0,0))
    
        
                                                                                #Events and Effects
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    key = pygame.key.get_pressed()
    if deltatime < (1/25):
        if key[K_w]:
            camera_y -=camera_movespeed*deltatime
        elif key[K_s]:
            camera_y +=camera_movespeed*deltatime
        elif key[K_a]:
            camera_x-=camera_movespeed*deltatime
        elif key[K_d]:
            camera_x+=camera_movespeed*deltatime
                                                                               #Create Terrain
    window.blit(terrain,(camera_x,camera_y))
    


    displayFPS()
    pygame.display.update()
    countFPS()