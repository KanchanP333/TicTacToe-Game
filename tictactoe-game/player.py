#Part of TicTacToe game 
#player.py



import math
import random

#Base player class
class Player:
    def __init__(self,letter):
        self.letter=letter  #X or O
    
    def getMove(self,game):
        pass


class RandomComputerPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter) #Initializing the super class
    
    def getMove(self,game):
        square=random.choice(game.availableMoves())
        return square

class HumanPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)
    
    def getMove(self,game):
        validSquare=False 
        val=None

        while not validSquare:
            square=input(self.letter+"\'s turn. Input move (0-8):")
            #Now we check that it is a correct value by type casting it to an integer
            #If not, then print that its invalid
            #If the spot is not available on the board, we also say its invalid
            try:
                val=int(square)
                if val not in game.availableMoves():
                    raise ValueError
                validSquare=True
            except ValueError:
                print("Invalid square. Try again!")
        return val