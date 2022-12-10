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

        if (int(firstValues[0]) >= int(secondValues[0]) and 
            int(firstValues[1]) <= int(secondValues[1])):
            totalOverlaps += 1
            print("Overlap found: {0} {1} - Original: {2}".format(firstRange, secondRange, rangeLine))
        elif (int(secondValues[0]) >= int(firstValues[0]) and 
              int(secondValues[1]) <= int(firstValues[1])):
            totalOverlaps +=1
            print("Overlap found: {0} {1} - Original: {2}".format(firstRange, secondRange, rangeLine))
        rangeLine = inputFile.readline()
    print("Total overlaps is {0}".format(totalOverlaps))
