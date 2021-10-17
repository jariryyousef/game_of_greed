from random import randint, sample
from collections import Counter

class GameLogic:
    
    
    # @staticmethod
    # def calculate_score(scoreTuple: int):
    #     """
    #     Input ==> tuple (int) represent a dice roll.
    #     which is the result for the six dices on each roll.
    #     # process
    #     Output == > int represent the score. according to rules of game.
    #     """
        

    @staticmethod
    def roll_dice(num_dice):
        """
        Input ==> int (1-6) Number of dices
        Output == > tuple with random values between 1 and 6.
        the length of it is the input
        """
        return tuple(randint(1,6) for _ in range(0,num_dice))
        # or
        # return tuple(sample(range(1, 6 + 1), num_dice))