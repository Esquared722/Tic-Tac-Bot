class Board:
    ''' Traditional Tic-Tac-Toe Board '''

    def __init__(self):
        self.board = [[' ' for x in range(3)] for y in range(3)]
    
    def __str__(self):
        boardStr = '\n'
        row = "  ---|---|---\n"

        for i in range(3):
            boardStr += "{} ".format(i)
            for j in range(3):
                boardStr += " " + self.board[i][j] + " |" if j < 2 else " {} \n".format(self.board[i][j])
            boardStr += row if i < 2 else "\n   0   1   2\n"
        
        return boardStr
    
    def __len__(self):
        counter = 0

        for i in range(3):
            for j in range(3):
                if self.board[i][j] != ' ':
                    counter += 1
        
        return counter
    
    def placePiece(self, piece, posX, posY):
        ''' Places piece object in given position on the board, simulating a move'''
        self.board[posY][posX] = str(piece)
    
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
                if self.board[i][j] == str(piece):
                    pieceCount += 1
                else:
                    break
            if pieceCount == 3:
                return True
            pieceCount = 0
        
        return False
    
    def checkCols(self, piece):
        pieceCount = 0
        for i in range(3):
            for j in range(3):
                if self.board[j][i] == str(piece): 
                    pieceCount += 1
                else:
                    break
            if pieceCount == 3:
                return True
            pieceCount = 0
        
        return False
    
    # Try to optimize, by reducing multiple checks
    def checkDiags(self, piece):
        pieceCount = 0

        if self.board[1][1] != str(piece):
            return False

        if self.board[0][0] == str(piece) and self.board[2][2] == str(piece):
            return True
        
        if self.board[2][0] == str(piece) and  self.board[0][2] == str(piece):
            return True
        
        return False
