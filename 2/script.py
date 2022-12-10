import os

totalScore = 0
with open('input.txt', 'r') as fileInput:
    currentLine = fileInput.readline()
    while currentLine != '':
        if (currentLine == 'A X\n'):
            totalScore += 4
        elif (currentLine == 'A Y\n'):
            totalScore += 8
        elif (currentLine == 'A Z\n'):
            totalScore += 3
        elif (currentLine == 'B X\n'):
            totalScore += 1
        elif (currentLine == 'B Y\n'):
            totalScore += 5
        elif (currentLine == 'B Z\n'):
            totalScore += 9
        elif (currentLine == 'C X\n'):
            totalScore += 7
        elif (currentLine == 'C Y\n'):
            totalScore += 2
        elif (currentLine == 'C Z\n'):
            totalScore += 6
        else:
            continue
        
        currentLine = fileInput.readline()
    
    print('Total score is {0}'.format(totalScore))

    # ax = 4
    # ay = 8
    # az = 3
    # bx = 1
    # by = 5
    # bz = 9
    # cx = 7
    # cy = 2
    # cz = 6

    # Rock = 1
    # Paper = 2
    # Scissors = 3

    # Loss = 0
    # Draw = 3
    # Win = 6
