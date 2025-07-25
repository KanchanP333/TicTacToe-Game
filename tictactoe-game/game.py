#Part of TicTacToe game 
#game.py

import time
from player import HumanPlayer, RandomComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board = [" " for i in range (9)] #Represents the 3x3 board
        self.currentWinner= None #Keeps track of the winner
    
    def printBoard(self):
        #i=0
        #self.board[0:3] = 0,1,2
        for row in [self.board[i*3:(i+1)*3]for i in range(3)]:
            print('| ' + ' | '.join(row)+' |')
    
    @staticmethod #Does not belong to any instance
    def printBoardNums():
        #j=0
        #self.board[0:3] = 0,1,2

        #Outer j loops runs three times
        #for i in range(j*3, (j+1)*3)] creates a row with 3 numbers
        #str(i) converts the number to string
        numberBoard=[[str(i) for i in range(j*3, (j+1)*3)] for j in range (3)]
        for row in numberBoard:
            print('| ' + ' | '.join(row)+' |') #Printing with the board lines
    
    def availableMoves(self):
        #Should return an array/ board
        return [i for (i,spot) in enumerate(self.board) if spot==' '] #List comprehension

        # moves=[] #Array to store the remaining spaces
        # for (i, spot) in enumerate(self.board):
        #     #['x','x','o'] --> [(0,'x'),(1,'x'),(2,'o')]
        #     if spot==' ':
        #         moves.append(i) #Index of the available position
        # return moves
    
    def emptySquares(self):
        return " " in self.board #Return true or false

    def numEmptySquares(self):
        return self.board.count(" ")

    def makeMove(self, square, letter):
        #If valid move, then makes the move (assigns the square to the letter)
        #Then return true, if invalid, return False
        if self.board[square]==" ":
            self.board[square]=letter
            if self.winner(square,letter):
                self.currentWinner=letter
            return True
        return False

    def winner(self,square,letter):
        #Checking the row
        rowIndex=square//3 #[0,1,2]
        row=self.board[rowIndex*3:(rowIndex+1)*3] #if rowIndex=1 [3:6] = 3,4,5
        if all([spot==letter for spot in row]):
            return True #If every spot in the row is the same letter, return True
    
        #Checking the column
        columnIndex=square%3
        column=[self.board[columnIndex+i*3] for i in range(3)]
        if all(spot==letter for spot in column):
            return True
    
        #Checking the diagnols
        #But only if the square is an even number (0, 2, 4, 6, 8)
        if square%2==0:
            diagonal1=[self.board[i] for i in [0,4,8]] #Left to right diagonal
            if all(spot==letter for spot in diagonal1):
                return True
            
            diagonal2=[self.board[i] for i in [2,4,6]] #Right to left diagonal
            if all(spot==letter for spot in diagonal2):
                return True

        return False



def play(game, xPlayer, oPlayer, printGame=True):
    #Returns the winner of the game, or None for a tie
    if printGame:
        game.printBoardNums()

    letter="X" #Starting letter
    #iterate while the game still has empty squares
    #When there is a winner, we just return this to break the loop

    while game.emptySquares():
        #Get the move from the player
        if letter=='O':
            square=oPlayer.getMove(game)
        else:
            square=xPlayer.getMove(game)
        
        #Used to make a move
        if game.makeMove(square,letter):
            if printGame:
                print(letter + f" makes a move to square {square}")
                game.printBoard()
                print() #Printing an empty line
            
            if game.currentWinner:
                if printGame:
                    print(letter + " wins!")
                return letter #Used to exit the game

            letter="O" if letter =="X" else "X" #Used to switch to the other player

        #Break between the computer and user moves
        time.sleep(0.75)

    if printGame:
        print("Its a tie!")
        
if __name__=="__main__":
    xPlayer=HumanPlayer("X")
    oPlayer=RandomComputerPlayer("O")
    t=TicTacToe()
    play(t,xPlayer,oPlayer,printGame=True)