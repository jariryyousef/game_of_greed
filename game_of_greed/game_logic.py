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

    def bank(self):
        self.balance = self.shelved
        self.shelved = 0

    def clear_shelf(self):
        self.shelved = 0
