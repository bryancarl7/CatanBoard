# -----Game Engine for Settlers of Catan-------
# Created: 8/3/2018
# Last Updated: 8/5/2018
# Mostly Containers for now
# ---------------------------------------------
import random
from model import GameEnv, GameElement, Player, Tile


def main():
    new_game = GameEnv([Player(1), Player(2), Player(3), Player(4)])
    new_game.setup_board()


if __name__ == '__main__':
    main()