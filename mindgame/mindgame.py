import random
from typing import Tuple

from mindgame import Guess, Pin


class MindGame:

    def __init__(self, width: int = 4, numcolors: int = 6):
        if not isinstance(width, int) or width < 1:
            raise ValueError(f"width must be greater than 0, got {width}")
        if not isinstance(width, int) or numcolors < 2:
            raise ValueError(f"number of colors must be greater than 1, got {numcolors}")
        self._width = width
        self._numcolors = numcolors

        self.__secret = self._think()

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

    def tell(self, guess: Guess) -> Tuple[int, int]:

        return guess.compare(self.__secret)
