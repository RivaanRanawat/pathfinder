#Maze Solver made with BFS(Breadth First Search)
#Used Idea of FIFO- First In First Out for Queues

import queue
import random

def createMaze():
    maze = []
    maze.append(["-","-", "-", "-", "-", "O","-"])
    maze.append(["-"," ", " ", " ", "-", " ","-"])
    maze.append(["-"," ", "-", " ", "-", " ","-"])
    maze.append(["-"," ", "-", " ", " ", " ","-"])
    maze.append(["-"," ", "-", "-", "-", " ","-"])
    maze.append(["-"," ", " ", " ", "-", " ","-"])
    maze.append(["-","-", "-", "-", "-", "X","-"])

    return maze

def createMaze2():
    maze = []
    maze.append(["-","-", "-", "-", "-", "O", "-", "-", "-"])
    maze.append(["-"," ", " ", " ", " ", " ", " ", " ", "-"])
    maze.append(["-"," ", "-", "-", " ", "-", "-", " ", "-"])
    maze.append(["-"," ", "-", " ", " ", " ", "-", " ", "-"])
    maze.append(["-"," ", "-", " ", "-", " ", "-", " ", "-"])
    maze.append(["-"," ", "-", " ", "-", " ", "-", " ", "-"])
    maze.append(["-"," ", "-", " ", "-", " ", "-", "-", "-"])
    maze.append(["-"," ", " ", " ", " ", " ", " ", " ", "-"])
    maze.append(["-","-", "-", "-", "-", "-", "-", "X", "-"])

    return maze

def createMaze3():
    maze = []
    maze.append(["-","-", "-", "-", "-", "O","-"])
    maze.append(["-"," ", " ", " ", "-", " ","-"])
    maze.append(["-"," ", "-", " ", "-", " ","-"])
    maze.append(["-"," ", "-", " ", " ", " ","-"])
    maze.append(["-"," ", "-", "-", "-", " ","-"])
    maze.append(["-"," ", " ", " ", "-", " ","-"])
    maze.append(["-","-", "-", "-", "-", "X","-"])

    return maze


def printMaze(maze, path=""):
    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
    pos = set()
    for move in path:
        if move == "L": #Left- if goes left the i decreases by one as in the number line
            i -= 1

        elif move == "R": #Right
            i += 1

        elif move == "U": #up
            j -= 1

        elif move == "D": #down
            j += 1
        pos.add((j, i))
    
    for j, row in enumerate(maze):
        for i, col in enumerate(row):
            if (j, i) in pos:
                print("+ ", end="")
            else:
                print(col + " ", end="")
        print()
        

# checks if the moves are valid
def valid(maze, moves):
    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

        if not(0 <= i < len(maze[0]) and 0 <= j < len(maze)):
            return False
        elif (maze[j][i] == "-"):
            return False

    return True

# finds the end of the project, we have indicated the end by an X
def findEnd(maze, moves):
    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

    if maze[j][i] == "X":
        print("Found: " + moves)
        printMaze(maze, moves)
        return True

    return False

#FIFO Algorithm
nums = queue.Queue()
nums.put("")
path = ""
maze  = createMaze2()
# while we dont get the end of the project(X)
while not findEnd(maze, path): 
    #we put the things in the queue in path
    path = nums.get()
    for j in ["L", "R", "U", "D"]:
        put = path + j
        # before we put in the solution we check if it is valid
        if valid(maze, put):
            nums.put(put)