#czekanie na peirwszzego
#łączenie z peirwszym
#info że czekanie na drugiego
#łąćzenie
#idziemy do rozgrywki

#połączenia współbieżne i osobne wątki na 

#rozgrywka: przekazywanie info o kolejnych ruchach między playerami
    #weryfikacja kto wygrywa


#!/usr/bin/env python3

import socket
import argparse
import _thread
from lib import *

IP = '127.0.0.1'

PORT = 6969

def servGameThread(firstPlayerSock, SecondPlayerSock):
    game = Game()

    if game.whoseturn:
        players = [firstPlayerSock, SecondPlayerSock]
    else:
        players = [SecondPlayerSock, firstPlayerSock]

    firstPlayerTurn = game.whoseturn
    while(game.active):
        players[int(firstPlayerTurn)].send(STATUS['get'].to_bytes(1, byteorder='big', signed=True))
        coords = int.from_bytes(players[int(firstPlayerTurn)].recv(1), byteorder='big', signed=True)
        tmp=game.setField(int(firstPlayerTurn)+1, coords)
        #print(tmp)
        while tmp==-10:
            players[int(firstPlayerTurn)].send(STATUS['get'].to_bytes(1, byteorder='big', signed=True))
            coords = int.from_bytes(players[int(firstPlayerTurn)].recv(1), byteorder='big', signed=True)
            tmp=game.setField(int(firstPlayerTurn)+1, coords)

        players[int(not firstPlayerTurn)].send(coords.to_bytes(1, byteorder='big', signed=True))
        if game.checkIfDraw():
            players[int(firstPlayerTurn)].send(STATUS['draw'].to_bytes(1, byteorder='big', signed=True))
            players[int(not firstPlayerTurn)].send(STATUS['draw'].to_bytes(1, byteorder='big', signed=True))
        elif game.checkIfMoveWinning(coords):
            players[int(firstPlayerTurn)].send(STATUS['won'].to_bytes(1, byteorder='big', signed=True))
            players[int(not firstPlayerTurn)].send(STATUS['lost'].to_bytes(1, byteorder='big', signed=True))
        firstPlayerTurn = not firstPlayerTurn


if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((IP, PORT)) 
    s.listen(True)

    while True:
        connX, addrX = s.accept()
        print("Player X connected from {}".format(addrX[0]))
        connO, addrO = s.accept()
        print("Player O connected from {}".format(addrO[0]))
        _thread.start_new_thread(servGameThread, (connX, connO,))
