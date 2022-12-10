import os

with open('input.txt', 'r') as inputFile:
    scoreSum = 0
    letterScore = [0, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    currentSack = inputFile.readline()
    while currentSack != '':
        lineSize = len(currentSack) - 1
        firstSack = currentSack[0:(lineSize // 2)]
        secondSack = currentSack[(lineSize // 2):lineSize]

        firstSet = set(firstSack)
        secondSet = set(secondSack)
        sharedLetters = firstSet & secondSet
        for letter in sharedLetters:
            scoreSum += letterScore.index(letter)
        currentSack = inputFile.readline()
    print("Total score is {0}".format(scoreSum))