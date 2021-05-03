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
                                    result.append([(indice_x+dx,indice_y+dy),group])
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
                    def validate(argument="None"):
                        groupX = group.copy()
                        groupX.add(direction)
                        answer = [argument, groupX]
                        if groupX not in result:
                            result.append(answer)
                    #eliminer les series de plus de 3 pions et les series qui se suicideraient
                    try:
                        if -1  in (xmax+dx,ymax+dy): #suicide
                            continue
                        if board[xmax+dx][ymax+dy] == 'E': #simple move
                            validate((xmax+dx,ymax+dy))
                            continue
                    except IndexError: #suicide
                        continue
                    if board[xmax+dx][ymax+dy] in ['X',player]: #suicide or serie of 4
                        continue
                    #board[xmax+dx][ymax+dy] = adversary
                    try:
                        if -1  in (xmax+2*dx,ymax+2*dy):
                            validate("kill")
                            continue
                        if board[xmax+2*dx][ymax+2*dy] == "X":
                            validate("kill")
                            continue
                    except IndexError:
                        validate("kill")
                        continue
                    if board[xmax+2*dx][ymax+2*dy] == "E":
                        validate(["push",(xmax+2*dx,ymax+2*dy)])
                        continue
                    if board[xmax+2*dx][ymax+2*dy] == player: #blocked by ally
                        continue
                    if board[xmax+2*dx][ymax+2*dy] == adversary:
                        if len(group) == 2: #not enough pushpower
                            continue
                        try:
                            if -1  in (xmax+3*dx,ymax+3*dy):
                                validate("kill") 
                                continue
                            if board[xmax+3*dx][ymax+3*dy] in [player,adversary]: #blocked
                                continue
                        except IndexError:
                            validate("kill") 
                            continue
                        if board[xmax+3*dx][ymax+3*dy] == "X":
                            validate("kill")
                            continue
                        if board[xmax+3*dx][ymax+3*dy] == "E":
                            validate(["doublepush",(xmax+3*dx,ymax+3*dy)])
                            continue
            indice_y+=1
        indice_x+=1
    return result

board = [
			['W', 'W', 'W', 'W', 'B', 'X', 'X', 'X', 'X'],
			['W', 'W', 'W', 'W', 'W', 'W', 'X', 'X', 'X'],
			['E', 'E', 'W', 'W', 'W', 'E', 'E', 'X', 'X'],
			['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'X'],
			['E', 'E', 'E', 'E', 'W', 'E', 'E', 'E', 'E'],
			['X', 'E', 'E', 'E', 'W', 'E', 'E', 'E', 'E'],
			['X', 'X', 'E', 'E', 'B', 'B', 'B', 'E', 'E'],
			['X', 'X', 'X', 'B', 'B', 'B', 'B', 'B', 'B'],
			['X', 'X', 'X', 'X', 'B', 'B', 'B', 'B', 'B']
		]