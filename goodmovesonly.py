import time
def good_moves(board,player):
    if player == 'B':
        adversary = 'W'
    else:
        adversary = 'B'
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
    indice_x = 0
    result = []
    for line in board:
        indice_y = 0
        for column in line:
            coord = (indice_x,indice_y)
            if board[indice_x][indice_y] == player:
                for direction in directions:
                    group = {coord}
                    dx, dy = directions[direction]
                    try:
                        while board[indice_x+len(group)*dx][indice_y+len(group)*dy] == player and len(group)<3 and -1 not in (indice_x+len(group)*dx,indice_y+len(group)*dy):
                            group.add((indice_x+len(group)*dx,indice_y+len(group)*dy))
                    except IndexError:
                        pass
                    if len(group) == 1:
                        try:
                            if board[indice_x+dx][indice_y+dy] == 'E' and -1 not in (indice_x+dx,indice_y+dy):
                                group.add(direction)
                                if group not in result:
                                    result.append(group)
                                continue
                            continue
                        except IndexError:
                            continue
                    #obtenir les tête de ligne en fonction de la direction du mouvement (dans les 2 directions)
                    def grouphead(value):
                        directioncoord = None
                        initiatecord = True
                        for coords in group:
                            x, y = coords
                            if initiatecord == True:
                                directioncoord = coords
                                initiatecord = False
                            else:
                                xmax, ymax = directioncoord
                                if (xmax+value*dx,ymax+value*dy) in group and ((xmax+value*dx,ymax+value*dy) == (x,y) or (xmax+value*2*dx,ymax+value*2*dy) == (x,y)):
                                    directioncoord = coords
                        return directioncoord
                    xmax, ymax = grouphead(1)
                    def validate(direction=direction):
                        groupX = group.copy()
                        groupX.add(direction)
                        if groupX not in result:
                            result.append(groupX)
                    #eliminer les series de plus de 3 pions et les series qui se suicideraient
                    try:
                        if xmax+dx == -1 or ymax+dy == -1:
                            continue
                        if board[xmax+dx][ymax+dy] in ['X',player]:
                            continue
                        if board[xmax+dx][ymax+dy] == 'E':
                            validate()
                            continue
                        try:
                            if -1  in (xmax+2*dx,ymax+2*dy): #kill
                                validate()
                                continue
                            if board[xmax+2*dx][ymax+2*dy] == player and -1 not in (xmax+2*dx,ymax+2*dy):
                                continue
                            if board[xmax+2*dx][ymax+2*dy] == adversary and -1 not in (xmax+2*dx,ymax+2*dy):
                                try:
                                    if board[xmax+3*dx][ymax+3*dy] in [player,adversary] and -1 not in (xmax+3*dx,ymax+3*dy):
                                        continue
                                except IndexError:
                                    if len(group) == 3: #kill
                                        validate() 
                                        continue
                                if len(group) == 3:
                                    validate()
                                    continue
                        except IndexError: #kill
                            validate()
                            continue
                    except IndexError:
                        continue
            indice_y+=1
        indice_x+=1
    return result
state = [
			['W', 'W', 'W', 'W', 'W', 'X', 'X', 'X', 'X'],
			['W', 'W', 'W', 'W', 'W', 'W', 'X', 'X', 'X'],
			['E', 'E', 'W', 'W', 'W', 'E', 'E', 'X', 'X'],
			['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'X'],
			['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
			['X', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
			['X', 'X', 'E', 'E', 'B', 'B', 'B', 'E', 'E'],
			['X', 'X', 'X', 'B', 'B', 'B', 'B', 'B', 'B'],
			['X', 'X', 'X', 'X', 'B', 'B', 'B', 'B', 'B']
		]
print(len(good_moves(state, "W")))
