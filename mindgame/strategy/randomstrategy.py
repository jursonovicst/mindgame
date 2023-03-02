import random

from mindgame import Guess
from mindgame.strategy import Template


class RandomStrategy(Template):
    def guesses(self):
        while True:
            yield Guess.fromint(random.choices(range(self._numcolors), k=self._width))
