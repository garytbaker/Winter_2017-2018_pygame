import pygame
import random
tilesize = 32

class Tiles:                                                                #what a tile is.
    def __init__(self,size):
        self.size=size

    def loadtile(self,file):                                                #loads a tile from a graphic
        bitmap = pygame.image.load(file)
        bitmap = pygame.transform.scale(bitmap,(self.size,self.size))
        return bitmap
T_grass1 = Tiles(tilesize).loadtile("Graphics\\Grassforgame1.png")          #loads the tiles
T_grass2 = Tiles(tilesize).loadtile("Graphics\\Grass2forgame1.png")
T_grass3 = Tiles(tilesize).loadtile("Graphics\\Grass3forgame1.png")
T_Water = Tiles(tilesize).loadtile("Graphics\\Waterforgame1.png")
T_Stone = Tiles(tilesize).loadtile("Graphics\\Stoneforgame1.png")
grasstile = None
def Grass():
    global T_grass1,T_grass2,T_grass3, grasstile                            #picks a random grass tile
    x = random.randint(0,2)
    if x == 0:
        grasstile = T_grass1
    elif x == 1:
        grasstile = T_grass2
    else: 
        grasstile = T_grass3
    return grasstile


tiletags = {"1": Grass(), "2": T_Water, "3": T_Stone}

    

