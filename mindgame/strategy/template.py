from abc import ABC, abstractmethod
from typing import Iterable

from mindgame import Guess


class Template(ABC):

    def __init__(self, width: int, numcolors: int):
        if not isinstance(width, int) or width < 1:
            raise ValueError(f"width must be greater than 0, got {width}")
        if not isinstance(width, int) or numcolors < 2:
            raise ValueError(f"number of colors must be greater than 1, got {numcolors}")
        self._width = width
        self._numcolors = numcolors

    @abstractmethod
    def guesses(self) -> Iterable[Guess]:
        pass
