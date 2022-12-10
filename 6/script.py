import os

with open('input.txt', 'r') as inputFile:
    message = inputFile.readline()
    startIndex = 0
    markerFound = False

    while markerFound != True:
        currentSlice = message[startIndex:(startIndex + 14)]
        uniqueLetters = set(currentSlice)
        if len(uniqueLetters) == 14:
            markerFound = True
        else:
            startIndex += 1

    print("Final position: " + str(startIndex + 14))
