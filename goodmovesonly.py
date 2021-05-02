import time
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
                    if (0, 3) in group and (1, 3) in group and(2, 3)in group:
                        #print(group,coord)
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
                    xmin, ymin = grouphead(-1)

                    def validate(direction=direction):
                        groupX = group.copy()
                        groupX.add(direction)
                        if groupX not in result:
                            result.append(groupX)
                    #eliminer les series de plus de 3 pions et les series qui se suicideraient
                    try:
                        if xmax+dx == -1 or ymax+dy == -1:
                            #print(0,xmax+dx,"MAX",(xmax, ymax),"MIN",(xmin, ymin),"dxdy", (dx, dy), direction)
                            continue
                        if board[xmax+dx][ymax+dy] in ['X',player]:
                            if (0, 3) in group and (1, 3) in group and(2, 3)in group:
                                pass
                                #print(1,xmax+dx,"MAX",(xmax, ymax),"MIN",(xmin, ymin),"dxdy", (dx, dy), direction)
                            continue
                        if board[xmax+dx][ymax+dy] == 'E':
                            if (0, 3) in group and (1, 3) in group and(2, 3)in group:
                                pass
                                #print(2,"MAX",(xmax, ymax),"MIN",(xmin, ymin),"dxdy", (dx, dy), direction)
                            validate()
                            continue
                        else:
                            try:
                                if board[xmax+2*dx][ymax+2*dy] == 'E':
                                    if (0, 3) in group and (1, 3) in group and(2, 3)in group:
                                        #print(3)
                                        pass
                                    validate()
                                    continue
                                elif board[xmax+3*dx][ymax+3*dy] == 'E' and board[xmax+2*dx][ymax+2*dy] != player and len(group) == 3:
                                    if (0, 3) in group and (1, 3) in group and(2, 3)in group:
                                        #print(4)
                                        pass
                                    validate()
                                    continue
                            except IndexError:
                                if (0, 3) in group and (1, 3) in group and(2, 3)in group:
                                    #print(5)
                                    pass
                                continue 
                    except IndexError:
                        if (0, 3) in group and (1, 3) in group and(2, 3)in group:
                            #print(6)
                            pass
                        continue
                    try:
                        if xmin-dx == -1 or ymax-dy == -1:
                            continue
                        if board[xmin-dx][ymin-dy] in ['X',player]:
                            if (0, 3) in group and (1, 3) in group and(2, 3)in group:
                                #print(7)
                                pass
                            continue
                        if board[xmin-dx][ymin-dy] == 'E':
                            if (0, 3) in group and (1, 3) in group and(2, 3)in group:
                                #print(8)
                                pass
                            validate(opposite[direction])
                            continue
                        else:
                            try:
                                if board[xmin-2*dx][ymin-2*dy] == 'E':
                                    if (0, 3) in group and (1, 3) in group and(2, 3)in group:
                                        #print(9)
                                        pass
                                    validate(opposite[direction])
                                    continue
                                elif board[xmin-3*dx][ymin-3*dy] == 'E' and board[xmin-2*dx][ymin-2*dy] != player and len(group) == 3:
                                    if (0, 3) in group and (1, 3) in group and(2, 3)in group:
                                        #print(10)
                                        pass
                                    validate(opposite[direction])
                                    continue
                            except IndexError:
                                if (0, 3) in group and (1, 3) in group and(2, 3)in group:
                                    #print(11)
                                    pass
                                continue 
                    except IndexError:
                        if (0, 3) in group and (1, 3) in group and(2, 3)in group:
                            #print(12)
                            pass
                        continue
            indice_y+=1
        indice_x+=1
    return result
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

counter = 0
xcounter = 0
for i in good_moves(state, 'W'):
    if len(i) == 4:
        xcounter+=1
        print(xcounter)
        print(i)
    