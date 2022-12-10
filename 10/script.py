cycle = 1
x = 1
signalStrengths = []
printLines = ['']
currentPrintIdx = 0
cycleDiff = 0

def executeCommand(command, input, register):
    if command[1] == '+': 
        register += int(input)
    return register

def printPixel(register, cycle):
    global currentPrintIdx 
    global cycleDiff

    position = cycle - 1 - cycleDiff
    pixelPos = [register - 1, register, register + 1]
    if position in pixelPos:
        newChar = '#'
    else: 
        newChar = '.'

    currentLine = printLines[currentPrintIdx]
    currentLine += newChar
    printLines[currentPrintIdx] = currentLine

    if cycle % 40 == 0:
        currentPrintIdx += 1
        printLines.append('')
        cycleDiff += 40

with open('input.txt', 'r') as inputFile:
    continueRunning = True
    commandDef = {'addx': (2, '+'), 'noop':(1, None)}
    currentCommand = None
    currentCommandCyclesRemaining = 0
    input = None

    # Execution loop
    while continueRunning == True:

        # Calc signal strength during cycle
        if (cycle == 20 or cycle % 40 == 20):
            signal = cycle * x
            signalStrengths.append(signal)
            print(str(cycle) + ' ' + str(x) + ' = ' + str(signal))

        printPixel(x, cycle)

        # Read a command if necessary
        if (currentCommand == None): 
            commandLine = inputFile.readline().strip()

            if commandLine == '':
                continueRunning = False
                break
            else:
                commandLine = commandLine.split()

            cmdDetail = commandDef[commandLine[0]]
            currentCommand = commandLine[0]
            currentCommandCyclesRemaining = cmdDetail[0]

            if len(commandLine) > 1:
                input = commandLine[1]
            else:
                input = None

        # Process cycle count for a running command, if needed
        if currentCommandCyclesRemaining > 0: 
            currentCommandCyclesRemaining -= 1
        
        if currentCommandCyclesRemaining == 0:
            x = executeCommand(cmdDetail, input, x)
            currentCommand = None
        
        cycle += 1
    cycle -= 1
    print('The last cycle was ' + str(cycle) + '. The register was at ' + str(x))
    print(signalStrengths)
    print('Total signal strengths: ' + str(sum(signalStrengths)))

    for line in printLines:
        print(line)