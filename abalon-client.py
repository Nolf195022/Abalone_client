import socket
import json
import sys
import random
import time
from goodmovesonly import good_moves
from betterai import bestmove

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

def subscribe(port,name):
    port = int(port)
    message = {"request": "subscribe","port": port,"name": name,"matricules": ["19022", "18164"]}
    s = socket.socket()
    s.connect(('localhost',3000))
    sendJSON(s, message)
    s.close()
    #boucle de réception de requêtes
    listening = True
    while listening == True:
        s = socket.socket()
        s.bind(('0.0.0.0', port))
        s.listen()
        client, address = s.accept()
        serverrequest = receiveJSON(client)
        if serverrequest['request'] == 'ping':
            sendJSON(client, {'response': 'pong'})
            listening = False

def SENDmove(server_request):
    # 'current': 0 -> black, 'current': 1 -> white
    playercolors = ['B','W']
    playerindice = server_request['state']['current']
    move = bestmove(server_request['state']['board'],playercolors[playerindice])
    print(move)
    marbles = []
    for i in move[1]:
        if type(i) is tuple:
            marbles.append(list(i))
        else:
            direction = i
    moverequest = {"marbles": marbles,"direction": direction}
    return {"response": "move","move": moverequest}

defaultport = '5996'
defaultname = 'Better AI'
if len(sys.argv) == 2:
    try:
        isinteger = int(sys.argv[1])
        port = sys.argv[1]
        name = defaultname
    except ValueError:
        port = defaultport
        name = sys.argv[1]
elif len(sys.argv) == 3:
    port = sys.argv[1]
    name = sys.argv[2]
elif len(sys.argv) > 3:
    print('Invalid input')
    sys.exit()
else:
    port = defaultport
    name = defaultname
subscribe(port, name)
listening = True
while listening == True:
        s = socket.socket()
        s.bind(('0.0.0.0', int(port)))
        s.listen()
        client, address = s.accept()
        serverrequest = receiveJSON(client)
        print(serverrequest['request'])
        if serverrequest['request'] == 'ping':
            sendJSON(client, {'response': 'pong'})
        if serverrequest['request'] == 'play':
            start = time.time()
            sendJSON(client, SENDmove(serverrequest))
            print('Temps de réponse : {} s'.format(time.time()-start))
