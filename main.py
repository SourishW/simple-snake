from board import SnakeBoard

def game_loop():
    board = SnakeBoard(55, 45)
    board.initialize()
    while (board.handle_input() or board.continue_playing()):
        board.update_snake()
        board.draw()
    
if __name__ == "__main__":
    game_loop()