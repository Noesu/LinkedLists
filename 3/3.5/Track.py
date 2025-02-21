from math import sqrt
from typing import List, Union

Coord = Union[int, float]

class TrackLine:
    def __init__(self, to_x: Coord, to_y: Coord, max_speed: int):
        self.max_speed = max_speed
        self.to_y = to_y
        self.to_x = to_x

class Track:
    def __init__(self, x: Coord, y: Coord):
        self.start_x = x
        self.start_y = y
        self.lines = []

    def __len__(self) -> int:
        return int(self.get_length())

    def __eq__(self, other: "Track") -> bool:
        return len(self) == len(other)

    def __lt__(self, other: "Track") -> bool:
        return len(self) < len(other)

    def add_track(self, tr: TrackLine) -> None:
        self.lines.append(tr)

    def get_tracks(self) -> List[TrackLine]:
        return self.lines

    def get_length(self) -> float:
        x, y = self.start_x, self.start_y
        length = 0
        for line in self.lines:
            length += sqrt(pow(x - line.to_x, 2) + pow(y - line.to_y, 2))
            x, y = line.to_x, line.to_y
        return length

########################################################################################################################

track1, track2 = Track(0, 0), Track(0, 1)
track1.add_track(TrackLine(2, 4, 100))
track1.add_track(TrackLine(5, -4, 100))
track2.add_track(TrackLine(3, 2, 90))
track2.add_track(TrackLine(10, 8, 90))
res_eq = track1 == track2


print(res_eq)

