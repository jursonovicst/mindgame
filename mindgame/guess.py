from typing import List, Tuple

from mindgame import Pin


class Guess:
    @classmethod
    def fromint(cls, colors: List[int]):
        return Guess([Pin(color) for color in colors])

    def __init__(self, pins: List[Pin]):
        self._pins = pins

    @property
    def width(self) -> int:
        return len(self._pins)

    @property
    def pin_set(self) -> List[Pin]:
        return list(set(self._pins))

    def __str__(self):
        return str(list(map(int, self._pins)))

    def compare(self, secret) -> Tuple[int, int]:
        if not isinstance(secret, Guess) or secret.width != self.width:
            raise ValueError(f"secret length mismatch {secret}")

        # calculate results
        right_place = sum([1 for g, s in zip(self._pins, secret._pins) if g == s])

        any_place = len([1 for g in self._pins if g in secret._pins])

        return any_place - right_place, right_place
