import socket
import json
import sys
from threading import Thread

#Donner l'option d'entrée un nom de port lors de l'éxecution du script
try:
    port = int(sys.argv [1])
except:
    port = 4000
try:
    pseudo = sys.argv [2]
except:
        pseudo = 'PLayer 1'


def receiveJSON(socket):
    fullreceive = False
    message = ''
    while not fullreceive:
        message += socket.recv(512).decode('utf8')
        try:
            data = json.loads(message)
            fullreceive = True
        except json.JSONDecodeError:
            pass
    return data

def sendJSON(socket, data):
    data = json.dumps(data).encode('utf8')
    totalsend = 0
    while totalsend < len(data):
        sent = socket.send(data[totalsend:])
        totalsend += sent

message = {"request": "subscribe","port": port,"name": pseudo,"matricules": ["195022", "02305"]}

s = socket.socket()
s.connect(('localhost',3000))
sendJSON(s, message)
s.close()
#boucle de réception de requêtes
while True: 
    s = socket.socket()
    s.bind(('0.0.0.0', port))
    s.listen()
    client, address = s.accept()
    serverrequest = receiveJSON(client)
    print(serverrequest)
    if serverrequest['request'] == 'ping':
        sendJSON(client, {'response': 'pong'})
    if serverrequest['request'] == 'play':
        # 'current': 0 -> black, 'current': 1 -> white
        if serverrequest['state']['current'] == 0:
            move = {"marbles": [[6, 4], [6, 5]],"direction": "W"}
            moverequest = {"response": "move","move": move,"message": "Fun message black"}
        if serverrequest['state']['current'] == 1:
            move = {"marbles": [[2, 2], [2, 3], [2, 4]],"direction": "W"}
            moverequest = {"response": "move","move": move,"message": "Fun message white"}
        
        sendJSON(client, moverequest)

# 'board': [
# 			['W', 'W', 'W', 'W', 'W', 'X', 'X', 'X', 'X'],
# 			['W', 'W', 'W', 'W', 'W', 'W', 'X', 'X', 'X'],
# 			['E', 'E', 'W', 'W', 'W', 'E', 'E', 'X', 'X'],
# 			['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'X'],
# 			['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
# 			['X', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
# 			['X', 'X', 'E', 'E', 'B', 'B', 'B', 'E', 'E'],
# 			['X', 'X', 'X', 'B', 'B', 'B', 'B', 'B', 'B'],
# 			['X', 'X', 'X', 'X', 'B', 'B', 'B', 'B', 'B']
# 		]




