import pygame, sys
from Graphicsdisplay import *
import math
from pygame.locals import *
mapheight,mapwidth = 32*int(input("howmany tiles tall? ")),32*int(input("How many tiles wide? ")) #gets picel width
window = pygame.display.set_mode((800,500))                                     #sets window
pygame.display.set_caption("Map Editor")
clock = pygame.time.Clock()
camerax = 0                                                                     #clock variable
cameray = 0
selector = pygame.Surface((tilesize,tilesize))                                  #creation of selector 
selector.fill((255,255,0))                                                      #and selector variables
selector.set_alpha(150)
selectory,selectorx = 0, 0
tiletype = "1"                                                                  #brush variable
newmapdata = []                                                                 #list of tiles that will be saved                                            
maxheight = 0                                                                   #map  dimension variables
maxwidth = 0
def finddimensions():                                                           #finds the dimensions of the map
    global maxheight, maxwidth
    for tile in newmapdata:
        if tile[0] > maxwidth:
            maxwidth = tile[0]
        if tile[1] > maxheight:
            maxheight = tile[1]
def exportmap(name):                                                            #exports tiletype to a file
   global newmapdata, maxheight, maxwidth
   finddimensions()
   stringofmap = str(int(maxwidth/32)+1) + "," + str(int(maxheight/32)+1) + "|\n"   #writes dimensions to string
   for tile in newmapdata:
       stringofmap += (str(int((tile[0]/32))) + "," + str(int((tile[1]/32))) + "," + str(tile[2]) + "|\n")  #creates string of tiles
   newmap = open("maps//" + str(name) + ".txt","w")                                 
   newmap.write(stringofmap)                                                    #writes string to file
   newmap.close()
   

for x in range(0,mapheight,tilesize):
    for y in range(0,mapwidth,tilesize):                                        #creates default grassy plain
        newmapdata.append([x,y,"1"])
while True:                                                                     #main loop
    window.fill((0,0,0))
    for event in pygame.event.get():                                            #leaving the system
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    key = pygame.key.get_pressed()
    if key[K_w]:                                                                #camera movement
            cameray -=tilesize
    elif key[K_s]:
            cameray +=tilesize
    elif key[K_a]:
            camerax-=tilesize
    elif key[K_d]:
            camerax+=tilesize
    elif key[K_UP]:                                                             #selector movement
            selectory -= tilesize
    elif key[K_DOWN]:
            selectory += tilesize
    elif key[K_LEFT]:
            selectorx-=tilesize
    elif key[K_RIGHT]:
            selectorx+=tilesize
    elif key[K_1]:                                                              #brush selection
        tiletype = "1"
    elif key[K_2]:
        tiletype = "2"
    elif key[K_3]: 
        tiletype = "3"
    elif key[K_SPACE]:                                                          #drawing with the brush
        for tile in newmapdata:
            if selectorx == tile[0] and selectory == tile[1]:                   #drawing over a tile
                newmapdata.remove(tile) 
        newmapdata.append([selectorx,selectory,tiletype])                       #drawing a new tile
    elif key[pygame.K_RETURN]:                                                  #saves the map
        mapname = input("name of map? ")
        exportmap(mapname)
        

    
    for tile in newmapdata:                                                     #renders map
        window.blit(tiletags[tile[2]], (tile[0] + camerax, tile[1] + cameray))
        
    window.blit(selector,(selectorx+camerax,selectory+cameray))                 #renders selector
    pygame.display.update()
    
    clock.tick(10)                                                              #FPS set to 10
