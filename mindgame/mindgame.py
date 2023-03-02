import random
from typing import Tuple

from mindgame import Guess, Pin
from mindgame.strategy import Template


class MindGame:

    def __init__(self, width: int = 4, numcolors: int = 6):
        if not isinstance(width, int) or width < 1:
            raise ValueError(f"width must be greater than 0, got {width}")
        if not isinstance(width, int) or numcolors < 2:
            raise ValueError(f"number of colors must be greater than 1, got {numcolors}")
        self._width = width
        self._numcolors = numcolors

        self.__secret = self._think()

        self._table = []

    @property
    def width(self) -> int:
        return self._width

    @property
    def numcolors(self) -> int:
        return self._numcolors

    def _think(self) -> Guess:
        return Guess(random.choices([Pin(color) for color in range(self._numcolors)], k=self._width))

    def reset(self):
        self.__secret = self._think()

    def guess(self, guess: Guess) -> Tuple[int, int]:

        results = guess.compare(self.__secret)

        # record progress
        self._table.append((guess, results))

        return results

    def print(self):
        i = 0
        for guess, (hit, good) in self._table:
            print(f"{i:02d}: {guess} {hit}, {good}")
            i += 1

    def solve(self, strategy: Template, maxiteration: int = 10000, display: bool = False) -> int:
        i = 0
        for guess in strategy.guesses():
            hit, good = self.guess(guess)
            if i == maxiteration:
                raise Exception("MAX reached")
            if good == self.width:
                if display:
                    self.print()
                break
            i += 1
        return i
