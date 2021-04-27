import time
state = [
			['W', 'W', 'W', 'W', 'W', 'X', 'X', 'X', 'X'],
			['W', 'W', 'W', 'W', 'W', 'W', 'X', 'X', 'X'],
			['E', 'E', 'W', 'W', 'W', 'E', 'E', 'X', 'X'],
			['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'X'],
			['E', 'E', 'E', 'E', 'W', 'E', 'E', 'E', 'E'],
			['X', 'E', 'E', 'E', 'W', 'E', 'E', 'E', 'E'],
			['X', 'X', 'E', 'E', 'B', 'B', 'B', 'E', 'E'],
			['X', 'X', 'X', 'B', 'B', 'B', 'B', 'B', 'B'],
			['X', 'X', 'X', 'X', 'B', 'B', 'B', 'B', 'B']
		]
state1 = [
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


def good_moves(board,player):
    if player == 'B':
        adversary = 'W'
    else:
        adversary = 'B'
    symbols = ['B', 'W']
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
    treatedgroups =[]
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
                        while board[indice_x+len(group)*dx][indice_y+len(group)*dy] == player and len(group)<3:
                            group.add((indice_x+len(group)*dx,indice_y+len(group)*dy))
                    except IndexError:
                        pass
                    if len(group) == 1:
                        try:
                            if board[indice_x+dx][indice_y+dy] == 'E':
                                group.add(direction)
                                if group not in result:
                                    result.append(group)
                                continue
                            else:
                                continue
                        except IndexError:
                            continue
                    if group in treatedgroups:
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
                            elif (x-value*dx,y-value*dy) in group:
                                directioncoord = coords
                        return directioncoord
                    xmax, ymax = grouphead(1)
                    xmin, ymin = grouphead(-1)

                    def validate(direction=direction):
                        treatedgroups.append(group.copy())
                        groupX = group.copy()
                        groupX.add(direction)
                        if groupX not in result:
                            result.append(groupX)
                    #eliminer les series de plus de 3 pions et les series qui se suicideraient
                    try:
                        if board[xmax+dx][ymax+dy] in ['X',player]:
                            continue
                        if board[xmax+dx][ymax+dy] == 'E':
                            validate()
                            continue
                        else:
                            try:
                                if board[xmax+2*dx][ymax+2*dy] == 'E':
                                    validate()
                                    continue
                                elif board[xmax+3*dx][ymax+3*dy] == 'E' and board[xmax+2*dx][ymax+2*dy] != player and len(group) == 3:
                                    validate()
                                    continue
                            except IndexError:
                                continue 
                    except IndexError:
                        continue
                    try:
                        if board[xmin-dx][ymin-dy] in ['X',player]:
                            continue
                        if board[xmin-dx][ymin-dy] == 'E':
                            validate(opposite[direction])
                            continue
                        else:
                            try:
                                if board[xmin-2*dx][ymin-2*dy] == 'E':
                                    validate(opposite[direction])
                                    continue
                                elif board[xmin-3*dx][ymin-3*dy] == 'E' and board[xmin-2*dx][ymin-2*dy] != player and len(group) == 3:
                                    validate(opposite[direction])
                                    continue
                            except IndexError:
                                continue 
                    except IndexError:
                        continue
            indice_y+=1
        indice_x+=1
    return result
