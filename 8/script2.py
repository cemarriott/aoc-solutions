import os

def getScore(rowIndex, colIndex, row, tree, rows):
    # Check up
    upScore = 0
    checkIndex = rowIndex - 1
    while checkIndex >= 0:
        checkRow = rows[checkIndex]
        checkTree = checkRow[colIndex]
        upScore += 1
        if int(checkTree) >= int(tree): break
        if checkIndex == 0: break
        checkIndex -= 1

    # Check down
    downScore = 0
    checkIndex = rowIndex + 1
    while checkIndex <= len(rows) - 1:
        checkRow = rows[checkIndex]
        checkTree = checkRow[colIndex]
        downScore += 1
        if int(checkTree) >= int(tree): break
        if checkIndex == len(rows) - 1: break
        checkIndex += 1

    # Check left
    leftScore = 0
    checkIndex = colIndex - 1
    while checkIndex >= 0:
        checkTree = row[checkIndex]
        leftScore += 1
        if int(checkTree) >= int(tree): break
        if checkIndex == 0: break
        checkIndex -= 1

    # Check right
    rightScore = 0
    checkIndex = colIndex + 1
    while checkIndex <= len(row) - 1:
        checkTree = row[checkIndex]
        rightScore += 1
        if int(checkTree) >= int(tree): break
        if checkIndex == len(row) - 1: break
        checkIndex += 1

    return (upScore * downScore * rightScore * leftScore)

with open('input.txt', 'r') as inputFile:
    rows = []
    inputLine = inputFile.readline()
    while inputLine != '':
        columns = list(inputLine.strip())
        rows.append(columns)
        inputLine = inputFile.readline()
    
    scenicScores = []
    for rowIndex, row in enumerate(rows):
        for colIndex, tree in enumerate(row):
            if (rowIndex == 0 or rowIndex == (len(rows) - 1)): continue
            if (colIndex == 0 or colIndex == (len(row) - 1)): continue
            scenicScores.append(getScore(rowIndex, colIndex, row, tree, rows))
    print('The scenic scores are:')
    print(scenicScores)
    print('The largest is:')
    print(sorted(scenicScores, reverse=True)[0])