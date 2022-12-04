from Board import Board
from UCS import UCS
from state import State
from GBFS import GBFS
from ASearch import AS


def ReadingFile(file):
    f = open(file, 'r')
    puzzles = []
    for lines in f:
        if not lines.startswith("#") and lines.strip():
            puzzles.append(lines.replace("\n", '').strip())
    return puzzles


def getAllFuel(line):
    keyLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                  'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    dict = {key: 100 for key in keyLetters}
    eachLine = [x for x in line]
    str = ""
    for character in range(len(eachLine)):
        if eachLine[character].isdigit():
            if not eachLine[character - 1].isdigit():
                tup = tuple(eachLine)
                keyDict = tup[character - 1]
            str += eachLine[character]
            if character != len(eachLine) - 1:
                if eachLine[character + 1].isdigit():
                    continue
            fuel = int(str)
            dict[keyDict] = fuel
            str = ""
    return dict


def getFuel(line, carName):
    dict = getAllFuel(line)
    return dict[carName]


def setAllFuel(line):
    board = Board(line)
    dict = getAllFuel(line)
    for key in dict:
        for i in range(len(board.cars)):
            if board.cars[i].name == key:
                board.cars[i].fuel = dict[key]
            continue
    return board


puzzles = ReadingFile("sample-input.txt")
for puzzle in puzzles:
    puzzleToBeSolved = puzzle
    board = setAllFuel(puzzleToBeSolved)
    print("-------------------------------------------------------------------------------------------------")
    print("Initial board configuration :", puzzleToBeSolved)
    print("Puzzle number: ", puzzles.index(puzzle)+1)
    print("!")
    board.printMatrix()
    print("")
    print("Car fuel available: ", end="")
    for i in board.cars:
        print(i.name, ":", i.fuel, ",", end=" ")
    print("")
    print("-------------------------------------------------------------------------------------------------")
    # Uncomment if running UCS Only and comment everything below
    # state = State(1, 0, None, board)
    # puzzleSolver = UCS()
    # puzzleSolver.solvePuzzle(state)
    state = State(1, 0, None, board)
    print("-------------------------------------------------------------------------------------------------")
    puzzleSolver = GBFS()
    puzzleSolver.solvePuzzle(state)
    print("-------------------------------------------------------------------------------------------------")
    puzzleSolver = AS()
    puzzleSolver.solvePuzzle(state)
    print("-------------------------------------------------------------------------------------------------")