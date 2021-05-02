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
            direction = i
    last_marble = ()
    for marble in marbles:
        pass
    

def winner(state):
    pass

