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
    
    def displayBoard(self):
        print(self)
    
    def clearBoard(self):
        ''' Clears board of all pieces '''
        for i in range(3):
            for j in range(3):
                board[i][j] = ' ';
    
    def getBoard(self):
        return self.board
    
    def checkRows(self, piece):
        pieceCount = 0
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == piece:
                    pieceCount += 1
            if pieceCount == 3:
                return True
            pieceCount = 0
        
        return False
    
    def checkCols(self, piece):
        pieceCount = 0
        for i in range(3):
            for j in range(3):
                if self.board[j][i] == piece:
                    pieceCount += 1
            if pieceCount == 3:
                return True
            pieceCount = 0
        
        return False
    
    def checkDiags(self, piece):
        pieceCount = 0

        if self.board[0][0] == piece and self.board[1][1] == piece and self.board[2][2] == piece:
            return True
        
        if self.board[0][2] == piece and self.board[1][1] == piece and self.board[2][0] == piece:
            return True
        
        return False
