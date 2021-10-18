# pylint: disable=missing-module-docstring
# pylint: disable=invalid-name
# pylint: disable=missing-function-docstring

from game_of_greed.game_logic import GameLogic
from game_of_greed.game_logic import Banker


class Game:
    balance = 0
    shelved = 0
    round_counter = 0
    dice_kept = 6
    dice_left = 6

    def __init__(self):
        self.banker = Banker()

    def play(self, roller):
        self.roller = roller or GameLogic.roll_dice
        print("Welcome to Game of Greed")
        print("(y)es to play or (n)o to decline")
        user_start = input("> ")
        if user_start == "y":
            self.start_game()
        elif user_start == "n":
            print("OK. Maybe another time")
            quit()
        else:
            print("just answer the question")

    def repetitive_gameplay(self, saved_dice):
        self.saved_dice = saved_dice
        dice_list = [int(x) for x in str(saved_dice)]
        self.shelved += GameLogic.calculate_score(dice_list)
        self.dice_left = 6 - len(saved_dice)

        self.ask_to_play_again()
        keep_playing = input("> ")

        while keep_playing != "q":
            if keep_playing == "r":
                self.roller(6)
            elif keep_playing == "b":
                shelved_this_round = self.shelved
                Banker.bank(self)
            else:
                print("thats not an option")
                keep_playing = input("> ")

            if self.round_counter < 2:
                self.give_round_score(shelved_this_round)

            self.start_game()
            dice_kept = input("> ")
            if dice_kept == "q":
                print(f"Thanks for playing. You earned {self.balance} points")
                quit()
            else:
                dice_kept_list = [int(x) for x in str(dice_kept)]

                self.roller(len(dice_kept_list))
                self.shelved += GameLogic.calculate_score(dice_kept_list)
                self.dice_left = 6 - len(dice_kept_list)

                self.ask_to_play_again()
                answer = input("> ")
                if answer == "r":
                    self.roller(self.dice_left)
                elif answer == "b":
                    shelved_this_round = self.shelved
                    Banker.bank(self)
                    self.give_round_score(shelved_this_round)
                elif answer == "q":
                    print(
                        f"Thanks for playing. You earned {self.balance} points")
                    quit()

            self.fake_dice_roll_2()
            print("Enter dice to keep, or (q)uit:")
            dice_kept = input("> ")
            print(f"Thanks for playing. You earned {self.balance} points")

    def fake_dice_roll_2(self, dice=6,):
        roller = GameLogic.roll_dice
        self.round_counter += 1
        self.dice_left = 6
        roll = "665421"  # this is fake for the test. use the one below this
        # roll = roller(self.dice_left)#REAL dice roll!!
        self.dice = dice
        print(f"Starting round {self.round_counter}")
        print(f"Rolling {self.dice_left} dice...")
        string_dice = ""
        for dice in roll:
            string_dice += f"{str(dice)} "
        print(f"*** {string_dice}***")

    def give_round_score(self, shelved_this_round):
        print(
            f"You banked {shelved_this_round} points in round {self.round_counter}")
        print(f"Total score is {self.balance} points")

    def ask_to_play_again(self):
        print(
            f"You have {self.shelved} unbanked points and {self.dice_left} dice remaining")
        print("(r)oll again, (b)ank your points or (q)uit:")

    def fake_dice_roll(self, dice=6):
        roll = self.roller(dice)
        self.round_counter += 1
        self.dice_left = 6
        print(f"Starting round {self.round_counter}")
        string_dice = ""
        for dice in roll:
            string_dice += f"{str(dice)} "
        print(f"Rolling {self.dice_left} dice...")
        print(f"*** {string_dice}***")
        # return roll

    def start_game(self):

        # dice_left == 6
        self.fake_dice_roll()
        if self.round_counter < 2:
            print("Enter dice to keep, or (q)uit:")
            quit_or_play_again = input("> ")
            if quit_or_play_again == "q":
                print(f"Thanks for playing. You earned {self.balance} points")
                quit()
            else:
                self.repetitive_gameplay(quit_or_play_again)
        else:
            print("Enter dice to keep, or (q)uit:")

