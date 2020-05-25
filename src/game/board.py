class Board:
    ''' Traditional Tic-Tac-Toe Board '''

    def __init__(self):
        self.board = [[' ' for x in range(3)] for y in range(3)]
    
    def __str__(self):
        boardStr = ''
        row = '\n-----------\n'

        for i in range(3):
            for j in range(3):
                boardStr += self.board[i][j] + '|'
            boardStr += row if i < 2 else ''
        
        return boardStr
    
    
    def placePiece(self, piece, posX, posY):
        ''' Places piece object in given position on the board, simulating a move'''
        self.board[posY][posX] = piece
    
    def clearBoard(self):
        ''' Clears board of all pieces '''
        for i in range(3):
            for j in range(3):
                board[i][j] = ' ';
    
    def getBoard(self):
        return self.board
