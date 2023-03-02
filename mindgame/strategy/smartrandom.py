from typing import Tuple

from mindgame import Guess
from mindgame.strategy import RandomStrategy


class SmartRandomStrategy(RandomStrategy):

    def guess(self) -> Tuple[Guess, int, int]:
        guess, hit, good = super(SmartRandomStrategy, self).guess()

        # exclude impossible, if any
        if hit == 0 and good == 0:
            for pin in guess.pin_set:
                self._possible_pins.remove(pin)
        return guess, hit, good
