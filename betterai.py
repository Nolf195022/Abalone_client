from goodmovesonly import good_moves
import copy
import random
gamestate = [
            ["W", "W", "W", "W", "W", "X", "X", "X", "X"],
            ["W", "W", "W", "W", "W", "W", "X", "X", "X"],
            ["E", "E", "W", "W", "W", "E", "E", "X", "X"],
            ["E", "E", "E", "B", "E", "E", "E", "E", "X"],
            ["E", "E", "E", "B", "E", "E", "E", "E", "E"],
            ["X", "E", "E", "E", "E", "E", "E", "E", "E"],
            ["X", "X", "E", "E", "B", "B", "B", "E", "E"],
            ["X", "X", "X", "B", "B", "B", "B", "B", "B"],
            ["X", "X", "X", "X", "B", "B", "B", "B", "B"]
		]
directions = {
        'NE': (-1,  0),
        'SW': ( 1,  0),
        'NW': (-1, -1),
        'SE': ( 1,  1),
        'E': ( 0,  1),
        'W': ( 0, -1)
    }
opposite = {
        'NE': 'SW',
        'SW': 'NE',
        'NW': 'SE',
        'SE': 'NW',
        'E': 'W',
        'W': 'E'
    }
def stateXdisplay(board):
    for i in board:
        print(i)
def makemove(state, move, player):
    print(move)
    stateX = copy.deepcopy(state)
    if player == 'B':
        adversary = 'W'
    else:
        adversary = 'B'
    marbles = []
    for item in move:
        if type(item) is tuple:
            marbles.append(list(item))
        else:
            direction = item
    dx, dy = directions[direction]
    def grouphead(value):
        directioncoord = None
        initiatecord = True
        for coords in marbles:
            x, y = coords
            if initiatecord == True:
                directioncoord = coords
                initiatecord = False
            else:
                xmax, ymax = directioncoord
                if (xmax+value*dx,ymax+value*dy) in move and ((xmax+value*dx,ymax+value*dy) == (x,y) or (xmax+value*2*dx,ymax+value*2*dy) == (x,y)):
                    directioncoord = coords
        return directioncoord
    xmax, ymax = grouphead(1)
    xmin, ymin = grouphead(-1)
    stateX[xmin][ymin] = "E"
    if stateX[xmax+dx][ymax+dy] == "E":
        stateX[xmax+dx][ymax+dy] = player
        stateXdisplay(stateX)
        return stateX
    stateX[xmax+dx][ymax+dy] = player
    try:
        if stateX[xmax+2*dx][ymax+2*dy] == adversary and -1 not in (xmax+2*dx,ymax+2*dy):
            try:
                if -1 not in (xmax+3*dx,ymax+3*dy) and stateX[xmax+3*dx][ymax+3*dy] != "X":
                    stateX[xmax+3*dx][ymax+3*dy] = adversary
                stateXdisplay(stateX)
                return stateX
            except IndexError:
                stateXdisplay(stateX)
                return stateX
        else:
            try:
                if -1 not in (xmax+2*dx,ymax+2*dy) and stateX[xmax+2*dx][ymax+2*dy] != "X":
                    stateX[xmax+2*dx][ymax+2*dy] = adversary
                stateXdisplay(stateX)
                return stateX
            except IndexError:
                stateXdisplay(stateX)
                return stateX
    except IndexError:
        stateXdisplay(stateX)
        return stateX

def winner(state):
    pass

