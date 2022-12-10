import os

def treeIsVisible(rowIndex, colIndex, row, tree, rows):
    # Check if this is an edge
    if (rowIndex == 0 or rowIndex == (len(rows) - 1)): return True
    if (colIndex == 0 or colIndex == (len(row) - 1)): return True

    # Check up
    checkIndex = rowIndex - 1
    while checkIndex >= 0:
        checkRow = rows[checkIndex]
        checkTree = checkRow[colIndex]
        if int(checkTree) >= int(tree): break
        if checkIndex == 0: return True
        checkIndex -= 1

    # Check down
    checkIndex = rowIndex + 1
    while checkIndex <= len(rows) - 1:
        checkRow = rows[checkIndex]
        checkTree = checkRow[colIndex]
        if int(checkTree) >= int(tree): break
        if checkIndex == len(rows) - 1: return True
        checkIndex += 1

    # Check left
    checkIndex = colIndex - 1
    while checkIndex >= 0:
        checkTree = row[checkIndex]
        if int(checkTree) >= int(tree): break
        if checkIndex == 0: return True
        checkIndex -= 1

    # Check right
    checkIndex = colIndex + 1
    while checkIndex <= len(row) - 1:
        checkTree = row[checkIndex]
        if int(checkTree) >= int(tree): break
        if checkIndex == len(row) - 1: return True
        checkIndex += 1

    return False

with open('input.txt', 'r') as inputFile:
    rows = []
    inputLine = inputFile.readline()
    while inputLine != '':
        columns = list(inputLine.strip())
        rows.append(columns)
        inputLine = inputFile.readline()
    
    visibleTrees = 0
    for rowIndex, row in enumerate(rows):
        for colIndex, tree in enumerate(row):
            if treeIsVisible(rowIndex, colIndex, row, tree, rows) == True:
                visibleTrees += 1
    print('There are ' + str(visibleTrees) + ' visible trees.')