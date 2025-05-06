from pathlib import Path
from game.board import Board

class Logger:
    def __init__(self, player1, player2):
        self.base = Path(__file__).parent.parent / "game_log"
        self.base.mkdir(parents=True, exist_ok=True)
        existing = [d for d in self.base.iterdir() if d.is_dir() and d.name.startswith("game")]
        idx = len(existing) + 1
        self.game_dir = self.base / f"game{idx}"
        self.game_dir.mkdir()
        self.logfile = self.game_dir / "log.txt"
        self.p1 = player1
        self.p2 = player2
        self.lines = []

    def log_start(self):
        self.lines.append(f"Game Log")
        self.lines.append("Players:")
        self.lines.append(f"- {self.p1.name} ({self.p1.marker})")
        self.lines.append(f"- {self.p2.name} ({self.p2.marker})")
        self.lines.append("")

    def log_move(self, move_no: int, player_name: str, position: int, board: Board):
        self.lines.append(f"Move {move_no}: {player_name} -> Position {position}")
        self.lines.append("Board After Move:")
        self.lines.append(str(board))
        self.lines.append("")

    def log_result(self, result: str):
        self.lines.append(f"Result: {result}")
        self._flush()

    def _flush(self):
        self.logfile.write_text("\n".join(self.lines))