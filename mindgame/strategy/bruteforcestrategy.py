from mindgame import Guess, MindGame
from mindgame.strategy import Template


class BruteForceStrategy(Template):
    def __init__(self, game: MindGame):
        super(BruteForceStrategy, self).__init__(game)
        self._n = -1

    def guess(self, hit: int, good: int) -> Guess:
        self._n += 1
        return Guess.fromint(
            [(self._n // self._numcolors ** (place - 1)) % self._numcolors for place in range(self._width, 0, -1)])
