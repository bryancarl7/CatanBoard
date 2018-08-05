# -------Model for Settlers of Catan-----------
# Created: 8/3/2018
# Last Updated: 8/5/2018
# Mostly Containers for now
# ---------------------------------------------
from VertexNode import VertexNode, MutablePair


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
            self.vp += 1
            self.pieces[0] -= 1
            self.spend_cards([1, 2, 3, 4])

    # TODO:
    def place_city(self):
        pass


# Each Game_Element Subclass inherits listeners to pick up on when they're being changed. Tiles act as their own entity,
# but with the new design this should look much, much better. This is just an early prototype, so feel free to
# implement whatever you feel comfortable with.
class Tile(GameElement):
    def __init__(self, resource, number, array):
        super().__init__()
        self.resource = resource
        self.value = number         # This is for the Dice #
        self.number = array[0]      # This is so that the tiles are numbered #
        self.vertexes = (array[1], array[2], array[3], array[4], array[5], array[6])
        self.robber = False

    def rob(self):
        self.robber = True

    def move_rob(self):
        self.robber = False
