import sys


class Player:
    def __init__(self, name: str, old: str, score: str) -> None:
        self.name = name
        self.old = int(old)
        self.score = int(score)

    def __bool__(self) -> bool:
        return 0 < self.score


lst_in = list(map(str.strip, sys.stdin.readlines()))
players = [Player(*line.split("; ")) for line in lst_in]
players_filtered = [player for player in players if player]






