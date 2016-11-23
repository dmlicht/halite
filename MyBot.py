from hlt import *
from networking import *
import logging

logger = logging.getLogger('botlogger')
myID, gameMap = getInit()
sendInit("MyPythonBot")


def choose_move(location):
    site = gameMap.getSite(location)
    # wait to build up some strength
    if site.strength < 10:
        return Move(location, STILL)

    neigh = neighbors(location)
    enemies = are_enemies(neigh)

    # Our space is on the border. Attack the weakest enemy.
    if len(enemies) > 0:
        weakest_direction, _ = weakest(enemies)
        return Move(location, weakest_direction)

    # Move inner
    else:
        return Move(location, random.choice([NORTH, EAST]))


def neighbors(location):
    """Return all locations touching a given location"""
    return {direction: gameMap.getSite(location, direction) for direction in DIRECTIONS[1:]}


def are_enemies(direction_sites):
    """Filter for sites that are controlled by enemies"""
    return {direction: site for (direction, site) in direction_sites.items() if site.owner != myID}


def weakest(direction_sites):
    """Return the weakest enemy"""
    weakest_strength = 999
    weakest_direction = None
    weakest_site = None
    for direction, site in direction_sites.items():
        if site.strength < weakest_strength:
            weakest_strength = site.strength
            weakest_direction = direction
            weakest_site = site
    return weakest_direction, weakest_site


while True:
    moves = []
    gameMap = getFrame()
    for y in range(gameMap.height):
        for x in range(gameMap.width):
            location = Location(x, y)
            site = gameMap.getSite(location)
            if site.owner == myID:
                moves.append(choose_move(location))
    sendFrame(moves)
