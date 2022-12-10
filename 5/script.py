import os

with open('input.txt', 'r') as inputFile:
    stackLine = inputFile.readline()
    stackCounter = 1
    stackInd = 0

    stacks = {}
    doneWithStacks = False
    while not doneWithStacks:
        while stackInd < len(stackLine):
            if stackLine[stackInd] == '[':
                letter = stackLine[stackInd + 1]
                if ('stack' + str(stackCounter)) not in stacks:
                    newStack = []
                    newStack.append(letter)
                    stacks['stack' + str(stackCounter)] = newStack
                else:
                    currentStack = stacks['stack' + str(stackCounter)]
                    currentStack.append(letter)
            stackInd += 4
            stackCounter += 1
        
        # Reset for next line
        stackLine = inputFile.readline()
        stackCounter = 1
        stackInd = 0

        # Done building stacks
        if stackLine[:3] == ' 1 ':
            doneWithStacks = True

    # Reverse the stacks
    for stack in stacks:
        currentStack = stacks[stack]
        currentStack.reverse()

    inputFile.readline()

    # Execute the directions
    directionLine = inputFile.readline()
    while directionLine != '':
        directions = directionLine.split(' ')
        amount = int(directions[1])
        source = directions[3]
        dest = str.strip(directions[5])

        sourceStack = stacks['stack' + str(source)]
        destStack = stacks['stack' + str(dest)]

        tempStack = []
        while amount > 0:
            moveVal = sourceStack.pop()
            tempStack.append(moveVal)
            amount -= 1
            
        for ind in range(len(tempStack)):
            moveVal = tempStack.pop()
            destStack.append(moveVal)
        directionLine = inputFile.readline()

    finalPositions = ''
    for i in range(1, 10):
        currentStack = stacks['stack' + str(i)]
        finalPositions += currentStack.pop()
    print("Final stack positions: " + finalPositions)
