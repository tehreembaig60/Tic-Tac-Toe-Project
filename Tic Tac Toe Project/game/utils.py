from typing import Generator
import re

_MOVE_RE = re.compile(r"^[1-9]$")

def clean_input(raw: str) -> str:
    return raw.strip()

def validate_move(move: str, board) -> bool:
    if not _MOVE_RE.match(move):
        return False
    pos = int(move)
    idx = pos - 1
    return 0 <= idx < 9 and board.cells[idx] is None

def available_moves(board) -> Generator[int, None, None]:
    for idx, cell in enumerate(board.cells):
        if cell is None:
            yield idx + 1
