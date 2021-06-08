

from game import constants
from game import actor
from game.actor import Actor
from game.point import Point

class Guess(Actor):
    """A limbless reptile. The responsibility of Snake is keep track of its segments. It contains methods for moving and growing among others.

    Stereotype:
        Structurer, Information Holder

    Attributes:
        _body (List): The snake's body (a list of Actor instances)
    """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Guess): An instance of snake.
        """
        super().__init__()
        self._word = ""
        position = Point(0, 20)
        self.set_position(position)
        self.set_text(f"Guess: {self._word}")


    def add_letters(self, letter):
        """adds a letter to the guess actor
        
        Args:
            Self (Guess): An instance of Guess.
            letter: A letter to be added to guess"""
        if letter == None:
            pass
        else:
            self._word += letter
            self.set_text(f"Guess: {self._word}")   
