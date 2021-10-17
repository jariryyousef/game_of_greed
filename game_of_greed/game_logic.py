

# pylint: disable=missing-module-docstring
# pylint: disable=invalid-name
# pylint: disable=missing-function-docstring


class Banker:
    def __init__(self, shelved=0, balance=0):
        self.balance = balance
        self.shelved = shelved

    def shelf(self, shelf):
        self.shelved += shelf

    def bank(self):
        self.balance = self.shelved
        self.shelved = 0



