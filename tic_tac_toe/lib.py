import random
import math

STATUS = {
    "get": -5,
    "won": -1,
    "lost": -2,
    "draw": -3,
    "error": -4
}

FIELDS = {
    0: ' ',
    1: 'X',
    2: 'O'
}

class Game:
    def __init__(self):
        self.board = [0, 0, 0, 0, #0 - empty field
                      0, 0, 0, 0, #1 - X
                      0, 0, 0, 0,
                      0, 0, 0, 0] #2 - O
        self.whoseturn = random.getrandbits(1) #0 - player X first / 1 -  first
        self.active = True

    def checkIfMoveWinning(self, coord: int):
        #vertical 
        r = coord % 4
        if (self.board[r] == self.board[r+4] == self.board[r+8] == self.board[r+12] != 0):
            return True
        #horizontal
        r = math.floor(coord/4)
        if (self.board[r*4] == self.board[r*4+1] == self.board[r*4+2] == self.board[r*4+3] != 0):
            return True
        #diagonal
        if (self.board[0] == self.board[5] == self.board[10] == self.board[15] != 0) or (self.board[3] == self.board[6] == self.board[9] == self.board[12] != 0):
            return True
        return False

    def checkIfDraw(self):
        if 0 in self.board:
            return False
        self.active = False
        return True

    def setField(self, XY: int, coord: int):
        if self.board[coord] == 0:
            self.board[coord] = XY
        else:
            print ("Field occupied. Try once more.")
            return -10
