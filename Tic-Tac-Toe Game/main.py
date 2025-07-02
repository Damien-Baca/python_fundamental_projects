# System imports
from sys import exit, path
# Third party imports
from pygame import quit
# Local imports
from game_state_manager import GameStateManager

if __name__ == "__main__":
    print("Starting Tic-Tac-Toe!")
    game = GameStateManager()
    game.game_loop()

quit()
exit()
