import os

with open('input.txt', 'r') as inputFile:
    scoreSum = 0
    letterScore = [0, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    sack1 = inputFile.readline()
    while sack1 != '':
        sack2 = inputFile.readline()
        sack3 = inputFile.readline()

        firstSet = set(sack1[:len(sack1) - 1])
        secondSet = set(sack2[:len(sack2) - 1])
        thirdSet = set(sack3[:len(sack3) - 1])

        sharedLetters = firstSet & secondSet & thirdSet
        for letter in sharedLetters:
            scoreSum += letterScore.index(letter)
        sack1 = inputFile.readline()
    print("Total score is {0}".format(scoreSum))