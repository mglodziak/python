

class sudoku():
    def create(self, bottom):
        self.board=[]
        if not bottom:
            self.board = [[sudoku() for x in range(3)] for y in range(3)]
            for x in self.board:
                    for y in x:
                        y.create(True)
        else:
            self.board = [[None for x in range(3)] for y in range(3)]


    def get_element(self, x, y):
        print(self.board[x][y].board)

#getter & setter

            #isinstance sudoku

a=sudoku()
a.create(False)
print(a.board[0][0].board[0][1])
