

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
        return (self.board[int(x/3)][int(y/3)].board[x%3][y%3])
    
    def set_element(self,x,y,w):
        self.board[int(x/3)][int(y/3)].board[x%3][y%3]=w

#getter & setter

            #isinstance sudoku

a=sudoku()
a.create(False)
a.set_element(1,2,9)
x=a.get_element(1,2)

print(x)
#print(a.board[0][0].board[0][1])
