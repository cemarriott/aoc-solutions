import os

with open('input.txt', 'r') as inputFile:
    rangeLine = inputFile.readline()
    totalOverlaps = 0

    while rangeLine != '':
        groupRanges = rangeLine.split(',')
        firstRange = groupRanges[0]
        secondRange = groupRanges[1].strip()
        firstValues = firstRange.split('-')
        secondValues = secondRange.split('-')

        setOne = set(range(int(firstValues[0]), int(firstValues[1]) + 1))
        setTwo = set(range(int(secondValues[0]), int(secondValues[1]) + 1))

        if len(setOne & setTwo) > 0:
            totalOverlaps += 1
            print("Overlap found: Original: {0}, Overlaps: {1}".format(rangeLine, (setOne & setTwo)))
        rangeLine = inputFile.readline()
    print("Total overlaps is {0}".format(totalOverlaps))
