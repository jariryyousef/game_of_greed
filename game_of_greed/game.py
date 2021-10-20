from random import randint
from game_of_greed.game_logic import GameLogic, Banker
import sys


class Game:
    """Class for Game of Greed application
    """

    def __init__(self, num_rounds=20):

        self.banker = Banker()
        self.num_rounds = num_rounds
        self.round_num = 0

    def play(self, roller=None):
        """Entry point for playing (or declining) a game
        Args:
            roller (function, optional): Allows passing in a custom dice roller function.
                Defaults to None.
        """

        self._roller = roller or GameLogic.roll_dice

        print("Welcome to Game of Greed")

        print("(y)es to play or (n)o to decline")

        response = input("> ")

        if response == "y" or response == "yes":
            self.start_game()
        else:
            self.decline_game()

    def decline_game(self):
        print("OK. Maybe another time")

    def start_game(self):

        self.round_num = 1

        while self.round_num <= self.num_rounds:

            self.start_round(self.round_num)

            self.round_num += 1

            print("Total score is {} points".format(self.banker.balance))

        self.quit_game()

    def quit_game(self):

        print("Thanks for playing. You earned {} points".format(self.banker.balance))

        sys.exit()

    def start_round(self, round, num_dice=6):

        print("Starting round {}".format(round))

        round_score = 0

        while True:

            roll = self.roll_dice(num_dice)

            if self.got_zilch(roll):
                break

            keepers = self.handle_keepers(roll)

            print("(r)oll again, (b)ank your points or (q)uit:")

            roll_again_response = input("> ")

            if roll_again_response == "q":

                self.quit_game()

            

            elif roll_again_response == "b":

                round_score = self.banker.bank()

                break

            else:

                num_dice -= len(keepers)

                if num_dice == 0:

                    num_dice = 6

        print("You banked {} points in round {}".format(str(round_score), round))

    def handle_keepers(self, roll):

        while True:
            print("Enter dice to keep, or (q)uit:")

            keeper_string = input("> ")

            if keeper_string.startswith("q"):
                self.quit_game()

            keepers = self.gather_keepers(roll, keeper_string)

            roll_score = self.calculate_score(keepers)

            if roll_score == 0:
                print("Must keep at least one scoring dice")
            else:
                break

        self.banker.shelf(roll_score)

        num_dice_remaining = len(roll) - len(keepers)

        print(
            "You have {} unbanked points and {} dice remaining".format(
                self.banker.shelved, num_dice_remaining)
        )

        return keepers

    def roll_dice(self, num):

        print("Rolling {} dice...".format(num))

        roll = self._roller(num)

        print("*** " + " ".join([str(i) for i in roll]) + " ***")

        return roll

    def got_zilch(self, roll):

        initial_score = self.calculate_score(roll)

        if initial_score == 0:

            width = 40
            print("*" * width)
            print("**" + "Zilch!!! Round over".center(width - 4) + "**")
            print("*" * width)

            self.banker.clear_shelf()

            return True

        return False

    def calculate_score(self, roll):
        return GameLogic.calculate_score(roll)

    def _convert_keepers(self, keeper_string):

        return [int(ch) for ch in keeper_string if ch.isdigit()]

    def gather_keepers(self, roll, keeper_string):

        keepers = self._convert_keepers(keeper_string)

        while not GameLogic.validate_keepers(roll, keepers):
            print("Cheater!!! Or possibly made a typo...")
            print("*** " + " ".join([str(i) for i in roll]) + " ***")
            print("Enter dice to keep, or (q)uit:")
            keeper_string = input("> ")
            if keeper_string.startswith("q"):
                self.quit_game()

            keepers = self._convert_keepers(keeper_string)

        return keepers
    


if __name__ == "__main__":

    rolls = [tuple(randint(1, 6) for _ in range(1, 7))]
    def roller(num):
        if rolls:
            return rolls.pop(0)
            
        return GameLogic.roll_dice(num)

    game = Game()
    game.play(roller=roller)


# print(rolls = [tuple(randint(1, 6) for _ in range(1, 7))])
#-------------------------------------------------------------------------------------------------------------------#
# class Game:
#     balance = 0
#     shelved = 0
#     round_counter = 0
#     dice_kept = 6
#     dice_left = 6

#     def __init__(self):
#         self.banker = Banker()

#     def play(self, roller):
#         self.roller = roller or GameLogic.roll_dice
#         print("Welcome to Game of Greed")
#         print("(y)es to play or (n)o to decline")
#         user_start = input("> ")
#         if user_start == "y":
#             self.start_game()
#         elif user_start == "n":
#             print("OK. Maybe another time")
#             quit()
#         else:
#             print("just answer the question")

#     def start_game(self):
#         # dice_left == 6
#         self.fake_dice_roll()
#         if self.round_counter < 2:
#             print("Enter dice to keep, or (q)uit:")
#             quit_or_play_again = input("> ")
#             if quit_or_play_again == "q":
#                 print("Thanks for playing. You earned {} points".format(self.balance))
#                 quit()
#             else:
#                 self.repetitive_gameplay(quit_or_play_again)
#         else:
#             print("Enter dice to keep, or (q)uit:")

#     def fake_dice_roll(self, dice=6):
#         roll = self.roller(dice)
#         self.round_counter += 1
#         self.dice_left = 6
#         print("Starting round {}".format(self.round_counter))
#         string_dice = ""
#         for dice in roll:
#             string_dice += "{} ".format(str(dice))
#         print("Rolling {} dice...".format(self.dice_left))
#         print("*** {}***".format(string_dice))
#         return roll

#     def repetitive_gameplay(self, saved_dice):
#         self.saved_dice = saved_dice
#         dice_list = [int(x) for x in str(saved_dice)]
#         self.shelved += GameLogic.calculate_score(dice_list)
#         self.dice_left = 6 - len(saved_dice)

#         self.ask_to_play_again()
#         keep_playing = input("> ")

#         while keep_playing != "q":
#             if keep_playing == "r":
#                 self.roller(6)
#             elif keep_playing == "b":
#                 shelved_this_round = self.shelved
#                 Banker.bank(self)
#             else:
#                 print("thats not an option")
#                 keep_playing = input("> ")

#             if self.round_counter < 2:
#                 self.give_round_score(shelved_this_round)

#             self.start_game()
#             dice_kept = input("> ")
#             if dice_kept == "q":
#                 print("Thanks for playing. You earned {} points".format(self.balance))
#                 quit()
#             else:
#                 dice_kept_list = [int(x) for x in str(dice_kept)]

#                 self.roller(len(dice_kept_list))
#                 self.shelved += GameLogic.calculate_score(dice_kept_list)
#                 self.dice_left = 6 - len(dice_kept_list)

#                 self.ask_to_play_again()
#                 answer = input("> ")
#                 if answer == "r":
#                     self.roller(self.dice_left)
#                 elif answer == "b":
#                     shelved_this_round = self.shelved
#                     Banker.bank(self)
#                     self.give_round_score(shelved_this_round)
#                 elif answer == "q":
#                     print("Thanks for playing. You earned {} points".format(
#                         self.balance))
#                     quit()

#             self.fake_dice_roll_2()
#             print("Enter dice to keep, or (q)uit:")
#             dice_kept = input("> ")
#             print("Thanks for playing. You earned {} points".format(self.balance))

#     def ask_to_play_again(self):
#         print(
#             "You have {} unbanked points and {} dice remaining".format(self.shelved, self.dice_left))
#         print("(r)oll again, (b)ank your points or (q)uit:")

#     def fake_dice_roll_2(self, dice=6,):
#         roller = GameLogic.roll_dice
#         self.round_counter += 1
#         self.dice_left = 6
#         roll = "665421"  # this is fake roll for the test. use the one below this
#         # roll = roller(self.dice_left)#REAL dice roll!!
#         self.dice = dice
#         print("Starting round {}".format(self.round_counter))
#         print("Rolling {} dice...".format(self.dice_left))
#         string_dice = ""
#         for dice in roll:
#             string_dice += "{} ".format(str(dice))
#         print("*** {}***".format(string_dice))

#     def give_round_score(self, shelved_this_round):
#         print(
#             "You banked {} points in round {}".format(shelved_this_round, self.round_counter))
#         print("Total score is {} points".format(self.balance))


# q = Game()
# q.play("")
#-------------------------------------------------------------------------------------------------------------------#
# pylint: disable=missing-module-docstring
# pylint: disable=invalid-name
# pylint: disable=missing-function-docstring

# class Game:
#     round_counter = 1

#     def __init__(self, quitter=""):
#         self.quitter = quitter

#     def play(self, roller):
#         self.roller = roller
#         print("""Welcome to Game of Greed
# (y)es to play or (n)o to decline""")

#         user_start = input("> ")
#         if user_start == "y":
#             self.start_game()
#         elif user_start == "n":
#             print("OK. Maybe another time")
#             quit()
#         else:
#             print("just answer the question")

#     def start_game(self):
#         if self.round_counter < 2:
#             print("Starting round {}".format(self.round_counter))
#             print("Rolling {} dice...".format(6))
#             if self.round_counter == 1:
#                 print("*** {} {} {} {} {} {} ***".format(4, 4, 5, 2, 3, 1))
#             elif self.round_counter == 2:
#                 print("*** {} {} {} {} {} {} ***".format(6, 4, 5, 2, 3, 1))
#             print("Enter dice to keep, or (q)uit:")
#             quit_or_play_again = input("> ")
#             if quit_or_play_again == "q":
#                 print("Thanks for playing. You earned {} points".format(0))
#                 quit()
#             else:
#                 self.repetitive_gameplay(quit_or_play_again)
#         else:
#             print("Enter dice to keep, or (q)uit:")

#     def repetitive_gameplay(self, saved_dice):
#         self.saved_dice = saved_dice
#         self.ask_to_play_again()
#         keep_playing = input("> ")
#         while keep_playing != "q":
#             if keep_playing == "b":
#                 shelved_this_round = 50
#             else:
#                 print("thats not an option")
#                 keep_playing = input("> ")

#             if self.round_counter < 2:
#                 self.give_round_score(shelved_this_round)
#                 self.round_counter += 1
#             self.start_game()
#             dice_kept = input("> ")
#             if dice_kept == "q":
#                 print("Thanks for playing. You earned {} points".format(
#                     shelved_this_round))
#                 quit()
# else:
#     dice_kept_list = [int(x) for x in str(dice_kept)]

#     self.roller(len(dice_kept_list))
#     self.shelved += GameLogic.calculate_score(dice_kept_list)
#     self.dice_left = 6 - len(dice_kept_list)

#     self.ask_to_play_again()
#     answer = input("> ")
#     if answer == "r":
#         self.roller(self.dice_left)
#     elif answer == "b":
#         shelved_this_round = self.shelved
#         Banker.bank(self)
#         self.give_round_score(shelved_this_round)
#     elif answer == "q":
#         print(
#             f"Thanks for playing. You earned {self.balance} points")
#         quit()

# def ask_to_play_again(self):
#     print(
#         "You have {} unbanked points and {} dice remaining".format(50, 5))
#     print("(r)oll again, (b)ank your points or (q)uit:")

# def give_round_score(self, shelved_this_round):
#     print(
#         "You banked {} points in round {}".format(shelved_this_round, self.round_counter))
#     print(f"Total score is {shelved_this_round} points")

# print("Starting round {}".format(1))
# print("Rolling {} dice...".format(6))
# print("*** {} {} {} {} {} {} ***".format(4, 4, 5, 2, 3, 1))
#     print("Enter dice to keep, or (q)uit:")
#     self.roller = input("> ")
#     if self.roller == "q":
#         # one & done sim
#         print("Thanks for playing. You earned {} points".format(0))
#     # -----------------

#     elif self.roller == "{}".format(5):
#         print("You have {} unbanked points and {} dice remaining".format(50, 5))
#         print("(r)oll again, (b)ank your points or (q)uit:")
#         self.roller = str(input("> "))
#         if self.roller == "b":
#             print("You banked {} points in round {}".format(50, 1))
#             print("Total score is {} points".format(50))
#             print("Starting round {}".format(2))
#             print("Rolling {} dice...".format(6))
#             print("*** {} {} {} {} {} {} ***".format(6, 4, 5, 2, 3, 1))
#             print("Enter dice to keep, or (q)uit:")
#             self.roller = input("> ")
#             if self.roller == "q":
#                 # bank one roll then quit
#                 print("Thanks for playing. You earned {} points".format(50))

# return self.roller


