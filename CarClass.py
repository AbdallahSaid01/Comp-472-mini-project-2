class Car:
    def __init__(self, name, orientation="", startingPosition=(), length=2, fuel=100):
        self.orientation = orientation
        self.startingPosition = startingPosition
        self.length = length
        self.fuel = fuel
        self.name = name
        self.allCarPositions = self.initializingCarPositions()

    def isMovingHorizontally(self):
        return self.orientation == "Horizontal"

    def isMovingVertically(self):
        return self.orientation == "Vertical"

    def printCarInformation(self):
        print("The car name is  ", self.name, " and its fuel is ", self.fuel, " and its start position is ",
              self.startingPosition, " and the car orientation is  ", self.orientation, " and its length  ",
              self.length, " and its full car location is ", self.allCarPositions)

    def initializingCarPositions(self):
        x = self.startingPosition[0]
        y = self.startingPosition[1]
        count = 0
        CarPosition = []
        if self.isMovingHorizontally():
            for i in range(self.length):
                CarPosition.append((x, y + count))
                count = count + 1
        elif self.isMovingVertically():
            for i in range(self.length):
                CarPosition.append((x + count, y))
                count = count + 1
        return CarPosition

    def returnAllCarPositions(self):
        return self.allCarPositions

    def setCarFullPosition(self, pos):
        self.allCarPositions = pos

    def useFuelAmount(self, amount):
        self.fuel = self.fuel - amount

    def hasFuel(self):
        return self.fuel > 0

    def __lt__(self, other):
        return self.name < other.name
