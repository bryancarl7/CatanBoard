# -------Model for Settlers of Catan-----------
# Created: 8/3/2018
# Last Updated: 8/5/2018
# Mostly Containers for now
# ---------------------------------------------
import random

# Two of each Number with 2 and 12 having only one
# edit: Just so that the program can run I changed the values temprarily.
number_list = [0, 2, 3, 3, 4, 4, 5, 5, 6, 6, 8, 8, 9, 9, 10, 10, 11, 11, 12]

# ----Resource List Key----- #
#    1 - WOOD                #
#    2 - CLAY                #
#    3 - HAY                 #
#    4 - SHEEP               #
#    5 - ORE                 #
#    6 - DESERT              #
# -------------------------- #
resource_list = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6]


class GameEnv(object):
    def __init__(self, player_list):
        self.board = [[], [], [], [], []]
        self.players = player_list

    def setup_board(self):
        # Shuffle up the list to get random
        random_num_list = number_list.copy()
        random_res_list = resource_list.copy()
        random.shuffle(random_num_list)
        random.shuffle(random_res_list)
        ctr = 0

        # First Row
        for i in range(0, 2):
            self.board[0].append(Tile(random_res_list[ctr], random_num_list[ctr], (0, i)))
            ctr += 1

        # Second Row
        for i in range(0, 3):
            self.board[1].append(Tile(random_res_list[ctr], random_num_list[ctr], (1, i)))
            ctr += 1

        # Third Row
        for i in range(0, 4):
            self.board[2].append(Tile(random_res_list[ctr], random_num_list[ctr], (2, i)))
            ctr += 1

        # Fourth Row
        for i in range(0, 3):
            self.board[3].append(Tile(random_res_list[ctr], random_num_list[ctr], (3, i)))
            ctr += 1

        # Fifth Row
        for i in range(0, 2):
            self.board[4].append(Tile(random_res_list[ctr], random_num_list[ctr], (4, i)))
            ctr += 1


# Base Class for listener control of game elements like tiles/players etc
class GameElement(object):
    def __init__(self):
        self.data_structure = ''  # Unsure what the overarching VertexNode structure will look like
        self.listener_list = []

    def add_event_listener(self, listener):
        for i in listener:
            self.listener_list.append(i)

    def notify(self):
        for listener in self.listener:
            pass  # bit more coding to do here


# Relatively the same Player class, but more simple. Add any additions you feel like
class Player(GameElement):
    def __init__(self, number):
        super().__init__()
        self.number = number
        self.hand = [0, 0, 0, 0, 0]
        self.dev = []
        self.pieces = [5, 4, 20]  # 5 settlements, 4 cities, and 20 roads (decrement for updates)
        self.current_cities = []
        self.vp = 0

    def add_cards(self, add_list):
        for i in add_list:
            self.hand.append(i)

    def spend_cards(self, remove_list):
        for i in remove_list:
            if i in self.hand:
                self.hand.remove(i)
            else:
                print("You don't have enough cards!")

    def spend_dev_cards(self, remove_list):
        for i in remove_list:
            if i in self.dev:
                self.dev.remove(i)

    def place_road(self):
        # only the cost of roads, not any placing yet because we dont have the VertexNode Yet
        if 1 in self.hand and 2 in self.hand:
            self.spend_cards([1, 2])

    def place_settlement(self):
        flag = True
        for i in range(0,3):
            if self.hand[i] <= 0:
                flag = False
        if flag:
            total += 1
            self.vp += 1
            self.pieces[0] -= 1
            self.spend_cards([1, 2, 3, 4])

    # TODO:
    def place_city(self):
        pass


# Each Game_Element Subclass inherits listeners to pick up on when they're being changed. Tiles act as their own entity,
#  but with the new design this should look much, much better. This is just an early prototype, so feel free to
# implement whatever you feel comfortable with.
class Tile(GameElement):
    def __init__(self, resource, number, position):
        super().__init__()
        self.position = position
        self.resource = resource
        self.number = number
        self.vertexes = (0, 0, 0, 0, 0, 0)  # Instead of this we can replace with the VertexNodes
        self.robber = False

    def rob(self):
        self.robber = True

    def move_rob(self):
        self.robber = False
