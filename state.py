class State:
    def __init__(self, cost, gCost, parent, board):
        self.parent = parent
        self.board = board
        self.gCost = gCost
        self.hCost = self.getHCost(cost, board)
        self.fCost = self.returnFCost(cost, gCost)

    def getHCost(self, h_cost, board):
        cost = 0
        # h1
        if h_cost == 1:
            carList = []
            car = board.getCarByName("A")
            if car not in board.cars:
                self.hCost = 0
                return 0
            carPositions = car.returnAllCarPositions()
            for pos in range(carPositions[-1][1] + 1, 6):
                nextCarName = board.getCarAtLocation(2, pos)
                if not carList.__contains__(nextCarName) and nextCarName != ".":
                    cost += 1
        # h2
        elif h_cost == 2:
            car = board.getCarByName("A")
            if car not in board.cars:
                self.hCost = 0
                return 0
            carPositions = car.returnAllCarPositions()
            for pos in range(carPositions[-1][1] + 1, 6):
                nextCarName = board.getCarAtLocation(2, pos)
                if nextCarName != ".":
                    cost += 1
        # h3
        elif h_cost == 3:
            carList = []
            car = board.getCarByName("A")
            if car not in board.cars:
                self.hCost = 0
                return 0
            carPositions = car.returnAllCarPositions()
            for pos in range(carPositions[-1][1] + 1, 6):
                nextCarName = board.getCarAtLocation(2, pos)
                if not carList.__contains__(nextCarName) and nextCarName != ".":
                    cost += 1
            cost *= 5
        # h4
        if h_cost == 4:
            car = board.getCarByName("A")
            if car not in board.cars:
                self.hCost = 0
                return 0
            carPositions = car.returnAllCarPositions()
            for pos in range(carPositions[-1][1] + 1, 6):
                nextCarName = board.getCarAtLocation(2, pos)
                if nextCarName != ".":
                    cost += 1
            cost *= 5
        return cost

    def incrementGCost(self):
        if self.parent is not None:
            parent = self.parent.board
            child = self.board
            if child.movedCar == parent.movedCar:
                self.gCost = self.parent.gCost
            else:
                self.gCost = self.parent.gCost + 1
        return self.gCost

    def returnFCost(self, h_Cost, g_Cost):
        cost = 0
        if self.hCost == 1:
            cost = self.getHCost(1, self.board) + self.incrementGCost()
        if self.hCost == 2:
            cost = self.getHCost(2, self.board) + self.incrementGCost()
        if self.hCost == 3:
            cost = self.getHCost(3, self.board) + self.incrementGCost()
        return cost
