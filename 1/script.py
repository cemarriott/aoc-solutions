import os

itemTotals = []
currentItem = 0
with open('input.txt', 'r') as txtInput:
    currentLine = txtInput.readline()
    while currentLine != '':
        if currentLine != '\n':
            currentItem += int(currentLine)
        else:
            itemTotals.append(currentItem)
            currentItem = 0
        currentLine = txtInput.readline()
    itemTotals.sort(reverse=True)
    print('The max 3 numbers are {0}, {1}, {2}. The sum is {3}.'.format(itemTotals[0], itemTotals[1], itemTotals[2], itemTotals[0] + itemTotals[1] + itemTotals[2]))
