# -----VertexNode for Settlers of Catan-------
# Created: 8/3/2018
# Last Updated: 8/5/2018
# Mostly Containers for now
# ---------------------------------------------


class MutablePair(object):
    def init(self, first, second):
        self.first = first
        self.second = second


class VertexNode(object):
    def init(self):
        self.resources = []
        self.port = MutablePair()
        self.city = MutablePair()
        self.listEdges = []