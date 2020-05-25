class Board:
    ''' Traditional Tic-Tac-Toe Board '''

    def __init__(self):
        self.pieces = []
    
    def __str__(self):
        row = '-----------'

        for i in range(3):
            for j in range(3):
                print(self.pieces[i][j], end = '|')
            print(row)
    
    
    def placePiece(self, piece, pos):
        ''' Places piece object in given position on the board, simulating a move'''
        # TODO
        return;
    
    def clearBoard(self):
        # TODO
        return;

