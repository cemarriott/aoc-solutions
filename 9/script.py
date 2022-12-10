import os
from copy import deepcopy

def doesTailMove(head, tail):
    xDiff = head[0] - tail[0]
    if abs(xDiff) > 1: return True
    yDiff = head[1] - tail[1]
    if abs(yDiff) > 1: return True
    return False

with open('input.txt', 'r') as inputFile:
    oldHeadPosition = (0, 0)
    headPosition = (0, 0)
    tailPosition = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
    tailVisits = set()

    commandLine = inputFile.readline().strip().split()

    while commandLine != []:
        for i in range(0, int(commandLine[1])):
            if commandLine[0] == 'R':
                oldHeadPosition = deepcopy(headPosition)
                headPosition = (headPosition[0] + 1, headPosition[1])
            elif commandLine[0] == 'L':
                oldHeadPosition = deepcopy(headPosition)
                headPosition = (headPosition[0] - 1, headPosition[1])
            elif commandLine[0] == 'U':
                oldHeadPosition = deepcopy(headPosition)
                headPosition = (headPosition[0], headPosition[1] + 1)
            elif commandLine[0] == 'D':
                oldHeadPosition = deepcopy(headPosition)
                headPosition = (headPosition[0], headPosition[1] - 1)
            
            leader = deepcopy(headPosition)
            for idx, tail in enumerate(tailPosition):
                if doesTailMove(leader, tail) == True:
                    if idx == 8:
                        tailVisits.add(tail)
                    if leader[0] != tail[0] and leader[1] != tail[1]:
                        xDiff = leader[0] - tail[0]
                        yDiff = leader[1] - tail[1]

                        oldTailPosition = deepcopy(tail)
                        if xDiff > 0:
                            currentTail = tailPosition[idx]
                            currentTail = (currentTail[0] + 1, currentTail[1])
                            tailPosition[idx] = currentTail
                        else:
                            currentTail = tailPosition[idx]
                            currentTail = (currentTail[0] - 1, currentTail[1])
                            tailPosition[idx] = currentTail
                        if yDiff > 0:
                            currentTail = tailPosition[idx]
                            currentTail = (currentTail[0], currentTail[1] + 1)
                            tailPosition[idx] = currentTail
                        else:
                            currentTail = tailPosition[idx]
                            currentTail = (currentTail[0], currentTail[1] - 1)
                            tailPosition[idx] = currentTail
                    else:
                        if leader[0] != tail[0]:
                            xDiff = leader[0] - tail[0]
                            oldTailPosition = deepcopy(tail)
                            if xDiff > 0:
                                currentTail = tailPosition[idx]
                                currentTail = (currentTail[0] + 1, currentTail[1])
                                tailPosition[idx] = currentTail
                            else:
                                currentTail = tailPosition[idx]
                                currentTail = (currentTail[0] - 1, currentTail[1])
                                tailPosition[idx] = currentTail
                        else:
                            yDiff = leader[1] - tail[1]
                            oldTailPosition = deepcopy(tail)
                            if yDiff > 0:
                                currentTail = tailPosition[idx]
                                currentTail = (currentTail[0], currentTail[1] + 1)
                                tailPosition[idx] = currentTail
                            else:
                                currentTail = tailPosition[idx]
                                currentTail = (currentTail[0], currentTail[1] - 1)
                                tailPosition[idx] = currentTail
                leader = deepcopy(tailPosition[idx])

        commandLine = inputFile.readline().strip().split()
    
    print('The tail visited ' + str(len(tailVisits)) + ' unique positions.')