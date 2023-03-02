class Pin:
    def __init__(self, color: int):
        assert isinstance(color, int) and 0 <= color, f"invalid color: {color}"
        self._color = color

    def __int__(self) -> int:
        return self._color

    def __eq__(self, other):
        if isinstance(other, Pin):
            return self._color == other._color
        elif isinstance(other, int):
            if other < 0:
                raise ValueError(f"Invalid color: {other}")
            return self._color == other
        else:
            raise ValueError(f"Cannot compare Pin and {type(other)}")
