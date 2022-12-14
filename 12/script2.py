from copy import deepcopy

with open('input.txt', 'r') as inputFile:
    squares = []
    lineIdx = 0
    startSq = None
    endSq = None

    adjList = {}
    startList = []

    class square:
        xCoord = 0
        yCoord = 0
        height = ''
        visited = False

        def __init__(self, x, y, h):
            self.xCoord = x
            self.yCoord = y
            self.height = h

    # DFS
    def pathChecker(start, stop):
        prev = {}
        visited = set()
        queue = []
        
        queue.append((start, 0))
        visited.add(start)

        while len(queue) > 0:
            current = queue.pop(0)
            if (current[0] == stop): 
                return current[1]
            
            currNeighbors = adjList[current[0]]
            for neighbor in currNeighbors:
                if neighbor not in visited:
                    prev[neighbor] = current[0]
                    queue.append((neighbor, current[1] + 1))
                    visited.add(neighbor)
        return -1

    # Get the square input
    line = inputFile.readline().strip()
    while line != '':
        for idx, char in enumerate(line):
            if char == 'S':
                currSq = square(idx, lineIdx, 'a')
                startSq = currSq
            elif char == 'E':
                currSq = square(idx, lineIdx, 'z')
                endSq = currSq
            else: 
                currSq = square(idx, lineIdx, char)
            squares.append(currSq)
        lineIdx += 1
        line = inputFile.readline().strip()

    for square in squares:
        neighborList = []
        neighborList += [x for x in squares if ord(x.height) <= ord(square.height) + 1 and x.xCoord in [square.xCoord - 1, square.xCoord + 1] and x.yCoord == square.yCoord]
        neighborList += [x for x in squares if ord(x.height) <= ord(square.height) + 1 and x.xCoord == square.xCoord and x.yCoord in [square.yCoord - 1, square.yCoord + 1]]
        adjList[square] = neighborList

        if square.height == 'a':
            startList.append(square)

    resultList = []
    for starter in startList:
        resultList.append(pathChecker(starter, endSq))

    shortestPath = sorted(resultList)
    print('The shortest path is ' + str(shortestPath))