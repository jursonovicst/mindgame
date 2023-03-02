import random
from typing import Tuple

from mindgame import Guess, MindGame, Pin
from mindgame.strategy import Template, Solved


class RandomStrategy(Template):
    def __init__(self, game: MindGame):
        super(RandomStrategy, self).__init__(game)
        self._possible_pins = [Pin(color) for color in range(self.numcolors)]

    def guess(self) -> Tuple[Guess, int, int]:
        guess = Guess(random.choices(self._possible_pins, k=self.width))
        hit, good = self.tell(guess)
        if good == self.width:
            raise Solved(guess)
        return guess, hit, good
