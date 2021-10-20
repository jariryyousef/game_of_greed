"""Place in root of Game of Greed Project,
at same level as pyproject.toml
"""


from abc import ABC, abstractmethod
import builtins
import re
from game_of_greed.game import Game
from game_of_greed.game_logic import GameLogic


class BaseBot(ABC):
    """Base class for Game of Greed bots"""

    def __init__(self, print_all=True):
        self.last_print = ""
        self.last_roll = []
        self.print_all = print_all
        self.dice_remaining = 0
        self.unbanked_points = 0

        self.real_print = print
        self.real_input = input
        builtins.print = self._mock_print
        builtins.input = self._mock_input
        self.total_score = 0

    def reset(self):
        """restores the real print and input builtin functions"""

        builtins.print = self.real_print
        builtins.input = self.real_input

    def report(self, text):
        """Prints out final score, and all other lines optionally"""

        # if self.print_all:
        self.real_print(text)
        if text.startswith("Thanks for playing."):
            score = re.sub("\D", "", text)
            self.total_score += int(score)

    def _mock_print(self, *args, **kwargs):
        """steps in front of the real builtin print function"""

        line = " ".join(args)

        if "unbanked points" in line:

            # parse the proper string
            # E.g. "You have 700 unbanked points and 2 dice remaining"
            unbanked_points_part, dice_remaining_part = line.split(
                "unbanked points")

            # Hold on to unbanked points and dice remaining for determining rolling vs. banking
            self.unbanked_points = int(re.sub("\D", "", unbanked_points_part))

            self.dice_remaining = int(re.sub("\D", "", dice_remaining_part))

        elif line.startswith("*** "):

            self.last_roll = [int(ch) for ch in line if ch.isdigit()]

        else:
            self.last_print = line

        self.report(*args, **kwargs)

    def _mock_input(self, *args, **kwargs):
        """steps in front of the real builtin print function"""

        if self.last_print == "(y)es to play or (n)o to decline":

            return "y"

        elif self.last_print == "Enter dice to keep, or (q)uit:":

            return self._enter_dice()

        elif self.last_print == "(r)oll again, (b)ank your points or (q)uit:":

            return self._roll_bank_or_quit()

        raise ValueError(f"Unrecognized last print {self.last_print}")

    def _enter_dice(self):
        """simulate user entering which dice to keep.
        Defaults to all scoring dice"""

        roll = GameLogic.get_scorers(self.last_roll)

        roll_string = ""

        for value in roll:
            roll_string += str(value)

        self.report("> " + roll_string)

        return roll_string

    @abstractmethod
    def _roll_bank_or_quit(self):
        """decide whether to roll the dice, bank the points, or quit"""

        # subclass MUST implement this method
        return "b"

    @classmethod
    def play(cls, num_games=1):
        """Tell Bot play game a given number of times.
        Will report average score"""
        
        mega_total = 0

        for _ in range(num_games):
            player = cls()
            game = Game()
            try:
                game.play()
            except SystemExit:
                # in game system exit is fine
                # because that's how they quit.
                pass

            mega_total += player.total_score
            player.reset()

        print(
            f"####$ $ $ $ $ {cls.__name__}: {num_games} games played with average score of {mega_total // num_games} $ $ $ $ $####"
        )


class NervousNellie(BaseBot):
    """NervousNellie banks the first roll always"""

    def _roll_bank_or_quit(self):
        return "b"


class HaneenBot(BaseBot):
    def _roll_bank_or_quit(self):
        """your logic here"""
        if self.unbanked_points >= 700 or self.dice_remaining < 4:
            return "b"

    def _enter_dice(self):
        """simulate user entering which dice to keep.
        Defaults to all scoring dice"""
        roll = GameLogic.get_scorers(self.last_roll)
        roll_string = ""
        for value in roll:
            roll_string += str(value)
        if GameLogic.calculate_score(roll) < 200:
            self.report("> " + roll_string[0])
            return roll_string[0]
        five_count = 0
        two_count = 0
        three_count = 0
        for value in roll_string:
            if value == "5":
                five_count += 1
            elif value == "2":
                two_count += 1
            elif value == "3":
                three_count += 1
        if two_count <= 4 and two_count != len(roll):
            roll_string.replace("2", "", two_count)
        if three_count <= 3 and three_count != len(roll):
            roll_string.replace("3", "", three_count)
        if five_count <= 2:
            if five_count == len(roll_string):
                roll_string.replace("5", "", 1)
            else:
                roll_string.replace("5", "", five_count)
        if roll_string == "":
            roll_string += str(roll[0])
        self.report("> " + roll_string)
        return roll_string


class BasharBot(BaseBot):
    def _zilch_chance(self):
        return {1: 2 / 3, 2: 4 / 9, 3: 5 / 18, 4: 17 / 108, 5: 25 / 324, 6: 5 / 216, }[
            self.dice_remaining
        ]

    def _roll_bank_or_quit(self):
        
        if not self.dice_remaining:
            return "r"
        if self._zilch_chance() > (95 / (self.unbanked_points)):
            return "b"
        return "r"


class YousefBot(BaseBot):
    """VERY aggressive playstyle : all or nothing """

    def _roll_bank_or_quit(self):
        if self.dice_remaining >= 3:
            return "r"
        if self.unbanked_points >= 800 or self.dice_remaining < 3:
            return "b"
        if self.unbanked_points > 350:
            if self.dice_remaining >= 3:
                return "r"
            else:
                return "b"
        if self.unbanked_points <= 400:
            return "r"


class AseelBot(BaseBot):
    def _roll_bank_or_quit(self):
        if self.unbanked_points >= 550 or self.dice_remaining < 2:
            return "b"
        if self.unbanked_points >= 450 and self.dice_remaining <= 3:
            return "b"
        elif self.unbanked_points >= 350 and self.dice_remaining == 2:
            return "b"
        if self.unbanked_points + self.total_score >= 10000:
            return "b"
        return "r"

if __name__ == "__main__":
    num_games = 20

    while True:
        print(f"""
        ##################################
        #### Welcome to Game of Greed ####
        __________________________________
        __________________________________
        ####        whose turn?       ####
        ----------------------------------
        #### {NervousNellie.__name__} ####
        #### {HaneenBot.__name__}     ####
        #### {BasharBot.__name__}     ####
        #### {YousefBot.__name__}     ####
        #### {AseelBot.__name__}      ####
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        $$$$   Enter (q)uit To Exit   $$$$
        ##################################
        """)
        user_response = input("> ")

        if user_response == "NervousNellie":
            NervousNellie.play(num_games)

        elif user_response == "HaneenBot":
            HaneenBot.play(num_games)

        elif user_response == "BasharBot":
            BasharBot.play(num_games)

        elif user_response == "YousefBot":
            YousefBot.play(num_games)

        elif user_response == "AseelBot":
            AseelBot.play(num_games)

        else:
            if user_response == "q" or "quit":
                break
