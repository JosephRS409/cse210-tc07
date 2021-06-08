import random
from game.word_list import random_words
from game import constants
from game import actor
from game.actor import Actor
from game.point import Point

class Words(Actor):
    """A nutritious substance that snake's like. The responsibility of Food is to keep track of its appearance and position. A Food can move around randomly if asked to do so. 
    
    Stereotype:
        Information Holder

    Attributes: 
        _points (integer): The number of points the food is worth.
    """
    def __init__(self):
        """The class constructor. Invokes the superclass constructor, set's the 
        text and moves the food to a random position within the boundary of the 
        screen.
        
        Args:
            self (Actor): an instance of Actor.
        """
        super().__init__()
        self._points = 0
        self._words = []
        self.words = random_words
        self.prepare()
        self.reset()

    def prepare(self):
        for _ in range(5):
            self.add_word()

    def get_word(self):
        """Gets a list of words and returns one
        
        Args:
            self (Words): An instance of Words"""
        get = random.randint(0,len(self.words)-1)
        word = self.words[get]
        self.words.pop(get)
        return word

    def get_points(self):
        """Gets the points this food is worth.
        
        Args:
            self (Food): an instance of Food.

        Returns:
            integer: The points this food is worth.
        """
        return self._points

    def reset(self):
        """Resets the food by moving it to a random position within the boundaries of the screen and reassigning the points to a random number.
        
        Args:
            self (Words): an instance of Words.
        """
        self._points = random.randint(1, 5)
        x = random.randint(1, constants.MAX_X - 2)
        y = random.randint(1, constants.MAX_Y - 2)
        position = Point(x, y)
        self.set_position(position)

    def add_word(self):
        """Adds a word to the screen
        
        Args:
            self (Words): an instance of Words.
        """
        word = Actor()
        word.set_text(self.get_word())
        word._points = random.randint(1, 5)
        x = random.randint(1, constants.MAX_X - 2)
        y = random.randint(1, constants.MAX_Y - 2)
        position = Point(x, y)
        word.set_position(position)
        velocity = Point(2, 0)
        word.set_velocity(velocity)
        self._words.append(word)

    def move_word(self):
        """Moves the words on the screen and adds another word when
        word at the beggining of the list is at y 2
        
        Args:
            self (Words): an instance of Words."""
        for n in self._words:
            spot = n.get_position()
            spoty = spot.get_y()
            if spoty == 19:
                spoty = 0
            position = Point(spot.get_x(),spoty+1)
            n.set_position(position)
        first_word = self._words[0]
        first_word = first_word.get_position()
        if len(self.words) >= 1 and first_word.get_y() == 2:
            self.add_word()

