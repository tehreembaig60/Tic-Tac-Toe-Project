import random
from game.utils import available_moves

class Player:
    def __init__(self, name: str, marker: str):
        self.name = name
        self.marker = marker

    def get_move(self, board) -> int:
        if self.name.lower() == "computer":
            moves = list(available_moves(board))
            return random.choice(moves)
        else:
            raw = input(f"{self.name}'s Turn ({self.marker}): ")
            return int(raw)