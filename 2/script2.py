import os

totalScore = 0
with open('input.txt', 'r') as fileInput:
    currentLine = fileInput.readline()
    while currentLine != '':
        if (currentLine == 'A X\n'):
            totalScore += 3
        elif (currentLine == 'A Y\n'):
            totalScore += 4
        elif (currentLine == 'A Z\n'):
            totalScore += 8
        elif (currentLine == 'B X\n'):
            totalScore += 1
        elif (currentLine == 'B Y\n'):
            totalScore += 5
        elif (currentLine == 'B Z\n'):
            totalScore += 9
        elif (currentLine == 'C X\n'):
            totalScore += 2
        elif (currentLine == 'C Y\n'):
            totalScore += 6
        elif (currentLine == 'C Z\n'):
            totalScore += 7
        else:
            continue
        
        currentLine = fileInput.readline()
    
    print('Total score is {0}'.format(totalScore))

    # ax = 3
    # ay = 4
    # az = 8
    # bx = 1
    # by = 5
    # bz = 9
    # cx = 2
    # cy = 6
    # cz = 7

    # X = Lose = 0
    # Y = Draw = 3
    # Z = Win = 6

    # Rock = 1
    # Paper = 2
    # Scissors = 3

