from State import State


class Node:
    def __init__(self, state, action, parent, cost):
        self.state = state
        self.action = action
        self.parent = parent
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost
