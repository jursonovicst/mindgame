from mindgame import Guess
from mindgame.strategy import Template


class BruteForceStrategy(Template):
    def guesses(self):
        n = -1
        while True:
            n += 1
            yield Guess.fromint(
                [(n // self._numcolors ** (place - 1)) % self._numcolors for place in range(self._width, 0, -1)])
