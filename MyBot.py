from hlt import *
from networking import *

myID, gameMap = getInit()
sendInit("MyPythonBot")

while True:
    moves = []
    gameMap = getFrame()
    for y in range(gameMap.height):
        for x in range(gameMap.width):
            location = Location(x, y)
            site = gameMap.getSite(location)
            if site.owner == myID:
                moves.append(Move(location, random.choice(DIRECTIONS)))
    sendFrame(moves)
