from time import sleep
from game import constants
from game.words import Words
from game.score import Score
from game.guess import Guess
import sys

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        food (Food): The snake's target.
        input_service (InputService): The input mechanism.
        keep_playing (boolean): Whether or not the game can continue.
        output_service (OutputService): The output mechanism.
        score (Score): The current score.
        snake (Snake): The player or snake.
    """

    def __init__(self, input_service, output_service):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self._words = Words()
        self._input_service = input_service
        self._keep_playing = True
        self._output_service = output_service
        self._score = Score()
        self._guess = Guess()
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._keep_playing:
            self._get_inputs()
            self._do_outputs()
            sleep(constants.FRAME_LENGTH)

    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the desired direction and moving the snake.

        Args:
            self (Director): An instance of Director.
        """
        letter = self._input_service.get_key()
        if letter == "clear":
            if self._score._points >= 100:
                print(f"""\n\n\n\n\n\n\n\n\n\n\n
                                   .''.       
       .''.      .        *''*    :_\/_:     . 
      :_\/_:   _\(/_  .:.*_\/_*   : /\ :  .'.:.'.
  .''.: /\ :   ./)\   ':'* /\ * :  '..'.  -=:o:=-
 :_\/_:'.:::.    ' *''*    * '.\\'/.' _\(/_'.':'.'
 : /\ : :::::     *_\/_*     -= o =-  /)\    '  *
  '..'  ':::'     * /\ *     .'/.\\'.   '
      *            *..*         :Congratulations! you won!""")
                sys.exit()
            else:
                for thing in self._words._words:
                    word = thing._text
                    if word.lower() == self._guess._word.lower():
                        self._score.add_points(thing._points)
                        self._words._words.remove(thing)
            
                self._guess._word = ""
                self._guess.set_text(f"Guess: {self._guess._word}")
        else:
            self._guess.add_letters(letter)
        self._words.move_word()

        
    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if there are stones left and declaring 
        the winner.

        Args:
            self (Director): An instance of Director.
        """
        self._output_service.clear_screen()
        self._output_service.draw_actors(self._words._words)
        self._output_service.draw_actor(self._guess)
        self._output_service.draw_actor(self._score)
        self._output_service.flush_buffer()