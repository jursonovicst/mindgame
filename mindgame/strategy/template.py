from abc import ABC, abstractmethod
from typing import Tuple

from mindgame import Guess, MindGame
from mindgame.strategy import Table


class Template(ABC):

    def __init__(self, game: MindGame):
        self.__game = game

    @property
    def width(self) -> int:
        return self.__game.width

    @property
    def numcolors(self) -> int:
        return self.__game.numcolors

    @abstractmethod
    def guess(self) -> Tuple[Guess, int, int]:
        pass

    def tell(self, guess: Guess) -> Tuple[int, int]:
        return self.__game.tell(guess)

    def solve(self, maxiteration: int = 10000) -> Guess:
        i = 0
        try:
            while True:
                self.guess()

                i += 1
                if i == maxiteration:
                    raise Exception("MAX reached")
        except Solved as e:
            hit, good = self.__game.tell(e.solution)
            if good != self.width:
                raise Exception(f"Cheating")
            return i


class Solved(Exception):
    def __init__(self, solution: Guess):
        super(Solved, self).__init__()
        self._solution = solution

    @property
    def solution(self) -> Guess:
        return self._solution


class TableTemplate(Template):
    def __init__(self, game: MindGame):
        super(TableTemplate, self).__init__(game)

        self._table = Table()

    def _guess(self, hit: int, good: int) -> Guess:
        self._table.add_result(hit, good)
        guess = super(TableTemplate, self)._guess(hit, good)
        self._table.append_guess(guess)
        return guess
