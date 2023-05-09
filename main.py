from board import SnakeBoard

def game_loop():
    board = SnakeBoard(35, 30)
    board.initialize()
    # while(board.handle_input()):
    while (board.handle_input()):
        board.update_snake()
        board.draw()
    
if __name__ == "__main__":
    game_loop()