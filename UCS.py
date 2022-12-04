import timeit
from Node import Node
from state import State
from queue import PriorityQueue


class UCS:

    def __init__(self):
        self.matrix = None

    def retracePath(self, state):
        path = []
        tempState = state
        while tempState.parent is not None:
            path.append(tempState)
            tempState = tempState.parent
        path.reverse()
        return path

    def solvePuzzle(self, state):
        print("Solving puzzle using UCS!")
        startTimer = timeit.default_timer()
        node = Node(state, None, None, 0)
        queue = PriorityQueue()
        queue.put((node.state.incrementGCost(), node))
        exploredSet = set()
        possibleGoalMatrix = state
        while not queue.empty():
            if possibleGoalMatrix.board.isAtGoalPosition(possibleGoalMatrix.board.getCarByName("A")):
                path = self.retracePath(possibleGoalMatrix)
                stop = timeit.default_timer()
                timing = stop - startTimer
                print("Runtime: ", round(timing, 3), " seconds")
                print("Search path length:", len(queue.queue), "states")
                print("Solution path length:", len(path), "moves")
                print("")
                for i in range(len(path)):
                    print(path[i].board.toString(), end="")
                    name = path[i].board.movedCar
                    for x in name:
                        fuel = path[i].board.getCarByName(x)
                        if fuel is None:
                            continue
                        print("", fuel.name, fuel.fuel, end="")
                    print("\n")
                print("!", end=" ")
                for name in possibleGoalMatrix.board.movedCar:
                    car = possibleGoalMatrix.board.getCarByName(name)
                    if car is None:
                        continue
                    print(car.name, car.fuel, end=" ")
                print("\nPuzzle solved!\n")
                possibleGoalMatrix.board.printMatrix()
                break
            node1 = queue.get()
            exploredSet.add(node1)
            if node1[1].state.board.getCarAtLocation(2, 5) != "A":
                for x in node1[1].state.board.cars:
                    if x.isMovingVertically():
                        boardup = node1[1].state.board
                        while boardup.moveableUp(boardup.getCarByName(x.name)) and boardup.getCarByName(x.name).hasFuel():
                            boardup = boardup.moveCarUp(boardup.getCarByName(x.name))
                            state1 = State(None, node1[1].state.gCost, node1[1].state, boardup)
                            child = Node(state1, 1, node1[1].state, node1[1].state.incrementGCost())
                            isinopen = False
                            isinclosed = False
                            for k in exploredSet:
                                if k[1].state.board.compare(child.state.board):
                                    isinclosed = True
                                    break
                            for k in queue.queue:
                                if k[1].state.board.compare(child.state.board):
                                    isinopen = True
                                    break
                            if isinclosed or isinopen:
                                break
                            else:
                                queue.put((child.state.incrementGCost(), child))
                        boarddown = node1[1].state.board
                        while boarddown.moveableDown(boarddown.getCarByName(x.name)) and boarddown.getCarByName(
                                x.name).hasFuel():
                            boarddown = boarddown.moveCarDown(boarddown.getCarByName(x.name))
                            state1 = State(None, node1[1].state.gCost, node1[1].state, boarddown)
                            child = Node(state1, 1, node1[1].state, node1[1].state.incrementGCost())
                            isinopen = False
                            isinclosed = False
                            for k in exploredSet:
                                if k[1].state.board.compare(child.state.board):
                                    isinclosed = True
                                    break
                            for k in queue.queue:
                                if k[1].state.board.compare(child.state.board):
                                    isinopen = True
                                    break
                            if isinclosed or isinopen:
                                break
                            else:
                                queue.put((child.state.incrementGCost(), child))
                    if x.isMovingHorizontally():
                        boardright = node1[1].state.board
                        while boardright.moveableRight(boardright.getCarByName(x.name)) and boardright.getCarByName(
                                x.name).hasFuel():
                            boardright = boardright.moveCarRight(boardright.getCarByName(x.name))
                            state1 = State(None, node1[1].state.gCost, node1[1].state, boardright)
                            child = Node(state1, 1, node1[1].state, node1[1].state.incrementGCost())
                            isinopen = False
                            isinclosed = False
                            for k in exploredSet:
                                if k[1].state.board.compare(child.state.board):
                                    isinclosed = True
                                    break
                            for k in queue.queue:
                                if k[1].state.board.compare(child.state.board):
                                    isinopen = True
                                    break
                            if isinclosed or isinopen:
                                break
                            else:
                                queue.put((child.state.incrementGCost(), child))
                            if boardright.getCarByName(x.name) not in boardright.cars:
                                possibleGoalMatrix = state1
                                break
                        boardleft = node1[1].state.board
                        while boardleft.moveableLeft(boardleft.getCarByName(x.name)) and boardleft.getCarByName(
                                x.name).hasFuel():
                            boardleft = boardleft.moveCarLeft(boardleft.getCarByName(x.name))
                            state1 = State(None, node1[1].state.gCost, node1[1].state, boardleft)
                            child = Node(state1, 1, node1[1].state, node1[1].state.incrementGCost())
                            isinopen = False
                            isinclosed = False
                            for k in exploredSet:
                                if k[1].state.board.compare(child.state.board):
                                    isinclosed = True
                                    break
                            for k in queue.queue:
                                if k[1].state.board.compare(child.state.board):
                                    isinopen = True
                                    break
                            if isinclosed or isinopen:
                                break
                            else:
                                queue.put((child.state.incrementGCost(), child))
        # only uncommented it if u need the search solution
        # print("-----------SEARCH-------------")
        # for i in explored:
        #     counter = 1
        #     if len(explored) != counter:
        #         print(0, i[1].state.g_Cost, 0, i[1].state.board.makingString(), end="")
        #         name = i[1].state.board.movedCar
        #         counter += 1
        #         for x in name:
        #             fuel = i[1].state.board.getCarName(x)
        #             if fuel is None:
        #                 continue
        #             print("", fuel.name, fuel.fuel, end="")
        #         print("\n")
        if queue.empty():
            stop = timeit.default_timer()
            timing = stop - startTimer
            print("")
            print("Sorry, could not solve the puzzle as specified.")
            print("Error: no solution found")
            print("")
            print("Runtime: ", round(timing, 3), " seconds")
