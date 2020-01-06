#łączenie z podanym serwerem
#czekanie na status
#jak status że gramy to gramy

#!/usr/bin/env python3
import socket
import _thread
from lib import *


IP = '127.0.0.1'
PORT = 6969

class ClientGame(Game):
    def __init__(self, sock):
        super().__init__()
        self.servsock = sock

    def printBoard(self):
        print("""\n[you're O]\n{} | {} | {} | {}\n--+---+---+--\n{} | {} | {} | {} \n--+---+---+--\n{} | {} | {} | {}\n--+---+---+--\n{} | {} | {} | {}\n
              """.format(*[FIELDS[i] for i in self.board]))

    def getCoords(self):
        coords = -1
        while(coords not in range(0, 16)):
            try:
                coords = int(input("choose field (0-16):"))
            except:
                coords = -1
        return coords

    def sendCoords(self):
        coords = self.getCoords()
        self.servsock.send(coords.to_bytes(1, byteorder='big', signed=True))
        self.setField(2, coords)
        self.printBoard()

    def winAction(self):
        print("***YOU WON!***")
        self.active = False

    def looseAction(self):
        print("***YOU LOST!***")
        self.active = False

    def drawAction(self):
        print("***DRAW!***")
        self.active = False

    def printError(self):
        print("Error")

if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))
    game = ClientGame(s)

    RCVSTATUS = {
        -1: game.winAction,
        -2: game.looseAction,
        -3: game.drawAction,
        -4: game.printError,
        -5: game.sendCoords
    }

    game.printBoard()
    while game.active:
        action = int.from_bytes(s.recv(1), byteorder='big', signed=True) #get action from server
        if action in range(0, 16): #opponent move
            game.setField(1, action)
            game.printBoard()
        elif action in range(-5, 0): #
            RCVSTATUS[action]()
