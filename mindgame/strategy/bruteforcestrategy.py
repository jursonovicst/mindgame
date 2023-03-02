from typing import Tuple

from mindgame import Guess, MindGame
from mindgame.strategy import Template, Solved


class BruteForceStrategy(Template):
    def __init__(self, game: MindGame):
        super(BruteForceStrategy, self).__init__(game)
        self._n = -1

    def guess(self) -> Tuple[Guess, int, int]:
        self._n += 1
        guess = Guess.fromint(
            [(self._n // self.numcolors ** (place - 1)) % self.numcolors for place in range(self.width, 0, -1)])
        hit, good = self.tell(guess)
        if good == self.width:
            raise Solved(guess)

        return guess, hit, good
