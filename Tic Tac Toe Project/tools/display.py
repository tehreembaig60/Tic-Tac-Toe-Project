from game.board import Board

def welcome_message(p1: str, p2: str) -> None:
    print(f"Welcome, {p1} and {p2}!")

def display_board(board: Board) -> None:
    print("Current Board:")
    print(board)

def announce_turn(player) -> None:
    print(f"{player.name}'s Turn ({player.marker}):")

def announce_winner(name: str) -> None:
    print(f"Congratulations, {name}! You win!")

def announce_draw() -> None:
    print("It's a draw!")

def prompt_restart() -> bool:
    ans = input("Would you like to play again? (yes/no): ").strip().lower()
    return ans in ("yes", "y")