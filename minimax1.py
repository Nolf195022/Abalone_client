gamestate = [
			['W', 'W', 'W', 'W', 'W', 'X', 'X', 'X', 'X'],
			['W', 'W', 'W', 'W', 'W', 'W', 'X', 'X', 'X'],
			['E', 'E', 'W', 'W', 'W', 'E', 'E', 'X', 'X'],
			['E', 'E', 'E', 'E', 'W', 'E', 'E', 'E', 'X'],
			['E', 'E', 'E', 'E', 'W', 'E', 'E', 'E', 'E'],
			['X', 'E', 'E', 'E', 'W', 'E', 'E', 'E', 'E'],
			['X', 'X', 'E', 'E', 'B', 'B', 'B', 'E', 'E'],
			['X', 'X', 'X', 'B', 'B', 'B', 'B', 'B', 'B'],
			['X', 'X', 'X', 'X', 'E', 'B', 'B', 'B', 'B']
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
def statedisplay(board):
    for i in board:
        print(i)
def makemove(state, move, player):
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
    state[xmin][ymin] = "E"
    if state[xmax+dx][ymax+dy] == "E":
        state[xmax+dx][ymax+dy] = player
        statedisplay(state)
        return state
    coord = (xmax+dx,ymax+dy)
    adversarygroup = [coord]
    if state[coord[0]+dx][coord[1]+dy] == adversary and -1 not in (coord[0]+dx,coord[1]+dy):
            adversarygroup.append((coord[0]+dx,coord[1]+dy))
            state[adversarygroup[0][0]][adversarygroup[0][1]] = player
            statedisplay(state)
            return state
    state[coord[0]][coord[1]] = player
    state[coord[0]+dx][coord[1]+dy] = adversary
    statedisplay(state)
    return state
    

def winner(state):
    pass

movey = {(2, 3), (2, 4), 'W', (2, 2)} #whitemove
movey2 = {(4, 4), (5, 4), (3, 4), 'SW'}
makemove(gamestate, movey2, "W")