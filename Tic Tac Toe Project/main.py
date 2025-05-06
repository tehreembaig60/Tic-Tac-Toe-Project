import sys
from game.board import Board
from game.players import Player
from game.utils import clean_input, validate_move, available_moves
from tools.display import welcome_message, display_board, announce_turn, announce_winner, announce_draw, prompt_restart
from tools.logger import Logger

def main():
    # Setup players
    p1_name = input("Please enter Player 1 name: ").strip()
    p2_name = input("Please enter Player 2 name: ").strip()
    player1 = Player(p1_name, "X")
    player2 = Player(p2_name if p2_name else "Computer", "O")

    welcome_message(player1.name, player2.name)

    game_number = 1
    while True:
        board = Board()
        logger = Logger(player1, player2)
        logger.log_start()

        current, other = player1, player2
        move_count = 0
        while True:
            display_board(board)
            announce_turn(current)
            raw = input(f"Enter a position (1-9): ")
            move = clean_input(raw)
            if not validate_move(move, board):
                print("Invalid move. Try again.")
                continue
            pos = int(move)
            board.place_move(pos, current.marker)
            move_count += 1
            logger.log_move(move_count, current.name, pos, board)

            if board.check_winner(current.marker):
                display_board(board)
                announce_winner(current.name)
                logger.log_result(f"{current.name} wins")
                break
            if board.is_full():
                display_board(board)
                announce_draw()
                logger.log_result("Draw")
                break

            # switch players
            current, other = other, current

        if not prompt_restart():
            print("Thanks for playing!")
            sys.exit()
        game_number += 1

if __name__ == "__main__":
    main()