from Graphicsdisplay import *

class Mapgenerator:
    
    def addtile(x, y, tile, tosurface):
        tosurface.blit(tile, (x * tilesize, y * tilesize))
    def load_map(file):                                                     #loads Map from File
        with open(file, "r") as mapfile:
            mapdata = mapfile.read()

            mapdata = mapdata.split("|")

            
            mapdimensions = mapdata[0]                                      # pulls out the map dimesions
            mapdata.remove(mapdimensions)
            mapdimensions = mapdimensions.split(",")
            mapdimensions[0],mapdimensions[1] = int(mapdimensions[0]) * tilesize, int(mapdimensions[1]) * tilesize
            
            tiles =  []                                                     #list of tiles. [x,y,tiletag]
            for tile in range(len(mapdata)):                                #adds tiles from file
                mapdata[tile] = mapdata[tile].strip("\n")
                tiles.append(mapdata[tile].split(","))
            tiles.remove([""])

            terrain = pygame.Surface(mapdimensions)
            for tile in tiles:
                if tile[2] in tiletags:                                     #adds tiles to terrain
                    Mapgenerator.addtile(int(tile[0]),int(tile[1]),tiletags[tile[2]],terrain)
                return terrain




