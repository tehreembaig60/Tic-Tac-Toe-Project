from typing import Optional, List

class Board:
    def __init__(self):
        self.cells: List[Optional[str]] = [None] * 9

    def place_move(self, position: int, marker: str) -> None:
        idx = position - 1
        if self.cells[idx] is None:
            self.cells[idx] = marker
        else:
            raise ValueError("Cell already occupied")

    def check_winner(self, marker: str) -> bool:
        wins = [
            (0,1,2),(3,4,5),(6,7,8),  # rows
            (0,3,6),(1,4,7),(2,5,8),  # cols
            (0,4,8),(2,4,6)           # diagonals
        ]
        return any(all(self.cells[i] == marker for i in line) for line in wins)

    def is_full(self) -> bool:
        return all(cell is not None for cell in self.cells)

    def __str__(self) -> str:
        def cell_str(i):
            return self.cells[i] if self.cells[i] is not None else str(i+1)
        rows = []
        for r in range(0,9,3):
            rows.append(" | ".join(cell_str(i) for i in range(r, r+3)))
        return "\n-----------\n".join(rows)