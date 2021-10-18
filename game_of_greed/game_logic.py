# pylint: disable=missing-module-docstring
# pylint: disable=invalid-name
# pylint: disable=missing-function-docstring

# from collections import Counter
from random import randint
from typing import Counter


class GameLogic:
    # def calculate_score(tuple :int):
    #     score=0
    #     count=Counter(tuple).most_common()

    #     if (len(count) == 3 and count[0][1] == count[1][1] == count[2][1]):
    #         score += 1500
    #         return score

    #     if (len(count) == 6):
    #         score += 1500
    #         return score

    #     for i in range(len(count)):

    #         if (count[i][0] == 1):
    #             print(count[i][0])
    #             if count[i][1] == 1:
    #                 score += 100
    #             if count[i][1] == 2:
    #                 score += 200
    #             if count[i][1] == 3:
    #                 score += 1000
    #             if count[i][1] == 4:
    #                 score += 2000
    #             if count[i][1] == 5:
    #                 score += 3000
    #             if count[i][1] == 6:
    #                 score += 4000

    #         if (count[i][0] == 5):
    #             print(count[i][0])
    #             if count[i][1] == 1:
    #                 score += 50
    #             if count[i][1] == 2:
    #                 score += 100
    #             if count[i][1] == 3:
    #                 score += 500
    #             if count[i][1] == 4:
    #                 score += 1000
    #             if count[i][1] == 5:
    #                 score += 1500
    #             if count[i][1] == 6:
    #                 score += 2000

    #         for j in range(2,6 and not 5):
    #                 if (count[j][0] == j):
    #                     print(count[j][0])
    #                     if count[j][1] == 1 or 2:
    #                         score += 0
    #                     if count[j][1] == 3:
    #                         score += j*100
    #                     if count[j][1] == 4:
    #                         score += (j*2)*100
    #                     if count[j][1] == 5:
    #                         score += (j*3)*100
    #                     if count[j][1] == 6:
    #                         score += (j*4)*100
    #     return score
    @staticmethod
    def calculate_score(rolled):
        rolled = Counter(rolled)
        score = 0
        if len(rolled) == 6:
            for value in rolled.values():
                if value == 1:
                    score = 1500
        if len(rolled) == 3:
            for value in rolled.values():
                if all(value == 2 for value in rolled.values()):
                    score = 750 * 2
        if score == 0:
            for number in rolled:
                appears = rolled[number]
                if appears >= 3:
                    if number == 1:
                        score += (number * 1000) * (appears-2)
                    else:
                        score += (number * 100) * (appears-2)
                else:
                    if number == 1:
                        score += 100*appears
                    if number == 5:
                        score += 50*appears
        return score

    @staticmethod
    def roll_dice(num_dice):
        return tuple(randint(1, 6) for _ in range(0, num_dice))


class Banker:

    """
        A class representing a BaseClass

        Attributes
        ----------
        shelved, balance

        Methods
        -------
        __init__(shelved=0, balance=0):\n
        the constructor method for the class, it takes two parameters,
        the shelved parameter is the reference to the shelved points
        with default value zerro that will be holded py BaseClass ,
        and the balance reference to the balance value
        with default value zerro that will be holded py BaseClass also.

        shelf(shelf):\n
        the shelf method for the {Banker} class, it takes one parameter,
        the shelf parameter is the new points that will be added to the shelved points on BaseClass.

        bank():\n
        the bank method for the {Banker} class, it replace the amount of
        ({Banker} class balance) with the amount of ({Banker} class shalved points)
        & reset it to default value

        clear_shelf():\n
        the clear_shelf method for the {Banker} class,
        will reset the amount of ({Banker} class shalved points) to the default value
    """

    def __init__(self, shelved=0, balance=0):
        self.balance = balance
        self.shelved = shelved

    def shelf(self, shelf):
        self.shelved += shelf
        return self.shelved

    def bank(self):
        self.balance = self.shelved
        self.shelved = 0
        return self.shelved, self.balance

    def clear_shelf(self):
        self.shelved = 0
        return self.shelved
