import random

from mindgame import Guess
from mindgame.strategy import Template


class RandomStrategy(Template):
    def guess(self, hit: int, good: int) -> Guess:
        return Guess.fromint(random.choices(range(self._numcolors), k=self._width))
