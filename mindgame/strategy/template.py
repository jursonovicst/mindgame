from abc import ABC, abstractmethod

from mindgame import Guess, MindGame


class Template(ABC):

    def __init__(self, game: MindGame):
        self.__game = game
        self._width = game.width
        self._numcolors = game.numcolors

    @abstractmethod
    def guess(self, hit: int, good: int) -> Guess:
        pass

    def solve(self, maxiteration: int = 10000) -> int:
        i = 0
        hit = 0
        good = 0
        while good != self.__game.width:
            guess = self.guess(hit, good)

            hit, good = self.__game.tell(guess)
            i += 1

            if i == maxiteration:
                raise Exception("MAX reached")

        return i

    # def print(self):
    #     i = 0
    #     for guess, (hit, good) in self._table:
    #         print(f"{i:02d}: {guess} {hit}, {good}")
    #         i += 1
