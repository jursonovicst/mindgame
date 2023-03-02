from mindgame import Guess


class Table:
    def __init__(self):
        self._table = []

    def append_guess(self, guess: Guess):
        self._table.append([guess, None, None])

    def add_result(self, hit: int, good: int):
        self._table[len(self._table) - 1][1] = hit
        self._table[len(self._table) - 1][2] = good
